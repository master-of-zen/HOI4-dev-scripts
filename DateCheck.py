"""Conversion of dates"""

import fileinput
import datetime
import settings
import parse

start = datetime.datetime(1936, 1, 1)


def get_days(dt):
    return (start - dt).days


def line_is_valid(line, key):
    pass


def valid_line(line):
    pass


def replace_all_date(key):
    for file in parse.file_walk(settings.event_path):
        for line in fileinput.input(file, inplace=True):
            if line_is_valid(line, key):
                print(valid_line(line))

