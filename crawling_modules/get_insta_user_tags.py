import re

def get_insta_user_tags(driver, content):
    """본문 내 사용자태그 크롤링 함수.
    
    Args:
        driver(webdriver): selenium의 webdriver.
    """
    try:
        driver.implicitly_wait(10)
        tags = re.findall(r'@[^W@, \\]+', content)

        if len(tags) == 0:
            return None

        listTostring = '\n'.join(tags)

        return listTostring
    except Exception as e:
        print("오류 발생 get_insta_user_tags:", e)