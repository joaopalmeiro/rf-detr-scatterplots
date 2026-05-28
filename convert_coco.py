from pathlib import Path

from gaveta.json import read_json, write_json
from loguru import logger
from PIL import Image
from sklearn.model_selection import train_test_split

from constants import IMAGES, METADATA, RANDOM_STATE, TEST, TRAIN, VALID
from utils import ensure_clean_dir, xyxy_to_xywh


def internal_to_coco(ids: list[str], subset: Path) -> None:
    annotations_coco = {
        "images": [],
        "categories": [
            {
                "id": 1,
                "name": "cluster",
            },
        ],
        "annotations": [],
    }

    for index, id in enumerate(ids, start=1):
        file_name = f"{id}.jpg"

        with Image.open(subset / f"{id}.png") as im:
            width, height = im.size
            im.convert("RGB").save(subset / file_name)

        annotations_coco["images"].append(
            {
                "id": index,
                "file_name": file_name,
                "width": width,
                "height": height,
            }
        )

        metadata = read_json(METADATA / f"{id}.json")

        for bbox_index, bbox in enumerate(metadata["bbox"], start=1):
            coordinates = xyxy_to_xywh(bbox)
            area = coordinates[2] * coordinates[3]

            annotations_coco["annotations"].append(
                {
                    "id": int(f"{index}{bbox_index}"),
                    "image_id": index,
                    "category_id": 1,
                    "bbox": coordinates,
                    "area": area,
                    "iscrowd": 0,
                }
            )

        write_json(annotations_coco, subset / "_annotations.coco.json")


if __name__ == "__main__":
    ensure_clean_dir(TRAIN)
    ensure_clean_dir(VALID)
    ensure_clean_dir(TEST)

    all_ids = sorted(d.stem for d in IMAGES.glob("*.png"))
    logger.info("Size: {size}", size=len(all_ids))

    # 80/10/10:
    train_ids, test_ids = train_test_split(all_ids, test_size=0.2, random_state=RANDOM_STATE)
    val_ids, test_ids = train_test_split(test_ids, test_size=0.5, random_state=RANDOM_STATE)

    internal_to_coco(train_ids, TRAIN)
    internal_to_coco(val_ids, VALID)
    internal_to_coco(test_ids, TEST)
