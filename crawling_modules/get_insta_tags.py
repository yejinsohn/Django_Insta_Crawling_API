import re

def get_insta_tags(driver, content):
    """본문 내 해시태그 크롤링 함수.
    
    Args:
        driver(webdriver): selenium의 webdriver.
    """
    try:
        driver.implicitly_wait(10)
        tags = re.findall(r'#[^W#,\\]+', content)
        filteringList = []
        for i in tags:
            if ' ' in i:
                if '\n' in i:
                    i = i.replace('\n', '')
                index = i.find(' ')
                filteringList.append(i[0:index])
            else:
                if '\n' in i:
                    i = i.replace('\n', '')
                filteringList.append(i[0:index])
        
        listTostring = '\n'.join(filteringList)

        if listTostring is None:
            return None
        
        return listTostring, len(filteringList)
    except Exception as e:
        print("오류 발생:", e)