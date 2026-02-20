# coding utf-8

from pathlib import Path

# Configuration variables

BASE_DIR = Path(__file__).resolve().parents[2]

ENV_FILE, JSON_FILE = [BASE_DIR / i for i in (".env", "config.json")]

ENV_PREFIX = "APP_"

# Variables for the entities

SNAKE_CASE_PATTERN = r"(?<!^)([A-Z][a-z])"

SNAKE_CASE_REPLACEMENT = r"_\1"

# Variables for config

URL_REQUIRED_FIELDS: frozenset[str] = frozenset(
    {"driver", "host", "port"},
)
