import pytest
import time
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_add_to_cart_button(browser):
    browser.get(link)
    add_to_cart_button = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')
    assert add_to_cart_button.is_displayed(), 'There is no add to cart button'
    
if __name__ == "__main__":
    pytest.main()