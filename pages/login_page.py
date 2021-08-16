from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        open(http://selenium1py.pythonanywhere.com/)
        assert "login" in self.browser.current_url, "Не тот url/wrong url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(By.CSS_SELECTOR, "#login_form"), "Поле для входа не найдено"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(By.CSS_SELECTOR, "#register_form"), "Поле для регистрации не найдено"

class LoginPageLocators(LoginPage):
    def test_should_be_login_url(self)
        should_be_login_url()
    def test_should_be_login_form(self)
        should_be_login_form()
    def test_should_be_register_form(self)
        should_be_register_form()