from configparser import ConfigParser

def readConfigdata(section,key):
    config_obj = ConfigParser()
    config_obj.read("Configuration/config.cfg")
    value = config_obj.get(section,key)
    return value

