from selenium.webdriver.common.by import By

def get_reels_date(driver, reels_data):
    """릴스 게시 날짜 크롤링 함수.
    
    Args:
        driver(webdriver): selenium의 webdriver.
    """
    try:
        driver.implicitly_wait(10)
        reels_data.click()

        reels_upload_date = driver.find_element(By.CSS_SELECTOR, 'time').get_attribute("datetime") # "2024-00-00T00:00:00.000Z"
        index = reels_upload_date.find('T')
        reels_date = reels_upload_date[0:index].replace('-', '')

        driver.implicitly_wait(10)
        driver.find_element(By.CSS_SELECTOR, 'div.x160vmok.x10l6tqk.x1eu8d0j.x1vjfegm').click()

        return int(reels_date)
    except Exception as e:
        print("오류 발생 get_reels_date:", e)