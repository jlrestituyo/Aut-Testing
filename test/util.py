from selenium.webdriver.support.wait import WebDriverWait


def wait_until_element_loads_by_xpath(driver, xpath):
    WebDriverWait(driver, timeout=20).until(lambda d: driver.find_element_by_xpath(xpath))