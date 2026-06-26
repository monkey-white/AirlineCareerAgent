import json
from pathlib import Path

import pytest

from src import config_loader


def write_json(file_path: Path, data: object) -> None:
    file_path.write_text(json.dumps(data), encoding="utf-8")


def test_load_json_config_successfully_reads_valid_json(tmp_path):
    config_file = tmp_path / "sample.json"
    expected_data = {"name": "AirlineCareerAgent", "enabled": True}

    write_json(config_file, expected_data)

    result = config_loader.load_json_config(config_file)

    assert result == expected_data


def test_load_json_config_raises_error_for_missing_file(tmp_path):
    missing_file = tmp_path / "missing.json"

    with pytest.raises(FileNotFoundError, match="Config file not found"):
        config_loader.load_json_config(missing_file)


def test_load_json_config_raises_error_for_invalid_json(tmp_path):
    config_file = tmp_path / "invalid.json"
    config_file.write_text("{invalid json", encoding="utf-8")

    with pytest.raises(ValueError, match="Invalid JSON"):
        config_loader.load_json_config(config_file)


def test_load_json_config_raises_error_for_empty_file(tmp_path):
    config_file = tmp_path / "empty.json"
    config_file.write_text("", encoding="utf-8")

    with pytest.raises(ValueError, match="Config file is empty"):
        config_loader.load_json_config(config_file)


def test_load_companies_config_success(monkeypatch, tmp_path):
    companies_file = tmp_path / "companies.json"
    company_data = [
        {
            "name": "Sabre",
            "career_url": "https://www.sabre.com/careers/",
            "category": "travel_technology",
            "notes": "Travel technology company",
        }
    ]

    write_json(companies_file, company_data)
    monkeypatch.setattr(config_loader, "COMPANIES_CONFIG", companies_file)

    result = config_loader.load_companies_config()

    assert result == company_data
    assert result[0]["name"] == "Sabre"


def test_load_companies_config_rejects_non_list(monkeypatch, tmp_path):
    companies_file = tmp_path / "companies.json"

    write_json(companies_file, {"name": "Sabre"})
    monkeypatch.setattr(config_loader, "COMPANIES_CONFIG", companies_file)

    with pytest.raises(ValueError, match="companies.json must contain a list"):
        config_loader.load_companies_config()


def test_load_role_keywords_config_success(monkeypatch, tmp_path):
    role_keywords_file = tmp_path / "role_keywords.json"
    keyword_data = {
        "role_keywords": ["QA Automation", "SDET"],
        "domain_keywords": ["airline", "ticketing"],
        "early_mvp_filters": {
            "locations": ["Remote", "United States"],
            "employment_types": ["Full-time"],
        },
    }

    write_json(role_keywords_file, keyword_data)
    monkeypatch.setattr(config_loader, "ROLE_KEYWORDS_CONFIG", role_keywords_file)

    result = config_loader.load_role_keywords_config()

    assert result == keyword_data
    assert "QA Automation" in result["role_keywords"]
    assert result["early_mvp_filters"]["locations"] == ["Remote", "United States"]


def test_load_role_keywords_config_rejects_non_dict(monkeypatch, tmp_path):
    role_keywords_file = tmp_path / "role_keywords.json"

    write_json(role_keywords_file, ["QA Automation", "SDET"])
    monkeypatch.setattr(config_loader, "ROLE_KEYWORDS_CONFIG", role_keywords_file)

    with pytest.raises(ValueError, match="role_keywords.json must contain a dictionary"):
        config_loader.load_role_keywords_config()


def test_load_role_keywords_config_rejects_non_string_keywords(monkeypatch, tmp_path):
    role_keywords_file = tmp_path / "role_keywords.json"

    write_json(
        role_keywords_file,
        {
            "role_keywords": ["QA Automation", 123],
        },
    )
    monkeypatch.setattr(config_loader, "ROLE_KEYWORDS_CONFIG", role_keywords_file)

    with pytest.raises(ValueError, match="All items in role keyword list"):
        config_loader.load_role_keywords_config()


def test_load_role_keywords_config_rejects_invalid_value_type(monkeypatch, tmp_path):
    role_keywords_file = tmp_path / "role_keywords.json"

    write_json(
        role_keywords_file,
        {
            "role_keywords": ["QA Automation"],
            "invalid_section": True,
        },
    )
    monkeypatch.setattr(config_loader, "ROLE_KEYWORDS_CONFIG", role_keywords_file)

    with pytest.raises(ValueError, match="must be either a list or a dictionary"):
        config_loader.load_role_keywords_config()