"""Conversion of dates"""

import fileinput
import datetime
import settings
import parse


class TimeObj:

    start = datetime.datetime(1936, 1, 1)


def get_days(dt):
    return (TimeObj.start - dt).days


def line_is_valid(line, key):
    if any(s in line for s in key):
        return True
    return False


def cut_key(line):
    return line[line.find("1"):line.find("#")].strip()


def valid_line(line):
    pass


def replace_all_date():
    for file in parse.file_walk(settings.event_path):
        for line in fileinput.input(file, inplace=True):
            if line_is_valid(line, settings.date_key):
                print(valid_line(line))

