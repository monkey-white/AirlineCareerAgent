# AirlineCareerAgent Project Brief

## 1. Project Name

**AirlineCareerAgent**

## 2. Project Goal

Build an AI-assisted job-search agent that helps identify relevant job openings for a QA automation professional with Accelya/Farelogix airline technology experience.

The agent should check selected airline, travel-tech, GDS, NDC, pricing, retailing, and travel-commerce companies for relevant openings, then rank and report the best-fit roles.

The first version should focus on finding and scoring roles, not applying automatically.

## 3. User Background

The user has experience as a **QA Automation Analyst** and previously worked for **Accelya Corp**, coming from a **Farelogix background**.

Relevant domain background includes:

* Airline technology
* Airline distribution
* Farelogix-style airline retailing
* NDC
* Airline shopping and booking flows
* Fares and pricing
* Ticketing
* Travel-commerce platforms
* API and integration testing
* QA automation
* Test validation across airline/travel systems

The user is looking for jobs in the same or closely related industry.

## 4. Target Role Types

The agent should prioritize roles such as:

* QA Automation Engineer
* Senior QA Automation Engineer
* QA Analyst
* Senior QA Analyst
* Quality Engineer
* Senior Quality Engineer
* SDET
* Software Development Engineer in Test
* Test Automation Engineer
* API Test Engineer
* Integration Test Engineer
* Automation Analyst
* QA Engineer, Travel Platform
* QA Engineer, Airline Systems
* QA Engineer, NDC
* Product QA Analyst
* Technical QA Analyst
* Business Analyst with airline/NDC domain
* Implementation Analyst
* Solutions Analyst
* Airline Distribution Analyst
* Travel Technology Analyst

## 5. Target Companies

### Highest-priority companies

These companies are closest to the user’s Accelya/Farelogix background:

1. Sabre
2. Amadeus
3. Travelport
4. ATPCO
5. PROS
6. Datalex
7. Lufthansa Systems
8. Navitaire
9. OpenJaw Technologies
10. ARC

### Secondary target companies

11. OAG
12. Cirium
13. SITA
14. IBS Software
15. TPConnects
16. Mystifly
17. Duffel
18. Hopper
19. Expedia Group
20. Booking Holdings / Priceline / Agoda

### Broader travel-tech and corporate travel targets

21. American Express Global Business Travel
22. BCD Travel
23. CWT
24. Navan
25. Spotnana
26. Serko
27. Kayak
28. Google Travel
29. Airline pricing / fare technology vendors
30. Airline digital teams: American Airlines, United Airlines, Delta Air Lines, Southwest Airlines, JetBlue

## 6. Suggested Initial Company Config

```yaml
companies:
  - name: Sabre
    career_url: https://www.sabre.com/careers/
    priority: high

  - name: Amadeus
    career_url: https://amadeus.com/en/careers
    priority: high

  - name: Travelport
    career_url: https://www.travelport.com/careers
    priority: high

  - name: ATPCO
    career_url: https://www.atpco.net/careers
    priority: high

  - name: PROS
    career_url: https://pros.com/careers/
    priority: high

  - name: Datalex
    career_url: https://www.datalex.com/careers/
    priority: high

  - name: Lufthansa Systems
    career_url: https://www.lhsystems.com/careers
    priority: high

  - name: OpenJaw Technologies
    career_url: https://www.openjawtech.com/careers/
    priority: high

  - name: ARC
    career_url: https://www2.arccorp.com/about-us/careers/
    priority: high

  - name: SITA
    career_url: https://www.sita.aero/careers/
    priority: medium

  - name: IBS Software
    career_url: https://www.ibsplc.com/careers/
    priority: medium

  - name: TPConnects
    career_url: https://www.tpconnects.com/careers/
    priority: medium

  - name: Mystifly
    career_url: https://www.mystifly.com/careers/
    priority: medium

  - name: Duffel
    career_url: https://duffel.com/careers
    priority: medium

  - name: Hopper
    career_url: https://www.hopper.com/careers
    priority: medium

  - name: Expedia Group
    career_url: https://careers.expediagroup.com/
    priority: medium

  - name: Navan
    career_url: https://navan.com/careers
    priority: medium

  - name: Spotnana
    career_url: https://www.spotnana.com/careers
    priority: medium

  - name: Serko
    career_url: https://www.serko.com/careers
    priority: medium

  - name: American Express Global Business Travel
    career_url: https://www.amexglobalbusinesstravel.com/careers/
    priority: medium
```

