from PageObject.LoginPage import LoginPage
from utilities.Logger import LogGenerator
from utilities.readProperties import Readconfig


class TestLoginParam:
    url = Readconfig.URL()
    email = Readconfig.Email()
    password = Readconfig.Password()
    log = LogGenerator.loggen()

    def test_login_param_004(self, setup, getdataforlogin):
        self.log.info("test_login_param_004 is started")
        self.driver = setup
        self.log.info("opening browser")
        self.driver.get(self.url)
        self.log.info("entering url" + self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.lp = LoginPage(self.driver)
        self.lp.my_account()
        self.log.info("clicking on myaccount")
        self.lp.login()
        self.log.info("clicking on login")
        self.lp.enter_email_address(getdataforlogin[0])
        self.log.info("entering email address-->" + self.email)
        self.lp.enter_password(getdataforlogin[1])
        self.log.info("entering password-->" + self.password)
        self.lp.login_btn()
        self.log.info("clicking on login button")
        statuslist = []
        if self.driver.title == "My Account":
            if getdataforlogin[2] == "Pass":
                self.log.info("page title-->" + self.driver.title)
                self.driver.save_screenshot("C:\\Users\\admin\\PycharmProjects\\TutorialNinjaProject\\Screenshots"
                                            "\\test_login_param_004_pass.png")
                self.lp.my_account()
                self.log.info("clicking on myaccount")
                self.lp.logout_option()
                self.log.info("clicking on logout")
                statuslist.append("Pass")
                self.driver.close()

            elif getdataforlogin[2] == "Fail":
                self.log.info("page title-->" + self.driver.title)
                self.driver.save_screenshot("C:\\Users\\admin\\PycharmProjects\\TutorialNinjaProject\\Screenshots"
                                            "\\test_login_param_004_fail.png")
                self.lp.my_account()
                self.log.info("clicking on myaccount")
                self.lp.logout_option()
                self.log.info("clicking on logout")
                statuslist.append("Fail")
                self.driver.close()

        else:
            if getdataforlogin[2] == "Pass":
                self.log.info("page title-->" + self.driver.title)
                self.driver.save_screenshot("C:\\Users\\admin\\PycharmProjects\\TutorialNinjaProject\\Screenshots"
                                            "\\test_login_param_004_fail.png")
                statuslist.append("Fail")
                self.driver.close()

            elif getdataforlogin[2] == "Fail":

                self.log.info("page title-->" + self.driver.title)
                self.driver.save_screenshot("C:\\Users\\admin\\PycharmProjects\\TutorialNinjaProject\\Screenshots"
                                            "\\test_login_param_004_pass.png")
                statuslist.append("Pass")
                self.driver.close()

        if "Pass" in statuslist:
            assert True
            self.log.info("test_login_param_004 is passed")
        else:
            self.log.info("test_login_param_004 is Failed")
            assert False

        self.log.info("test_login_param_004 is completed")

