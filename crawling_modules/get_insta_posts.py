from selenium.webdriver.common.by import By

def get_insta_posts(driver):
    """게시물 수 크롤링 함수.
    
    Args:
        driver(webdriver): selenium의 webdriver.
    """
    try:
        driver.implicitly_wait(10)
        posts = driver.find_element(By.CSS_SELECTOR, 'li:nth-child(1)>span').text
        if '만' in posts:
            if '.' in posts:
                posts = posts.replace('.', '')
                posts = posts.replace('만', '000')
            else: 
                posts = posts.replace('만', '0000')
        if '억' in posts:
            if '.' in posts:
                posts = posts.replace('.', '')
                posts = posts.replace('억', '0000000')
            else:
                posts = posts.replace('억', '00000000')
                
        return int(posts)
    except Exception as e:
        print("오류 발생:", e)