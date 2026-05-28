import os

from rfdetr import RFDETRMedium

train_run = os.environ.get("TRAIN_RUN", "tmp")

model = RFDETRMedium()

model.train(
    dataset_dir="/dataset",
    epochs=100,
    batch_size=16,
    grad_accum_steps=1,
    output_dir=f"/output/{train_run}",
)
