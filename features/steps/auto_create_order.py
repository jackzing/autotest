from behave import *
from app.base.utils import Util

from selenium import webdriver

use_step_matcher("re")

@given(u'`(?P<page_code>[^`]+)` page url')
def step_open_home_page(context, page_code):
    #context.browser.get("http://www.baidu.com")
    home_url = context.site_conf.conf("pages." + page_code)
    context.browser.get(home_url)


@when(u'Click Home Page class is `(?P<banner_class>[^`]+)` banner randomly')
def step_open_home_page(context, banner_class):
    banners = context.browser.find_elements_by_css_selector(banner_class)
    web_el = banners[Util.random(len(banners))]
    actions = webdriver.ActionChains(context.browser)
    actions.move_to_element(web_el)
    actions.click(web_el)
    actions.perform()
#
#
# @when("I add the numbers")
# def step_impl(context):
#     context.sum = int(context.a) + int(context.b)
#
#
# @then("I print the addition result")
# def step_impl(context):
#     print("Sum of", context.a, "and", context.b, "is:",context.sum)
