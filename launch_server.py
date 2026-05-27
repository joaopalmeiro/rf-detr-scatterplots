from string import Template

import pandas as pd
from fastcore.xml import FT
from fasthtml.common import Div, Main, Script, fast_app, serve

from constants import DATASETS

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


def compute_cluster_bounding_boxes(dataset: pd.DataFrame) -> str:
    bounding_boxes = dataset.groupby("cluster", as_index=False).agg(
        x_min=("x", "min"), x_max=("x", "max"), y_min=("y", "min"), y_max=("y", "max")
    )

    return bounding_boxes.to_json(orient="records")


app, _ = fast_app(
    pico=False,
    live=False,
    hdrs=(
        Script(src="https://cdn.jsdelivr.net/npm/vega@6.1.2"),
        Script(src="https://cdn.jsdelivr.net/npm/vega-lite@6.1.0"),
        Script(src="https://cdn.jsdelivr.net/npm/vega-embed@7.0.2"),
    ),
)


@app.get("/{dataset_id}/{chart_design}/{scale_factor}")
def home(dataset_id: str, chart_design: str, scale_factor: float) -> FT:
    dataset = pd.read_json(DATASETS / f"{dataset_id}.json")

    bounding_boxes = compute_cluster_bounding_boxes(dataset)

    # TODO
    vl_spec = CHART_DESIGNS[chart_design](dataset)

    return Main(
        Div(id="chart"),
        Script(
            VL_SCRIPT.safe_substitute(
                vl_spec=vl_spec,
                bounding_boxes=bounding_boxes,
                scale_factor=scale_factor,
                padding=DEFAULT_PADDING,
            )
        ),
    )


if __name__ == "__main__":
    serve()
