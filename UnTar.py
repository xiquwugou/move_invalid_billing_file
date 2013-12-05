import glob
import os
from BackupFile import BackupFile
from MyMd5 import md5_for_file, get_file_md5

__author__ = 'song'


def is_normal_file(tgz=None):
    #global _for_file, tgz, _get_file_md5
    _for_file = md5_for_file(open(tgz, 'rb'))
    tgz = os.path.basename(tgz)
    _get_file_md5 = get_file_md5(tgz)
    if _for_file == _get_file_md5:
        return True
    else:
        return False


if __name__ == '__main__':
    tgz_s = glob.glob("C:\\StatisticData*.tgz")
    for tgz in tgz_s:
        if is_normal_file(tgz):
            backup = BackupFile(tgz)
            backup.extract("c:\\tt\\logs_invalid", "c:\\tt\\logs")


