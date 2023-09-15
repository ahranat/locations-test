import pytest
import time
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_add_to_cart_button(browser):
    browser.get(link)
    time.sleep(30)
    assert browser.find_element(By.CLASS_NAME, 'btn-add-to-basket'), 'There is no add to cart button'

if __name__ == "__main__":
    pytest.main()