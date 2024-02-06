from selenium.webdriver.common.by import By

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