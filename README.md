# rf-detr-scatterplots

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)

## Development

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) (if necessary):

```bash
curl -LsSf https://astral.sh/uv/0.11.6/install.sh | sh
```

```bash
uv python install
```

```bash
uv audit --verbose
```

```bash
uv run python generate_datasets.py
```

```bash
uv run playwright install
```

```bash
uv run python launch_server.py
```

```bash
uv run python annotate_datasets.py
```

```bash
uv run python convert_coco.py
```

```bash
uv run python validate_images.py
```

```bash
uv run python test_models.py
```

```bash
uv run mypy
```

```bash
uv run ruff format
```

```bash
uv run ruff check --fix
```

```bash
HF_TOKEN="op://Development/Hugging Face/HF_TOKEN" op run -- uv run hf buckets create scatterplots
```

```bash
HF_TOKEN="op://Development/Hugging Face/HF_TOKEN" op run -- uv run hf buckets sync ./output/dataset hf://buckets/joaompalmeiro/scatterplots --delete
```
