from src.config_loader import load_companies_config, load_role_keywords_config


def main() -> None:
    companies = load_companies_config()
    role_keywords_config = load_role_keywords_config()

    role_keywords = role_keywords_config.get("role_keywords", [])
    domain_keywords = role_keywords_config.get("domain_keywords", [])
    early_mvp_filters = role_keywords_config.get("early_mvp_filters", [])

    print("Targeted Job Search Agent Config Summary")
    print("=" * 42)

    print(f"Companies loaded: {len(companies)}")
    print("Company names:")
    for company in companies:
        print(f"- {company.get('name', 'UNKNOWN')}")

    print()
    print(f"Role keywords: {len(role_keywords)}")
    print(f"Domain keywords: {len(domain_keywords)}")

    print()
    print("Early MVP filters:")
    if early_mvp_filters:
        for item in early_mvp_filters:
            print(f"- {item}")
    else:
        print("- None configured")


if __name__ == "__main__":
    main()