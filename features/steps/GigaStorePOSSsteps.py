import time
import allure

from behave import *
from selenium import webdriver
from POM import home_page


@given(u'login to the GigaStore')
def login(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://gigastore.holeapi.com/#/')
    time.sleep(5)
    context.driver.find_element_by_xpath('//*[@id="start"]/div[2]/div/div/div[2]/div[1]/div/button[2]').click()
    time.sleep(5)
    context.driver.find_element_by_id('username').send_keys('t.m@tm.tm')
    context.driver.find_element_by_id('password').send_keys('Qwerty12345')
    context.driver.find_element_by_id('kc-login').click()
    time.sleep(5)


@when(u'navigate to Point of Sale store')
def navigate_to_poss(context):
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]/div[1]/div[3]/div[2]').click()
    time.sleep(2)
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]/div[2]/div[1]/div[2]/button').click()
    time.sleep(2)


@when(u'click on New Customer card')
def click_on_new_customer_card(context):
    tab_list = context.driver.window_handles
    context.driver.switch_to.window(tab_list[1])
    time.sleep(2)
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div/div/div[1]/h2').click()


@then(u'verify navigation to New Customer card')
def verify_customer_card(context):
    try:
        element = context.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div/h2')
        assert element.text == "New Customer"
    except:
        allure.attach(context.driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
        context.driver.close()


@then(u'close browser')
def close_browser(context):
    context.driver.close()
