import pytest
import time 

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    assert browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket"), 'basket button not found'