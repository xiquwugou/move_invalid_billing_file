#!/usr/bin/env python
#encoding: utf-8

from datetime import date, datetime, time
import re
from util.MyDate import is_counting_day
import unittest

__author__ = 'song'


class FilterByDate():
    def __init__(self, bill_file_name):
        self.__bill_file_name = bill_file_name

    def is_fc_file(self):
        fc_pattern = "[0-9A-Za-z]{10,}_[0-9A-Za-z|\\-]*\\.billing[0-9]*\\.[0-9]*\\.log"
        if not re.match(fc_pattern, self.__bill_file_name) is None:
            return True
        else:
            return False

    def is_idc_file(self):
        idc_pattern = "[0-9|A-Za-z]{10,}_[0-9]{12}_idc_[0-9]*.gz"
        if not re.match(idc_pattern, self.__bill_file_name) is None:
            return True
        else:
            return False

    def get_file_date(self):
        str_date = self.__bill_file_name.split("billing")[1].split(".")[0]
        current_date = date.today()
        str_date = str(current_date.year) + str_date
        return datetime.strptime(str_date, '%Y%m%d%H%M%S')

    #只检查fc文件
    def is_in_counting_day(self):
        if not self.is_fc_file():
            return True
        else:
            _create_file_date = self.get_file_date()
            return is_counting_day(_create_file_date)


class MyTest(unittest.TestCase):
    ##初始化工作
    def setup(self):
        pass

    #退出清理工作
    def teardown(self):
        pass

    def test_get_file_date(self):
        f = FilterByDate("1000107358_CCN-BJ-7.billing0602144601.219726832.log")
        expect = datetime(2013, 06, 02, 14, 46, 01)
        self.assertEqual(expect, f.get_file_date())

    def test_is_in_counting_day(self):
        f = FilterByDate("1000107358_CCN-BJ-7.billing0602144601.219726832.log")
        result = f.is_in_counting_day()
        self.assertTrue(result)

    def test_is_in_counting_file(self):
        d = date(2013, 10, 1)
        dt = datetime.combine(d, time())
        result = is_counting_day(dt)
        self.assertTrue(result)

        d = date(2013, 9, 1)
        dt = datetime.combine(d, time())
        result = is_counting_day(dt)
        self.assertFalse(result)

        d = date(2013, 9, 30)
        dt = datetime.combine(d, time())
        result = is_counting_day(dt)
        self.assertFalse(result)





