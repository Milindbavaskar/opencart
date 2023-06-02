from selenium.webdriver.common.by import By


class RegisterPage:
    Click_MyAccount_XPATH = (By.XPATH, "//span[normalize-space()='My Account']")
    Click_Register_XPATH = (By.XPATH, "//a[normalize-space()='Register']")
    Text_FirstName_XPATH = (By.XPATH, "//input[@id='input-firstname']")
    Text_LastName_XPATH = (By.XPATH, "//input[@id='input-lastname']")
    Text_Email_XPATH = (By.XPATH, "//input[@id='input-email']")
    Text_Telephone_XPATH = (By.XPATH, "//input[@id='input-telephone']")
    Text_Password_XPATH = (By.XPATH, "//input[@id='input-password']")
    Text_Confpassword_XPATH = (By.XPATH, "//input[@id='input-confirm']")
    Click_Ppolicy_XPATH = (By.XPATH, "//input[@name='agree']")
    Btn_Continue_XPATH = (By.XPATH, "//input[@value='Continue']")
    Click_Continue_XPATH = (By.XPATH, "//a[@class='btn btn-primary']")
    Click_Logout_XPATH = (By.XPATH, "//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='Logout']")

    def __init__(self, driver):
        self.driver = driver

    def my_account(self):
        self.driver.find_element(*RegisterPage.Click_MyAccount_XPATH).click()

    def register(self):
        self.driver.find_element(*RegisterPage.Click_Register_XPATH).click()

    def enter_firstname(self, fname):
        self.driver.find_element(*RegisterPage.Text_FirstName_XPATH).send_keys(fname)

    def enter_lastname(self, lname):
        self.driver.find_element(*RegisterPage.Text_LastName_XPATH).send_keys(lname)

    def enter_email(self, email):
        self.driver.find_element(*RegisterPage.Text_Email_XPATH).send_keys(email)

    def enter_telephone(self, tel):
        self.driver.find_element(*RegisterPage.Text_Telephone_XPATH).send_keys(tel)

    def enter_password(self, password):
        self.driver.find_element(*RegisterPage.Text_Password_XPATH).send_keys(password)

    def enter_confirm_password(self, cpassword):
        self.driver.find_element(*RegisterPage.Text_Confpassword_XPATH).send_keys(cpassword)

    def privacy_policy(self):
        self.driver.find_element(*RegisterPage.Click_Ppolicy_XPATH).click()

    def btn_continue(self):
        self.driver.find_element(*RegisterPage.Btn_Continue_XPATH).click()

    def logout(self):
        self.driver.find_element(*RegisterPage.Click_Logout_XPATH).click()

    def continue_btn(self):
        self.driver.find_element(*RegisterPage.Click_Continue_XPATH).click()
