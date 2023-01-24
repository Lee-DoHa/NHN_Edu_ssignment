import requests
from bs4 import BeautifulSoup

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "doha.settings")
import django
django.setup()

from main.models import School, BlogData
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from datetime import datetime

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome('/Users/johnn/Downloads/chromedriver_mac64/chromedriver')
driver.implicitly_wait(3)


def parse_school():
    driver.get('https://school.iamservice.net/organization/1674/group/2001892')
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser') ## BeautifulSoup사용하기
    notices = soup.select('div.bx_cont')
    
    result = []
    for div in notices:
        url = div.find('a').attrs['href']
        title = div.find('h4').string
        body = str(div.find('p'))

        published_datetime = div.find_all('span')[-1].get_text()
        date_time_obj = datetime.strptime(published_datetime, '%Y.%m.%d')

        attachment_list = div.find_all('span', attrs = {"class":"name"})
        attach_string = ""
        for i in attachment_list:
            attach_string = attach_string + i.get_text() + " "

        result.append({'url':url, 'title':title,  'body':body, 'published_datetime':date_time_obj, 'attachment_list': attach_string})

    return result


# if __name__=='__main__':
#     data_dict = parse_school()

#     for i in data_dict:
#         s = School(url = i['url'], title = i['title'], body = i['body'], published_datetime = i['published_datetime'], attachment_list = i['attachment_list'])
#         s.save()