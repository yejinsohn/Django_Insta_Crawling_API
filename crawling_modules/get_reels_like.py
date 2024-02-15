from selenium.webdriver.common.by import By

def get_reels_like(driver, reels_data):
    """릴스 캡션 크롤링 함수.
    
    Args:
        driver(webdriver): selenium의 webdriver.
    """
    try:
        driver.implicitly_wait(10)
        reels_data.click()

        driver.implicitly_wait(10)
        reels_like = driver.find_element(By.CSS_SELECTOR, 'section._ae5m > div > div > span > a > span > span').text

        if '만' in reels_like:
            if '.' in reels_like:
                reels_like = reels_like.replace('.', '')
                reels_like = reels_like.replace('만', '000')
            else: 
                reels_like = reels_like.replace('만', '0000')
        if '억' in reels_like:
            if '.' in reels_like:
                reels_like = reels_like.replace('.', '')
                reels_like = reels_like.replace('억', '0000000')
            else:
                reels_like = reels_like.replace('억', '00000000')

        driver.implicitly_wait(10)
        driver.find_element(By.CSS_SELECTOR, 'div.x160vmok.x10l6tqk.x1eu8d0j.x1vjfegm').click()

        return int(reels_like)
    except Exception as e:
        print("오류 발생 get_reels_like:", e)