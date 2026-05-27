from sklearn.model_selection import train_test_split

from constants import DATASETS, FINAL_DATASET, RANDOM_STATE
from utils import ensure_clean_dir

if __name__ == "__main__":
    ensure_clean_dir(FINAL_DATASET)

    all_ids = sorted(d.stem for d in DATASETS.glob("*.json"))

    # 80/10/10:
    train_ids, test_ids = train_test_split(all_ids, test_size=0.2, random_state=RANDOM_STATE)
    val_ids, test_ids = train_test_split(test_ids, test_size=0.5, random_state=RANDOM_STATE)

    # TODO
