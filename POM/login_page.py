
def set_email(driver, email):
    driver.find_element_by_id('username').send_keys(email)


def set_password(driver, password):
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)


def get_sign_in_button(driver):
    return driver.find_element_by_xpath('//*[@id="kc-login"]')
