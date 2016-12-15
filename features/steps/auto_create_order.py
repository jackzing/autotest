from behave import *
from app.base.utils import Util

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

use_step_matcher("re")

@given(u'`(?P<page_code>[^`]+)` page url')
def step_open_home_page(context, page_code):
    #context.browser.get("http://www.baidu.com")
    home_url = context.site_conf.conf("pages." + page_code)
    context.browser.get(home_url)


@when(u'Click Home Page class is `(?P<banner_class>[^`]+)` banner randomly')
def step_open_list_page(context, banner_class):
    banners = context.browser.find_elements_by_css_selector(banner_class)
    web_el = banners[Util.random(len(banners))]
    actions = webdriver.ActionChains(context.browser)
    actions.move_to_element(web_el)
    actions.click(web_el)
    actions.perform()

@when(u'Click product `(?P<product_class>[^`]+)` div information randomly')
def step_open_product_page(context, product_class):
    current_windows = context.browser.window_handles
    products = context.browser.find_elements_by_css_selector(product_class)
    web_el = products[Util.random(len(products))]
    actions = webdriver.ActionChains(context.browser)
    actions.move_to_element(web_el)
    actions.click(web_el)
    #actions.key_down(Keys.CONTROL).key_down(Keys.TAB).key_up(Keys.TAB).key_up(Keys.CONTROL)
    actions.perform()

    #switch new window, don't forgot
    new_windows = context.browser.window_handles
    new_window = list(set(new_windows) - set(current_windows))[0]
    context.browser.switch_to_window(new_window)

@then(u'Select class `(?P<color_class>[^`]+)` color')
def step_select_product_color(context, color_class):
    print(context.browser.current_url)
    #20231
    #918
    context.ele_exists(context.browser, By.CSS_SELECTOR, color_class)
    prod_colors = context.browser.find_elements_by_css_selector(color_class)
    web_el = prod_colors[Util.random(len(prod_colors))]
    actions = webdriver.ActionChains(context.browser)
    actions.move_to_element(web_el)
    actions.click(web_el)
    actions.perform()

@then(u'Select all `(?P<select_class>[^`]+)` visible select randomly')
def step_select_product_color(context, select_class):
    select_list = context.browser.find_elements_by_css_selector(select_class)
    for sl in select_list:
        if sl.is_displayed():
            select_box = Select(sl)
            index = Util.random(len(select_box.options))
            select_box.select_by_index(index)


@then(u'Click class `(?P<add_to_cart_btncls>[^`]+)` button to add item')
def step_select_product_color(context, add_to_cart_btncls):
    add_cart_btn = context.browser.find_element_by_css_selector(add_to_cart_btncls)
    actions = webdriver.ActionChains(context.browser)
    actions.move_to_element(add_cart_btn)
    actions.click(add_cart_btn)
    actions.perform()


@then(u'Click class `(?P<continue_btn_cls>[^`]+)` button to continue to checkout')
def step_select_product_color(context, continue_btn_cls):
    context.ele_exists(context.browser, By.CSS_SELECTOR, continue_btn_cls)
    continue_btn = context.browser.find_element_by_css_selector(continue_btn_cls)
    actions = webdriver.ActionChains(context.browser)
    actions.move_to_element(continue_btn)
    actions.click(continue_btn)
    actions.perform()


#
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
