import json
import os
import datetime
from os.path import dirname as up

import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from multipledispatch import dispatch

from org_hrm_xpath.org_hrm_objects import Hrm_Login_Pg

cwd = os.getcwd()
cwd_one_up = up(up(__file__))
json_file_path = cwd_one_up + "\\org_hrm_data_source\\org_hrm_test_data.json"
with open(json_file_path) as json_file:
    data_dict = json.load(json_file)


def login(my_driver):
    hrm_login_obj = Hrm_Login_Pg(my_driver)
    my_driver.find_element(By.XPATH, hrm_login_obj.login_btn).click()


def login_as_admin(my_driver):
    hrm_login_obj = Hrm_Login_Pg(my_driver)
    my_driver.find_element(By.NAME, hrm_login_obj.username).send_keys(
        data_dict.get("login_credentials").get("correct_username"))
    my_driver.find_element(By.NAME, hrm_login_obj.password).send_keys(
        data_dict.get("login_credentials").get("correct_password"))
    my_driver.find_element(By.XPATH, hrm_login_obj.login_btn).click()


def logout(my_driver):
    hrm_login_obj = Hrm_Login_Pg(my_driver)
    my_driver.find_element(By.XPATH, hrm_login_obj.logout_dd).click()
    my_driver.find_element(By.XPATH, hrm_login_obj.logout_txt).click()


def check_for_title(driver, title_name):
    dashboard_header_locator = "h6"
    dashboard_header_locator = driver.find_element(By.TAG_NAME, dashboard_header_locator)
    if dashboard_header_locator is not None:
        return True


@dispatch(selenium.webdriver.chrome.webdriver.WebDriver)
def take_screenshot(my_driver):
    vDate = datetime.datetime.now().date()
    vHOUR = datetime.datetime.now().hour  # the current hour
    vMINUTE = datetime.datetime.now().minute  # the current minute
    vSECONDS = datetime.datetime.now().second  # the current second
    result = str(vDate) + "_ts" + str(vHOUR) + str(vMINUTE) + str(vSECONDS)
    cwd = os.getcwd()
    my_driver.get_screenshot_as_file(
        f"C:\\Users\\gayat\\PycharmProjects\\pythonProject\\AT_Project2_OrangeHRM\\pytest_screenshots\\{result}.png")


@dispatch(selenium.webdriver.chrome.webdriver.WebDriver, str)
def take_screenshot(my_driver, testcase_name):
    vDate = datetime.datetime.now().date()
    vHOUR = datetime.datetime.now().hour  # the current hour
    vMINUTE = datetime.datetime.now().minute  # the current minute
    vSECONDS = datetime.datetime.now().second  # the current second
    result = "__" + str(vDate) + "_ts" + str(vHOUR) + str(vMINUTE) + str(vSECONDS)
    cwd = os.getcwd()
    my_driver.get_screenshot_as_file(
        f"C:\\Users\\gayat\\PycharmProjects\\pythonProject\\AT_Project2_OrangeHRM\\pytest_screenshots\\{testcase_name}{result}.png")


def scroll_to_page(my_driver, element_selenium):
    my_driver.execute_script("arguments[0].scrollIntoView(true);", element_selenium)


def wait_for_element(my_driver, element_selenium):
    WebDriverWait(my_driver, 10).until(EC.presence_of_element_located((By.XPATH, element_selenium)))


def verify_unsuccessful_login_attempt_required_fields_missing(my_driver):
    hrm_login_obj = Hrm_Login_Pg(my_driver)
    try:
        dashboard_header_text = my_driver.find_element(By.TAG_NAME, hrm_login_obj.dashboard_header_locator).text
    except:
        pass
    username_required_text = my_driver.find_element(By.XPATH, hrm_login_obj.username_required_locator).text
    assert username_required_text == "Required"
    password_required_text = my_driver.find_element(By.XPATH, hrm_login_obj.password_required_locator).text
    assert password_required_text == "Required"


def verify_unsuccessful_login_attempt(my_driver):
    hrm_login_obj = Hrm_Login_Pg(my_driver)
    try:
        dashboard_header_text = my_driver.find_element(By.TAG_NAME, hrm_login_obj.dashboard_header_locator).text
    except:
        pass
    invalid_credentials_text = my_driver.find_element(By.XPATH, hrm_login_obj.invalid_credential_locator).text
    assert invalid_credentials_text == "Invalid credentials"


def login_pg_reset_password(self, p_username):
    self.my_driver.find_element(By.XPATH, self.login_forgot_password).click()
    self.my_driver.find_element(By.XPATH, self.reset_password_username).send_keys(p_username)


def verify_pwd_reset_cancel(my_driver):
    hrm_login_obj = Hrm_Login_Pg(my_driver)
    my_driver.find_element(By.XPATH, hrm_login_obj.reset_cancel_btn).click()
    login_header_text = my_driver.find_element(By.XPATH, hrm_login_obj.login_header).text
    assert login_header_text == "Login"


def verify_pwd_reset_successful(my_driver):
    hrm_login_obj = Hrm_Login_Pg(my_driver)
    my_driver.find_element(By.XPATH, hrm_login_obj.reset_btn).click()
    reset_success_text = my_driver.find_element(By.XPATH, hrm_login_obj.reset_password_success).text
    assert reset_success_text == "Reset Password link sent successfully"
