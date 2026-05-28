from huggingface_hub import Volume, run_uv_job

TRAIN_RUN = "medium-v1"

run_uv_job(
    "train.py",
    dependencies=["rfdetr[train,loggers]==1.6.5.post2"],
    flavor="a100-large",
    volumes=[
        Volume(type="bucket", source="joaompalmeiro/scatterplots", mount_path="/dataset"),
        Volume(type="bucket", source="joaompalmeiro/checkpoints", mount_path="/output"),
    ],
    env={"TRAIN_RUN": TRAIN_RUN},
)
