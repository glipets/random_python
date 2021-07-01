#!/usr/bin/python3
from selenium import webdriver
chromedriver = "C:\\Users\\glipets\\Downloads\\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
driver.get("http://www.youtube.com")
