def search_insta_account(driver, URL):
    """인스타그램 게정 검색 함수.
    
    Args:
        driver(webdriver): selenium의 webdriver.
        URL(string): 검색하고자 하는 계정 URL.
    """
    driver.get(URL)
    driver.implicitly_wait(50)

def generate_account_URL(URL, account):
    """검색하고자 하는 계정 URL 생성 함수.
    
    Args:
        URL(string): 생성하고자 하는 SNS의 URL.
        account(string): 검색하고자 하는 계정의 이름.

    Returns:
        generatedURL(string): URL과 account를 합친 계정 URL 문자열을 반환합니다.
    """
    generatedURL = URL + account
    return generatedURL

