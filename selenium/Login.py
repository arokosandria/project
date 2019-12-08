import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from unittest import TestCase
from selenium import webdriver

class Login(TestCase):
        def setUp(self) -> None:
         self.driver = webdriver.Chrome()
         self.driver.get('https://www.saucedemo.com/index.html')
        def tearDown(self) -> None:
         self.driver.close()

        def test_login_correct(self):


         input_name = self.driver.find_element_by_id('user-name')
         input_name.send_keys('standard_user')
         input_password = self.driver.find_element_by_id('password')
         input_password.send_keys('secret_sauce')
         button = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/form/input[3]')
         button.click()
         assert 'Products' in self.driver.page_source

        def test_login_unregister(self):

         input_name = self.driver.find_element_by_id('user-name')
         input_name.send_keys('abc')
         input_password = self.driver.find_element_by_id('password')
         input_password.send_keys('abc')
         button = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/form/input[3]')
         button.click()
         assert 'Epic sadface: Username and password do not match any user in this service' in self.driver.page_source

        def test_login_badpassword(self):


             input_name = self.driver.find_element_by_id('user-name')
             input_name.send_keys('abc')
             input_password = self.driver.find_element_by_id('password')
             input_password.send_keys('abc')
             button = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/form/input[3]')
             button.click()
             assert 'Epic sadface: Username and password do not match any user in this service' in self.driver.page_source

        def test_login_bloked(self):


             input_name = self.driver.find_element_by_id('user-name')
             input_name.send_keys('locked_out_user')
             input_password = self.driver.find_element_by_id('password')
             input_password.send_keys('secret_sauce')
             button = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/form/input[3]')
             button.click()
             assert 'Epic sadface: Sorry, this user has been locked out.' in self.driver.page_source

        def test_login_logout(self):
            input_name = self.driver.find_element_by_id('user-name')
            input_name.send_keys('standard_user')
            input_password = self.driver.find_element_by_id('password')
            input_password.send_keys('secret_sauce')
            button = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/form/input[3]')
            button.click()
            WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div/div[3]/div/button'))).click()
            time.sleep(2)
            logout=self.driver.find_element_by_xpath('//*[@id="logout_sidebar_link"]')
            logout.click()
            assert 'secret_sauce' in self.driver.page_source

if __name__ == '__main__':
 unittest.main()