#!/usr/bin/env python
#encoding: utf-8
import unittest

__author__ = 'song'

from datetime import date, datetime, time
from time import strftime


def first_day_of_month(d):
    return date(d.year, d.month, 1)


def get_bill_date(d):
    return date(d.year, d.month, 2)


def first_day_of_last_month(d):
    return date(d.year, d.month - 1, 1)


def get_str_date(_date):
    return strftime("%Y-%m-%d %H:%M:%S", _date)


def get_counting_day():
    current_date = date.today()
    account_date = get_bill_date(current_date)
    if current_date >= account_date:
        return first_day_of_month(current_date)
    else:
        return first_day_of_last_month(current_date)


def is_counting_day(bill_day):
    count_day = get_counting_day()

    count_day = datetime.combine(count_day, time(0, 0))

    if bill_day >= count_day:
        return True
    else:
        return False


class MyTest(unittest.TestCase):
    ##初始化工作
    def setup(self):
        pass

    #退出清理工作
    def teardown(self):
        pass

    def test_is_counting_day(self):
        d = date(2013, 9, 3)
        dt = datetime.combine(d, time())
        print time(0, 0)
        print dt
        x = is_counting_day(dt)
        print x
        self.assertTrue(x)

    #如果当前日期在2号0:00 以前，账单日设为上月1号，如果当前日期在2号：00 以后，取当月1号为账单日
    def test_sum(self):
        _date = get_counting_day()
        _test = date(2013, 8, 1)
        self.assertEqual(_date, _test, 'test sum fail')
        #def test_sub(self):
        #    self.assertEqual(2, 1, 'test sub fail')



