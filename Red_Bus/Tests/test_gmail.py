import datetime
import time

import pytest

from POM.gmail import GmailPage
from library.excel_lib import ReadExcel
from library.config import Configuration

class TestGmail:
    read_xl = ReadExcel()
    data = read_xl.read_testdata(Configuration.GMAIL_DATA)

    @pytest.mark.parametrize("gmail ,password", data)
    def test_login(self, gmail, password, init_driver):

        driver = init_driver

        gm = GmailPage(driver)

        try:
            gm.signup_icon()
            gm.signup_link()
            gm.gmail_link()
            gm.gmail(gmail)
            gm.mail_btn()
            gm.g_password(password)
            gm.g_password_btn()

        except BaseException as error_msg:
            td = datetime.datetime.now()
            name = f"screenshot_{td.hour}_{td.minute}_{td.second}.png"
            driver.save_screenshot(Configuration.SCREENSHOT_PATH + name)
            raise error_msg
