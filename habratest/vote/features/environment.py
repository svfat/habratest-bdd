from splinter.browser import Browser
from habratest import populate

def before_all(context):
    context.browser = Browser()

def after_all(context):
    context.browser.quit()
    context.browser = None
