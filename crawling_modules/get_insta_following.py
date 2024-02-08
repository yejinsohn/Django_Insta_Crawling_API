from selenium.webdriver.common.by import By

def get_insta_following(driver):
    """팔로잉 수 크롤링 함수.
    
    Args:
        driver(webdriver): selenium의 webdriver.
    """
    try:
        driver.implicitly_wait(10)
        following = driver.find_element(By.XPATH, '//a[contains(@href, "/following/")]/span').text
        if '만' in following:
            if '.' in following:
                following = following.replace('.', '')
                following = following.replace('만', '000')
            else: 
                following = following.replace('만', '0000')
        if '억' in following:
            if '.' in following:
                following = following.replace('.', '')
                following = following.replace('억', '0000000')
            else:
                following = following.replace('억', '00000000')

        return int(following)
    except Exception as e:
        print("오류 발생 get_insta_following:", e)