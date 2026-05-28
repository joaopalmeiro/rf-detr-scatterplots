from pathlib import Path

INPUT = Path("input")
DATASETS = INPUT / "datasets"
IMAGES = INPUT / "images"
METADATA = INPUT / "metadata"

OUTPUT = Path("output")
FINAL_DATASET = OUTPUT / "dataset"
TRAIN = FINAL_DATASET / "train"
VALID = FINAL_DATASET / "valid"
TEST = FINAL_DATASET / "test"

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

# https://vega.github.io/vega-lite/docs/size.html#autosize
DEFAULT_AUTO_SIZE = {"type": "fit", "contains": "padding"}

# Source: https://github.com/vega/vega-themes/blob/v3.0.0/src/theme-dark.ts
DARK_THEME_CONFIG = {
    "background": "#333",
    "view": {
        "stroke": "#888",
    },
    "title": {
        "color": "#fff",
        "subtitleColor": "#fff",
    },
    "style": {
        "guide-label": {
            "fill": "#fff",
        },
        "guide-title": {
            "fill": "#fff",
        },
    },
    "axis": {
        "domainColor": "#fff",
        "gridColor": "#888",
        "tickColor": "#fff",
    },
}
