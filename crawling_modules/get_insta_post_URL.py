def get_insta_post_URL(driver):
    """게시물 링크 크롤링 함수.
    
    Args:
        driver(webdriver): selenium의 webdriver.
    """
    try:
        post_URL = driver.current_url

        return post_URL
    except Exception as e:
        print("오류 발생 get_insta_post_URL:", e)