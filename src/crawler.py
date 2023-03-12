import os
import time
from setup import driver, actions


def get_website():
    url = os.environ.get("URL")
    driver.get(url)


def sign_in():
    sign_in_button = driver.find_element("css selector", ".nav__button-secondary")
    sign_in_button.click()

    time.sleep(5)

    username = os.environ.get("USERNAME")
    user_name_field = driver.find_element("css selector", "#username")
    user_name_field.send_keys(f"{username}")

    time.sleep(10)

    password = os.environ.get("PASSWORD")
    password_field = driver.find_element("css selector", "#password")
    password_field.send_keys(f"{password}")

    sign_in_button = driver.find_element("css selector", ".btn__primary--large")
    sign_in_button.click()

    # in case two auth verification is required, wait enough time to put in code
    time.sleep(30)


def apply_to_jobs():
    all_listings = driver.find_elements("class name", "jobs-search-results__list-item")

    for job in all_listings:
        actions.move_to_element(job).perform()
        job.click()
        time.sleep(2)

        save_job_button = driver.find_element("class name", "jobs-save-button")
        save_job_button.click()
        time.sleep(2)

        dialog_box_button = driver.find_element("class name", "artdeco-toast-item__dismiss")
        dialog_box_button.click()
        time.sleep(1)
