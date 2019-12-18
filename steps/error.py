import time
from behave import given, when, then

@when('Fill login and password problem_user')
def step_set_login_in(context):
    context.driver.find_element_by_id('user-name').send_keys('problem_user')
    context.driver.find_element_by_id('password').send_keys('secret_sauce')
    context.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/form/input[3]').click()
@then('Check picture')
def step_check_picture(context):
