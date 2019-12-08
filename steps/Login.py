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
def step_valid_login(context):
 assert context.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[1]/div[3]/div')

 @given('user is on saucedemo next')
 def open_website(context):
     context.driver.get('https://www.saucedemo.com/index.html')

 @when('Fill login and password bad')
 def step_set_login_in(context):
     context.driver.find_element_by_id('user-name').send_keys('abc')
     context.driver.find_element_by_id('password').send_keys('abc')
     context.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/form/input[3]').click()

 @then('Login not success')
 def step_valid_login(context):
     assert 'Epic sadface: Username and password do not match any user in this service' in context.driver.page_source

@given('user is on saucedemo next iteral')
def open_website(context):
 context.driver.get('https://www.saucedemo.com/index.html')

@when('Fill password bad')
def step_set_login_in(context):
    context.driver.find_element_by_id('user-name').send_keys('standard_user')
    context.driver.find_element_by_id('password').send_keys('abc')
    context.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/form/input[3]').click()

@then('Login not success with bad password')
def step_valid_login(context):
     assert 'Epic sadface: Username and password do not match any user in this service' in context.driver.page_source



