from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from unittest import TestCase
class Buy(TestCase):
        def setUp(self) -> None:
         self.driver = webdriver.Chrome()
         self.driver.get('https://www.saucedemo.com/index.html')
         input_name = self.driver.find_element_by_id('user-name')
         input_name.send_keys('standard_user')
         input_password = self.driver.find_element_by_id('password')
         input_password.send_keys('secret_sauce')
         button = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/form/input[3]')
         button.click()
         product_add=self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/button')
         product_add.click()
        def tearDown(self) -> None:
         self.driver.close

        def test_add_product(self):
         assert 'REMOVE' == self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/button').text

        def test_delate_basket(self):
         basket= self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/a')
         basket.click()
         remove=self.driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[1]/div[3]/div[2]/div[2]/button')
         remove.click()
         assert 'CONTINUE SHOPPING'==self.driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/a[1]').text

        def test_delate_list_product(self):
         remove=self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/button')
         remove.click()
         assert 'ADD TO CART' == self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/button').text

        def test_delate_details_product(self):
         input_products=self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div/div[1]/div[1]/a/img')
         input_products.click()
         remove=self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div/button')
         remove.click()
         assert 'ADD TO CART' == self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div/button').text

        def test_view_basket_one(self):
         basket = self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/a')
         basket.click()
         assert 'Sauce Labs Backpack'== self.driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[1]/div[3]/div[2]/a/div').text

        def test_view_basket_double(self):
         product_next=self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/button')
         product_next.click()
         basket = self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/a')
         basket.click()
         assert 'Sauce Labs Backpack'== self.driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[1]/div[3]/div[2]/a/div').text
         assert 'Sauce Labs Bike Light'== self.driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[1]/div[4]/div[2]/a/div').text

        def test_buy_continue(self):
         basket = self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/a')
         basket.click()
         continue_shopping=self.driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/a[1]')
         continue_shopping.click()
         assert 'Products' in self.driver.page_source

        def test_information_continue(self):
         basket = self.driver.find_element_by_id('shopping_cart_container')
         basket.click()
         checkout= self.driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/a[2]')
         checkout.click()
         first_name=self.driver.find_element_by_id('first-name')
         last_name=self.driver.find_element_by_id('last-name')
         postal_code=self.driver.find_element_by_id('postal-code')
         first_name.send_keys("Karolina")
         last_name.send_keys("Mrówka")
         cont= self.driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/form/div[2]/input')
         cont.click()
         assert 'Error: Postal Code is required' == self.driver.find_element_by_xpath(
             '/html/body/div/div[2]/div[3]/div/form/h3').text
         postal_code.send_keys("23-100")
         cont.click()
         assert 'Checkout: Overview'==self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]').text
         assert 'Item total: $29.99'==self.driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[5]').text
         cancel= self.driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[8]/a[1]')
         cancel.click()
         assert 'Products' in self.driver.page_source

        def test_buy_finish(self):
         basket = self.driver.find_element_by_id('shopping_cart_container')
         basket.click()
         checkout= self.driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/a[2]')
         checkout.click()
         first_name=self.driver.find_element_by_id('first-name')
         last_name=self.driver.find_element_by_id('last-name')
         postal_code=self.driver.find_element_by_id('postal-code')
         first_name.send_keys("Karolina")
         last_name.send_keys("Mrówka")
         postal_code.send_keys("23-100")
         cont= self.driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/form/div[2]/input')
         cont.click()
         finish=self.driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[8]/a[2]')
         finish.click()
         assert 'THANK YOU FOR YOUR ORDER'==self.driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/h2').text



