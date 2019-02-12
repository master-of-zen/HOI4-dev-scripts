import os


def file_walk(path):
    for root, dirs, files in os.walk(path):
        for name in files:
            yield open(os.path.join(root, name), 'r')


def have_key(fl, key):
    for ln in fl:
        if key in ln:
            yield ln.strip()