## 7. Role Keywords

The agent should search for these role-related keywords:

```yaml
role_keywords:
  - QA Automation
  - QA Engineer
  - Senior QA Engineer
  - Quality Engineer
  - Senior Quality Engineer
  - SDET
  - Software Development Engineer in Test
  - Test Automation
  - Test Automation Engineer
  - Automation Engineer
  - API Testing
  - Integration Testing
  - Test Engineer
  - QA Analyst
  - Quality Assurance
  - Software QA
  - Manual QA
  - Regression Testing
  - Functional Testing
  - UAT
  - Business Analyst
  - Product Analyst
  - Implementation Analyst
  - Solutions Analyst
```

## 8. Airline / Travel-Tech Domain Keywords

The agent should give extra relevance to jobs containing these airline/travel-tech terms:

```yaml
domain_keywords:
  - airline
  - airlines
  - travel
  - travel technology
  - travel tech
  - NDC
  - IATA
  - GDS
  - Sabre
  - Amadeus
  - Travelport
  - Farelogix
  - Accelya
  - fare
  - fares
  - pricing
  - fare pricing
  - dynamic pricing
  - revenue management
  - booking
  - reservation
  - reservations
  - PSS
  - passenger service system
  - ticketing
  - e-ticket
  - EMD
  - ancillary
  - ancillaries
  - offer
  - order
  - offer management
  - order management
  - airline retailing
  - merchandising
  - distribution
  - airline distribution
  - shopping
  - availability
  - itinerary
  - PNR
  - agency
  - corporate travel
  - OTA
  - online travel agency
  - flight
  - flights
  - settlement
  - ARC
  - ATPCO
```

## 9. Technical Keywords

The agent should also detect technical fit using these terms:

```yaml
technical_keywords:
  - Python
  - Java
  - JavaScript
  - TypeScript
  - Selenium
  - Playwright
  - Cypress
  - Postman
  - REST API
  - SOAP
  - JSON
  - XML
  - SQL
  - CI/CD
  - Jenkins
  - GitHub Actions
  - Git
  - Agile
  - Jira
  - test automation framework
  - API automation
  - integration testing
  - regression suite
  - test cases
  - test strategy
```

## 10. MVP Scope

The first version of AirlineCareerAgent should do the following:

1. Load a list of companies from a config file.
2. Visit each company’s career page.
3. Detect visible job listings or links.
4. Search job titles and descriptions for relevant role keywords.
5. Apply airline/travel-tech domain scoring.
6. Rank jobs by fit score.
7. Export results to CSV.
8. Optionally export results to HTML.
9. Avoid auto-applying to jobs.
10. Keep logs of visited companies and any failures.

## 11. Non-MVP / Later Features

Later versions can add:

* ATS-specific collectors for Greenhouse, Lever, Workday, SmartRecruiters, Ashby, and iCIMS
* LLM-based job fit scoring
* Resume-to-job matching
* Cover letter draft generation
* Saved job history
* Duplicate detection across runs
* Daily or weekly monitoring
* Email summary report
* Streamlit dashboard
* RAG search over saved job postings and resume files
* Interview preparation based on selected job descriptions

## 12. Recommended Tech Stack

### Beginner MVP

```text
Python
VS Code or PyCharm
Playwright
pandas
BeautifulSoup
rapidfuzz
CSV export
```

### Later AI-enhanced version

```text
Python
Playwright
requests
pandas
BeautifulSoup
rapidfuzz
OpenAI API or local LLM
YAML config files
SQLite
Streamlit
```

## 13. Recommended Folder Structure

```text
AirlineCareerAgent/
  README.md
  requirements.txt
  .gitignore

  config/
    companies.yaml
    keywords.yaml

  src/
    main.py

    company_loader.py
    keyword_loader.py

    collectors/
      __init__.py
      playwright_collector.py
      greenhouse_collector.py
      lever_collector.py
      workday_collector.py

    scoring/
      __init__.py
      keyword_score.py
      llm_score.py

    output/
      __init__.py
      csv_report.py
      html_report.py

    utils/
      __init__.py
      logger.py
      dedupe.py
      text_cleaner.py

  output/
    airline_career_agent_results.csv
    airline_career_agent_results.html

  logs/
    run.log
```

## 14. Suggested Requirements File

```text
playwright
pandas
beautifulsoup4
rapidfuzz
pyyaml
requests
```

