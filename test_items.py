import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_proverka_knopki_bascet(browser):
    browser.get(link)
    time.sleep(30)
    assert browser.find_element(By.XPATH, "//button[@value='Добавить в корзину']")

