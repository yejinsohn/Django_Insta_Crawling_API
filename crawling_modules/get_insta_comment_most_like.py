from selenium.webdriver.common.by import By

def get_insta_comment_most_like(driver):
    """본문 댓글 내 좋아요를 가장 많이 받은 댓글 크롤링 함수.
    
    Args:
        driver(webdriver): selenium의 webdriver.
    """
    try:
        driver.implicitly_wait(10)
        like_list = driver.find_elements(By.CSS_SELECTOR, 'div._ae5q > ul > div.x9f619 > div > div > div > ul > div > li > div > div > div._a9zr > div.x9f619 > span > button:nth-child(2) > span')
        comment_like_dict = {}

        for idx in range(len(like_list)):
            if '좋아요' in like_list[idx].text:
                comment_like_dict[idx] = int(like_list[idx].text.replace('좋아요 ', '').replace('개', ''))
            else:
                comment_like_dict[idx] = 0

        sorted_comment_like_dict = sorted(comment_like_dict.items(), key=lambda x: x[1], reverse=True)

        driver.implicitly_wait(10)
        comment_list = driver.find_elements(By.CSS_SELECTOR, 'div._ae5q > ul > div.x9f619 > div > div > div > ul > div > li > div > div > div._a9zr')
        comment_most_like_name = comment_list[list(dict(sorted_comment_like_dict).keys())[0]].find_element(By.CSS_SELECTOR, 'h3 > div > span > div > a').text
        comment_most_like_content = comment_list[list(dict(sorted_comment_like_dict).keys())[0]].find_element(By.CSS_SELECTOR, 'div._a9zs > span').text
        comment_most_like_date = comment_list[list(dict(sorted_comment_like_dict).keys())[0]].find_element(By.CSS_SELECTOR, 'div.x9f619 > span > a > time').get_attribute("datetime")
        index = comment_most_like_date.find('T')
        date = comment_most_like_date[0:index].replace('-', '')

        comment_most_like = comment_most_like_name + '\n' + comment_most_like_content + '\n' + date + '\n' + str(list(dict(sorted_comment_like_dict).values())[0])
        print(comment_most_like)

        return comment_most_like
    except Exception as e:
        print("오류 발생:", e)