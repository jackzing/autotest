#load common module
import init
from app.util.path import get_current_path

from selenium import webdriver
import logging
logging.basicConfig(level=logging.INFO)

def before_all(context):
     print("Executing before all")
     print(get_current_path())

def before_feature(context, feature):
     print("Before feature\n")

#Scenario level objects are popped off context when scenario exits
def before_scenario(context,scenario):
     path = "/Users/jgao/jjshoue/autotest/bin/chromedriver"
     context.browser = webdriver.Chrome(path)
     print("Before scenario\n")

def after_scenario(context,scenario):
     context.browser.quit()
     print("After scenario\n")

def after_feature(context,feature):
     print("\nAfter feature")

def after_all(context):
     print("Executing after all")

