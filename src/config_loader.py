"""
Safe configuration loading utilities for AirlineCareerAgent.

This module reads local JSON configuration files only.
It does not scrape websites, call external APIs, or run agent logic.
"""

import json
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CONFIG_DIR = PROJECT_ROOT / "config"

COMPANIES_CONFIG = CONFIG_DIR / "companies.json"
ROLE_KEYWORDS_CONFIG = CONFIG_DIR / "role_keywords.json"


def load_json_config(file_path: Path) -> Any:
    """
    Safely load a JSON configuration file.

    Args:
        file_path: Path to the JSON file.

    Returns:
        Parsed JSON content.

    Raises:
        FileNotFoundError: If the config file does not exist.
        ValueError: If the file is empty or contains invalid JSON.
    """
    if not file_path.exists():
        raise FileNotFoundError(f"Config file not found: {file_path}")

    if not file_path.is_file():
        raise ValueError(f"Config path is not a file: {file_path}")

    try:
        with file_path.open("r", encoding="utf-8") as file:
            content = file.read().strip()

            if not content:
                raise ValueError(f"Config file is empty: {file_path}")

            return json.loads(content)

    except json.JSONDecodeError as error:
        raise ValueError(f"Invalid JSON in config file: {file_path}") from error


def load_companies_config() -> list[dict[str, Any]]:
    """
    Load company configuration from config/companies.json.

    Returns:
        A list of company configuration dictionaries.
    """
    data = load_json_config(COMPANIES_CONFIG)

    if not isinstance(data, list):
        raise ValueError("companies.json must contain a list of companies.")

    return data


def load_role_keywords_config() -> dict[str, Any]:
    """
    Load role keyword configuration from config/role_keywords.json.

    Returns:
        A dictionary containing role keyword groups and MVP filters.
    """
    data = load_json_config(ROLE_KEYWORDS_CONFIG)

    if not isinstance(data, dict):
        raise ValueError("role_keywords.json must contain a dictionary.")

    for key, value in data.items():
        if not isinstance(key, str):
            raise ValueError("All top-level keys in role_keywords.json must be strings.")

        if isinstance(value, list):
            if not all(isinstance(item, str) for item in value):
                raise ValueError(
                    f"All items in role keyword list '{key}' must be strings."
                )

        elif isinstance(value, dict):
            # Allow structured config blocks such as early_mvp_filters.
            continue

        else:
            raise ValueError(
                f"Value for '{key}' must be either a list or a dictionary."
            )

    return data