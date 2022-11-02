import datetime
import time

from behave import *
from selenium import webdriver


@given(u'User should be able to launch the browser')
def launch_browser(context):
    path = r"C:\Users\shris\PycharmProjects\behaveREDBUS\drivers\chromedriver.exe"
    context.driver = webdriver.Chrome(executable_path=path)
    context.driver.get(r"https://www.redbus.in/")
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)


@when(u'User should be able to click on signup icon')
def signup_icon(context):
    try:
        context.driver.find_element('css selector', 'i[id="i-icon-profile"]').click()
    except BaseException as error_msg:
        td = datetime.datetime.now()
        name = f"screenshot_{td.hour}_{td.minute}_{td.second}.png"
        ss_path = r"../screenshots/"
        context.driver.save_screenshot(ss_path + name)
        raise error_msg


@then(u'User should be able to click on signup link')
def signup_link(context):
    try:
        context.driver.find_element('css selector', 'li[id="signInLink"]').click()
    except BaseException as error_msg:
        td = datetime.datetime.now()
        name = f"screenshot_{td.hour}_{td.minute}_{td.second}.png"
        ss_path = r"../screenshots/"
        context.driver.save_screenshot(ss_path + name)
        raise error_msg

@then(u'user should be able to enter the phone number "{number}"')
def mobile_num(context, number):
    try:
        element = context.driver.find_element("xpath", '//iframe[@class="modalIframe"]')
        context.driver.switch_to.frame(element)
        context.driver.find_element('css selector', 'input[id="mobileNoInp"]').send_keys(number)
        time.sleep(20)
    except BaseException as error_msg:
        td = datetime.datetime.now()
        name = f"screenshot_{td.hour}_{td.minute}_{td.second}.png"
        ss_path = r"../screenshots/"
        context.driver.save_screenshot(ss_path + name)
        raise error_msg


@then(u'user should be able to click on Generate OTP button')
def generate_btn(context):
    try:
        context.driver.find_element('xpath', '//span[@class="f-w-b"]').click()
        time.sleep(15)
    except BaseException as error_msg:
        td = datetime.datetime.now()
        name = f"screenshot_{td.hour}_{td.minute}_{td.second}.png"
        ss_path = r"../screenshots/"
        context.driver.save_screenshot(ss_path + name)
        raise error_msg


@then(u'user should be able to click on Verify user button')
def login_btn(context):
    try:
        context.driver.find_element('xpath', '//button[@id="verifyUser"]').click()
        time.sleep(4)
        context.driver.find_element('css selector', 'i[id="i-icon-profile"]').click()
        context.driver.find_element('xpath', '//li[text()="Sign Out From All Devices"]').click()
    except BaseException as error_msg:
        td = datetime.datetime.now()
        name = f"screenshot_{td.hour}_{td.minute}_{td.second}.png"
        ss_path = r"../screenshots/"
        context.driver.save_screenshot(ss_path + name)
        raise error_msg

@then(u'User should be able to click on Facebook link')
def facebook_link(context):
    try:
        element = context.driver.find_element("xpath", '//iframe[@class="modalIframe"]')
        context.driver.switch_to.frame(element)
        gmail = context.driver.find_element("xpath", '//iframe[@title="Sign in with Google Button"]')
        context.driver.switch_to.frame(gmail)
        context.driver.find_element('xpath', '//div[text()="Facebook"]').click()
        time.sleep(4)
    except BaseException as error_msg:
        td = datetime.datetime.now()
        name = f"screenshot_{td.hour}_{td.minute}_{td.second}.png"
        ss_path = r"../screenshots/"
        context.driver.save_screenshot(ss_path + name)
        raise error_msg


@then(u'user should be able to provide vaild email "{email}"')
def email(context, email):
    try:

        handles = context.driver.window_handles
        context.driver.switch_to.window(handles[1])
        context.driver.find_element('css selector', 'input[id="email"]').send_keys(email)

    except BaseException as error_msg:
        td = datetime.datetime.now()
        name = f"screenshot_{td.hour}_{td.minute}_{td.second}.png"
        ss_path = r"../screenshots/"
        context.driver.save_screenshot(ss_path + name)
        raise error_msg


@then(u'user should be able to provide vaild password "{password}"')
def password(context, password):
    try:
        context.driver.find_element('css selector', 'input[id="pass"]').send_keys(password)
    except BaseException as error_msg:
        td = datetime.datetime.now()
        name = f"screenshot_{td.hour}_{td.minute}_{td.second}.png"
        ss_path = r"../screenshots/"
        context.driver.save_screenshot(ss_path + name)
        raise error_msg


@then(u'user should be able to click on login button')
def login(context):
    try:
        context.driver.find_element('css selector', 'input[name="login"]').click()
        context.driver.find_element('css selector', 'i[id="i-icon-profile"]').click()
        context.driver.find_element('xpath', '//li[text()="Sign Out From All Devices"]').click()

    except BaseException as error_msg:
        td = datetime.datetime.now()
        name = f"screenshot_{td.hour}_{td.minute}_{td.second}.png"
        ss_path = r"../screenshots/"
        context.driver.save_screenshot(ss_path + name)
        raise error_msg

@then(u'User should be able to click on gmail link')
def gmail_link(context):
    try:
        element = context.driver.find_element("xpath", '//iframe[@class="modalIframe"]')
        context.driver.switch_to.frame(element)
        gmail = context.driver.find_element("xpath", '//iframe[@title="Sign in with Google Button"]')
        context.driver.switch_to.frame(gmail)
        context.driver.find_element('xpath', '(//span[text()="Sign in with Google"])[1]').click()

    except BaseException as error_msg:
        td = datetime.datetime.now()
        name = f"screenshot_{td.hour}_{td.minute}_{td.second}.png"
        ss_path = r"../screenshots/"
        context.driver.save_screenshot(ss_path + name)
        raise error_msg


@then(u'user should be able to enter email "{gmail}"')
def gmail(context, gmail):
    try:

        handles = context.driver.window_handles
        context.driver.switch_to.window(handles[1])
        time.sleep(1)
        context.driver.find_element('xpath', '//input[@id="identifierId"]').send_keys(gmail)

    except BaseException as error_msg:
        td = datetime.datetime.now()
        name = f"screenshot_{td.hour}_{td.minute}_{td.second}.png"
        ss_path = r"../screenshots/"
        context.driver.save_screenshot(ss_path + name)
        raise error_msg


@then(u'user should be able to click om next button')
def next_btn(context):
    try:
        context.driver.find_element('xpath', '//span[text()="Next"]').click()
        time.sleep(2)

    except BaseException as error_msg:
        td = datetime.datetime.now()
        name = f"screenshot_{td.hour}_{td.minute}_{td.second}.png"
        ss_path = r"../screenshots/"
        context.driver.save_screenshot(ss_path + name)
        raise error_msg

@then(u'user should be able to enter password "{password}"')
def password(context, password):
    try:
        context.driver.find_element('xpath', '(//input[@jsname="YPqjbf"])[1]').send_keys(password)

    except BaseException as error_msg:
        td = datetime.datetime.now()
        name = f"screenshot_{td.hour}_{td.minute}_{td.second}.png"
        ss_path = r"../screenshots/"
        context.driver.save_screenshot(ss_path + name)
        raise error_msg



