from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

def formular():
    driver = webdriver.Firefox()
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

    #upload an image
    #download file
    #click submit

formular()