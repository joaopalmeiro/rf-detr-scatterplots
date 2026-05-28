from pathlib import Path

import cv2
import supervision as sv
from loguru import logger

from constants import VALID, VALIDATION
from utils import ensure_clean_dir

VALIDATION = Path("input") / "validation"


if __name__ == "__main__":
    ensure_clean_dir(VALIDATION)

    dataset = sv.DetectionDataset.from_coco(
        images_directory_path=str(VALID),
        annotations_path=str(VALID / "_annotations.coco.json"),
    )

    box_annotator = sv.BoxAnnotator()

    for image_path, image, annotations in dataset:
        annotated_image = box_annotator.annotate(scene=image, detections=annotations)

        output_path = VALIDATION / Path(image_path).name
        cv2.imwrite(output_path, annotated_image)
        logger.info("{path} generated", path=output_path)
