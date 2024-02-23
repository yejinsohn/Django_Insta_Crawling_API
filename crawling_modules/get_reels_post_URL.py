from selenium.webdriver.common.by import By

def get_reels_post_URL(driver, reels_data):
    """게시물 링크 크롤링 함수.
    
    Args:
        driver(webdriver): selenium의 webdriver.
    """
    try:
        driver.implicitly_wait(10)
        reels_data.click()

        post_URL = driver.current_url

        driver.implicitly_wait(10)
        driver.find_element(By.CSS_SELECTOR, 'div.x160vmok.x10l6tqk.x1eu8d0j.x1vjfegm').click()

        return post_URL
    except Exception as e:
        print("오류 발생 get_reels_post_URL:", e)