from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

print("라이브러리 임포트 완료\n".rjust(20, '-'))

base_url = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
plus_url = input("무엇을 검색하시겠습니까?  ")
url = base_url + quote_plus(plus_url)
print(url)

html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
img = soup.find_all(class_="_img")

print("사진을 다운로드 중입니다".rjust(20, '-'))

# 반복문으로 사진 url 가져오기 및 저장하기
img_num = 1
for i in img:
    img_url = i['data-source']

    with urlopen(img_url) as f:
        with open(plus_url + str(img_num) + '.jpg', 'wb') as file_name:
            img = f.read()
            file_name.write(img)
    img_num += 1

print("사진 다운로드 완료".rjust(20, '-'))
