from selenium import webdriver as wb
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import crawling_modules
import re

# 파일이 실행될 때 환경변수에 현재 자신의 프로젝트의 settings.py파일 경로를 등록.
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","django_piium_insta_project.settings")

# 실행파일에 Django 환경을 불러오는 작업.
import django
django.setup()

# Django ORM으로 데이터를 저장하기 위해 ProfileSerializer import.
# django.setup()이후에 호출 해줘야 함. django가 초기화 되지 않은 상황에서 model을 불러오려 하기 때문.
from django_piium_insta_api.serializers import ProfileSerializer

# 관리자 인스타그램 아이디, 패스워드 변수
administratorID = 'inteonsib412@gmail.com'
administratorPW = 'dlsxjstlq1234!!'

# 인스타그램 URL 변수
instagramURL = 'https://www.instagram.com/'

# 인스타그램 계정명 변수
instagramAccount = 'incheon_gov'

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 크롬 웹 브라우저 호출
driver = wb.Chrome(options=chrome_options)
driver.get(instagramURL)

crawling_modules.login_insta_admin(driver, administratorID, administratorPW)

crawling_modules.searching_insta_account.search_insta_account(driver, crawling_modules.searching_insta_account.generate_account_URL(instagramURL, instagramAccount))

# 인스타 프로필의 정보를 갖고있는 딕셔너리
profileDict = {
    'name': instagramAccount,
    'posts': crawling_modules.get_insta_posts(driver),
    'followers': crawling_modules.get_insta_followers(driver), 
    'following': crawling_modules.get_insta_following(driver),
}

# 게시물의 정보를 갖고있는 딕셔너리를 담을 리스트
postList = []

# 첫 번째 게시글 선택 후 정보 크롤링
driver.find_element(By.CSS_SELECTOR, 'div._aagw').click()
driver.implicitly_wait(10)
tags, tag_length = crawling_modules.get_insta_tags(driver, crawling_modules.get_insta_content(driver)) # 해시태그, 해시태그 개수를 튜플로 반환해서 언패킹.
postDict = {
    'date': crawling_modules.get_insta_date(driver),
    'like': crawling_modules.get_insta_like(driver), 
    'content': crawling_modules.get_insta_content(driver), 
    'tags': tags,
    'tag_length': tag_length,
    'comment_most_like': crawling_modules.get_insta_comment_most_like(driver),
}
postList.append(postDict)

# 원하는 게시물 수만큼 반복
for i in range(1):
    driver.find_element(By.CSS_SELECTOR, 'div._aaqg._aaqh').click()
    driver.implicitly_wait(10)
    tags, tag_length = crawling_modules.get_insta_tags(driver, crawling_modules.get_insta_content(driver)) # 해시태그, 해시태그 개수를 튜플로 반환해서 언패킹.
    postDict = {
        'date': crawling_modules.get_insta_date(driver),
        'like': crawling_modules.get_insta_like(driver), 
        'content': crawling_modules.get_insta_content(driver), 
        'tags': tags,
        'tag_length': tag_length,
        'comment_most_like': crawling_modules.get_insta_comment_most_like(driver),
    }
    postList.append(postDict)
profileDict['post'] = postList

# print(profileDict)

# 크롤링한 데이터를 DB에 업로드.
if __name__ == '__main__': # 이 파일이 import가 아닌 python에서 직접 실행할 경우에만 동작하도록 구현.
    serializer = ProfileSerializer(data=profileDict)
    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.errors)