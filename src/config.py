from pathlib import Path
import yaml

BASE_DIR = Path(__file__).resolve().parent.parent

CONFIG_FILE = BASE_DIR / "config" / "config.yaml"

with open(CONFIG_FILE, "r") as file:
    CONFIG = yaml.safe_load(file)

RAW_PATH = BASE_DIR / CONFIG["paths"]["raw"]

REPORTS_PATH = BASE_DIR / "reports"

CLEANED_PATH = BASE_DIR / "data" / "cleaned"
FAILED_PATH = BASE_DIR / "data" / "failed"
TRANSFORMED_PATH = BASE_DIR / "data" / "transformed"
HASHED_PATH = BASE_DIR / "data" / "hashed"