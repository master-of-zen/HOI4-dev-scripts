"""Conversion of dates"""
import fileinput
import datetime
import os
from settings import bice_path
_forbidden = ("{", "}", "/", '"', "has")

start = datetime.date(1936, 1, 1)
date_key = ("date <", "date >")


def get_days(dt):
    return (dt - start).days


def line_is_valid(line, key):
    line = line[:line.find("#")]
    if any(s in line for s in key):
        if not any(s in line for s in _forbidden):
            return True
    return False


def cut_date(line):
    ln = line[line.find("1"):line.find("#")].strip()
    return datetime.datetime.strptime(ln, "%Y.%m.%d").date()


def change_time(line):

    ln_dt = cut_date(line)
    days = get_days(ln_dt)
    return "\t\t\tcheck_variable = { global.days_passed > %d }" % days + " # " + str(ln_dt)


def file_walk(path):
    for root, dirs, files in os.walk(path):
        for name in files:
            yield os.path.join(root, name)


def do_all_shit(path):
    path = os.path.join(path, 'events')
    for file in file_walk(path):
        for line in fileinput.input(file, inplace=True, backup=None):
            if line_is_valid(line, date_key):
                print(change_time(line))
            else:
                print(line, end='')


if __name__ == '__main__':
    do_all_shit(bice_path)
