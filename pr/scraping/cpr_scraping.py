from bs4 import BeautifulSoup
import csv
import os
import sys
sys.path.append('/pr/scraping')
from slugify import slugify
import json
from requests import ConnectionError
import requests
import time
import re

link = 'https://calpolyratings.com/'
api_url = 'http://localhost:8000/api/'

def get_num_pages():
    response = requests.get(link, timeout=5)
    if response.status_code == 404:
        return -1
    soup = BeautifulSoup(response.content, 'lxml')
    return int(soup.find('div', 'pagination').p.text.split()[2])

def scrape_majors():
    response = requests.get(link, timeout=5)
    soup = BeautifulSoup(response.content, 'lxml')
    if not os.path.isfile('majors.csv'):
        print('majors file does not exist. Creating now.')
        with open('majors.csv', mode='w', newline='') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerow(['abbreviation', 'major'])
            print('done!')
    for ind, opt in enumerate(soup.find_all('option')):
        if ind != 0:
            soup_str = str(opt)
            major = re.findall('"([^"]*)"', soup_str)[0].replace('-', ' ')
            word_major = major.split(' ')
            for (i, word) in enumerate(word_major):
                if word != 'and' and word != 'in':
                    word_major[i] = word.capitalize()
            major = ' '.join(word_major)
            abbv = opt.string
            # write_majors(abbv, major)
            r = requests.post(api_url + 'majors/', 
                data={'major': major, 'abbreviation': abbv})
            print(major, 'posted')

def scrape_professors():
    page_limit = get_num_pages() + 1
    x = 0
    professors = {}
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
            print(full_name)
            print(major)
            if not os.path.isfile('majors.csv'):
                scrape_majors()
            with open('majors.csv', mode='r', newline='') as f:
                old_major = major[:]
                reader = csv.DictReader(f)
                found = False
                for row in reader:
                    if row['major'] == major:
                        print('major found.')
                        found = True
                        break
                if not found:
                    for row in reader:
                        if row['abbreviation'] == major:
                            print('found major as abbv')
                            major = row['major']
                            break
                if major == old_major:
                    print('could not find {}\nAdding {} to log'.format(major, full_name[0] + ' ' + full_name[-1]))
                    if not os.path.isfile('add_professors.csv'):
                        create_prof_add_file()
                    else:
                        manual_prof_add(full_name[0], full_name[-1], major)
            # major_fk = response.json()
            # print(major_fk)
            # post_data = {
            #     'first_name': full_name[0],
            #     'last_name': full_name[-1],
            #     major: major_fk
            # }
            # r = requests.post(api_url + 'professors/', data=post_data)
            # print('professor {} added'.format(post_data['first_name']))
        x += 1

def create_prof_add_file():
    print('creating add_professors.csv')
    with open('add_professors.csv', mode='w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(['firstName', 'LastName', 'email', 'major'])
        print('done!')

def manual_prof_add(first, last, major):
    with open('add_professors.csv', mode='a', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(first, last, None, major)

def write_majors(abbv, major):
    with open('majors.csv', mode='a', newline='') as f:
        for line in f:
            if abbv in line:
                return
        writer = csv.writer(f, delimiter=',')
        writer.writerow([abbv, major])

# scrape_majors()
# get_num_pages()
scrape_professors()