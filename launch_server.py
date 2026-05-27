import json
from string import Template

import pandas as pd
from fasthtml.common import Div, Main, Script, fast_app, serve

from constants import DATASETS, DEFAULT_HEIGHT, DEFAULT_OPACITY, DEFAULT_PADDING, DEFAULT_POINT_SIZE, DEFAULT_WIDTH

VL_SCRIPT = Template("""
vegaEmbed("#chart", $vl_spec).then((result) => {
  const [xOrigin, yOrigin] = result.view.origin();
  const padding = $padding;

  const xOffset = xOrigin + padding;
  const yOffset = yOrigin + padding;

  const boundingBoxes = $bounding_boxes;

  const scaledBoundingBoxes = boundingBoxes.map((boundingBox) => {
    const xMinPx = result.view.scale("x")(boundingBox.x_min);
    const xMaxPx = result.view.scale("x")(boundingBox.x_max);

    const yMaxPx = result.view.scale("y")(boundingBox.y_min);
    const yMinPx = result.view.scale("y")(boundingBox.y_max);

    return [
      (xMinPx + xOffset) * $scale_factor,
      (yMinPx + yOffset) * $scale_factor,
      (xMaxPx + xOffset) * $scale_factor,
      (yMaxPx + yOffset) * $scale_factor,
    ];
  });

  result.view.toImageURL("png", $scale_factor).then((data_url) => {
    console.log(data_url, {
      bbox: scaledBoundingBoxes,
    });
  });
});
""")


def generate_default_spec(dataset: pd.DataFrame) -> str:
    return json.dumps(
        {
            "padding": DEFAULT_PADDING,
            "data": {"values": dataset.to_dict(orient="records")},
            "mark": {
                "type": "point",
                "filled": True,
                "size": DEFAULT_POINT_SIZE,
                "opacity": DEFAULT_OPACITY,
            },
            "encoding": {
                "x": {
                    "field": "x",
                    "type": "quantitative",
                    "axis": {"title": None},
                    "scale": {"zero": False},
                },
                "y": {
                    "field": "y",
                    "type": "quantitative",
                    "axis": {"title": None},
                    "scale": {"zero": False},
                },
            },
            "config": {
                "view": {
                    "continuousWidth": DEFAULT_WIDTH,
                    "continuousHeight": DEFAULT_HEIGHT,
                }
            },
        },
        ensure_ascii=False,
    )


def compute_cluster_bounding_boxes(dataset: pd.DataFrame) -> str:
    bounding_boxes = dataset.groupby("cluster", as_index=False).agg(
        x_min=("x", "min"), x_max=("x", "max"), y_min=("y", "min"), y_max=("y", "max")
    )

    return bounding_boxes.to_json(orient="records")


app, rt = fast_app(
    pico=False,
    live=False,
    hdrs=(
        Script(src="https://cdn.jsdelivr.net/npm/vega@6.1.2"),
        Script(src="https://cdn.jsdelivr.net/npm/vega-lite@6.1.0"),
        Script(src="https://cdn.jsdelivr.net/npm/vega-embed@7.0.2"),
    ),
)


@rt("/{dataset_id}")
def home(dataset_id: str):
    dataset = pd.read_json(DATASETS / f"{dataset_id}.json")

    bounding_boxes = compute_cluster_bounding_boxes(dataset)

    vl_spec = generate_default_spec(dataset)

    return Main(
        Div(id="chart"),
        Script(
            VL_SCRIPT.safe_substitute(
                vl_spec=vl_spec,
                bounding_boxes=bounding_boxes,
                scale_factor=1,
                padding=DEFAULT_PADDING,
            )
        ),
    )


if __name__ == "__main__":
    serve()
