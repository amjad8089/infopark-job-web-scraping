# Infopark Job Web Scraping

## Project Overview
A Python-based web scraping application developed to extract job listing information from the Infopark website and organize the collected information into an Excel spreadsheet.

## Features
- Extracts company names and job titles.
- Collects job posting dates and application deadlines.
- Retrieves individual job detail page links.
- Processes extracted information using Pandas.
- Exports structured job data into an Excel file.
- Includes HTTP error handling and request timeouts.

## Technologies Used
- Python
- Requests
- BeautifulSoup
- Pandas
- LXML
- Excel

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## How to Run

Execute the following command:

```bash
python infopark_scraper.py
```

The extracted job listings are saved as:

`infopark_jobs.xlsx`

## Data Source
[Infopark – Companies and Jobs](https://infopark.in/companies-job)

## Author
**MUHAMMED AMJAD P A**

[GitHub Profile](https://github.com/amjad8089)
