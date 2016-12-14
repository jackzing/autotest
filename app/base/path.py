import os
class Path:
    @staticmethod
    def getRoot():
        curdir = os.path.dirname(__file__)
        rootdir = os.path.realpath(os.path.join(curdir, "..", ".."))
        return rootdir