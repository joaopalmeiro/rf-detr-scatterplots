import supervision as sv
from loguru import logger
from PIL import Image
from rfdetr import RFDETRMedium

from constants import RESULTS, TEST
from utils import ensure_clean_dir


def evaluate_medium_model() -> None:
    ensure_clean_dir(RESULTS / "medium")

    model = RFDETRMedium()
    box_annotator = sv.BoxAnnotator()

    for image in TEST.glob("*.jpg"):
        detections = model.predict(str(image), threshold=0.5)
        logger.info("Number of predicted bounding boxes: {total}", total=len(detections.xyxy))

        annotated_image = box_annotator.annotate(
            scene=detections.metadata["source_image"],
            detections=detections,
        )

        Image.fromarray(annotated_image).save(RESULTS / "medium" / image.name)

        logger.info("{image} evaluated", image=image.name)


if __name__ == "__main__":
    evaluate_medium_model()
