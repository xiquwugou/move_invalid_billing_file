#!/usr/bin/env python
#encoding: utf-8
import sys
import unittest

__author__ = 'song'

import hashlib


def md5_for_file(f, block_size=2 ** 20):
    md5 = hashlib.md5()
    while True:
        data = f.read(block_size)
        if not data:
            break
        md5.update(data)
    return md5.hexdigest()


def get_file_md5(f):
    try:
        x = f.split("_")
        return x[2].split(".")[0]
    except Exception, e:
        print e


class MyTest(unittest.TestCase):
    ##初始化工作
    def setup(self):
        pass

    #退出清理工作
    def teardown(self):
        pass

    #具体的测试用例，一定要以test开头
    def test_md5_for_file(self):
        f = open("c:\\StatisticData_20131012100501_4b201542799477e41923d43120fd89a2.tgz", 'rb')
        x = md5_for_file(f)
        self.assertEqual(x, "4b201542799477e41923d43120fd89a2", 'test sum fail')

    def test_get_file_md5(self):
        _md5 = get_file_md5("c:\\StatisticData_20131012100501_4b201542799477e41923d43120fd89a2.tgz")
        self.assertEqual(_md5, "4b201542799477e41923d43120fd89a2", 'test sub fail')


if __name__ == '__main__':
    f = open("c:\\StatisticData_20131012100501_4b201542799477e41923d43120fd89a2.tgz", 'rb')
    x = md5_for_file(f)
    print x
    print get_file_md5("c:\\StatisticData_20131012100501_4b201542799477e41923d43120fd89a2.tgz")

