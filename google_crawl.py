import errno
import sys, os
from bs4 import BeautifulSoup
from selenium import webdriver
import urllib, urllib.request
import requests
import random
import time
from selenium.webdriver.common.keys import Keys

folder = "image"
url = "https://www.google.com/search"
webDriver = "chromedriver.exe"
searchItem = input("검색어를 입력하세요:  ")
size = 300

params = {
    "q": searchItem
    , "tbm": "isch"
    , "sa": "1"
    , "source": "lnms&tbm=isch"
}

url = url + "?" + urllib.parse.urlencode(params)
browser = webdriver.Chrome(webDriver)
time.sleep(0.5)
browser.get(url)
html = browser.page_source
time.sleep(0.5)

soup_temp = BeautifulSoup(html, 'html.parser')
img4page = len(soup_temp.findAll("img"))

elem = browser.find_element_by_tag_name("body")
imgCnt = 0
while imgCnt < size * 35:
    elem.send_keys(Keys.PAGE_DOWN)
    rnd = random.random()
    print(imgCnt)
    time.sleep(rnd)
    imgCnt += img4page

html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')
img = soup.findAll("img")

browser.find_elements_by_tag_name('img')

fileNum = 0
srcURL = []

for line in img:
    if str(line).find('data-src') != -1 and str(line).find('http') < 10000:
        print(fileNum, " : ", line['data-src'])
        srcURL.append(line['data-src'])
        fileNum += 1

saveDir = searchItem

try:
    if not (os.path.isdir(saveDir)):
        os.makedirs(os.path.join(saveDir))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("Failed to create directory!!!!!")
        raise

for i, src in zip(range(fileNum), srcURL):
    urllib.request.urlretrieve(src, saveDir + "/" + str(i) + ".jpg")
    print(i, "saved")

print("프로그램 종료".rjust(50, "="))
