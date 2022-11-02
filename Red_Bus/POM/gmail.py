import time
import re
from library.excel_lib import ReadExcel
from library.config import Configuration


class GmailPage:

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


    def gmail_link(self):
        loc = self.log_loc["switch_ele"]
        self.driver.switch_to.frame(self.driver.find_element(*loc))
        time.sleep(3)
        loc1 = self.log_loc["Gmail_iframe"]
        self.driver.switch_to.frame(self.driver.find_element(*loc1))
        loc3 = self.log_loc["Gmail_link"]
        self.driver.find_element(*loc3).click()

    def gmail(self, gmail):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        time.sleep(3)
        loc = self.log_loc["Gmail_mail"]
        self.driver.find_element(*loc).send_keys(gmail)

    def mail_btn(self):
        loc = self.log_loc["Gmail_login_btn"]
        self.driver.find_element(*loc).click()
        time.sleep(1)

    def g_password(self, password):
        time.sleep(1)
        loc = self.log_loc["G_password"]
        self.driver.find_element(*loc).send_keys(password)

    def g_password_btn(self):
        loc = self.log_loc["G_password_btn"]
        self.driver.find_element(*loc).click()
