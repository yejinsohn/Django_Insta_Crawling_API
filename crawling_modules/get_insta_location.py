from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def get_insta_location(driver):
    """소개 내용 사용자 태그 크롤링 함수.
    
    Args:
        driver(webdriver): selenium의 webdriver.
    """
    try:
        driver.implicitly_wait(10)
        div_element = driver.find_element(By.CSS_SELECTOR, '._aaqm')
        location = "위치 설정 있음"

        location_detail = driver.find_element(By.CSS_SELECTOR, 'div._aaql > div > div > div > a').text

    except NoSuchElementException:
        location = "위치 설정 없음"

    print(f'위치: {location}')
    print('위치 정보: ', location_detail)


    try:
        return highlight_count
    except Exception as e:
        print("오류 발생 get_insta_highlight_count:", e)