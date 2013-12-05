#!/usr/bin/env python
#encoding: utf-8
import os
import re
import shutil
import unittest
from os import listdir
from os.path import isfile, join

import glob


__author__ = 'song'


def parse_line(line):
    result = line.split("=")
    return result[1]


def read_patterns():
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


def match_bill_file(pattern, bill_file):
    print pattern, bill_file
    if re.match(pattern, bill_file):
        return True
    else:
        return False


def match_bill_files(patterns, bill_file):
    is_bill_file = False
    for pattern in patterns:
        is_bill_file = match_bill_file(pattern, bill_file)
        if is_bill_file:
            return is_bill_file
    return is_bill_file


def move_invalid_file(src, dst):
    #print glob.glob("C:\\tt\\*")
    #shutil.move("C:\\tt\\temp", "C:\\bak\\style.css.bak")
    try:
        shutil.move(src, dst)
        return True
    except (OSError, IOError, shutil.Error), e:
        print e
        return False


if __name__ == '__main__':
    bill_files = glob.glob("C:\\logs\\dest\\*")
    patterns = read_patterns()
    for bill_file in bill_files:
        _bill_file = os.path.basename(bill_file)
        is_bill_file = match_bill_files(patterns, _bill_file)
        if not is_bill_file:
            move_invalid_file(bill_file, "C:\\logs\\invalid_file\\" + _bill_file)


class MyTest(unittest.TestCase):
    ##初始化工作
    def setup(self):
        pass

    #退出清理工作
    def teardown(self):
        pass

    #具体的测试用例，一定要以test开头
    def test_read_pattern(self):
        result = read_patterns()
        print result
        self.assertEqual(len(result), 13, 'test sum fail')

    def test_parse_line(self):
        result = parse_line("pattern.p2pstream.old=[0-9|A-Za-z]{10,}_[0-9]*_P2PSTREAM.gz")
        self.assertEqual(result, "[0-9|A-Za-z]{10,}_[0-9]*_P2PSTREAM.gz")

    def test_match_bill_file(self):
        result = match_bill_file("[0-9|A-Za-z]{10,}_[0-9]{12}_idc_[0-9]*.gz", "3100101571_201006021825_idc_9.gz")
        self.assertTrue(result)
        result = match_bill_file("[0-9|A-Za-z]{10,}_[0-9]{12}_idc_[0-9]*.gz", "33100101_201006021825_idc_9.gz")
        self.assertFalse(result)

        result = match_bill_file("\\w{10,}_\\d+_live_\\d+_\\d{17}\\.log", "01051333FA_304_live_512_20131008154500277.log")
        self.assertTrue(result)



    def test_match_bill_files(self):
        patterns = read_patterns()

        #
        #result = match_bill_files(patterns, "3100101571_201006021825_idc_9.gz")
        #self.assertTrue(result)
        #result = match_bill_files(patterns, "0100102396_CHN-BJ-2.billing0922203901.000900755.log")
        #self.assertTrue(result)

        result = match_bill_files(patterns, "01051333FA_304_live_512_20131008154500277.log")
        self.assertTrue(result)

        result = match_bill_files(patterns, "06054333y_CNC-BZ-3.billing0806150207.000558392.log")
        self.assertFalse(result)

        result = match_bill_files(patterns, "0123EA_FVSS_STREAM_20130815192101.log.gz")
        self.assertFalse(result)

        result = match_bill_files(patterns, "01057123A2_localhost.localdomain.billing1008114151.000397727.log")
        self.assertFalse(result)

        result = match_bill_files(patterns, "01002913g_CHN-XA-1.billing0922102252.000517466.log")
        self.assertFalse(result)






        #def test_move_invalid_file(self):
        #    result = move_invalid_file("C:\\bak\\style.css.bak", "C:\\tt\\keybd_open.png-bak")
        #    self.assertTrue(result)


