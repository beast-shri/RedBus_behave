import pytest
import datetime

from POM.login_page import LoginPage
from library.excel_lib import ReadExcel
from library.config import Configuration

class TestLoginPage:
    read_xl = ReadExcel()
    data = read_xl.read_testdata(Configuration.LOGIN_DATA)

    @pytest.mark.parametrize("number", data)
    def test_login(self, number, init_driver):

        driver = init_driver
        try:
            lp = LoginPage(driver)
            lp.signup_icon()
            lp.signup_link()
            lp.mobile_num(number)
            lp.generate_btn()
            lp.login_btn()

        except BaseException as error_msg:
            td = datetime.datetime.now()
            name = f"screenshot_{td.hour}_{td.minute}_{td.second}.png"
            driver.save_screenshot(Configuration.SCREENSHOT_PATH + name)
            raise error_msg
