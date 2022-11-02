import pytest

from POM.facebook import FacePage
from library.excel_lib import ReadExcel
from library.config import Configuration

class TestFaceBook:
    read_xl = ReadExcel()
    data = read_xl.read_testdata(Configuration.FACEBOOK_DATA)

    @pytest.mark.parametrize("email, password", data)
    def test_login(self, email, password, init_driver):

        driver = init_driver

        fb = FacePage(driver)

        fb.signup_icon()
        fb.signup_link()
        fb.face_book_link()
        fb.email(email)
        fb.password(password)
        fb.login()
