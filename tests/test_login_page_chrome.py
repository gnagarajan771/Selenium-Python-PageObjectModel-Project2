import json
import os
import time
import unittest
from os.path import dirname as up

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from org_hrm_xpath.org_hrm_objects import Hrm_Login_Pg, Hrm_Admin_Pg
from utilities.util import login, take_screenshot, logout, verify_unsuccessful_login_attempt_required_fields_missing, \
    verify_unsuccessful_login_attempt, login_pg_reset_password, verify_pwd_reset_cancel


# This file lists the tests related to the LOGIN module of the Orange HRM website
class LoginPgTestClass(unittest.TestCase):
    driver = None
    data_dict = None

    # The setup class loads the test data and the webpage
    @classmethod
    def setUpClass(cls) -> None:
        cwd = os.getcwd()
        cwd_one_up = up(up(__file__))
        json_file_path = cwd_one_up + "\\org_hrm_data_source\\org_hrm_test_data.json"
        with open(json_file_path) as json_file:
            cls.data_dict = json.load(json_file)
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(15)
        cls.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    #   Positive test for successful login to the Orange HRM Portal
    def test_tc_login_01_success(self):
        print(self.data_dict.get("login_credentials").get("correct_username"))
        hrm_login_obj = Hrm_Login_Pg(self.driver)
        self.driver.find_element(By.NAME, hrm_login_obj.username).send_keys(
            self.data_dict.get("login_credentials").get("correct_username"))
        self.driver.find_element(By.NAME, hrm_login_obj.password).send_keys(
            self.data_dict.get("login_credentials").get("correct_password"))
        login(self.driver)
        assert hrm_login_obj.my_driver.find_element(By.TAG_NAME, hrm_login_obj.dashboard_header_locator).text == "Dashboard"
        print(f"SUCCESS # Logged in Successfully using")
        take_screenshot(self.driver, 'tc_login_01_login_success')
        logout(self.driver)

    #   Negative test for unsuccessful login to the Orange HRM Portal
    def test_tc_login_02_unsuccessful_blank_username_password(self):
        hrm_login_obj = Hrm_Login_Pg(self.driver)
        self.driver.find_element(By.NAME, hrm_login_obj.username).send_keys(
            (self.data_dict.get("login_credentials").get("blank_username")))
        self.driver.find_element(By.NAME, hrm_login_obj.password).send_keys(
            self.data_dict.get("login_credentials").get("blank_password"))
        login(self.driver)
        verify_unsuccessful_login_attempt_required_fields_missing(self.driver)
        take_screenshot(self.driver, 'tc_login_02_unsuccessful_blanks')

    #   Negative test for unsuccessful login to the Orange HRM Portal
    def test_tc_login_03_unsuccessful_incorrect_username(self):
        hrm_login_obj = Hrm_Login_Pg(self.driver)
        self.driver.find_element(By.NAME, hrm_login_obj.username).send_keys(
            (self.data_dict.get("login_credentials").get("incorrect_username")))
        self.driver.find_element(By.NAME, hrm_login_obj.password).send_keys(
            self.data_dict.get("login_credentials").get("correct_password"))
        login(self.driver)
        verify_unsuccessful_login_attempt(self.driver)
        take_screenshot(self.driver, 'tc_login_03_unsuccessful_username_issue')
        print(f'SUCCESS # Login was unsuccessful with incorrect username {self.data_dict.get("login_credentials").get("incorrect_username")}')

    # Negative test for unsuccessful login to the Orange HRM Portal
    def test_tc_login_04_unsuccessful_incorrect_password(self):
        hrm_login_obj = Hrm_Login_Pg(self.driver)
        self.driver.find_element(By.NAME, hrm_login_obj.username).send_keys(
            (self.data_dict.get("login_credentials").get("correct_username")))
        self.driver.find_element(By.NAME, hrm_login_obj.password).send_keys(
            self.data_dict.get("login_credentials").get("incorrect_password"))
        login(self.driver)
        verify_unsuccessful_login_attempt(self.driver)
        take_screenshot(self.driver, 'tc_login_04_unsuccessful_pwd_issue')
        print('SUCCESS # Login was unsuccessful with incorrect password')

    # Positive test for password reset cancellation
    def test_tc_password_reset_05_cancel(self):
        hrm_login_obj = Hrm_Login_Pg(self.driver)
        self.driver.find_element(By.XPATH, hrm_login_obj.login_forgot_password).click()
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, hrm_login_obj.reset_password_username)))
        self.driver.find_element(By.XPATH, hrm_login_obj.reset_password_username).send_keys(self.data_dict.get("login_credentials").get("correct_username"))
        take_screenshot(self.driver, 'tc_login_05_password_reset_cancellation')
        self.driver.find_element(By.XPATH, hrm_login_obj.reset_cancel_btn).click()
        login_header_text = self.driver.find_element(By.XPATH, hrm_login_obj.login_header).text
        assert login_header_text == "Login"
        take_screenshot(self.driver, 'tc_login_05_password_reset_cancellation')
        print(
            f'SUCCESS # Password reset was successfully cancelled for {self.data_dict.get("login_credentials").get("correct_username")}')

    #   Positive test for password reset cancellation
    def test_tc_password_reset_06_success(self):
        hrm_login_obj = Hrm_Login_Pg(self.driver)
        self.driver.find_element(By.XPATH, hrm_login_obj.login_forgot_password).click()
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, hrm_login_obj.reset_password_username)))
        self.driver.find_element(By.XPATH, hrm_login_obj.reset_password_username).send_keys(
            self.data_dict.get("login_credentials").get("correct_username"))
        take_screenshot(self.driver, 'tc_login_06_password_reset_success')
        self.driver.find_element(By.XPATH, hrm_login_obj.reset_btn).click()
        reset_success_text = self.driver.find_element(By.XPATH, hrm_login_obj.reset_password_success).text
        assert reset_success_text == "Reset Password link sent successfully"
        take_screenshot(self.driver, 'tc_login_06_password_reset_success')
        print(f'SUCCESS # Password reset was successful with the message:- {reset_success_text}')
