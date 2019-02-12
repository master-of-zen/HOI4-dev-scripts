import os
import datetime


start = datetime.datetime(1936, 1, 1)


def get_days(dt):
    return (start - dt).days


def file_walk(path):
    for root, dirs, files in os.walk(path):
        for name in files:
            yield open(os.path.join(root, name), 'r')


