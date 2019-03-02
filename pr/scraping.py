from bs4 import BeautifulSoup
from django.utils.text import slugify
import json
import requests
import time
import re

link = 'https://calpolyratings.com/'
api_url = 'http://localhost:8000/api/'

def scrape_majors():
    response = requests.get(link, timeout=5)
    soup = BeautifulSoup(response.content, 'lxml')
    for ind, opt in enumerate(soup.find_all('option')):
        if ind != 0:
            soup_str = str(opt)
            major = re.findall('"([^"]*)"', soup_str)[0].replace('-', ' ')
            word_major = major.split(' ')
            for (i, word) in enumerate(word_major):
                if word != 'and':
                    word_major[i] = word.capitalize()
            major = ' '.join(word_major)
            abbv = opt.string

            r = requests.post(api_url + 'majors/', 
                data={'major': major, 'abbreviation': abbv})

def scrape_professors():
    x = 0
    professors = {}
    while x < 43:
        if x != 0:
            response = requests.get(link + '?page=' + str(x), timeout=5)
        else:
            response = requests.get(link, timeout=5)
        soup = BeautifulSoup(response.content, 'lxml')
        content = soup.find_all('button', {'class': 'teacher-btn'})
        for prof in content:
            # I feel dirty doing it like this.
            full_name = prof.contents[2].split(' ')
            print(full_name)
            major = prof.contents[3].span.contents[1]
            if major == 'AEPS':
                major = 'agricultural-and-environmental-plant-sciences'
            response = requests.get(api_url + 'majors/' + slugify(major))
            major_fk = response.json()['id']
            post_data = {
                'first_name': full_name[0],
                'last_name': full_name[1],
                'major': major_fk
            }
            r = requests.post(api_url + 'professors/', data=post_data)
            print('professor {} added'.format(post_data['first_name']))
        x += 1
            
scrape_professors()
# scrape_majors()
