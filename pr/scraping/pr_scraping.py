from bs4 import BeautifulSoup
import csv
import requests

link = 'http://polyratings.com/list.php'
api_url = 'http://localhost:8000/api/'

def get_prof_list():
    response = requests.get(link, timeout=5)
    soup = BeautifulSoup(response.content, 'lxml')
    content = soup.find_all('div', {'class': 'item-border'})
    print(content)

get_prof_list()