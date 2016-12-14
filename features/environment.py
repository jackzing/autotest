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
     context.browser = webdriver.Chrome(chrome_path)

def after_scenario(context,scenario):
     context.browser.quit()
     print("After scenario\n")

def after_feature(context,feature):
     print("\nAfter feature")

def after_all(context):
     print("Executing after all")

