from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from unittest import TestCase
class Products(TestCase):
        def setUp(self) -> None:
         self.driver = webdriver.Chrome()
         self.driver.get('https://www.saucedemo.com/index.html')
         input_name = self.driver.find_element_by_id('user-name')
         input_name.send_keys('standard_user')
         input_password = self.driver.find_element_by_id('password')
         input_password.send_keys('secret_sauce')
         button = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/form/input[3]')
         button.click()
        def tearDown(self) -> None:
         self.driver.close()

        def test_ascending_albetically(self):
         input_menu=Select(self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[1]/div[3]/select'))
         input_menu.select_by_index(0)
         assert 'Sauce Labs Backpack'==self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/a/div').text

        def test_desc_albetically(self):
         input_menu = Select(self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[1]/div[3]/select'))
         input_menu.select_by_index(1)
         assert 'Test.allTheThings() T-Shirt (Red)' == self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/a/div').text

        def test_ascending_price(self):
         input_menu = Select(self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[1]/div[3]/select'))
         input_menu.select_by_index(2)
         assert '$7.99' == self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/div').text

        def test_desc_price(self):
         input_menu = Select(self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[1]/div[3]/select'))
         input_menu.select_by_index(3)
         assert '$49.99' == self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/div').text

if __name__ == '__main__':
 unittest.main()


