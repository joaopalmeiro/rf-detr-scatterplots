import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.request import urlopen

from gaveta.json import write_json
from loguru import logger
from playwright.sync_api import ConsoleMessage, sync_playwright

from constants import DATASETS, IMAGES, METADATA
from utils import ensure_clean_dir

thread_local = threading.local()


def init_browser() -> None:
    thread_local.playwright = sync_playwright().start()
    thread_local.browser = thread_local.playwright.chromium.launch(headless=False)
    thread_local.page = thread_local.browser.new_page()


def handle_msg(msg: ConsoleMessage, dataset_id: str, chart_design: str) -> None:
    image = msg.args[0].json_value()
    metadata = msg.args[1].json_value()

    extra_metadata = {"dataset_id": dataset_id, "chart_design": chart_design}

    final_id = f"{dataset_id}+{chart_design}"

    with (
        urlopen(image) as i,
        (IMAGES / f"{final_id}.png").open(mode="wb") as f,
    ):
        f.write(i.read())

    write_json({**metadata, **extra_metadata}, METADATA / f"{final_id}.json")


def run_job(job: tuple[str, str]) -> None:
    dataset_id, chart_design = job
    url = f"http://localhost:5001/{dataset_id}/{chart_design}"

    with thread_local.page.expect_console_message() as msg_info:
        thread_local.page.goto(url)
        msg = msg_info.value

    handle_msg(msg, dataset_id, chart_design)


if __name__ == "__main__":
    ensure_clean_dir(IMAGES)
    ensure_clean_dir(METADATA)

    all_jobs: list[tuple[str, str]] = [
        (d.stem, chart_design) for d in DATASETS.glob("*.json") for chart_design in ["dark", "default", "x2_point_size"]
    ]

    with ThreadPoolExecutor(max_workers=5, initializer=init_browser) as executor:
        futures = {executor.submit(run_job, job): job for job in all_jobs}

        for future in as_completed(futures):
            job = futures[future]

            try:
                future.result()
                logger.info("{job} generated", job=job)
            except Exception as e:
                logger.error(e)
