"""
BICE for HOI4 mods
"""
import os
from settings import strings, forbidden, bice_path

_events_print = "All Events with missing localisation :" + "\n" * 5
_ideas_print = "\n" * 5 + "All ideas with missing localisation :" + "\n" * 5


def _file_walk(path):
    for root, dirs, files in os.walk(path):
        for name in files:
            yield open(os.path.join(root, name), 'r+')


def _have_key(fl, key):
    for ln in fl:
        if key in ln:
            yield ln.strip()


def _get_key_line(file, key, start_f, end_f):
    lines = []
    for line in _have_key(file, key):
        lines.append(line[line.find(start_f):line.find(end_f)].strip())
    return lines


def _walk_over_folder(path, key, start_f, end_f, lines):
    for file in _file_walk(path):
            lines.extend(_get_key_line(file, key, start_f, end_f))


def _f_loc(path):
    items = []
    _walk_over_folder(path, ":0", "", ":0", items)
    return list(set(items))


def _f_ideas(path):
    items = []
    _walk_over_folder(path, "= {\n", "", "=", items)
    return list(set(items))


def hard_find(path, loc):
    for f in _file_walk(path):
        for line in f:
            if any(s in line for s in strings):
                if not any(s in line for s in forbidden):
                    if line[line.find("=")+1:line.find("#")].strip() != "":
                        loc.append(line[line.find("=")+1:line.find("#")].strip())


def _f_events(path):
    loc = list()
    hard_find(path, loc)
    return loc


def _out_print(list1, list2):
    return list(set(list1).difference(list2))


def print_results(list1, list2, start):
    with open('output.txt', 'a') as f:
        f.write(start)
        for item in sorted(_out_print(list1, list2)):
            f.write("%s\n" % item)
    f.close()


def localisation_check(path):
    open('output.txt', 'w')
    loc_path = path + 'localisation/'
    event_path = path + 'events/'
    idea_path = path + 'common/ideas'
    print_results(_f_events(event_path), _f_loc(loc_path), _events_print)
    print_results(_f_ideas(idea_path), _f_loc(loc_path), _ideas_print)


if __name__ == '__main__':
    localisation_check(bice_path)
