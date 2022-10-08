import requests
from bs4 import BeautifulSoup

URL = "https://pk.mpei.ru/inform/list14bacc.html"
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'accept': '*/*'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all(class_='acceptedPoint accepted')

    abiturients = []

    for item in items:
        abiturients.append(item.find('td'))
    return abiturients


def correct_mass(mass):
    correct = []
    for i in mass:
        i = str(i).replace('<td>', '')
        i = str(i).replace('</td>', '')
        correct.append(i)
    return sorted(correct, reverse=False)

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        answer = correct_mass(get_content(html.text))
        return answer
    else:
        print('Error')

def your_position(base):
    return (f'{len(base) - (base.index("253") + 1)}/{len(base)}(157)')


your_position(parse())
