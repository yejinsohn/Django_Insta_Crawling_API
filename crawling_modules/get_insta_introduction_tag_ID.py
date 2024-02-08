import re

def get_insta_introduction_tag_ID(driver, introduction):
    """소개 내용 사용자 태그 크롤링 함수.
    
    Args:
        driver(webdriver): selenium의 webdriver.
        introduction(string): 인스타그램 프로필 내용.
    """
    try:
        driver.implicitly_wait(10)

        # 태깅 아이디
        matches = re.findall(r'@(\S+)', introduction)

        if matches:
            # 쉼표로 구분하여 출력
            tag_id = ', '.join(matches)

        return tag_id
    except Exception as e:
        print("오류 발생 get_insta_introduction_tag_ID:", e)