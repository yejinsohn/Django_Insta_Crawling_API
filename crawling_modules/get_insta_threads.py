from selenium.webdriver.common.by import By

def get_insta_threads(driver):
    """스레드 계정 크롤링 함수.
    
    Args:
        driver(webdriver): selenium의 webdriver.
    """
    try:
        driver.implicitly_wait(10)
        threads = driver.find_element(By.CSS_SELECTOR, 'header.x1qjc9v5 > section > div > div.x1dc814f > a').get_attribute("href")

        return threads
    except Exception as e:
        print("오류 발생 get_insta_threads:", e)