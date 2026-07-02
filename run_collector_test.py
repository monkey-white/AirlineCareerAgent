from src.config_loader import load_companies_config
from src.collectors.playwright_collector import collect_job_links


def main() -> None:
    companies = load_companies_config()

    first_company = companies[0]
    company_name = first_company["name"]
    career_url = first_company["career_url"]

    print(f"Checking {company_name}...")
    print(f"URL: {career_url}")
    print()

    job_links = collect_job_links(
        company_name=company_name,
        career_url=career_url,
        headless=True,
    )

    print(f"Job-like links found: {len(job_links)}")
    print("=" * 50)

    for job_link in job_links[:20]:
        print(f"Company: {job_link['company']}")
        print(f"Title: {job_link['title']}")
        print(f"URL: {job_link['url']}")
        print("-" * 50)


if __name__ == "__main__":
    main()