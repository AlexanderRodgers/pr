import pr.scraping.cpr_scraping as scraping
from bs4 import BeautifulSoup
import csv
import requests

link = 'https://calpolyratings.com/'
api_url = 'http://localhost:8000/api/'

def check_prof_ratings():
    page_limit = scraping.get_num_pages() + 1
    while x < page_limit:
        if x == 0:
            response = requests.get(link, timeout=5)
        else:
            response = requests.get(link + '?page=' + str(x), timeout=5)
            soup = BeautifulSoup(response.content, 'lxml')
        content = soup.find_all('button', {'class': 'teacher-btn'})
        done = False
        for prof in content:
            full_name = prof.contents[2].split(' ')
            major = str(prof.contents[3].span.contents[1])
    