import pytest

from PageObject.RegisterPage import RegisterPage
from utilities.Logger import LogGenerator
from utilities.readProperties import Readconfig


class TestRegister:
    url=Readconfig.URL()
    log=LogGenerator.loggen()

    @pytest.mark.regression
    def test_page_title_001(self, setup):
        self.log.info("test_page_title_001 is started")
        self.driver = setup
        self.log.info("opening browser")
        self.driver.get(self.url)
        self.log.info("Going to url--->"+ self.url)
        self.driver.maximize_window()
        self.log.info("maximize window")
        if self.driver.title == "Your Store":
            self.log.info("page title-->" + self.driver.title)
            self.driver.save_screenshot("C:\\Users\\admin\\PycharmProjects\\TutorialNinjaProject\\Screenshots"
                                        "\\test_reg_001_pass.png")
            self.log.info("taking screenshot")
            self.log.info("test_page_title_001 is passed")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\admin\\PycharmProjects\\TutorialNinjaProject\\Screenshots"
                                        "\\test_reg_001_failed.png")
            self.log.info("taking screenshot")
            self.log.info("test_page_title_001 is failed")
            assert False
        self.log.info("test_page_title_001 is completed")


    def test_register_002(self, setup):
        self.log.info("test_register_002 is started")
        self.driver = setup
        self.log.info("opening browser")
        self.driver.get(self.url)
        self.log.info("Going to url--->"+ self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.rp = RegisterPage(self.driver)
        self.rp.my_account()
        self.log.info("click on myaccount")
        self.rp.register()
        self.log.info("click on register")
        self.rp.enter_firstname("Somesh")
        self.log.info("entering firstname")
        self.rp.enter_lastname("Patil")
        self.log.info("entering lastname")
        self.rp.enter_email("Spatil@xyz.com")
        self.log.info("entering email")
        self.rp.enter_telephone("+91-8888335522")
        self.log.info("entering telephone")
        self.rp.enter_password("Test@1234")
        self.log.info("entering password")
        self.rp.enter_confirm_password("Test@1234")
        self.log.info("entering confirm password")
        self.rp.privacy_policy()
        self.log.info("clicking on privacy policy")
        self.rp.btn_continue()
        self.log.info("clicking on continue button")
        if self.driver.title == "Your Account Has Been Created!":
            self.log.info("page title--->"+ self.driver.title)
            self.driver.save_screenshot("C:\\Users\\admin\\PycharmProjects\\TutorialNinjaProject\\Screenshots"
                                        "\\test_reg_002_pass.png")
            self.log.info("taking sceernshot")
            self.rp.continue_btn()
            self.log.info("clicking on continue button")
            self.rp.my_account()
            self.log.info("clicking on myaccount")
            self.rp.logout()
            self.log.info("clicking on logout")
            self.log.info("test_register_002 is passed")
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\admin\\PycharmProjects\\TutorialNinjaProject\\Screenshots"
                                        "\\test_reg_002_failed.png")
            self.log.info("test_register_002 is passed")
            assert False

        self.log.info("test_register_002 is completed")
