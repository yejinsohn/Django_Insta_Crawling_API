from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def get_insta_location(driver):
    """위치 정보 크롤링 함수.
    
    Args:
        driver(webdriver): selenium의 webdriver.
    """
    try:
        driver.implicitly_wait(10)
        div_element = driver.find_element(By.CSS_SELECTOR, '._aaqm')

        location_detail = driver.find_element(By.CSS_SELECTOR, 'div._aaql > div > div > div > a').text
        return location_detail

    except NoSuchElementException as e:
        print("오류 발생 get_insta_location:", e)
        return None