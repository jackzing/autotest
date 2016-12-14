from ..base.utils import Util
import os
class Driver:
    @staticmethod
    def get_driver_path(driver_dir, driver_name):
        osname = Util.getOS()
        if osname in ["windows"] :
            driver_name = driver_name + ".exe"
        return os.path.realpath(os.path.join(driver_dir, driver_name))