import time
from behave import given, when, then
url='https://www.saucedemo.com/index.html'
@given ('user is on saucedemo')
def open_website(context):
 context.driver.get(url)

@when('Fill login and password')
def step_set_login_in(context):
    context.driver.find_element_by_id('user-name').send_keys('standard_user')
    context.driver.find_element_by_id('password').send_keys('secret_sauce')
    context.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/form/input[3]').click()

@then('Login success')
def step_login(context):
 assert context.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[1]/div[3]/div')

 @given('user bad is on saucedemo')
 def open_website(context):
     context.driver.get('https://www.saucedemo.com/index.html')

 @when('Fill "{login}" and "{password}"')
 def step_set_login_in(context, login,password):
     context.driver.find_element_by_id('user-name').send_keys(login)
     context.driver.find_element_by_id('password').send_keys(password)
     context.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/form/input[3]').click()

 @then('View {messeage}')
 def step_valid_login(context, messeage):
     assert context.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/form/h3').text in messeage

 @then('Login success and logout')
 def step_valid_login(context):
     context.driver.find_element_by_xpath('/html/body/div/div[1]/div/div[3]/div/button').click()
     time.sleep(2)
     context.driver.find_element_by_xpath('//*[@id="logout_sidebar_link"]').click()
     assert context.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/form/input[3]')





