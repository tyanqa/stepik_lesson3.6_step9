import time
link='http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_guest_should_see_basket(browser):
    browser.get(link)
    time.sleep(30)
    basket_button=len(browser.find_elements_by_css_selector(".btn-add-to-basket"))
    assert basket_button > 0, 'basket_button not found'
