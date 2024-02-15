from selenium.webdriver.common.by import By

def get_reels_caption(driver, reels_data):
    """릴스 캡션 크롤링 함수.
    
    Args:
        driver(webdriver): selenium의 webdriver.
    """
    try:
        driver.implicitly_wait(10)
        reels_data.click()
        reels_caption = driver.find_element(By.CSS_SELECTOR, 'div._a9zs').text
        driver.implicitly_wait(10)
        driver.find_element(By.CSS_SELECTOR, 'div.x160vmok.x10l6tqk.x1eu8d0j.x1vjfegm').click()

        return reels_caption
    except Exception as e:
        print("오류 발생 get_reels_caption:", e)