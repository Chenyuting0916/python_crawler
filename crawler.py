from lib2to3.pgen2 import driver
from bs4 import BeautifulSoup
import urllib.request as req
import time
import re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def getHtmlData(url):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(3)
    driver.get(url)
    for i in range(1, 20):
        driver.execute_script(
            'window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(1.1)

    # with req.urlopen(url) as response:
    #     data = response.read().decode("utf-8")

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # divs = soup.find_all("div", class_="story-list__text")
    # for div in divs:
    #     if div.time:
    #             print(div.a.string)
    titles = soup.findAll(text=re.compile('老人'))
    for title in titles:
        print(title)


pageUrl = "https://udn.com/news/breaknews/1/99#breaknews"
getHtmlData(pageUrl)
