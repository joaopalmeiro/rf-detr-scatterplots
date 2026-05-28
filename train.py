import os
import subprocess

from rfdetr import RFDETRMedium

train_run = os.environ.get("TRAIN_RUN", "tmp")

print(subprocess.run(["nvidia-smi"], capture_output=True, text=True, check=True).stdout)

model = RFDETRMedium()

model.train(
    dataset_dir="/dataset",
    epochs=100,
    batch_size=16,
    grad_accum_steps=1,
    output_dir=f"/output/{train_run}",
    early_stopping=True,
    early_stopping_patience=5,
    early_stopping_min_delta=0.005,
    skip_best_epochs=3,
)
