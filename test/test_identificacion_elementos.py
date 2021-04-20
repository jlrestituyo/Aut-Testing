from pytest import mark
from selenium import webdriver
import time
from test import util as my_util
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


@mark.parametrize("item", [
    "Keyboard"
]
)

@mark.ui
def test_delete_item_from_cart(item):
    driver = webdriver.Remote(command_executor='http://10.0.0.14:4444/wd/hub', desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True})
    driver.get('https://amazon.com')
    # DOM
    time.sleep(2)
    parent_element = driver.find_element_by_xpath("//*[contains(@class, 'glow-toaster-footer')]")
    parent_element.find_element_by_xpath('//*[contains (@class, "a-button-input")]').click()

    driver.find_element_by_id('twotabsearchtextbox').send_keys(item + Keys.RETURN)

    driver.find_element_by_xpath("//*[contains(@class, 'a-size-medium a-color-base') "
                                 "and contains(text(), 'Keyboard')]").click()

    driver.find_element_by_id('add-to-cart-button').click()

    WebDriverWait(driver, timeout=20).until(lambda d: driver.find_element_by_id('attach-sidesheet-view-cart-button'))
    cart_button = driver.find_element_by_id('attach-sidesheet-view-cart-button')
    time.sleep(5)
    cart_button.click()

    time.sleep(3)
    my_cart = driver.find_elements_by_xpath("//*[contains(@name, 'submit.delete')]")

    for i in range(0, len(my_cart)):
        try:
            driver.find_element_by_xpath("//*[contains(@name, 'submit.delete')]").click()
        except (StaleElementReferenceException, TimeoutException):
            pass

    my_util.wait_until_element_loads_by_xpath(driver, "//*[contains(@class, 'a-column a-span8 a-span-last')]")
    car_empty = driver.find_element_by_xpath("//*[contains(@class, 'a-column a-span8 a-span-last')]")

    assert car_empty.is_displayed()

    time.sleep(10)
    driver.quit()


@mark.ui
def test_open_diario_libre():
    driver = webdriver.Remote(command_executor='http://10.0.0.14:4444/wd/hub', desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True})
    driver.get('https://www.diariolibre.com')
    # DOM
    time.sleep(10)
    driver.quit()

@mark.ui
def test_open_listin_diario():
    driver = webdriver.Remote(command_executor='http://10.0.0.14:4444/wd/hub', desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True})
    driver.get('https://www.listindiario.com')
    # DOM
    time.sleep(10)
    driver.quit()


@mark.ui
def test_open_ebay():
    driver = webdriver.Remote(command_executor='http://10.0.0.14:4444/wd/hub', desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True})
    driver.get('https://www.ebay.com')
    # DOM
    time.sleep(10)
    driver.quit()


@mark.ui
def test_open_selenium_Docs():
    driver = webdriver.Remote(command_executor='http://10.0.0.14:4444/wd/hub', desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True})
    driver.get('https://www.selenium.dev/')
    # DOM
    time.sleep(10)
    elementos_tabla = driver.find_elements_by_tag_name('td')

    for x in elementos_tabla:
        x.find_element_by_xpath('//button[]').click()


    assert driver.find_element_by_xpath("//*[text() = 'Tus Pedidos' ]") is not None

    driver.quit()


def wait_element_by_id(driver, id):
    WebDriverWait(driver, timeout=20).until(lambda d: driver.find_element_by_id(id))