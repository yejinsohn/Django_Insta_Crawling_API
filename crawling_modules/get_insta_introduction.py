from selenium.webdriver.common.by import By

def get_insta_introduction(driver):
    """소개 내용 크롤링 함수.
    
    Args:
        driver(webdriver): selenium의 webdriver.
    """
    try:
        driver.implicitly_wait(10)
        introduction = driver.find_element(By.CSS_SELECTOR, 'h1._ap3a._aaco._aacu._aacx._aad6._aade').text

        return introduction
    except Exception as e:
        print("오류 발생 get_insta_introduction:", e) 