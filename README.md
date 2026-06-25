# AirlineCareerAgent

AirlineCareerAgent is a Python-based automation project designed to identify relevant job openings across airline, aviation technology, and travel software companies.

The project focuses on collecting career opportunities from selected company websites, filtering them by role and domain relevance, and organizing the results for review.

## Project Goal

The goal of AirlineCareerAgent is to demonstrate practical automation, job-search workflow design, and applied agentic AI concepts in a real-world career search use case.

The system is intended to:

* Search selected airline and travel-tech company career pages
* Identify relevant QA, automation, software testing, and technology roles
* Filter jobs using role-specific and domain-specific keywords
* Store job results in a structured format
* Provide a foundation for future AI-assisted job matching and reporting

## Current Scope

This repository is currently in the initial setup phase.

Current focus:

* Project structure
* Safe configuration management
* Git and GitHub workflow
* Environment variable setup
* Initial documentation

## MVP Scope

The first version of the project will focus on a controlled, maintainable workflow:

* Define a list of target companies
* Store company career page URLs
* Visit selected career pages
* Collect visible job posting data where technically feasible
* Filter jobs by relevant keywords
* Save results to a local CSV or JSON file

## Out of Scope for the Initial Version

The initial version will not:

* Automatically apply to jobs
* Store passwords or private credentials
* Bypass website protections
* Use personal job application data
* Depend on paid AI services

## Tech Stack

Planned stack:

* Python
* Playwright
* `python-dotenv`
* Git and GitHub
* CSV or JSON for initial data storage
* PyCharm as the development environment

Potential future additions:

* AI-assisted job relevance scoring
* Scheduled job checks
* Database storage
* Report generation
* Streamlit or lightweight dashboard interface

## Suggested Project Structure

```text
AirlineCareerAgent/
├── README.md
├── .env.example
├── .gitignore
├── requirements.txt
├── src/
│   └── main.py
├── data/
│   └── .gitkeep
├── tests/
│   └── .gitkeep
└── docs/
    └── notes.md
```

## Environment Variables

The project uses environment variables for configuration.

The `.env.example` file provides a safe template for local settings.

Do not commit the real `.env` file to GitHub.

To create a local `.env` file:

```bash
cp .env.example .env
```

On Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

Then edit `.env` locally.

## Git Workflow

Recommended feature-branch workflow:

```bash
git checkout main
git pull origin main
git checkout -b feature/readme-env-example
git status
git add README.md .env.example
git commit -m "Add initial README and env example"
git push origin feature/readme-env-example
```

## Security Notes

This repository should not contain:

* API keys
* Passwords
* Personal tokens
* Resume files
* Private job application data
* Real `.env` files

Use `.env.example` for safe configuration examples only.

## Planned Next Steps

1. Add `.gitignore`
2. Add `requirements.txt`
3. Create the initial `src/main.py`
4. Define the target company list
5. Define role and domain keyword filters
6. Add the first controlled career-page check
7. Save matched job results locally
