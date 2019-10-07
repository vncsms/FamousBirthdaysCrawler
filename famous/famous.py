from constants import MONTHS, MAIN_URL
from bs4 import BeautifulSoup
import requests


def get_all_people_birthday_day(month, day):

    if month not in MONTHS:
        return {'detail': 'month not found'}

    if day > MONTHS[month]['total'] or day < 0:
        return {'detail': 'day out of range'}

    url = MAIN_URL + '/' + month + str(day) + '.html'

    response = requests.get(url)

    if response.status_code != 200:
        return {'detail': 'invalid url'}

    persons = html_extract_day_page(response.text)

    for person in persons:
        person['birth_month'] = MONTHS[month]['id']
        person['birth_day'] = day

    return persons


def get_all_people_birthday():

    persons = []

    for month in MONTHS:

        for day in range(1, MONTHS[month]['total'] + 1):

            url = MAIN_URL + '/' + month + str(day) + '.html'

            response = requests.get(url)

            if response.status_code != 200:
                continue

            persons_temp = html_extract_day_page(response.text)

            for person in persons_temp:
                person['birth_month'] = MONTHS[month]['id']
                person['birth_day'] = day

            persons += persons_temp

    return persons


def html_extract_day_page(body):

    soup = BeautifulSoup(body, 'html.parser')
    birthdays = soup.find_all('a', class_='person-item')

    persons = []

    for b in birthdays:
        person = get_person_information(b.attrs['href'])

        if person:
            persons.append(person)

    return persons


def get_person_information(url):

    try:
        response = requests.get(url, timeout=10)
    except requests.exceptions.Timeout:
        return None

    if response.status_code != 200:
        return None

    person = {}

    soup = BeautifulSoup(response.text, 'html.parser')

    '''
        Get title
    '''

    tag_name = soup.find('h1')
    div = tag_name.find('div')

    if not div:
        return None

    div.clear()
    person['title'] = tag_name.get_text().replace('\n', '')

    '''
        Get bio
    '''

    bio = soup.find('div', class_='bio')
    person['body'] = str(bio)

    '''
        Get picture
    '''

    img_container = soup.find('div', class_='img1')
    img = img_container.find('img')
    person['avatar'] = img.attrs['src']

    '''
        Get birthyear
    '''

    stat_container = soup.find('div', class_='stat')
    stat_container_link_children = stat_container.find_all('a')

    try:
        person['year'] = int(stat_container_link_children[-1].get_text())
    except ValueError:
        return None

    return person