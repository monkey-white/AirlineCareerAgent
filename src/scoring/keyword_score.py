from __future__ import annotations


def find_keyword_matches(text: str, keywords: list[str]) -> list[str]:
    """
    Return keywords found in the provided text, case-insensitively.
    """
    normalized_text = text.lower()

    return [
        keyword
        for keyword in keywords
        if keyword.lower() in normalized_text
    ]


def score_job_link(
    job_link: dict[str, str],
    role_keywords: list[str],
    domain_keywords: list[str],
) -> dict[str, object]:
    """
    Score a collected job link using simple keyword matching.

    MVP scoring:
    - Role keyword match: up to 50 points
    - Domain keyword match: up to 30 points
    """
    title = job_link.get("title", "")
    url = job_link.get("url", "")
    searchable_text = f"{title} {url}"

    matched_role_keywords = find_keyword_matches(searchable_text, role_keywords)
    matched_domain_keywords = find_keyword_matches(searchable_text, domain_keywords)

    role_score = min(len(matched_role_keywords) * 15, 50)
    domain_score = min(len(matched_domain_keywords) * 10, 30)
    fit_score = role_score + domain_score

    matched_keywords = matched_role_keywords + matched_domain_keywords

    return {
        **job_link,
        "fit_score": fit_score,
        "matched_keywords": "; ".join(matched_keywords),
        "reason": build_reason(
            matched_role_keywords=matched_role_keywords,
            matched_domain_keywords=matched_domain_keywords,
            fit_score=fit_score,
        ),
    }


def build_reason(
    matched_role_keywords: list[str],
    matched_domain_keywords: list[str],
    fit_score: int,
) -> str:
    """
    Build a short human-readable explanation for the score.
    """
    if fit_score == 0:
        return "No configured role or domain keywords matched."

    reason_parts: list[str] = []

    if matched_role_keywords:
        reason_parts.append(
            f"Matched role keywords: {', '.join(matched_role_keywords)}"
        )

    if matched_domain_keywords:
        reason_parts.append(
            f"Matched domain keywords: {', '.join(matched_domain_keywords)}"
        )

    return " | ".join(reason_parts)