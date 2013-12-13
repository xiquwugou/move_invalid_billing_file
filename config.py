__author__ = 'song'

import ConfigParser

cf = ConfigParser.ConfigParser()
cf.read("conf/my.conf")

tgz_path = cf.get("path", "tgz_path")
invalid_file_path = cf.get("path", "invalid_file_path")
normal_file_path = cf.get("path", "normal_file_path")
idc_file_path = cf.get("path", "idc_file_path")
up_file_path = cf.get("path", "up_file_path")
up_device_path = cf.get("path", "up_device_path")
