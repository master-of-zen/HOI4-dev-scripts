"""Conversion of dates"""
import fileinput
import datetime
from settings import forbidden, event_path, date_key
import os

start = datetime.date(1936, 1, 1)


def get_days(dt):
    return (dt - start).days


def line_is_valid(line, key):
    line = line[:line.find("#")]
    if any(s in line for s in key):
        if not any(s in line for s in forbidden):
            return True
    return False


def cut_date(line):
    ln = line[line.find("1"):line.find("#")].strip()
    return datetime.datetime.strptime(ln, "%Y.%m.%d").date()


def valid_line(line):

    ln_dt = cut_date(line)
    days = get_days(ln_dt)
    return "\t\t\tcheck_variable = { global.days_passed > %d }" % days + " # " + str(ln_dt)


def file_walk(path):
    for root, dirs, files in os.walk(path):
        for name in files:
            yield os.path.join(root, name)


def do_all_shit():
    for file in file_walk(event_path):
        for line in fileinput.input(file, inplace=True, backup = None):
            if line_is_valid(line, date_key):
                print(valid_line(line))
            else:
                print(line, end='')


do_all_shit()