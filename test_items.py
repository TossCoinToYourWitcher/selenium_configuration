import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_for_existing_addtocart_button(browser):
    browser.get(link)
    # time.sleep(30)
    button = browser.find_elements_by_css_selector("button.btn.btn-add-to-basket")
    assert button is not None
