class Util:
    @staticmethod
    def conf(list, key, default_value):
        keys = key.split(".")
        conf = default_value
        length = len(keys)

        conf = list
        index = 0
        for k in keys:
            index = index + 1
            if isinstance(conf, dict) and k in conf.keys() :
                conf = conf.get(k)
            else:
                if index <= length:
                    conf = default_value
                    break
        return conf