from steps import Login
import time
from selenium.webdriver.support.ui import Select
from behave import given, when, then
@given ('user is login')
def steps_user_is_login(context):
    context.driver.get('https://www.saucedemo.com/index.html')
    context.driver.find_element_by_id('user-name').send_keys('standard_user')
    context.driver.find_element_by_id('password').send_keys('secret_sauce')
    context.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/form/input[3]').click()
@when('Click sort A-Z')
def steps_sort(context):
    Select(context.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[1]/div[3]/select')).select_by_index(0)
@then ('Sort A-Z and success')
def sort_success(context):
    assert context.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/a/div').text in 'Sauce Labs Backpack'
@when('Click sort Z-A')
def steps_sort(context):
    Select(context.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[1]/div[3]/select')).select_by_index(1)
@then ('Sort Z-A and success')
def sort_success(context):
    assert context.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/a/div').text in 'Test.allTheThings() T-Shirt (Red)'

@when('Click sort low to hight')
def steps_sort(context):
    Select(context.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[1]/div[3]/select')).select_by_index(2)
@then ('Sort low to hight and success')
def sort_success(context):
    assert context.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/div').text in '$7.99'

@when('Click sort hight to low')
def steps_sort(context):
    Select(context.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[1]/div[3]/select')).select_by_index(3)
@then ('Sort hight to low and success')
def sort_success(context):
    assert context.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/div').text in '$49.99'