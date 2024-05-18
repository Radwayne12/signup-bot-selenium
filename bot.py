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

user_input = 'Bot-user'  # default user that bot inputs
password_input = 'strong password'  # default password that bot inputs
country_input: int = 2  # default country [0-195] alphabetically | lines 50-52 to find desired index


def signup_enter():
    signup_button = driver.find_element(By.NAME, 'signup')

    actions = ActionChains(driver)

    actions.click(signup_button)

    actions.perform()


def signup_filling():
    user_name_text = driver.find_element(By.ID, 'user_name')
    user_name_text.send_keys(user_input)

    sleep(2)

    clue = driver.find_element(By.ID, 'nickname')
    clue.send_keys(password_input)

    sleep(2)

    country = driver.find_element(By.NAME, 'country')
    actions = ActionChains(driver)
    actions.click(country)
    actions.perform()

    sleep(2)

    # countries_el = driver.find_elements(By.TAG_NAME, 'option')
    # country_text_list = [i.text for i in countries_el]
    # country_input = country_text_list.index('Your-country-name'))

    select = Select(driver.find_elements(By.TAG_NAME, 'select')[0])
    select.select_by_index(country_input)

    sleep(2)

    actions.click(country)
    actions.perform()

    submit = driver.find_element(By.XPATH, '/html/body/div/form/div[2]/input')
    actions.click(submit)
    actions.perform()


def main():
    signup_enter()

    sleep(2)

    signup_filling()


if __name__ == "__main__":
    main()
