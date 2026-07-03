from __future__ import annotations

import html
from datetime import datetime
from pathlib import Path
from typing import Any


def save_jobs_to_html(
    matched_jobs: list[dict[str, Any]],
    company_results: list[dict[str, Any]],
    output_path: Path,
) -> None:
    """
    Save a human-friendly HTML report with matched jobs and company run status.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)

    successful_no_matches = [
        result
        for result in company_results
        if result["status"] == "success_no_matches"
    ]

    failed_results = [
        result
        for result in company_results
        if result["status"].startswith("failed")
    ]

    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Targeted Job Search Agent Report</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 32px;
            background: #f7f8fa;
            color: #222;
        }}
        h1, h2 {{
            color: #1f2937;
        }}
        .summary {{
            display: grid;
            grid-template-columns: repeat(4, minmax(150px, 1fr));
            gap: 16px;
            margin-bottom: 32px;
        }}
        .summary-card,
        .job-card,
        .status-card {{
            background: #ffffff;
            border: 1px solid #d9dde3;
            border-radius: 10px;
            padding: 16px;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.06);
        }}
        .summary-card strong {{
            display: block;
            font-size: 24px;
            margin-top: 4px;
        }}
        .job-card {{
            margin-bottom: 16px;
        }}
        .status-card {{
            margin-bottom: 12px;
        }}
        .score {{
            display: inline-block;
            background: #e0f2fe;
            color: #075985;
            padding: 4px 8px;
            border-radius: 999px;
            font-weight: bold;
        }}
        .failed {{
            border-left: 5px solid #dc2626;
        }}
        .no-match {{
            border-left: 5px solid #f59e0b;
        }}
        .button {{
            display: inline-block;
            margin-top: 10px;
            padding: 8px 12px;
            background: #2563eb;
            color: #ffffff;
            text-decoration: none;
            border-radius: 6px;
        }}
        .muted {{
            color: #6b7280;
        }}
        code {{
            background: #eef2f7;
            padding: 2px 4px;
            border-radius: 4px;
        }}
    </style>
</head>
<body>
    <h1>Targeted Job Search Agent Report</h1>
    <p class="muted">Generated at {html.escape(generated_at)}</p>

    <section class="summary">
        <div class="summary-card">
            Companies checked
            <strong>{len(company_results)}</strong>
        </div>
        <div class="summary-card">
            Matched jobs
            <strong>{len(matched_jobs)}</strong>
        </div>
        <div class="summary-card">
            No-match companies
            <strong>{len(successful_no_matches)}</strong>
        </div>
        <div class="summary-card">
            Failed companies
            <strong>{len(failed_results)}</strong>
        </div>
    </section>

    <h2>Matched Jobs</h2>
    {build_matched_jobs_html(matched_jobs)}

    <h2>Companies With No Matching Jobs</h2>
    {build_no_matches_html(successful_no_matches)}

    <h2>Failed / Needs Review</h2>
    {build_failed_results_html(failed_results)}
</body>
</html>
"""

    output_path.write_text(html_content, encoding="utf-8")


def build_matched_jobs_html(jobs: list[dict[str, Any]]) -> str:
    if not jobs:
        return "<p>No matched jobs found for this run.</p>"

    cards: list[str] = []

    for job in jobs:
        company = html.escape(str(job.get("company", "")))
        title = html.escape(str(job.get("title", "")))
        fit_score = html.escape(str(job.get("fit_score", "")))
        matched_keywords = html.escape(str(job.get("matched_keywords", "")))
        reason = html.escape(str(job.get("reason", "")))
        url = html.escape(str(job.get("url", "")), quote=True)

        cards.append(
            f"""
            <div class="job-card">
                <h3>{title}</h3>
                <p><strong>Company:</strong> {company}</p>
                <p><span class="score">Fit score: {fit_score}</span></p>
                <p><strong>Matched keywords:</strong> {matched_keywords or "None"}</p>
                <p><strong>Reason:</strong> {reason or "No reason provided."}</p>
                <a class="button" href="{url}" target="_blank" rel="noopener noreferrer">
                    Open job posting
                </a>
            </div>
            """
        )

    return "\n".join(cards)


def build_no_matches_html(results: list[dict[str, Any]]) -> str:
    if not results:
        return "<p>No companies landed in this category.</p>"

    cards: list[str] = []

    for result in results:
        company = html.escape(str(result.get("company", "")))
        career_url = html.escape(str(result.get("career_url", "")), quote=True)
        collected_count = html.escape(str(result.get("collected_count", 0)))

        cards.append(
            f"""
            <div class="status-card no-match">
                <h3>{company}</h3>
                <p>Checked successfully, but no jobs matched the configured keywords.</p>
                <p><strong>Job-like links collected:</strong> {collected_count}</p>
                <a href="{career_url}" target="_blank" rel="noopener noreferrer">
                    Open career page manually
                </a>
            </div>
            """
        )

    return "\n".join(cards)


def build_failed_results_html(results: list[dict[str, Any]]) -> str:
    if not results:
        return "<p>No failed companies in this run.</p>"

    cards: list[str] = []

    for result in results:
        company = html.escape(str(result.get("company", "")))
        career_url = html.escape(str(result.get("career_url", "")), quote=True)
        status = html.escape(str(result.get("status", "")))
        error_message = html.escape(str(result.get("error_message", "")))

        cards.append(
            f"""
            <div class="status-card failed">
                <h3>{company}</h3>
                <p><strong>Status:</strong> <code>{status}</code></p>
                <p><strong>Reason:</strong> {error_message or "No error message captured."}</p>
                <a href="{career_url}" target="_blank" rel="noopener noreferrer">
                    Open career page manually
                </a>
            </div>
            """
        )

    return "\n".join(cards)