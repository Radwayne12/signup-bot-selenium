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


def signup_filling():
    user_name_text = driver.find_element(By.ID, 'user_name')
    user_name_text.send_keys('Bot-user')

    sleep(2)

    clue = driver.find_element(By.ID, 'nickname')
    clue.send_keys('strong password')

    sleep(2)

    country = driver.find_element(By.NAME, 'country')
    actions = ActionChains(driver)
    actions.click(country)
    actions.perform()

    sleep(2)

    # countries_el = driver.find_elements(By.TAG_NAME, 'option')

    select = Select(driver.find_elements(By.XPATH, '/html/body/div/div/form/select')[0])
    print(select)
    select.select_by_index(120)

    sleep(2)

    actions.click(country)
    actions.perform()

    submit = driver.find_element(By.XPATH, '/html/body/div/form/div[2]/input')
    actions.click(submit)
    actions.perform()

def main():
    signup_enter()

    sleep(3)

    signup_filling()


if __name__ == "__main__":
    mian()
