#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# leave for windows
#chromedriver = "C:\\Users\\glipets\\Downloads\\chromedriver_win32\chromedriver.exe"
# leave below for firefox
#driver= webdriver.Firefox()
#linux with chromedriver downloaded and CHROME installed
driver = webdriver.Chrome("/home/jbiden/Downloads/chromedriver")
driver.get("http://www.youtube.com")
search = driver.find_element_by_id("search")
search.send_keys('python')
search.send_keys(Keys.ENTER)
#driver.quit()
# DO NOT FORGET TO INSTALL THIS
# sudo pip install webdrivermanager
# which webdrivermanager
# sudo webdrivermanager firefox chrome --linkpath /usr/local/bin

# TO INSTALL CHROME on linux
# wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
# sudo dpkg -i google-chrome-stable_current_amd64.deb