import pytest
from selenium import webdriver
from library.config import Configuration


@pytest.fixture(params=["Chrome"])
def init_driver(request):
    browser = request.param

    if browser.lower() == 'chrome':
        driver = webdriver.Chrome(executable_path=Configuration.CHROME_PATH)
    elif browser.lower() == 'firefox':
        driver = webdriver.Firefox(executable_path=Configuration.FIRE_PATH)
    else:
        driver = webdriver.Edge(executable_path=Configuration.EDGE_PATH)


    driver.get(Configuration.URL)

    driver.maximize_window()
    yield driver
    driver.quit()