from selenium import webdriver

def before_feature(context, feature):
    context.driver = webdriver.Chrome()

