from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests as req
from selenium.webdriver.chrome.options import Options 


# driver.get("http://www.google.com")
# def load():
    

def getSuggestions(keyword):
    chrome_options = Options()  
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("http://www.google.com")
    search = keyword
    text =  search + " filetype:pdf"
    search_element = driver.find_element_by_name("q")
    search_element.send_keys(text,Keys.ENTER)
    # print(driver.current_url)
    res_element = driver.find_elements_by_tag_name("a")
    # res_element.click()
    # print(res_element)

    suggest = ''
    for data in res_element:
        link = data.get_attribute("href")
        len_link = len(str(link))
        if(str(link).find(".pdf")==len_link-4):
            # print(str(link).find(".pdf"))
            suggest=suggest+str(link)
            # print(suggest)
    return suggest

    # return suggest
# class server_class :
#     main_driver 

#     def load(self):
#         chrome_options = Options()  
#         chrome_options.add_argument("--headless")
#         driver = webdriver.Chrome(chrome_options=chrome_options)
#         driver.get("http://www.google.com")
#         self.main_driver = driver
    

