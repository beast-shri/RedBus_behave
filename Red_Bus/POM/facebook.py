import time
import re
from library.excel_lib import ReadExcel
from library.config import Configuration


class FacePage:

    read_xl = ReadExcel()
    log_loc = read_xl.read_locators(Configuration.LOGIN_PAGE)

    def __init__(self, driver):
        self.driver = driver

    def signup_icon(self):
        loc = self.log_loc["signup_icon"]
        self.driver.find_element(*loc).click()

    def signup_link(self):
        loc = self.log_loc["signup_link"]
        self.driver.find_element(*loc).click()
        time.sleep(3)


    def face_book_link(self):
        loc = self.log_loc["switch_ele"]
        self.driver.switch_to.frame(self.driver.find_element(*loc))
        time.sleep(3)
        loc = self.log_loc["FB_link"]
        self.driver.find_element(*loc).click()
        time.sleep(2)

    def email(self, email):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        time.sleep(2)

        pattern = r"\w+@gmail\.com"
        result = re.findall(pattern, email)
        assert result, "invalid email"

        loc = self.log_loc["FB_email"]
        self.driver.find_element(*loc).send_keys(email)

    def password(self, password):
        loc = self.log_loc["FB_password"]
        self.driver.find_element(*loc).send_keys(password)

    def login(self):
        loc = self.log_loc["FB_login"]
        self.driver.find_element(*loc).click()
