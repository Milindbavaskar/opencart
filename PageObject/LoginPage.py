from selenium.webdriver.common.by import By


class LoginPage:
    Click_MyAccount_XPATH = (By.XPATH, "//span[normalize-space()='My Account']")
    Click_Login_XPATH = (By.XPATH, "//a[normalize-space()='Login']")
    Text_Email_address_XPATH = (By.XPATH, "//input[@id='input-email']")
    Text_Password_XPATH = (By.XPATH, "//input[@id='input-password']")
    Btn_Login_XPATH = (By.XPATH, "//input[@type='submit']")
    Click_Logout_XPATH = (By.XPATH, "//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='Logout']")

    def __init__(self, driver):
        self.driver = driver

    def my_account(self):
        self.driver.find_element(*LoginPage.Click_MyAccount_XPATH).click()

    def login(self):
        self.driver.find_element(*LoginPage.Click_Login_XPATH).click()

    def enter_email_address(self, email):
        self.driver.find_element(*LoginPage.Text_Email_address_XPATH).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*LoginPage.Text_Password_XPATH).send_keys(password)

    def login_btn(self):
        self.driver.find_element(*LoginPage.Btn_Login_XPATH).click()

    def logout_option(self):
        self.driver.find_element(*LoginPage.Click_Logout_XPATH).click()


