from selenium.webdriver.common.by import By

def get_insta_authentication(driver):
    """인증 뱃지 크롤링 함수.
    
    Args:
        driver(webdriver): selenium의 webdriver.
    """
    try:
        driver.implicitly_wait(10)
        authentication = driver.find_element(By.CSS_SELECTOR, 'header.x1qjc9v5 > section > div.x6s0dn4 > div > svg').get_attribute("aria-label")

        return authentication
    except Exception as e:
        print("오류 발생 get_insta_authentication:", e)