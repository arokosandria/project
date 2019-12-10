from steps import Login
import time
from selenium.webdriver.support.ui import Select
from behave import given, when, then
@when('Click add to cart')
def steps_add_product(context):
    context.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/button').click()
    time.sleep(2)
@then('User see product in basket')
def steps_product_in_basket(context):
    assert context.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/button').text in 'REMOVE'
@when('Click delete product in basket')
def steps_delete_product_in_basket(context):
    context.driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[1]/div[3]/div[2]/div[2]/button').click()
@then('Product is delete')
def steps_product_delete(context):
    assert context.driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/a[1]').text in 'CONTINUE SHOPPING'