from __future__ import annotations

import webbrowser
from pathlib import Path
from typing import Any

from src.collectors.playwright_collector import collect_job_links
from src.config_loader import load_companies_config, load_role_keywords_config
from src.output.csv_report import save_jobs_to_csv
from src.output.html_report import save_jobs_to_html
from src.scoring.keyword_score import score_job_link


CSV_OUTPUT_PATH = Path("outputs/targeted_job_search_results.csv")
HTML_OUTPUT_PATH = Path("outputs/targeted_job_search_results.html")
MINIMUM_FIT_SCORE = 1


def main() -> None:
    """
    Run the first MVP pipeline:
    - load config
    - collect job-like links
    - score links
    - save CSV report
    - save HTML report
    - open HTML report
    """
    companies = load_companies_config()
    keyword_config = load_role_keywords_config()

    role_keywords = keyword_config["role_keywords"]
    domain_keywords = keyword_config["domain_keywords"]

    all_scored_jobs: list[dict[str, Any]] = []
    company_results: list[dict[str, Any]] = []

    print(f"Loaded {len(companies)} companies.")
    print("Starting collection...")
    print("=" * 60)

    for company in companies:
        company_name = company["name"]
        career_url = company["career_url"]

        print(f"Checking {company_name}...")
        print(f"URL: {career_url}")

        try:
            job_links = collect_job_links(
                company_name=company_name,
                career_url=career_url,
                headless=True,
            )

            print(f"Collected job-like links: {len(job_links)}")

            scored_jobs = [
                score_job_link(
                    job_link=job_link,
                    role_keywords=role_keywords,
                    domain_keywords=domain_keywords,
                )
                for job_link in job_links
            ]

            matching_jobs = [
                job
                for job in scored_jobs
                if int(job["fit_score"]) >= MINIMUM_FIT_SCORE
            ]

            print(f"Keyword-matched jobs: {len(matching_jobs)}")

            if matching_jobs:
                status = "success_with_matches"
            else:
                status = "success_no_matches"

            company_results.append(
                {
                    "company": company_name,
                    "career_url": career_url,
                    "status": status,
                    "collected_count": len(job_links),
                    "matched_count": len(matching_jobs),
                    "error_message": "",
                }
            )

            all_scored_jobs.extend(matching_jobs)

        except Exception as error:
            error_message = str(error)
            print(f"Failed while checking {company_name}: {error_message}")

            company_results.append(
                {
                    "company": company_name,
                    "career_url": career_url,
                    "status": "failed_error",
                    "collected_count": 0,
                    "matched_count": 0,
                    "error_message": error_message,
                }
            )

        print("-" * 60)

    all_scored_jobs.sort(
        key=lambda job: int(job["fit_score"]),
        reverse=True,
    )

    save_jobs_to_csv(
        jobs=all_scored_jobs,
        output_path=CSV_OUTPUT_PATH,
    )

    save_jobs_to_html(
        matched_jobs=all_scored_jobs,
        company_results=company_results,
        output_path=HTML_OUTPUT_PATH,
    )

    print("=" * 60)
    print(f"Saved {len(all_scored_jobs)} scored job links to:")
    print(CSV_OUTPUT_PATH)
    print()
    print("Saved HTML report to:")
    print(HTML_OUTPUT_PATH)

    webbrowser.open(HTML_OUTPUT_PATH.resolve().as_uri())


if __name__ == "__main__":
    main()