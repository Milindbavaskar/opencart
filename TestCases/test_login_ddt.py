import allure
from PageObject.LoginPage import LoginPage
from utilities import XLutils
from utilities.Logger import LogGenerator
from utilities.readProperties import Readconfig


class TestLoginDdt:
    url = Readconfig.URL()
    log = LogGenerator.loggen()
    path = "C:\\Users\\admin\\PycharmProjects\\TutorialNinjaProject\\TestData\\test_login_ddt.xlsx"


    @allure.issue("ABC-123")
    @allure.title("Test login ddt")
    @allure.description("This test case verfying login fucntionality with different login scenario using Excel of application ")
    @allure.link(" https://tutorialsninja.com/demo/")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_ddt_005(self, setup):
        self.log.info("test_login_ddt_005 is started")
        self.driver = setup
        self.log.info("opening browser")
        self.driver.get(self.url)
        self.log.info("entering url" + self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.lp = LoginPage(self.driver)
        self.row = XLutils.Rowcount(self.path, "Sheet1")
        print("Number of rows in sheet1 is-->" + str(self.row))
        statuslist = []
        for r in range(2,self.row+1):
            self.lp.my_account()
            self.log.info("clicking on myaccount")
            self.lp.login()
            self.log.info("clicking on login")
            self.email=XLutils.ReadData(self.path,"Sheet1",r,2)
            self.password=XLutils.ReadData(self.path,"Sheet1",r,3)
            self.exp_result=XLutils.ReadData(self.path,"Sheet1",r,4)
            self.lp.enter_email_address(self.email)
            self.log.info("entering email address-->"+ self.email)
            self.lp.enter_password(self.password)
            self.log.info("entering password-->"+ self.password)
            self.lp.login_btn()
            self.log.info("clicking on login button")
            if self.driver.title == "My Account":
                if self.exp_result == "Pass":
                    self.log.info("page title-->" + self.driver.title)
                    self.driver.save_screenshot("C:\\Users\\admin\\PycharmProjects\\TutorialNinjaProject\\Screenshots"
                                                "\\test_login_ddt_005_pass.png")
                    self.lp.my_account()
                    self.log.info("clicking on myaccount")
                    self.lp.logout_option()
                    self.log.info("clicking on logout")
                    statuslist.append("Pass")
                    XLutils.WriteData(self.path,"Sheet1",r,5,"Pass")


                elif self.exp_result == "Fail":
                    self.log.info("page title-->" + self.driver.title)
                    self.driver.save_screenshot("C:\\Users\\admin\\PycharmProjects\\TutorialNinjaProject\\Screenshots"
                                                "\\test_login_ddt_005_fail.png")
                    self.lp.my_account()
                    self.log.info("clicking on myaccount")
                    self.lp.logout_option()
                    self.log.info("clicking on logout")
                    statuslist.append("Fail")
                    XLutils.WriteData(self.path, "Sheet1", r, 5,"Fail")


            else:
                if self.exp_result == "Pass":
                    self.log.info("page title-->" + self.driver.title)
                    self.driver.save_screenshot("C:\\Users\\admin\\PycharmProjects\\TutorialNinjaProject\\Screenshots"
                                                "\\test_login_ddt_005_fail.png")
                    statuslist.append("Fail")
                    XLutils.WriteData(self.path, "Sheet1", r, 5,"Fail")


                elif self.exp_result == "Fail":

                     self.log.info("page title-->" + self.driver.title)
                     self.driver.save_screenshot("C:\\Users\\admin\\PycharmProjects\\TutorialNinjaProject\\Screenshots"
                                                "\\test_login_ddt_005_pass.png")
                     statuslist.append("Pass")
                     XLutils.WriteData(self.path, "Sheet1", r, 5,"Fail")


            if "Fail" not in statuslist:
               assert True
               self.log.info("test_login_ddt_005 is passed")
            else:
               self.log.info("test_login_ddt_005 is Failed")
               assert False

        self.log.info("test_login_ddt_005 is completed")
