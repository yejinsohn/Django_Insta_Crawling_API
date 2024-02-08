from selenium.webdriver.common.by import By

def get_insta_highlight_count(driver):
    """하이라이트 그룹 갯수 크롤링 함수.
    
    Args:
        driver(webdriver): selenium의 webdriver.
    """
    try:
        driver.implicitly_wait(10)
         # 하이라이트 수
        highlight_count = len(driver.find_elements(By.CSS_SELECTOR, '._acaz'))

        return int(highlight_count)
    except Exception as e:
        print("오류 발생 get_insta_highlight_count:", e)
