import profile
import unittest
from FilterBillFile import FilterBillFile
from util.FilterByDate import FilterByDate

__author__ = 'song'

import tarfile
import os.path


def get_bill_name(name):
    try:
        return name.split("/")[-1]
    except Exception, e:
        print e
        pass


class BackupFile(object):
    def __init__(self, fileName):
        self.__filename = fileName

    # add upload dir in prefix, so easy!
    def add_files(self, file_list):
        backup_file = tarfile.open(self.__filename, 'w:gz')
        try:
            for fl in file_list:
                try:
                    tarinfo = backup_file.gettarinfo(fl, "upload/" + os.path.basename(fl))
                    backup_file.addfile(tarinfo, open(fl, 'rb'))
                except Exception, e:
                    print e
                    continue
        finally:
            backup_file.close()

    def extract(self, invalid_dir, log_dir, idc_dir, up_dir):
        backup_file = tarfile.open(self.__filename, 'r')
        try:
            try:
                for info in backup_file.getmembers():

                    info.name = os.path.basename(info.name)
                    bill_file_name = get_bill_name(info.name)
                    if bill_file_name is None:
                        continue
                    is_bill_file = FilterBillFile(bill_file_name).match_bill_files()
                    is_up_file = FilterBillFile(bill_file_name).is_up_file()
                    is_idc_file = FilterBillFile(bill_file_name).is_idc_file()
                    #is_fc_file_in_count_day = FilterByDate(bill_file_name).is_in_counting_day()
                    if is_bill_file:
                        if is_idc_file:
                            backup_file.extract(info, idc_dir)
                        elif is_up_file:
                            backup_file.extract(info, up_dir)
                        else:
                            #backup_file.extract(info, log_dir)
                            pass
                    else:
                        if "upload" in info.name:
                            continue
                        backup_file.extract(info, invalid_dir)
            except Exception, e:
                print e
        finally:
            backup_file.close()


class IsOddTests(unittest.TestCase):
    def testOne(self):
        backup = BackupFile("song.test.tar")
        backup.add_files(file_list=["C:\\baidu player\\style.css", "C:\\Sites\\a.txt"])
        self.assertEqual(1, 1)

    def test_extract(self):
        #backup = BackupFile("c:\\StatisticData_20131012100501_4b201542799477e41923d43120fd89a2.tgz")
        backup = BackupFile("e:\\logs\\StatisticData_20131012175931_cf8e28bdc676972790878fc621595e72.tgz")
        backup.extract("c:\\tt\\logs_invalid", "c:\\tt\\logs")
        self.assertEqual(1, 2)




