from selectorlib import Extractor
import requests
import csv
from datetime import datetime, timedelta
import re
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import time

# Create an Extractor by reading from the YAML file
e = Extractor.from_yaml_file('selectors.yml')

def convert_flipkart_date(date_str):
    today = datetime.today()
    
    # Handle 'n days ago'
    days_ago_match = re.match(r'(\d+) days ago', date_str)
    if days_ago_match:
        days_ago = int(days_ago_match.group(1))
        return (today - timedelta(days=days_ago)).strftime('%Y-%m-%d')
    
    # Handle 'n months ago'
    months_ago_match = re.match(r'(\d+) months ago', date_str)
    if months_ago_match:
        months_ago = int(months_ago_match.group(1))
        new_month = today.month - months_ago
        new_year = today.year
        while new_month <= 0:
            new_month += 12
            new_year -= 1
        new_date = today.replace(year=new_year, month=new_month)
        return new_date.strftime('%Y-%m-%d')
    
    # Handle 'a year ago'
    if date_str == 'a year ago':
        return (today.replace(year=today.year - 1)).strftime('%Y-%m-%d')
    
    # Handle 'month, year'
    try:
        return datetime.strptime(date_str, '%b, %Y').strftime('%Y-%m-%d')
    except ValueError:
        pass
    
    return None  # If format doesn't match any expected pattern

def get_session_with_retries():
    session = requests.Session()
    retries = Retry(total=5,
                    backoff_factor=1,
                    status_forcelist=[500, 502, 503, 504])
    session.mount('http://', HTTPAdapter(max_retries=retries))
    session.mount('https://', HTTPAdapter(max_retries=retries))
    return session

def scrape(url, session):
    headers = {
        'authority': 'www.flipkart.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    # Download the page using requests
    print("Downloading %s" % url)
    r = session.get(url, headers=headers)
    # Simple check to check if page was blocked (Usually 503)
    if r.status_code > 500:
        if "To discuss automated access to Amazon data please contact" in r.text:
            print("Page %s was blocked by Amazon. Please try using better proxies\n" % url)
        else:
            print("Page %s must have been blocked by Amazon as the status code was %d" % (url, r.status_code))
        return None
    # Pass the HTML of the page and create
    return e.extract(r.text)

# Create a session with retry logic
session = get_session_with_retries()

# Open the URL list and CSV output file
with open("Urls.txt", 'r') as urllist, open('reviews.csv', 'w', encoding='utf-8', newline='') as outfile:
    # Define CSV fieldnames
    fieldnames = ["ProductTitle", "ReviewTitle", "ReviewContent", "Date", "Rating", "Author","Country"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
    writer.writeheader()
    
    # Iterate through each URL
    for url in urllist.readlines():
        data = scrape(url.strip(), session)
        if data:
            for r in data['reviews']:
                # Prepare data for CSV
                rating = r.get('rating')
                if rating:
                    rating = rating.split(' out of')[0]

                # Convert title and content to English, to ensure that the other language reviews are also in English        
                title = r.get("title", "").strip() if r.get("title") else ""

                content = r.get("content", "").strip() if r.get("content") else ""
                # Truncate content to ensure its size is between 0 and 5000 characters
                if len(content) > 4999:
                    content = content[:4999]

                country = 'India'

                # Convert the date using the custom function
                date_str = r.get('date')
                if date_str:
                    date = convert_flipkart_date(date_str.strip())
                else:
                    date = ''

                row = {
                    "ProductTitle": data["product_title"].strip() if data.get("product_title") else "",
                    "ReviewTitle": title,
                    "ReviewContent": content,
                    "Date": date,
                    "Rating": rating,
                    "Author": r.get("author", "").strip() if r.get("author") else "",
                    "Country": country
                }
                # Write row to CSV
                writer.writerow(row)
        # we can use sleep to avoid rate limiting
        time.sleep(5)  # Sleep for 5 seconds between each request

print("Scraping completed.")
