# This class lists the Login module elements
class Hrm_Login_Pg:
    def __init__(self, a_driver):
        self.my_driver = a_driver

    username = "username"
    password = "password"
    login_btn = '//form/div[3]/button'
    login_header = '//h5[text()="Login"]'
    dashboard_header_locator = "h6"
    invalid_credential_locator = '//p[text()="Invalid credentials"]'
    username_required_locator = "(//span[text()='Required'])[1]"
    password_required_locator = "(//span[text()='Required'])[2]"
    logout_dd = "//p[@class='oxd-userdropdown-name']"
    logout_txt = "//a[text()='Logout']"
    login_forgot_password = '//div[@class="orangehrm-login-forgot"]'
    reset_password_header_text = '//div[@class="orangehrm-forgot-password-wrapper"]/div/form/h6[text()="Reset ' \
                                 'Password"]'
    reset_password_username = '//input[@name="username"]'
    reset_cancel_btn = '//button[text()=" Cancel "]'
    reset_btn = '//button[text()=" Reset Password "]'
    reset_password_success = '//h6[text()="Reset Password link sent successfully"]'


# This class lists the Admin module elements
class Hrm_Admin_Pg:
    def __init__(self, a_driver):
        self.my_driver = a_driver

    admin_menu_link = '//span[text()="Admin"]'
    pim_menu_link = '//span[text()="PIM"]'
    leave_menu_link = '//span[text()="Leave"]'
    time_menu_link = '//span[text()="Time"]'
    recruitment_menu_link = '//span[text()="Recruitment"]'
    my_info_menu_link = '//span[text()="My Info"]'
    performance_menu_link = '//span[text()="Performance"]'
    dashboard_menu_link = '//span[text()="Dashboard"]'
    directory_menu_link = '//span[text()="Directory"]'
    maintenance_menu_link = '//span[text()="Maintenance"]'
    claim_menu_link = '//span[text()="Claim"]'
    buzz_menu_link = '//span[text()="Buzz"]'
    admin_dashboard_header_locator1 = '//h6[text()="Admin"]//following-sibling::h6[text()="Admin"]'
    admin_dashboard_header_locator2 = '//h6[text()="Admin"]//following-sibling::h6[text()="User Management"]'
    admin_tab_user_mgmt = '//nav[@class="oxd-topbar-body-nav"]//li//span[text()="User Management "]'
    admin_tab_job = '//nav[@class="oxd-topbar-body-nav"]//li//span[text()="Job "]'
    admin_tab_organization = '//nav[@class="oxd-topbar-body-nav"]//li//span[text()="Organization "]'
    admin_tab_qualification = '//nav[@class="oxd-topbar-body-nav"]//li//span[text()="Qualifications "]'
    admin_tab_nationalities = '//nav[@class="oxd-topbar-body-nav"]//li//a[text()="Nationalities"]'
    admin_tab_corporate_branding = '//nav[@class="oxd-topbar-body-nav"]//li//a[text()="Corporate Branding"]'
    admin_tab_configuration = '//nav[@class="oxd-topbar-body-nav"]//li//span[text()="Configuration "]'


# This class lists the PIM module elements
class HRM_PIM_Page:
    def __init__(self, a_driver):
        self.my_driver = a_driver

    element_pim_link = "//span[text()='PIM']"
    add_employee_btn = "//button[text()=' Add ']"
    emp_first_name = "firstName"
    emp_middle_name = "middleName"
    emp_last_name = "lastName"
    save_btn = "//button[text()=' Save ']"
    emp_id = 0
    emp_list = []
    pim_pg_tabs = "//a[@class='oxd-topbar-body-nav-tab-item']"
    pim_emp_total = "//div[@class='orangehrm-header-container']/following-sibling::div/div[1]/span"
    pim_emp_search_by_name = "//input[@placeholder='Type for hints...'][1]"
    pim_emp_search_btn = "//button[@type='submit']"
    pim_search_no_records_found = "//span[text()='No Records Found']"
    pim_delete_emp_btn = "//button[text()=' Delete Selected ']"
    pim_emp_yes_delete = "//button[text()=' Yes, Delete ']"
    pim_emp_no_cancel = "//button[text()=' No, Cancel ']"
    pim_search_results_table = "//*[@role='table']/div[2]/div"
    pim_search_results_table_select_ck_box = "(//i[@class='oxd-icon bi-check oxd-checkbox-input-icon'])[2]"
    pim_search_results_table_emp_id = "//div[@class='oxd-table-body']/div/div/div[2]/div"
    pim_search_results_table_emp_first_and_middle_name = "//div[@class='oxd-table-body']/div/div/div[3]/div"
    pim_emp_fname_search_input = "//input[@placeholder='Type for hints...'][1]"
    pim_emp_search_id_label = "//label[text()='Employee Id']"
    pim_search_table_rows = "//div[@class='oxd-table-card']"
    pim_add_img_btn = "//div[@class='employee-image-wrapper']//following-sibling::button"
    pim_details_emp_nickname = "//label[text()='Nickname']"
    pim_details_emp_other_id = "//label[text()='Other Id']"
    pim_emp_id_label = "//label[text()='Employee Id']"
    pim_emp_drivers_license_label = "//label[contains (text(), 'License Number')]"
    pim_emp_drivers_license_expiry_label = "//label[text()='License Expiry Date']"
    pim_emp_ssn_label = "//label[text()='SSN Number']"
    pim_emp_sin_label = "//label[text()='SIN Number']"
    pim_emp_nationality_label = "//label[text()='Nationality']"
    pim_emp_nationality_dd = "(//div[@class='oxd-select-text-input'])[1]"
    pim_emp_marital_status_label = "//label[text()='Marital Status']"
    pim_emp_marital_status_dd = "(//div[@class='oxd-select-text-input'])[2]"
    pim_emp_dob_label = "//label[text()='Date of Birth']"
    pim_emp_gender_male = "//input[@type='radio'][@value='1']"
    pim_emp_gender_female = "//input[@type='radio'][@value='2']"
    pim_emp_military_status = "//label[text()='Military Service']"
    pim_emp_smokes_checkbox = "//input[@type='checkbox']//following-sibling::span"
    pim_emp_blood_group_dd = "(//div[@class='oxd-select-text-input'])[3]"
    pim_emp_standard_fields_save_btn = "(//form[@class='oxd-form']//button[text()=' Save '])[1]"
    pim_emp_custom_field_save_btn = "//div[@class='orangehrm-custom-fields']//button[text()=' Save ']"
    pim_emp_id_exists_msg = "//span[text()='Employee Id already exists']"


