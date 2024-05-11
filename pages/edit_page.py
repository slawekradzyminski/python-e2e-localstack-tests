from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.abstract_base_page import AbstractBasePage
from selenium.webdriver.support import expected_conditions as EC
from api.data.register import RegisterRequestDto

class EditPage(AbstractBasePage):
    first_name_input = (By.NAME, "firstName")
    last_name_input = (By.NAME, "lastName")
    email_input = (By.NAME, "email")
    username_input = (By.NAME, "username")
    roles_input = (By.NAME, "roles")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def verify_user_autocomplete(self, user: RegisterRequestDto):
        self.wait.until(EC.visibility_of_element_located(self.first_name_input))
        assert self.driver.find_element(*self.first_name_input).get_attribute('value') == user.firstName, f"Expected first name to be {user.firstName}"
        assert self.driver.find_element(*self.last_name_input).get_attribute('value') == user.lastName, f"Expected last name to be {user.lastName}"
        assert self.driver.find_element(*self.email_input).get_attribute('value') == user.email, f"Expected email to be {user.email}"
        assert self.driver.find_element(*self.username_input).get_attribute('value') == user.username, f"Expected username to be {user.username}"
        assert self.driver.find_element(*self.roles_input).get_attribute('value') == ','.join(user.roles), f"Expected roles to be {','.join(user.roles)}"