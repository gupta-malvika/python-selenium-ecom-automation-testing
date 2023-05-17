import time
from tests.confest import web_browser_setup
from pageObjects.login_page import LoginPage
from selenium.webdriver.common.keys import Keys
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class TestLogin01:
    baseURL = ReadConfig.get_application_url()
    username = ReadConfig.get_user_email()
    password = ReadConfig.get_password()

    logger = LogGen.loggen()

    def test_home_page_title(self, web_browser_setup):

        self.logger.info("****************TestLogin01***********")
        self.logger.info("")
        self.driver = web_browser_setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            time.sleep(5)
            self.driver.close()
            assert True
        else:
            file_name1 = ".\\screenshot\\" + "test_home_page_title.jpg"
            self.driver.save_screenshot(file_name1)
            self.driver.close()
            assert False

    def test_login(self, web_browser_setup):
        self.driver = web_browser_setup
        self.driver.get(self.baseURL)
        #     call action methods from page object class.
        # need to create an object of Login page class and through that object we access the action method
        self.lp = LoginPage(webdriver=self.driver)
        time.sleep(2)
        self.lp.set_user_name(self.username)
        time.sleep(2)
        self.lp.set_password(self.password)
        self.lp.click_login()
        act_title = self.driver.title
        # print(f"*****{act_title}")
        if act_title == "Dashboard / nopCommerce administration":
            time.sleep(5)
            self.driver.close()
            assert True
        else:
            file_name = ".\\screenshot\\" + "test_login.png"
            self.driver.save_screenshot(file_name)
            self.driver.close()
            assert False
