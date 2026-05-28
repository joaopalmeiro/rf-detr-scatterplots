import supervision as sv
from huggingface_hub import download_bucket_files
from loguru import logger
from PIL import Image
from rfdetr import RFDETRMedium
from rfdetr.assets.coco_classes import COCO_CLASSES

from constants import RESULTS, TEST
from utils import ensure_clean_dir


def evaluate_medium_model() -> None:
    ensure_clean_dir(RESULTS / "medium")

    model = RFDETRMedium()
    model.optimize_for_inference()

    box_annotator = sv.BoxAnnotator()

    for image in TEST.glob("*.jpg"):
        detections = model.predict(str(image), threshold=0.5)
        logger.info("Number of predicted bounding boxes: {total}", total=len(detections.xyxy))
        logger.info("Classes: {classes}", classes=detections.class_id)

        labels = [f"{COCO_CLASSES[class_id]}" for class_id in detections.class_id]

        annotated_image = box_annotator.annotate(
            scene=detections.metadata["source_image"],
            detections=detections,
        )
        annotated_image = sv.LabelAnnotator().annotate(annotated_image, detections, labels)

        Image.fromarray(annotated_image).save(RESULTS / "medium" / image.name)

        logger.info("{image} evaluated", image=image.name)


def evaluate_medium_trained_model() -> None:
    ensure_clean_dir(RESULTS / "medium_trained")

    download_bucket_files(
        "joaompalmeiro/checkpoints",
        files=[
            ("medium-v1/checkpoint_best_total.pth", "./checkpoint_best_total.pth"),
        ],
    )

    classes = sv.DetectionDataset.from_coco(
        images_directory_path=TEST,
        annotations_path=TEST / "_annotations.coco.json",
    ).classes

    model = RFDETRMedium(pretrain_weights="checkpoint_best_total.pth")
    model.optimize_for_inference()

    box_annotator = sv.BoxAnnotator()

    for image in TEST.glob("*.jpg"):
        detections = model.predict(str(image), threshold=0.5)
        logger.info("Number of predicted bounding boxes: {total}", total=len(detections.xyxy))
        logger.info("Classes: {classes}", classes=detections.class_id)

        labels = [f"{classes[class_id]}" for class_id in detections.class_id]

        annotated_image = box_annotator.annotate(
            scene=detections.metadata["source_image"],
            detections=detections,
        )

        Image.fromarray(annotated_image).save(RESULTS / "medium_trained" / image.name)
        annotated_image = sv.LabelAnnotator().annotate(annotated_image, detections, labels)

        logger.info("{image} evaluated", image=image.name)


if __name__ == "__main__":
    evaluate_medium_model()
    evaluate_medium_trained_model()
