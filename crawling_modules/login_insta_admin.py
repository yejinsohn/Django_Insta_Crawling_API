from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def login_insta_admin(driver, ID, PW):
    """관리자 인스타그램 자동 로그인 함수.
    
    Args:
        driver(webdriver): selenium의 webdriver.
        ID(string): 관리자의 인스타그램 아이디.
        PW(string): 관리자의 인스타그램 패스워드.
    """
    driver.implicitly_wait(10)
    inputID = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')
    inputID.send_keys(ID)
    inputPW = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
    inputPW.send_keys(PW)
    driver.implicitly_wait(10)
    inputID.send_keys(Keys.ENTER)

    # 로그인 저장 나중에 하기 버튼
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//div[text()="나중에 하기"]').click()

    # 알림 설정 나중에 하기 버튼
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//button[text()="나중에 하기"]').click()