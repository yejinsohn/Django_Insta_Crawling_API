def get_insta_introduction_tag_length(driver, introduction):
    """소개 내용 사용자 태그 수 크롤링 함수.
    
    Args:
        driver(webdriver): selenium의 webdriver.
        introduction(string): 인스타그램 프로필 내용.
    """
    try:
        driver.implicitly_wait(10)
        tag_length = introduction.count('@')

        return int(tag_length)
    except Exception as e:
        print("오류 발생 get_insta_introduction_tag_length:", e)