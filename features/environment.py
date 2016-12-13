#load common module
import init
from app.base.config import Config

from selenium import webdriver
import logging


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
     path = "/Users/jgao/jjshoue/autotest/bin/chromedriver"
     context.browser = webdriver.Chrome(path)

def after_scenario(context,scenario):
     context.browser.quit()
     print("After scenario\n")

def after_feature(context,feature):
     print("\nAfter feature")

def after_all(context):
     print("Executing after all")

