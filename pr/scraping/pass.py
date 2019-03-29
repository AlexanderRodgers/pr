import requests
import lxml
from bs4 import BeautifulSoup

pass_url = 'https://idp.calpoly.edu/idp/profile/cas/login?service=https://pass.calpoly.edu/j_spring_cas_security_check'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

login_data = {
    'j_username': 'aerodger@calpoly.edu',
    'j_password': 'sharK543$$nado',
}

with requests.Session() as s:
    url = 'https://myportal.calpoly.edu/f/u17l1s6/normal/render.uP'
    r = s.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    my_button = soup.find('button', attrs={ 'name': '_eventId_proceed'})['onclick']
    r = s.post(url, data=login_data, headers=headers)
    # r = s.post(pass_url, data=login_data, headers=headers)
    print(r.content)