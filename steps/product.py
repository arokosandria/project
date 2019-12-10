from steps import products
import time
from selenium.webdriver.support.ui import Select
from behave import given, when, then

@when('click product')
def steps_user_is_login_and_add_product(context):
 context.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div/div[1]/div[1]/a/img').click()
@then('User see pricture product')
def steps_product_is_pictures(context):
    assert context.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/img').is_displayed()
@then('User see title product')
def steps_product_is_title(context):
   assert context.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div/div[1]').text in 'Sauce Labs Backpack'
@then('User see description product')
def steps_product_is_description(context):
    assert context.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div/div[2]').text in 'carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.'
@then('User see price product')
def steps_product_is_price(context):
    assert context.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div/div[3]').text in '$29.99'
