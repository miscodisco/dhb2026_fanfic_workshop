from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup

import unidecode
import time
from pathlib import Path
import json

import utils


def main():
    test_url = "https://archiveofourown.org/works"

    driver = utils.init_chrome_driver()
    driver.get(test_url)

    utils.tos_check(driver)
    time.sleep(1)
    driver.refresh()

    utils.mature_check(driver)

    html = driver.page_source

    driver.quit()

    soup = BeautifulSoup(html, "html.parser")

    title = soup.find("h2").get_text(strip=True)

    if title == "Recent Works":
        print("everything works as expected")
    else:
        print(
            "something did not run as expected, check venv is activated and dependencies are correctly installed"
        )


if __name__ == "__main__":
    main()
