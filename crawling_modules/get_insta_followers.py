from selenium.webdriver.common.by import By

def get_insta_followers(driver):
    """팔로워 수 크롤링 함수.
    
    Args:
        driver(webdriver): selenium의 webdriver.
    """
    try:
        driver.implicitly_wait(10)
        followers = driver.find_element(By.XPATH, '//a[contains(@href, "/followers/")]/span').get_attribute("title")
        if '만' in followers:
            if '.' in followers:
                followers = followers.replace('.', '')
                followers = followers.replace('만', '000')
            else: 
                followers = followers.replace('만', '0000')
        if '억' in followers:
            if '.' in followers:
                followers = followers.replace('.', '')
                followers = followers.replace('억', '0000000')
            else:
                followers = followers.replace('억', '00000000')

        return int(followers)
    except Exception as e:
        print("오류 발생:", e)