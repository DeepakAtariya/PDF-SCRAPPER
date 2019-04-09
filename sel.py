from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests as req
from selenium.webdriver.chrome.options import Options 

chrome_options = Options()  
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("http://www.google.com")
search = "deep learning with python"
text =  search + " filetype:pdf"
search_element = driver.find_element_by_name("q")
search_element.send_keys(text,Keys.ENTER)
# print(driver.current_url)
res_element = driver.find_elements_by_tag_name("a")
# res_element.click()
# print(res_element)

for data in res_element:
    link = data.get_attribute("href")
    len_link = len(str(link))
    if(str(link).find(".pdf")==len_link-4):
        # print(str(link).find(".pdf"))
        print(link)
        # break
    # else:
        # print("no pdf")


    # print (data.get_attribute("href").find())


# results = req.get(driver.current_url)
# source_code = results.text



