from selenium.webdriver.common.by import By

def get_insta_like(driver):
    """게시물에 달린 좋아요 수 크롤링 함수.
    
    Args:
        driver(webdriver): selenium의 webdriver.
    """
    try:
        driver.implicitly_wait(10)
        like = driver.find_element(By.CSS_SELECTOR, 'section._ae5m > div > div > span > a > span > span').text

        if '만' in like:
            if '.' in like:
                like = like.replace('.', '')
                like = like.replace('만', '000')
            else: 
                like = like.replace('만', '0000')
        if '억' in like:
            if '.' in like:
                like = like.replace('.', '')
                like = like.replace('억', '0000000')
            else:
                like = like.replace('억', '00000000')

        return int(like)
    except Exception as e:
        print("오류 발생:", e)