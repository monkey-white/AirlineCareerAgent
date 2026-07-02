# src/collectors/playwright_collector.py
from urllib.parse import urljoin

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import sync_playwright


JOB_LINK_KEYWORDS = (
    "job",
    "jobs",
    "career",
    "careers",
    "opening",
    "openings",
    "position",
    "positions",
    "apply",
    "requisition",
    "greenhouse",
    "lever",
    "workday",
    "smartrecruiters",
    "ashby",
    "icims",
)


def looks_like_job_link(text: str, href: str) -> bool:
    """
    Decide whether a link looks related to jobs/careers.

    This is intentionally broad for the first MVP collector.
    Later we can make this smarter per ATS/platform.
    """
    combined = f"{text} {href}".lower()

    return any(keyword in combined for keyword in JOB_LINK_KEYWORDS)


def collect_job_links(
    company_name: str,
    career_url: str,
    headless: bool = True,
    timeout_ms: int = 30_000,
) -> list[dict[str, str]]:
    """
    Visit a company career page and collect job-like links.

    Args:
        company_name: Company name from config.
        career_url: Company career page URL.
        headless: Whether to run the browser invisibly.
        timeout_ms: Page load timeout in milliseconds.

    Returns:
        A list of dictionaries with company, title, and url.
    """
    results: list[dict[str, str]] = []

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=headless)
        page = browser.new_page()

        try:
            page.goto(career_url, wait_until="domcontentloaded", timeout=timeout_ms)
            page.wait_for_timeout(2_000)

            links = page.locator("a").all()

            for link in links:
                text = link.inner_text().strip()

                href = link.get_attribute("href")
                if not href:
                    continue

                absolute_url = urljoin(career_url, href)

                if not text:
                    text = absolute_url

                if looks_like_job_link(text, absolute_url):
                    results.append(
                        {
                            "company": company_name,
                            "title": text,
                            "url": absolute_url,
                        }
                    )

        except PlaywrightTimeoutError:
            print(f"Timed out while loading career page for {company_name}: {career_url}")

        finally:
            browser.close()

    return deduplicate_job_links(results)


def deduplicate_job_links(job_links: list[dict[str, str]]) -> list[dict[str, str]]:
    """
    Remove duplicate links while preserving original order.
    """
    seen_urls: set[str] = set()
    unique_links: list[dict[str, str]] = []

    for job_link in job_links:
        url = job_link["url"]

        if url in seen_urls:
            continue

        seen_urls.add(url)
        unique_links.append(job_link)

    return unique_links