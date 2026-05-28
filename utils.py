import shutil
from pathlib import Path

from gaveta.files import ensure_dir


def ensure_clean_dir(folder: Path) -> None:
    try:
        shutil.rmtree(folder)
        ensure_dir(folder)
    except FileNotFoundError:
        ensure_dir(folder)


def xyxy_to_xywh(xyxy: list[float]) -> list[int]:
    x_min, y_min, x_max, y_max = xyxy
    return [int(x_min), int(y_min), int(x_max - x_min), int(y_max - y_min)]
