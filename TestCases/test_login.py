import pytest

from PageObject.LoginPage import LoginPage
from utilities.Logger import LogGenerator
from utilities.readProperties import Readconfig


class TestLogin:
    url = Readconfig.URL()
    email = Readconfig.Email()
    password = Readconfig.Password()
    log=LogGenerator.loggen()

    @pytest.mark.regression
    def test_login_003(self, setup):
        self.log.info("test_login_003 is started")
        self.driver = setup
        self.log.info("opening browser")
        self.driver.get(self.url)
        self.log.info("entering url"+ self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.lp=LoginPage(self.driver)
        self.lp.my_account()
        self.log.info("clicking on myaccount")
        self.lp.login()
        self.log.info("clicking on login")
        self.lp.enter_email_address(self.email)
        self.log.info("entering email address-->"+ self.email)
        self.lp.enter_password(self.password)
        self.log.info("entering password-->"+ self.password)
        self.lp.login_btn()
        self.log.info("clicking on login button")
        if self.driver.title=="My Account":
            self.log.info("page title-->"+ self.driver.title)
            self.driver.save_screenshot("C:\\Users\\admin\\PycharmProjects\\TutorialNinjaProject\\Screenshots"
                                        "\\test_login_003_pass.png")
            self.lp.my_account()
            self.log.info("clicking on myaccount")
            self.lp.logout_option()
            self.log.info("clicking on logout")
            self.log.info("test_login_003 is passed")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\admin\\PycharmProjects\\TutorialNinjaProject\\Screenshots"
                                        "\\test_login_003_fail.png")
            self.log.info("test_login_003 is failed")
            assert False
        self.log.info("test_login_003 is completed")