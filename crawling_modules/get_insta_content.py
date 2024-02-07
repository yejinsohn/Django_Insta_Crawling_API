from selenium.webdriver.common.by import By

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
        print("오류 발생 get_insta_content:", e)