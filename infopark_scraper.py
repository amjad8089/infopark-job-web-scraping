import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "https://infopark.in/companies-job"

# Using a full browser User-Agent to avoid potential HTTP 403 blocks
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

try:
    res = requests.get(url, headers=headers, timeout=10)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    # Find all table rows across the table body safely
    rows = soup.find_all("tr")

    jobs = []

    for row in rows:
        cols = row.find_all("td")

        # Skip header rows or empty rows
        if len(cols) < 5:
            continue

        # Extract details with safe fallback checks
        company = cols[0].get_text(strip=True)
        title = cols[1].get_text(strip=True)
        post_date = cols[2].get_text(strip=True)
        last_date = cols[3].get_text(strip=True)

        detail_tag = cols[4].find("a")
        detail_url = urljoin(url, detail_tag["href"]) if detail_tag and "href" in detail_tag.attrs else "N/A"

        jobs.append({
            "Company": company,
            "Job Title": title,
            "Post Date": post_date,
            "Last Date": last_date,
            "Details Page": detail_url
        })

    # Save to Excel
    df = pd.DataFrame(jobs)
    
    if not df.empty:
        df.to_excel("infopark_jobs.xlsx", index=False)
        print(f"Successfully scraped {len(df)} jobs!\n")
        print(df.head(10))
    else:
        print("No job rows found. Check if the site layout changed.")

except Exception as e:
    print(f"An error occurred: {e}")
