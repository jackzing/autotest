from behave import *
import logging
logging.basicConfig(level=logging.INFO)

use_step_matcher("re")

@given("I have two integers a and b")
def step_impl(context):
    context.browser.get("http://www.baidu.com")  
    print(context.browser.title)
    logging.info(context.browser.title)
    context.a = 1
    context.b = 2


@when("I add the numbers")
def step_impl(context):
    context.sum = int(context.a) + int(context.b)


@then("I print the addition result")
def step_impl(context):
    print("Sum of", context.a, "and", context.b, "is:",context.sum)
