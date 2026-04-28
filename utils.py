# load relevant libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from bs4 import BeautifulSoup

import unidecode

# create helper functions


def init_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)
    driver.delete_all_cookies()

    return driver


def tos_check(driver: webdriver) -> None:
    # wait for the TOS and data processing checkboxes
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.ID, "data_processing_agree"))
    )

    # click them
    for button in ["tos_agree", "data_processing_agree", "accept_tos"]:
        driver_button = driver.find_element(By.ID, button)
        driver_button.click()


def mature_check(driver: webdriver) -> None:
    # if the text is explicit or mature we need to agree to see it
    try:
        driver.find_element(By.LINK_TEXT, "Yes, Continue").click()
    except NoSuchElementException:
        pass


def get_tags(soup: BeautifulSoup, tag: str) -> list[str]:
    """
    returns a list of tags for a given tag type
    """
    css_pattern = f"dd.{tag}.tags > ul.commas > li"

    tags_list = [unidecode(element.get_text()) for element in soup.select(css_pattern)]

    return tags_list


def get_fulltext(soup: BeautifulSoup) -> str:
    """
    Get the full text / all chapters, loop over them to clean and concatenate
    """
    chapters = soup.select("div#chapters")
    full_text = ""

    for chapter in chapters:
        chapter_text = unidecode(chapter.text)

        full_text += chapter_text.strip()

        break

    return full_text
