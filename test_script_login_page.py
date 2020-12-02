import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class LoginPage(unittest.TestCase):
    
    def setUp(self):
         # create a new Safari session
        self.driver = webdriver.Safari()
        # navigate to the application home page
        self.driver.get("https://clientmanagement.xtracta.com/clientarea.php")

    def test_login_in_xtracta(self):
        """TC_002_01 :-Verify if a user will be able to login with a valid username and valid password."""
         # get the login textbox
        username = self.driver.find_element_by_id("username") #username for login
        username.send_keys("charu.matta@yahoo.com") 
        time.sleep(2)
        # get the password textbox
        password = self.driver.find_element_by_id("password") #password for login
        password.send_keys("Testing@123")
        time.sleep(2)
        NEXT_BUTTON_XPATH = '//input[@type="submit" and @value="Login"]' #xpath for submit button
        button = self.driver.find_element_by_xpath(NEXT_BUTTON_XPATH)
        button.click()
        time.sleep(2)
        #validating if you have logined successfully
        text = self.driver.find_elements_by_xpath("//ul[@class='nav pull-right']//a[@class='dropdown-toggle']//text()")
        self.assertTrue(text,("Hello, Charu! ")) 




    def test_with_invalid_password(self):
        """TC_003_01 :-Verify if a user cannot login with a valid username and an invalid password."""
        username = self.driver.find_element_by_id("username")
        username.send_keys("charu.matta@yahoo.com")
        time.sleep(2)
        password = self.driver.find_element_by_id("password")
        #invalid password
        password.send_keys("hello@12")
        NEXT_BUTTON_XPATH = '//input[@type="submit" and @value="Login"]'
        button = self.driver.find_element_by_xpath(NEXT_BUTTON_XPATH)
        time.sleep(3)
        button.click()
        time.sleep(5)
        #validating error message after entering wrong password
        err_msg  = self.driver.find_element_by_xpath("//div[@class='alert alert-error textcenter']//text()")
        self.assertTrue(err_msg,("Login Details Incorrect. Please try again."))

    def test_to_reset_password(self):
        """TC_004_01 :-Verify the ‘Forgot Password’ functionality."""
        #to get link for reset password
        password = self.driver.find_element_by_xpath("//p//a[contains(text(),'Request a Password Reset')]")
        time.sleep(2)
        password.click()
        time.sleep(2)
        emaidId = self.driver.find_element_by_id("email")
        emaidId.send_keys("charu.matta@yahoo.com")
        NEXT_BUTTON_XPATH = '//input[@type="submit" and @value="Submit"]'
        button = self.driver.find_element_by_xpath(NEXT_BUTTON_XPATH)
        button.click()
        time.sleep(20)
        #validating link sent messge
        validation_msg  = self.driver.find_element_by_xpath("//div[@class='alert alert-success']//text()")
        self.assertTrue(validation_msg,("Validation Email Sent"))

    def tearDown(self):
        #closing the Safari session
        self.driver.close()

if __name__ == "__main__":
    unittest.main()