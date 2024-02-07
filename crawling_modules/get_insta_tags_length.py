import re

def get_insta_tags_length(driver, content):
    """본문 내 해시태그 수 크롤링 함수.
    
    Args:
        driver(webdriver): selenium의 webdriver.
    """
    try:
        driver.implicitly_wait(10)
        tags = re.findall(r'#[^W#,\\]+', content)

        return len(tags)
    except Exception as e:
        print("오류 발생 get_insta_tags_length:", e)