After installing requirements, Playwright needs this command:

```bash
playwright install
```

## 15. Fit Scoring Logic

The first scoring version can be rule-based.

Suggested scoring:

```text
Role keyword match: up to 50 points
Airline/travel-tech domain match: up to 30 points
Technical keyword match: up to 15 points
Seniority/location/remote preference: up to 5 points

Maximum score: 100
```

Example interpretation:

```text
90-100: Excellent fit
75-89: Strong fit
60-74: Possible fit
40-59: Weak fit
0-39: Ignore
```

## 16. Example Job Output Format

```csv
company,title,location,fit_score,matched_keywords,reason,url
Sabre,Senior QA Automation Engineer,Remote,92,"QA Automation; API Testing; airline; distribution","Strong QA automation and airline distribution match",https://...
ATPCO,Quality Engineer,Hybrid,88,"Quality Engineer; fare; pricing; ATPCO","Excellent fare/pricing domain match",https://...
```

## 17. Step-by-Step Build Plan

### Step 1: Local setup

Install:

```text
Python
VS Code or PyCharm
Git, optional
```

Verify Python:

```bash
python --version
pip --version
```

Create the project folder:

```bash
mkdir AirlineCareerAgent
cd AirlineCareerAgent
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

Windows:

```bash
.venv\Scripts\activate
```

Mac/Linux:

```bash
source .venv/bin/activate
```

Install packages:

```bash
pip install playwright pandas beautifulsoup4 rapidfuzz pyyaml requests
playwright install
```

### Step 2: Create config files

Create:

```text
config/companies.yaml
config/keywords.yaml
```

Add company career URLs and keyword lists.

### Step 3: Build the first Playwright collector

Create:

```text
src/collectors/playwright_collector.py
```

Goal:

* Visit one career page
* Extract all links
* Keep links that look like job postings
* Return title, URL, and company name

### Step 4: Build keyword scoring

Create:

```text
src/scoring/keyword_score.py
```

Goal:

* Score title and description against role keywords
* Add bonus for airline/travel-tech keywords
* Add bonus for API/testing/tool keywords

### Step 5: Build CSV report

Create:

```text
src/output/csv_report.py
```

Goal:

* Save all matching jobs to `output/airline_career_agent_results.csv`

### Step 6: Build main script

Create:

```text
src/main.py
```

Goal:

* Load companies
* Visit each career page
* Collect matching jobs
* Score jobs
* Deduplicate jobs
* Export CSV

### Step 7: Run MVP

Run:

```bash
python src/main.py
```

Expected result:

```text
Checking Sabre...
Checking Amadeus...
Checking Travelport...
...
Saved output/airline_career_agent_results.csv
```

### Step 8: Improve with ATS connectors

After the MVP works, add collectors for:

```text
Greenhouse
Lever
Workday
SmartRecruiters
Ashby
iCIMS
```

Use ATS APIs or public job feeds when available. This is usually more reliable than scraping dynamic pages.

### Step 9: Add AI scoring

Add an LLM-based scoring step that evaluates each job description against this profile:

```text
QA automation analyst with Accelya/Farelogix background, airline distribution experience, NDC familiarity, API/integration testing experience, and interest in airline/travel-tech roles.
```

The AI should return:

```json
{
  "fit_score": 0,
  "reason": "",
  "matched_keywords": [],
  "concerns": []
}
```

### Step 10: Add reporting

Later reports can include:

* CSV
* HTML
* Markdown
* Email summary
* Streamlit dashboard

## 18. Agent Rules

The agent should:

* Find and rank relevant jobs.
* Avoid auto-applying.
* Respect website rate limits.
* Prefer public APIs or ATS feeds when available.
* Avoid excessive scraping.
* Log errors clearly.
* Deduplicate jobs.
* Keep the user in control of applications.
* Treat fit scores as recommendations, not final decisions.

## 19. Initial Success Criteria

The MVP is successful when it can:

1. Check at least 10 company career pages.
2. Find job-like links or postings.
3. Filter for QA/SDET/Test Automation/Analyst roles.
4. Add airline/travel-tech relevance scoring.
5. Export a CSV report.
6. Produce useful job leads without manual searching each company site.

## 20. One-Sentence Project Summary

**AirlineCareerAgent is a Python-based AI-assisted job discovery tool that monitors airline and travel-tech companies for QA automation, SDET, analyst, and airline retailing roles that match an Accelya/Farelogix background.**
