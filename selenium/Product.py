from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from unittest import TestCase
class Product(TestCase):
        def setUp(self) -> None:
         self.driver = webdriver.Chrome()
         self.driver.get('https://www.saucedemo.com/index.html')
         input_name = self.driver.find_element_by_id('user-name')
         input_name.send_keys('standard_user')
         input_password = self.driver.find_element_by_id('password')
         input_password.send_keys('secret_sauce')
         button = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/form/input[3]')
         button.click()
         input_products=self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div/div[1]/div[1]/a/img')
         input_products.click()
        def tearDown(self) -> None:
         self.driver.close()

        def test_picture(self):
         picture=self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/img')
         bool=picture.is_displayed()
         self.assertTrue(bool)

        def test_title(self):
         assert 'Sauce Labs Backpack' == self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div/div[1]').text

        def test_details(self):
         assert 'carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.' == self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div/div[2]').text
        def test_price(self):
         assert '$29.99' == self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div/div[3]').text

if __name__ == '__main__':
 unittest.main()
