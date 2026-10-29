from pages.main_page import MainPage
import time

def test_guest_should_see_login_link(browser):
    link = "https://www.demoblaze.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

