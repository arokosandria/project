from steps import Login
import time
from selenium.webdriver.support.ui import Select
from behave import given, when, then
@when('Click add to cart')
def steps_add_product(context):

    context.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/button').click()

@then('User see product in basket')
def steps_product_in_basket(context):

    assert context.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/button').text in 'REMOVE'
@when('Go to the basket')
def steps_go_to_the_basket(context):

    context.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/a').click()
@when('Click delete product in basket')
def steps_delete_product_in_basket(context):

    context.driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[1]/div[3]/div[2]/div[2]/button').click()
@then('Product is delete')
def steps_product_delete(context):
   assert 'Sauce Labs Backpack' not in context.driver.page_source
@when('Click remove in product list')
def steps_click_remove(context):
    context.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/button').click()
@then('Product is delete in product list')
def step_product_delete(context):
    assert context.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/button').text in 'ADD TO CART'

@when('Click in product')
def steps_click_product(context):
    context.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div/div[1]/div[1]/a/img').click()
@when('Click remove in product details')
def step_click_remove(context):
    context.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div/button').click()
@then('Product is delete in product details')
def step_delete_product(context):
    assert context.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div/button').text in 'ADD TO CART'
@then('View product in basket')
def step_view_product(context):
    assert context.driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[1]/div[3]/div[2]/a/div').text in 'Sauce Labs Backpack'
@when('Click add to cart next product')
def step_click_product(context):
    time.sleep(2)
    context.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/button').click()
@then('View products in basket')
def step_view_product(context):
    time.sleep(9)
    assert context.driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[1]/div[3]/div[2]/a/div').text in 'Sauce Labs Backpack'
    assert context.driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[1]/div[4]/div[2]/a/div').text in 'Sauce Labs Bike Light'

@when('Click continue')
def step_continue_shop(context):
    time.sleep(2)
    context.driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/a[1]').click()
@when('Go to checkout')
def step_checkout(context):
    context.driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/a[2]').click()
@when('Continue')
def step_continue_shop(context):
    time.sleep(2)
    context.driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/form/div[2]/input').click()
@when('Fill First Name and Last_Name')
def step_fill_name(context):
    context.driver.find_element_by_id('first-name').send_keys('Karolina')
    context.driver.find_element_by_id('last-name').send_keys('Mrowka')
@then('View error information')
def step_view_error(context):
    assert context.driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/form/h3/button').text in 'Error: Postal Code is require'
@when('Fill Zip')
def step_fill_zip(context):
    context.driver.find_element_by_id('postal-code').send_keys('27-600')
@then('Checkout')
def steps_checkout(context):
    assert context.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]').text in 'Checkout: Overview'
@when('Click cancel')
def steps_cancel(context):
    context.driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[8]/a[1]').click()
@then('Price Order')
def steps_price_order(context):
    assert context.driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[7]').text in 'Total: $43.18'
@when('Click finish')
def steps_click_finish(context):
    context.driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[8]/a[2]').click()
@then('Finish')
def steps_finish(context):
    assert context.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]').text in 'Finish'

