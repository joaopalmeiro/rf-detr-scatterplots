import shutil
from pathlib import Path

from gaveta.files import ensure_dir


def ensure_clean_dir(folder: Path) -> None:
    try:
        shutil.rmtree(folder)
        ensure_dir(folder)
    except FileNotFoundError:
        ensure_dir(folder)
