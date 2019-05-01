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
            abbv = opt.string.strip()
            write_majors(abbv, major)
            # r = requests.post(api_url + 'majors/', 
            #     data={'major': major, 'abbreviation': abbv})
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
            if "women" in major:
                major = "Womens and Gender Studies"
            print(major)
            if not os.path.isfile('majors.csv'):
                scrape_majors()
            with open('majors.csv', mode='r', newline='') as f:
                reader = csv.DictReader(f)
                found = False
                for row in reader:
                    if row['major'] == major:
                        print('major found.')
                        found = True
                        if not os.path.isfile('professors.csv'):
                            params = ['firstName', 'LastName', 'email', 'major']
                            create_csv('professors.csv', *params)
                        prof_params = [full_name[0], full_name[-1], None, major]
                        prof_append('professors.csv', *prof_params)
                        break
                f.seek(0)
                if not found:
                    new_reader = csv.DictReader(f)
                    is_abbv = False
                    for row in reader:
                        print('searching for', major)
                        if row['abbreviation'] == major:
                            print('found major as abbv')
                            major = row['major']
                            is_abbv = True
                            break
                    if not is_abbv:
                        print('could not find {}\nAdding {} to log'.format(major, full_name[0] + ' ' + full_name[-1]))
                        if not os.path.isfile('add_professors.csv'):
                            params = ['firstName', 'LastName', 'email', 'major']
                            create_csv('add_professors.csv', *params)
                        else:
                            prof_params = [full_name[0], full_name[-1], None, major]
                            prof_append('add_professors.csv', *prof_params)
                    else:
                        if not os.path.isfile('professors.csv'):
                            params = ['firstName', 'LastName', 'email', 'major']
                            create_csv('professors.csv', *params)
                        prof_params = [full_name[0], full_name[-1], None, major]
                        prof_append('professors.csv', *prof_params)
        time.sleep(1)
        x += 1

def test_find_abbv(abbv):
    with open('majors.csv', mode='r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['abbreviation'] == abbv:
                print('found major')
                break
        print('done')

def create_csv(filename, *args):
    print('creating {}'.format(filename))
    with open(filename, mode='w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow([arg for arg in args])
        print('done!')

def prof_append(filename, *args):
    with open(filename, mode='a', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow([arg for arg in args])

def write_majors(abbv, major):
    with open('majors.csv', mode='a', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow([abbv, major])

def post_professor_from_file():
    with open('professors.csv', mode='r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            response = requests.get(api_url + 'majors/' + slugify(row['major']))
            major_fk = int(response.json()['id'])
            print(row['firstName'], type(row['firstName']))
            print(row['LastName'], type(row['LastName']))
            print(major_fk, type(major_fk))
            post_data = {
                'first_name': row['firstName'],
                'last_name': row['LastName'],
                'major': major_fk
            }
            print(post_data)
            r = requests.post(api_url + 'professors/', data=post_data)
            print(r)
            # print('professor {} added'.format(post_data['first_name']))

# scrape_majors()
# get_num_pages()
# scrape_professors()
# gender_studies()
# post_professor_from_file()
