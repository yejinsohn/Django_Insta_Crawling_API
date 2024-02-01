from selenium import webdriver as wb
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
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
instagramAccount = 'todayhouse'

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 크롬 웹 브라우저 호출
driver = wb.Chrome(options=chrome_options)
driver.get(instagramURL)

def login_insta_admin(driver, ID, PW):
    """관리자 인스타그램 자동 로그인 함수.
    
    Args:
        driver(webdriver): selenium의 webdriver.
        ID(string): 관리자의 인스타그램 아이디.
        PW(string): 관리자의 인스타그램 패스워드.
    """
    driver.implicitly_wait(10)
    inputID = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')
    inputID.send_keys(ID)
    inputPW = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
    inputPW.send_keys(PW)
    driver.implicitly_wait(10)
    inputID.send_keys(Keys.ENTER)

def generate_account_URL(URL, account):
    """검색하고자 하는 계정 URL 생성 함수.
    
    Args:
        URL(string): 생성하고자 하는 SNS의 URL.
        account(string): 검색하고자 하는 계정의 이름.

    Returns:
        generatedURL(string): URL과 account를 합친 계정 URL 문자열을 반환합니다.
    """
    generatedURL = URL + account
    return generatedURL

def search_insta_account(driver, URL):
    """인스타그램 게정 검색 함수.
    
    Args:
        driver(webdriver): selenium의 webdriver.
        URL(string): 검색하고자 하는 계정 URL.
    """
    driver.get(URL)
    driver.implicitly_wait(50)

def get_insta_posts(driver):
    """게시물 수 크롤링 함수.
    
    Args:
        driver(webdriver): selenium의 webdriver.
    """
    try:
        driver.implicitly_wait(10)
        posts = driver.find_element(By.CSS_SELECTOR, 'li:nth-child(1)>span').text

        return posts
    except Exception as e:
        print("오류 발생:", e)

def get_insta_followers(driver):
    """팔로워 수 크롤링 함수.
    
    Args:
        driver(webdriver): selenium의 webdriver.
    """
    try:
        driver.implicitly_wait(10)
        followers = driver.find_element(By.XPATH, '//a[contains(@href, "/followers/")]/span').get_attribute("title")

        return followers
    except Exception as e:
        print("오류 발생:", e)

def get_insta_following(driver):
    """팔로잉 수 크롤링 함수.
    
    Args:
        driver(webdriver): selenium의 webdriver.
    """
    try:
        driver.implicitly_wait(10)
        following = driver.find_element(By.XPATH, '//a[contains(@href, "/following/")]/span').text

        return following
    except Exception as e:
        print("오류 발생:", e)
        
def get_insta_date(driver):
    """게시물 개시 날짜 크롤링 함수.
    
    Args:
        driver(webdriver): selenium의 webdriver.
    """
    try:
        driver.implicitly_wait(10)
        datetime = driver.find_element(By.CSS_SELECTOR, 'time').get_attribute("datetime") # "2024-00-00T00:00:00.000Z"
        index = datetime.find('T')
        date = datetime[0:index].replace('-', '')

        return int(date)
    except Exception as e:
        print("오류 발생:", e)

def get_insta_like(driver):
    """게시물에 달린 좋아요 수 크롤링 함수.
    
    Args:
        driver(webdriver): selenium의 webdriver.
    """
    try:
        driver.implicitly_wait(10)
        like = driver.find_element(By.CSS_SELECTOR, 'section._ae5m > div > div > span > a > span > span').text

        return int(like)
    except Exception as e:
        print("오류 발생:", e)

def get_insta_content(driver):
    """본문 내용 크롤링 함수.
    
    Args:
        driver(webdriver): selenium의 webdriver.
    """
    try:
        driver.implicitly_wait(10)
        content = driver.find_element(By.CSS_SELECTOR, 'div._a9zs').text

        return content
    except Exception as e:
        print("오류 발생:", e)

def get_insta_tags(driver):
    """본문 내 해시태그 크롤링 함수.
    
    Args:
        driver(webdriver): selenium의 webdriver.
    """
    try:
        driver.implicitly_wait(10)
        tags = re.findall(r'#[^Ws#,\\]+', get_insta_content(driver))
        listTostring = '\n'.join(tags)

        if listTostring is None:
            return None

        return listTostring
    except Exception as e:
        print("오류 발생:", e)

login_insta_admin(driver, administratorID, administratorPW)

# 로그인 저장 나중에 하기 버튼
driver.implicitly_wait(10)
driver.find_element(By.XPATH, '//div[text()="나중에 하기"]').click()

# 알림 설정 나중에 하기 버튼
driver.implicitly_wait(10)
driver.find_element(By.XPATH, '//button[text()="나중에 하기"]').click()

search_insta_account(driver, generate_account_URL(instagramURL, instagramAccount))

profileDict = {
    'name': instagramAccount,
    'posts': get_insta_posts(driver), 
    'followers': get_insta_followers(driver), 
    'following': get_insta_following(driver),
}

# 첫 번째 게시글 선택
driver.find_element(By.CSS_SELECTOR, 'div._aagw').click()
driver.implicitly_wait(10)

# 게시물의 정보를 갖고있는 딕셔너리를 담을 리스트
postList = []

# 원하는 게시물 수만큼 반복
for i in range(1):
    driver.find_element(By.CSS_SELECTOR, 'div._aaqg._aaqh').click()
    driver.implicitly_wait(10)
    postDict = {
        'date': get_insta_date(driver),
        'like': get_insta_like(driver), 
        'content': get_insta_content(driver), 
        'tags': get_insta_tags(driver),
    }
    postList.append(postDict)
profileDict['post'] = postList

# 크롤링한 데이터를 DB에 업로드.
if __name__ == '__main__': # 이 파일이 import가 아닌 python에서 직접 실행할 경우에만 동작하도록 구현.
    serializer = ProfileSerializer(data=profileDict)
    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.errors)