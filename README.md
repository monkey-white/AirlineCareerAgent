# Targeted Job Search Agent

Targeted Job Search Agent is a configurable Python-based automation project designed to identify relevant job openings from selected company career pages.

The project focuses on collecting career opportunities, filtering them by role and domain relevance, scoring potential matches, and organizing results for review.

The initial profile focuses on QA automation, software testing, analyst, airline, aviation technology, and travel software roles. The long-term goal is to support additional search profiles such as finance QA, healthcare QA, general SDET roles, and other targeted career searches.

## Project Goal

The goal of Targeted Job Search Agent is to demonstrate practical automation, job-search workflow design, and applied agentic AI concepts in a real-world career search use case.

The system is intended to:

* Search selected company career pages
* Identify relevant QA, automation, software testing, analyst, and technology roles
* Filter jobs using role-specific and domain-specific keywords
* Store job results in a structured format
* Generate user-friendly reports for manual review and application decisions
* Provide a foundation for future AI-assisted job matching and application tracking

## Current Scope

This repository is currently in the early MVP phase.

Current focus:

* Project structure
* Safe configuration management
* Git and GitHub workflow
* Environment variable setup
* Initial documentation
* Career page link collection
* Keyword-based scoring
* CSV result export

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

The project is organized as follows:

- `README.md` - project overview and usage notes
- `.env.example` - safe template for local environment variables
- `.gitignore` - files and folders excluded from Git
- `requirements.txt` - Python dependencies
- `config/` - company and keyword configuration files
- `src/` - application source code
  - `main.py` - MVP pipeline entry point
  - `cli.py` - configuration summary CLI
  - `config_loader.py` - configuration loading helpers
  - `collectors/` - career page collectors
  - `scoring/` - job scoring logic
  - `output/` - CSV and future report writers
- `data/` - local data files, kept out of Git except `.gitkeep`
- `outputs/` - generated reports, kept out of Git except `.gitkeep`
- `tests/` - automated tests

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

This project uses a feature-branch workflow.

Avoid committing directly to `main` for normal development work. Instead, create a feature branch, push it to GitHub, and open a Pull Request.

### Start a new feature branch

Run these commands from the project root:

```powershell
git checkout main
git pull origin main
git checkout -b feature/descriptive-branch-name
```

Example:

```powershell
git checkout -b feature/workday-collector
```

### Check changes before committing

```powershell
git status
```

Make sure private files such as `.env` are not staged.

### Run tests

```powershell
pytest
```

### Commit changes

Stage only the files that should be included:

```powershell
git add README.md
```

Or stage a specific source file:

```powershell
git add src/collectors/playwright_collector.py
```

Then commit:

```powershell
git commit -m "Describe the change clearly"
```

### Push the feature branch

```powershell
git push origin feature/descriptive-branch-name
```

After pushing, open a Pull Request on GitHub.

### Pull Request description template

Use this template for Pull Request descriptions:

```markdown
## Summary

- Added/changed ...
- Added/changed ...

## Testing

- Ran `pytest`
- Ran manual command if applicable: `python run_collector_test.py`

## Notes

- No secrets or private files were committed.
- This change does not auto-apply to jobs.
- Follow-up work: ...
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

1. Add HTML report generation for reviewed job results
2. Open the HTML report automatically at the end of a run
3. Add company-level collection status tracking
4. Include failed or no-result companies in the report
5. Improve job-link filtering to reduce noisy results
6. Add profile-based configuration for different job searches
7. Add persistent application tracking for statuses, notes, and resume versions

## CLI Usage

Targeted Job Search Agent includes a simple CLI entry point that loads the local configuration files and prints a summary.

Run from the project root:

```powershell
python -m src.cli
```

The CLI displays:

* number of configured companies
* company names
* number of role keywords
* number of domain keywords
* early MVP filters