import time

from behave import *
from selenium import webdriver
from POM import home_page, login_page, dashboard_page


@given('launch Chrome browser')
def launch_chrome(context):
    context.driver = webdriver.Chrome()


@when('open GigaStore Homepage')
def navigate_homepage(context):
    context.driver.get('https://gigastore.holeapi.com/#/')
    time.sleep(2)
    home_page.get_login_button(context.driver).click()


@when('Enter username "{username}" and password "{password}"')
def step_impl(context, username, password):
    time.sleep(2)
    login_page.set_email(context.driver, username)
    login_page.set_password(context.driver, password)


@when('Click on login button')
def step_impl(context):
    login_page.get_sign_in_button(context.driver).click()
    time.sleep(2)


@then('User must successfully login to the Dashboard page')
def step_impl(context):
    assert dashboard_page.get_logo_img(context.driver).is_displayed() is True
