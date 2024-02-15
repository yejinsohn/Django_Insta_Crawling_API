from selenium.webdriver.common.by import By

def get_reels_view(driver, reels_data):
    """릴스 조회수 크롤링 함수.
    
    Args:
        driver(webdriver): selenium의 webdriver.
    """
    try:
        driver.implicitly_wait(10)
        reels_view = reels_data.find_element(By.CSS_SELECTOR, 'div > span > span').text

        if '만' in reels_view:
            if '.' in reels_view:
                reels_view = reels_view.replace('.', '')
                reels_view = reels_view.replace('만', '000')
            else: 
                reels_view = reels_view.replace('만', '0000')
        if '억' in reels_view:
            if '.' in reels_view:
                reels_view = reels_view.replace('.', '')
                reels_view = reels_view.replace('억', '0000000')
            else:
                reels_view = reels_view.replace('억', '00000000')

        return int(reels_view)
    except Exception as e:
        print("오류 발생 get_reels_view:", e)