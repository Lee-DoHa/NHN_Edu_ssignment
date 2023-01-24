from django.shortcuts import render, get_list_or_404

# Create your views here.
from .models import ParseData

import requests
from bs4 import BeautifulSoup

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "doha.settings")
import django
django.setup()

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from datetime import datetime

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome('/Users/johnn/Downloads/chromedriver_mac64/chromedriver')
driver.implicitly_wait(3)

def index(request):
    return render(request, 'index.html')


def school1(request):
    driver.get('https://school.iamservice.net/organization/1674/group/2001892')
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser') ## BeautifulSoup사용하기
    notices = soup.select('div.bx_cont')
    
    result = []
    
    for div in notices:
        url = div.find('a').attrs['href']
        title = div.find('h4').string
        
        if ParseData.objects.filter(parse_type = "school_1").first() != None and ParseData.objects.filter(parse_type = "school_1").first().title == title:
            break
        body = str(div.find('p'))

        published_datetime = div.find_all('span')[-1].get_text()
        date_time_obj = datetime.strptime(published_datetime, '%Y.%m.%d')

        attachment_list = div.find_all('span', attrs = {"class":"name"})
        attach_string = ""
        for i in attachment_list:
            attach_string = attach_string + i.get_text() + " "

        result.append({'url':url, 'title':title,  'body':body, 'published_datetime':date_time_obj, 'attachment_list': attach_string})

    for i in result:
        s = ParseData(parse_type = "school_1", url = i['url'], title = i['title'], body = i['body'], published_datetime = i['published_datetime'], attachment_list = i['attachment_list'])
        s.save()

    
    data = get_list_or_404(ParseData.objects.filter(parse_type = "school_1"))
    return render(request, 'result.html', {'result':data[0:10]})

def school2(request):
    driver.get('https://school.iamservice.net/organization/19710/group/2091428')
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser') ## BeautifulSoup사용하기
    notices = soup.select('div.bx_cont')
    
    result = []
    
    for div in notices:
        url = div.find('a').attrs['href']
        title = div.find('h4').string
        
        if ParseData.objects.filter(parse_type = "school_2").first() != None and ParseData.objects.filter(parse_type = "school_2").first().title == title:
            break
        body = str(div.find('p'))

        published_datetime = div.find_all('span')[-1].get_text()
        date_time_obj = datetime.strptime(published_datetime, '%Y.%m.%d')

        attachment_list = div.find_all('span', attrs = {"class":"name"})
        attach_string = ""
        for i in attachment_list:
            attach_string = attach_string + i.get_text() + " "

        result.append({'url':url, 'title':title,  'body':body, 'published_datetime':date_time_obj, 'attachment_list': attach_string})

    for i in result:
        s = ParseData(parse_type = "school_2", url = i['url'], title = i['title'], body = i['body'], published_datetime = i['published_datetime'], attachment_list = i['attachment_list'])
        s.save()

    data = get_list_or_404(ParseData.objects.filter(parse_type = "school_2"))
    return render(request, 'result.html', {'result':data[0:10]})

def blog1(request):
    driver.get('https://blog.naver.com/PostList.nhn?blogId=sntjdska123&from=postList&categoryNo=51')
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser') ## BeautifulSoup사용하기
    notices = soup.select('a.link.pcol2')
    
    result = []
    
    for div in notices:
        url = "https://blog.naver.com/" + div.attrs['href']
        title = div.find('strong').string
        
        if ParseData.objects.filter(parse_type = "blog_1").first() != None and ParseData.objects.filter(parse_type = "blog_1").first().title == title:
            break
        body = str(div.find('img'))

        published_datetime = div.find('span', attrs = {"class":"date"}).text
        date_time_obj = datetime.strptime(published_datetime, '%Y. %m. %d.')

        result.append({'url':url, 'title':title,  'body':body, 'published_datetime':date_time_obj, 'attachment_list': "empty"})

    for i in result:
        s = ParseData(parse_type = "blog_1", url = i['url'], title = i['title'], body = i['body'], published_datetime = i['published_datetime'], attachment_list = i['attachment_list'])
        s.save()

    data = get_list_or_404(ParseData.objects.filter(parse_type = "blog_1"))
    return render(request, 'result.html', {'result':data[0:10]})


def blog2(request):
    driver.get('https://blog.naver.com/PostList.nhn?blogId=hellopolicy&from=postList&categoryNo=168')
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser') ## BeautifulSoup사용하기
    notices = soup.select('a.link.pcol2')
    
    result = []
    
    for div in notices:
        url = "https://blog.naver.com/" + div.attrs['href']
        title = div.find('strong').string
        
        if ParseData.objects.filter(parse_type = "blog_2").first() != None and ParseData.objects.filter(parse_type = "blog_2").first().title == title:
            break
        body = str(div.find('img'))

        published_datetime = div.find('span', attrs = {"class":"date"}).text
        date_time_obj = datetime.strptime(published_datetime, '%Y. %m. %d.')

        result.append({'url':url, 'title':title,  'body':body, 'published_datetime':date_time_obj, 'attachment_list': "empty"})

    for i in result:
        s = ParseData(parse_type = "blog_2", url = i['url'], title = i['title'], body = i['body'], published_datetime = i['published_datetime'], attachment_list = i['attachment_list'])
        s.save()

    data = get_list_or_404(ParseData.objects.filter(parse_type = "blog_2"))
    return render(request, 'result.html', {'result':data[0:10]})

def news(request):
    driver.get('http://feeds.bbci.co.uk/news/rss.xml')
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser') ## BeautifulSoup사용하기
    notices = soup.select('div.paditembox > div')
    
    result = []
    
    for div in notices:
        url = div.find('a').attrs['href']
        title = div.find('a').string
        
        if ParseData.objects.filter(parse_type = "news").first() != None and ParseData.objects.filter(parse_type = "news").first().title == title:
            break
        body = str(div.find('div'))

        # date_time_obj = datetime.strptime('0000.00.00', '%Y.%m.%d')

        result.append({'url':url, 'title':title,  'body':body, 'attachment_list': "empty"})

    for i in result:
        s = ParseData(parse_type = "news", url = i['url'], title = i['title'], body = i['body'], attachment_list = i['attachment_list'])
        s.save()

    data = get_list_or_404(ParseData.objects.filter(parse_type = "news"))
    return render(request, 'result.html', {'result':data[0:10]})


def result(request):
    return render(request, 'result.html')