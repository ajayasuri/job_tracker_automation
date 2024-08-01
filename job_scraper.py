import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import json 
import os

def scrape_job_info(job_url):
    response = requests.get(job_url)
    if response.status_code != 200:
        print(f"Failed to retrieve data from {job_url}")
        return None
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    job_title = extract_job_title(soup)
    company_name = extract_company_name(soup)
    location = soup.find('div', class_='location').text.strip() if soup.find('div', class_='location') else "N/A"
    posted_date = soup.find('div', class_='posted-date').text.strip() if soup.find('div', class_='posted-date') else "N/A"
    job_description = soup.find('div', class_='job-description').text.strip() if soup.find('div', class_='job-description') else "N/A"
    
    job_data = {
        'Job Title': job_title,
        'Company Name': company_name,
        'Location': location,
        'Posted Date': posted_date,
        'Date Applied': datetime.now().strftime("%Y-%m-%d"),
        'Job Link': job_url,
        'Job Description': job_description
    }
    
    return job_data

def extract_job_title(soup):
    for tag in ['h1', 'h2']:
        element = soup.find(tag)
        if element and "view" not in element.text.lower():
            return element.text.strip()
    return "N/A"

def extract_company_name(soup):
    json_ld = soup.find('script', type='application/ld+json')
    if json_ld:
        try:
            data = json.loads(json_ld.string)
            company_name = data.get('hiringOrganization', {}).get('name')
            if company_name:
                return company_name.strip()
        except json.JSONDecodeError:
            pass
    
    possible_patterns = [
        {'tag': 'meta', 'attrs': {'property': 'og:site_name'}},
        {'tag': 'meta', 'attrs': {'name': 'og:site_name'}},
        {'tag': 'div', 'class_': 'company'},
        {'tag': 'span', 'class_': 'company'},
        {'tag': 'a', 'class_': 'topcard__org-name-link'},
        {'tag': 'div', 'class_': 'job-company'},
        {'tag': 'div', 'class_': 'company-info'},
        {'tag': 'span', 'class_': 'company-name'},
        {'tag': 'div', 'class_': 'job-header__company'}
    ]
    
    for pattern in possible_patterns:
        element = soup.find(pattern['tag'], attrs=pattern.get('attrs'), class_=pattern.get('class_'))
        if element:
            company_name = element.text.strip()
            if company_name:
                return company_name

    return "N/A"

def save_to_csv(data, filename="jobs_applied.csv"):
    new_data = pd.DataFrame(data)
    
    # Append data to the CSV file
    new_data.to_csv(filename, mode='a', header=not os.path.exists(filename), index=False)
    print(f"Data saved to {filename}")

def main():
    while True:
        job_url = input("Enter the job URL you applied to (or type 'exit' to stop): ")
        if job_url.lower() == 'exit':
            break
        
        job_data = scrape_job_info(job_url)
        
        if job_data:
            save_to_csv([job_data])

if __name__ == "__main__":
    main()
