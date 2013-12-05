#!/usr/bin/env python
#encoding: utf-8
import re
import unittest

__author__ = 'song'


def parse_line(line):
    result = line.split("=")
    return result[1]


class FilterBillFile():
    def __init__(self, bill_file_name=None):
        self.bill_file_name = bill_file_name

    def read_patterns(self):
        #print self.bill_file_name
        lines = []
        try:
            with open(r'system.properties') as f:
                content = f.read().splitlines()
                for line in content:
                    if "pattern" in line and "=" in line:
                        line = line.strip('\n')
                        line = line.replace("\\\\", "\\")
                        pattern = parse_line(line)
                        lines.append(pattern)
                return lines
        except Exception, e:
            return lines

    def match_bill_files(self):
        is_bill_file = False

        if not self.match_invalid_bill_file() is None:
            return False
        for pattern in self.read_patterns():
            if not re.match(pattern, self.bill_file_name) is None:
                return True
        return is_bill_file

    def match_invalid_bill_file(self):
        if self.bill_file_name.endswith('tmp'):
            return False
        if self.bill_file_name.endswith("temp"):
            return False


class MyTest(unittest.TestCase):
    ##初始化工作
    def setup(self):
        pass

    #退出清理工作
    def teardown(self):
        pass

    def test_match_invalid_bill_file(self):
        f = FilterBillFile("01002913gd_CHN-XA-1.billing0922102252.000517466.log.tmp").match_bill_files()
        self.assertFalse(f)

    def test_match_bill_files(self):
        f = FilterBillFile("01002913g_CHN-XA-1.billing0922102252.000517466.log")
        result = f.match_bill_files()
        self.assertFalse(result)

        f = FilterBillFile("010021C3dH_CHN-SH-C.billing1012174511.000883891.log")
        result = f.match_bill_files()
        self.assertTrue(result)

        #result = f.match_bill_files(patterns, "01051333FA_304_live_512_20131008154500277.log")
        #self.assertTrue(result)
        #
        #result = f.match_bill_files(patterns, "06054333y_CNC-BZ-3.billing0806150207.000558392.log")
        #self.assertFalse(result)
        #
        #result = f.match_bill_files(patterns, "0123EA_FVSS_STREAM_20130815192101.log.gz")
        #self.assertFalse(result)
        #
        #result = f.match_bill_files(patterns, "01057123A2_localhost.localdomain.billing1008114151.000397727.log")
        #self.assertFalse(result)




    

