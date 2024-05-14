from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from time import sleep

# Fix auto closing browser
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get('http://127.0.0.1:5000')

sleep(2)


def signup_enter():
    signup_button = driver.find_element(By.NAME, 'signup')

    actions = ActionChains(driver)

    actions.click(signup_button)

    actions.perform()

