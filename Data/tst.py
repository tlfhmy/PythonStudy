from selenium import  webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS(executable_path=r"C:\Program Files\Python37\phantomjs.exe")
#driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
driver.get("https://opsin.ch.cam.ac.uk/")

# 百度关键词输入框
searchInput = driver.find_element_by_id("chemicalName")
# 我们来搜索一下 "python"这个关键字
searchInput.send_keys("2,4,6-trinitrotoluene")
driver.implicitly_wait(1)
print(searchInput.text)
# 百度输入框提交按钮
label = driver.find_element_by_xpath("html/body/div[4]/div[1]/div[1]/div[1]/form/fieldset/input[2]")
#searchSubmitBtn=driver.find_element_by_css_selector("<input type='submit' value='Submit'>")
#searchSubmitBtn = driver.find_element_by_id("submit")
print(label.text)
label.click() # 模拟提交表单
driver.implicitly_wait(1)
# 因为百度的搜索是异步的
# 我们这里设置等待20秒
# 如果网页标题中包含了"python" 我们就认为加载成功了
#WebDriverWait(driver,20).until(expected_conditions.title_contains("python"))

#html = driver

#oBj = BeautifulSoup(html)
#print(driver.current_url)
#print(driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/div[1]/div[2]/p").get_attribute('value'))
print(driver.find_element_by_id("chemicalName").text)