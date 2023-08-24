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
from utilities.util import login, take_screenshot, login_as_admin


# This file lists the tests related to the ADMIN module of the Orange HRM website
class AdminPgTestClass(unittest.TestCase):
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

    #   Test verification of the admin page tile and the headers available to an Admin user
    def test_tc_admin_01_verify_headers(self):
        hrm_login_obj = Hrm_Login_Pg(self.driver)
        login_as_admin(self.driver)
        assert hrm_login_obj.my_driver.find_element(By.TAG_NAME,
                                                    hrm_login_obj.dashboard_header_locator).text == "Dashboard"
        print("SUCCESS # Logged in Successfully")

        hrm_admin_obj = Hrm_Admin_Pg(self.driver)
        self.driver.find_element(By.XPATH, hrm_admin_obj.admin_menu_link).click()
        time.sleep(10)
        take_screenshot(self.driver, 'tc_admin_01_verify_headers')
        assert self.driver.title == "OrangeHRM"
        print(f"SUCCESS # Page Title Captured Successfully {self.driver.title}")

        header_user_mgmt_text = self.driver.find_element(By.XPATH, hrm_admin_obj.admin_tab_user_mgmt).text
        header_job_text = self.driver.find_element(By.XPATH, hrm_admin_obj.admin_tab_job).text
        header_organization_text = self.driver.find_element(By.XPATH, hrm_admin_obj.admin_tab_organization).text
        header_qualification_text = self.driver.find_element(By.XPATH, hrm_admin_obj.admin_tab_qualification).text
        header_nationalities = self.driver.find_element(By.XPATH, hrm_admin_obj.admin_tab_nationalities).text
        header_corporate_branding_text = self.driver.find_element(By.XPATH,hrm_admin_obj.admin_tab_corporate_branding).text
        header_config_text = self.driver.find_element(By.XPATH, hrm_admin_obj.admin_tab_configuration).text
        assert header_user_mgmt_text == 'User Management'
        print(f"SUCCESS # Header Verified Successfully for {header_user_mgmt_text}")
        assert header_job_text == 'Job'
        print(f"SUCCESS # Header Verified Successfully for {header_job_text}")
        assert header_organization_text == 'Organization'
        print(f"SUCCESS # Header Verified Successfully for {header_organization_text}")
        assert header_qualification_text == 'Qualifications'
        print(f"SUCCESS # Header Verified Successfully for {header_qualification_text}")
        assert header_nationalities == "Nationalities"
        print(f"SUCCESS # Header Verified Successfully for {header_nationalities}")
        assert header_corporate_branding_text == 'Corporate Branding'
        print(f"SUCCESS # Header Verified Successfully for {header_corporate_branding_text}")
        assert header_config_text == 'Configuration'
        print(f"SUCCESS # Header Verified Successfully for {header_config_text}")

    #   Test verification for the menu options available to an Admin user
    def test_tc_admin_02_verify_menu(self):
        hrm_admin_obj = Hrm_Admin_Pg(self.driver)
        assert self.driver.find_element(By.XPATH, hrm_admin_obj.admin_menu_link).text == "Admin"
        assert self.driver.find_element(By.XPATH, hrm_admin_obj.pim_menu_link).text == "PIM"
        assert self.driver.find_element(By.XPATH, hrm_admin_obj.leave_menu_link).text == "Leave"
        assert self.driver.find_element(By.XPATH, hrm_admin_obj.time_menu_link).text == "Time"
        assert self.driver.find_element(By.XPATH, hrm_admin_obj.recruitment_menu_link).text == "Recruitment"
        assert self.driver.find_element(By.XPATH, hrm_admin_obj.my_info_menu_link).text == "My Info"
        assert self.driver.find_element(By.XPATH, hrm_admin_obj.performance_menu_link).text == "Performance"
        assert self.driver.find_element(By.XPATH, hrm_admin_obj.dashboard_menu_link).text == "Dashboard"
        assert self.driver.find_element(By.XPATH, hrm_admin_obj.directory_menu_link).text == "Directory"
        assert self.driver.find_element(By.XPATH, hrm_admin_obj.maintenance_menu_link).text == "Maintenance"
        assert self.driver.find_element(By.XPATH, hrm_admin_obj.claim_menu_link).text == "Claim"
        assert self.driver.find_element(By.XPATH, hrm_admin_obj.buzz_menu_link).text == "Buzz"
        print(f"SUCCESS # Menu Options were verified Successfully for an Admin user")
        take_screenshot(self.driver, 'tc_admin_02_verify_menu')
