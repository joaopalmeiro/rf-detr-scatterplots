from pathlib import Path

INPUT = Path("input")
OUTPUT = Path("output")
DATASETS = INPUT / "datasets"
IMAGES = INPUT / "images"
METADATA = INPUT / "metadata"

RANDOM_STATE = 42

# https://rfdetr.roboflow.com/latest/learn/run/detection/
RF_DETR_M_SIZE = 576

# https://vega.github.io/vega-lite/docs/spec.html#config
DEFAULT_HEIGHT = RF_DETR_M_SIZE
DEFAULT_WIDTH = RF_DETR_M_SIZE
DEFAULT_OPACITY = 0.7
DEFAULT_PADDING = 5

# https://vega.github.io/vega-lite/docs/point.html
DEFAULT_POINT_SIZE = 30
