import os
from configparser import SafeConfigParser
#don't forget dot. for python3
from .utils import Util

class Config:
    __site_conf = {}

    def initBase(self):
        curdir = os.path.dirname(__file__)
        setting_dir = os.path.realpath(os.path.join(curdir, ".."))
        setting_file = os.path.realpath(os.path.join(curdir, "..", "setting.ini"))
        self.read_ini_file(setting_file)
        stage = Util.conf(self.__site_conf, "env.stage", "")
        domain = Util.conf(self.__site_conf, "env.domain", "")
        if stage == False:
            print("file not exists")
        else:
            file_list = ["common.ini","setting." + domain + ".ini", "setting." + stage + ".ini"]
            for file in file_list:
                real_path = os.path.realpath(os.path.join(curdir, "..", "setting", file))
                if os.path.exists(real_path):
                    self.read_ini_file(real_path)
        #print(self.__site_conf)

    def read_ini_file(self, file):
        parser = SafeConfigParser()
        parser.read(file)

        for section_name in parser.sections():
            if section_name not in self.__site_conf.keys() :
                self.__site_conf[section_name] = {}

            for name, value in parser.items(section_name):
                #print '  %s = %s' % (name, value)
                self.__site_conf[section_name][name] = value
            print

    def conf(self, key, defval=None):
        return Util.conf(self.__site_conf, key, defval)