import time
from library.excel_lib import ReadExcel
from library.config import Configuration


class LoginPage:

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
        loc = self.log_loc["switch_ele"]
        self.driver.switch_to.frame(self.driver.find_element(*loc))

    def mobile_num(self, number):
        if isinstance(number,float):
            number = int(number)
        # assert len(number[0]) == 10
        loc = self.log_loc["mobile_number"]
        self.driver.find_element(*loc).send_keys(number)
        time.sleep(15)

    def generate_btn(self):

        loc = self.log_loc["generate_btn"]
        self.driver.find_element(*loc).click()
        time.sleep(2)

    def login_btn(self):
        time.sleep(30)
        loc = self.log_loc["login_btn"]
        self.driver.find_element(*loc).click()



