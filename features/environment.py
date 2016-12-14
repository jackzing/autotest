#load common module
import init
import os
import logging
from app.base.config import Config
from app.base.path import Path
from app.util.driver import Driver

from selenium import webdriver


def before_all(context):
     print("Executing before all")
     #load all config
     conf = Config()
     conf.initBase()
     context.site_conf = conf
     logging_level = conf.conf("logger.level", logging.INFO)
     logging.basicConfig(level=logging_level)

def before_feature(context, feature):
     print("Before feature\n")

#Scenario level objects are popped off context when scenario exits
def before_scenario(context,scenario):
     #print("Before scenario\n")
     app_root = Path.getRoot()
     chrome_driver = context.site_conf.conf("browser.chrome_driver")
     chrome_path = Driver.get_driver_path(app_root, chrome_driver)

     PROXY = "socks5://192.168.1.41:9003"  # IP:PORT or HOST:PORT
     chrome_options = webdriver.ChromeOptions()
     chrome_options.add_argument('--proxy-server=%s' % PROXY)
     context.browser = webdriver.Chrome(chrome_path, chrome_options=chrome_options)
     #set time out
     #context.browser.set_page_load_timeout(5)

def after_scenario(context,scenario):
     #context.browser.quit()
     print("After scenario\n")

def after_feature(context,feature):
     print("\nAfter feature")

def after_all(context):
     print("Executing after all")

