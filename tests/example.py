import os, sys

basePath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app'))
sys.path.append(basePath)
from base.Initializer import *

print(BaseConfig.siteConf)

baseConfig = BaseConfig();
baseConfig.loadExtraConf('setting.domain.jsuk');

print(BaseConfig.siteConf)


"""
output:
{'domain': 'jjshouse', 'position': 'js', 'basePath': '/var/www/http/jjswork/autotest/app', 'url': 'www.jjshouse.com'}
{'domain': 'jjshouse', 'position': 'jsuk', 'url': 'www.jjshouse.co.uk', 'basePath': '/var/www/http/jjswork/autotest/app'}

"""