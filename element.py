from  selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


def get_element(driver, locator):

    try:
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located(locator))
        return driver.find_element(*locator)

    except TimeoutException:
        raise print("ELEMENT %s IS NOT VISIBLE" % locator)

def click_bar(driver, locator):

    try:
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(locator))
        return get_element(driver, locator)

    except NoSuchElementException:
        print("Element %s is not clickable" % locator)


