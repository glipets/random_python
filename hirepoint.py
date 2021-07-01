#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chromedriver = "C:\\Users\\glipets\\Downloads\\chromedriver_win32_83\chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
driver.get("https://hirepoint.checkpoint.com/index.php?m=employeereferral")
search = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div[1]/div/div/div[3]/div[2]/div[1]/div[2]/label/input")
#search = driver.find_element_by_class_name('placeholder')
search.send_keys('Denver')
search.send_keys(Keys.ENTER)
