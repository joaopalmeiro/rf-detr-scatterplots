from collections import Counter

import pandas as pd
from loguru import logger
from sklearn.datasets import make_blobs

from constants import DATASETS
from utils import ensure_clean_dir


def generate_gaussian_blobs() -> None:
    prefix = "gaussian_blobs"

    min_n_clusters = 2
    max_n_clusters = 10

    for n_samples in [100, 500, 1_000, 2_000]:
        for n_clusters in range(min_n_clusters, max_n_clusters + 1):
            for cluster_std in [0.2, 0.4, 0.6]:
                for random_state in [0, 42]:
                    coordinates, labels = make_blobs(
                        n_samples=n_samples, centers=n_clusters, cluster_std=cluster_std, random_state=random_state
                    )

                    dataset = pd.DataFrame(coordinates, columns=["x", "y"])
                    dataset = dataset.assign(cluster=labels)

                    dataset_id = f"{prefix}+{n_samples}+{n_clusters}+{cluster_std}+{random_state}".replace(".", "_")
                    dataset.to_json(DATASETS / f"{dataset_id}.json", orient="records", force_ascii=False)

                    logger.info("{dataset_id} generated", dataset_id=dataset_id)


def generate_imbalanced_gaussian_blobs() -> None:
    prefix = "imbalanced_gaussian_blobs"

    imbalance_levels = {
        "mild": [
            [60, 30, 10],
            [300, 150, 50],
            [600, 300, 100],
            [1200, 600, 200],
        ],
        "severe": [
            [80, 15, 5],
            [400, 75, 25],
            [800, 150, 50],
            [1600, 300, 100],
        ],
    }

    for cluster_std in [0.2, 0.4, 0.6]:
        for imbalance_label, counts in imbalance_levels.items():
            for n_samples in counts:
                for random_state in [0, 42]:
                    total = sum(n_samples)
                    n_clusters = len(n_samples)

                    coordinates, labels = make_blobs(
                        n_samples=n_samples, cluster_std=cluster_std, random_state=random_state
                    )

                    dataset = pd.DataFrame(coordinates, columns=["x", "y"])
                    dataset = dataset.assign(cluster=labels)

                    dataset_id = (
                        f"{prefix}+{total}+{n_clusters}+{cluster_std}+{random_state}+{imbalance_label}".replace(
                            ".", "_"
                        )
                    )
                    dataset.to_json(DATASETS / f"{dataset_id}.json", orient="records", force_ascii=False)

                    logger.info("{dataset_id} generated", dataset_id=dataset_id)


if __name__ == "__main__":
    ensure_clean_dir(DATASETS)

    generate_gaussian_blobs()
    generate_imbalanced_gaussian_blobs()

    all_datasets = list(DATASETS.glob("*.json"))

    logger.info("{total} datasets generated", total=len(all_datasets))
    logger.info(
        "Dataset breakdown: {breakdown}",
        breakdown=Counter(dataset.stem.split("+", maxsplit=1)[0] for dataset in all_datasets),
    )
