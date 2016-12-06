#TODO: 以后应该还会有改动
from base.baseConfig import *
from etc import stage

confLoader = BaseConfig(stage.siteConf)
confLoader.load()