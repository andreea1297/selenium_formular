from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import os
import urllib3

def formular():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.techlistic.com/p/selenium-practice-form.html") #accesare site
    time.sleep(5)

    #enter the first and second name
    first_name = driver.find_element_by_name("firstname");
    first_name.clear()
    first_name.send_keys("Calin")

    second_name = driver.find_element_by_name("lastname")
    second_name.clear()
    second_name.send_keys("Andreea")
    time.sleep(3)

    #select radio button - gender button
    gender = driver.find_element_by_id("sex-1").click()
    time.sleep(3)

    #select years of experience
    years_experiences = driver.find_element_by_id("exp-3").click()
    time.sleep(3)

    #date
    date = driver.find_element_by_id("datepicker")
    date.clear()
    date.send_keys("19/11/2000")
    time.sleep(2)

    #select profession
    profession = driver.find_element_by_id("profession-0").click()
    time.sleep(2)

    automation_tools = driver.find_element_by_id("tool-1").click()
    time.sleep(2)

    #select continents
    continent = Select(driver.find_element_by_name("continents"))
    continent.select_by_visible_text("Europe")
    time.sleep(2)

    #selenium commands section
    commands = Select(driver.find_element_by_name("selenium_commands"))
    commands.select_by_visible_text("Wait Commands")
    a = ActionChains(driver)
    a.key_down(Keys.CONTROL)
    commands.select_by_visible_text("Switch Commands")
    time.sleep(2)
    a.key_up(Keys.CONTROL)
    time.sleep(5)

    #upload an image
    driver.find_element_by_id("photo").send_keys(os.getcwd()+"\parrots.bmp") #getcwd - calea pt folderul curent
    time.sleep(5)

    #download file -> trebe modificat
    #download_dir = os.getcwd() #current directory

    #profile = webdriver.FirefoxProfile()
    #profile.set_preference('browser.download.folderList', 2)  # custom location
    #profile.set_preference('browser.download.manager.showWhenStarting', False)
    #profile.set_preference('browser.download.dir', download_dir)
    #profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')

    #driver = webdriver.Firefox(profile)
    #driver.get("https://www.techlistic.com/p/selenium-practice-form.html")  # accesare site

   # driver.find_element_by_partial_link_text("https://github.com/stanfy/behave-rest/blob/master/features/conf.yaml").click()
    link = driver.find_element_by_partial_link_text("Click here to Download File")
    link_download = link.get_attribute("href")
    #print(link_download)
    connection_pool = urllib3.PoolManager()
    #print(link_download[0:8] + "raw.githubusercontent" + link_download[14:38] + link_download[43:])
    url_2 = link_download[0:8] + "raw.githubusercontent" + link_download[14:38] + link_download[43:]
    resp = connection_pool.request('GET', url_2)
    filename = os.path.join(os.getcwd(), 'data_download.txt')
    f = open(filename, 'wb')
    f.write(resp.data)
    f.close()
    resp.release_conn()
    time.sleep(5)

    #click submit
    driver.find_element_by_id("submit").click()
    time.sleep(3)

formular()