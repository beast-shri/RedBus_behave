# import time
#
# from behave import *
# from selenium import webdriver
#
#
# @given(u'User should be able to launch the browser')
# def launch_browser(context):
#     path = r"C:\Users\shris\PycharmProjects\behaveREDBUS\drivers\chromedriver.exe"
#     context.driver = webdriver.Chrome(executable_path=path)
#     context.driver.get(r"https://www.redbus.in/")
#     context.driver.maximize_window()
#     context.driver.implicitly_wait(10)
#
#
# @when(u'User should be able to click on signup icon')
# def signup_icon(context):
#     context.driver.find_element('css selector', 'i[id="i-icon-profile"]').click()
#
#
# @then(u'User should be able to click on signup link')
# def signup_link(context):
#     context.driver.find_element('css selector', 'li[id="signInLink"]').click()
#
#
# @then(u'User should be able to click on gmail link')
# def gmail_link(context):
#     element = context.driver.find_element("xpath", '//iframe[@class="modalIframe"]')
#     context.driver.switch_to.frame(element)
#
#     gmail = context.driver.find_element("xpath", '//iframe[@title="Sign in with Google Button"]')
#     context.driver.switch_to.frame(gmail)
#     context.driver.find_element('xpath', '(//span[text()="Sign in with Google"])[1]').click()
#
#
# @then(u'user should be able to enter email "{gmail}"')
# def gmail(context, gmail):
#
#     handles = context.driver.window_handles
#     context.driver.switch_to.window(handles[1])
#     time.sleep(1)
#     context.driver.find_element('xpath', '//input[@id="identifierId"]').send_keys(gmail)
#
#
# @then(u'user should be able to click om next button')
# def next_btn(context):
#     context.driver.find_element('xpath', '//span[text()="Next"]').click()
#
#
