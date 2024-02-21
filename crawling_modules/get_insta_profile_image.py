from selenium.webdriver.common.by import By
import urllib.request

def get_insta_profile_image(driver, username):
    """프로필 사진 크롤링 함수.
    
    Args:
        driver(webdriver): selenium의 webdriver.
    """
    try:
        driver.implicitly_wait(10)
        img = driver.find_element(By.CSS_SELECTOR, 'div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5 > div.x9f619 > div.x1gryazu > div:nth-child(2) > section > main > div > header > div > div > span > img').get_attribute('src')
        img_path = "crawling_images/"
        img_name = username + "_profile_img.jpg"
        urllib.request.urlretrieve(img, img_path + img_name)

        return img_path + img_name

    except Exception as e:
        print("오류 발생 get_insta_profile_image:", e)