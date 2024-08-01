Job Application Tracker

Overview

This project is a Python-based tool designed to help job seekers keep track of the positions they apply for. By entering the URL of the job listing, this tool automatically scrapes key details such as the job title, company name, location, and other relevant information. The data is then stored in a CSV file for easy reference and tracking of applications.

Features

Job Data Extraction: Scrapes essential information such as job title, company name, location, posted date, and job description from job listing URLs.
CSV Storage: Saves all job application data to a CSV file (jobs_applied.csv) for easy access and record-keeping.
Simple Interface: The tool runs in a loop, allowing users to input multiple job URLs until they choose to exit.
How It Works

Web Scraping: The tool uses requests to fetch the HTML content of the job listing page and BeautifulSoup to parse the HTML.
Data Extraction: Key details are extracted from the HTML, including job title, company name, location, posted date, and job description.
CSV Export: The extracted data is appended to a CSV file, which acts as a log of all job applications.
Getting Started

Prerequisites
Python 3.x
requests, beautifulsoup4, and pandas libraries (installable via pip)
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/ajayasuri/job_tracker_automation.git
Install the required Python libraries:
bash
Copy code
pip install -r requirements.txt
Run the script:
bash
Copy code
python job_scraper.py
Usage
Run the script in your terminal.
Enter the job URL you want to track when prompted.
The job details will be extracted and saved to jobs_applied.csv.
Continue entering URLs or type "exit" to stop the process.
Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for any improvements or bug fixes.

License

This project is licensed under the MIT License.

