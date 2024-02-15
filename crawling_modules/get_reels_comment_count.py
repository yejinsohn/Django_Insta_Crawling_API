from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def get_reels_comment_count(driver, reels_data):
    """릴스 좋아요 크롤링 함수.
    
    Args:
        driver(webdriver): selenium의 webdriver.
    """
    try:
        driver.implicitly_wait(10)
        ActionChains(driver).move_to_element(reels_data).perform()
        reels_hover = reels_data.find_elements(By.XPATH, '//*[@id="mount_0_0_XJ"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/div[3]/div/div/div[1]/div[1]/div/a/div[2]/div[1]/div/ul/li[2]/span[1]/span')
        print(reels_hover)

        return reels_hover
    except Exception as e:
        print("오류 발생 get_reels_comment_count:", e)