"""
BICE for HOI4 mods
"""

import settings as st
from parse_lib import have_key, file_walk


def get_key_line(file, key, start_f, end_f):
    lines = []
    for line in have_key(file, key):
        lines.append(line[line.find(start_f):line.find(end_f)].strip())
    return lines


def walk_over_folder(path, key, start_f, end_f, lines):
    for file in file_walk(path):
            lines.extend(get_key_line(file, key, start_f, end_f))


def find_all_loc(path):
    items = []
    walk_over_folder(path, ":0", "", ":0", items)
    return list(set(items))


def find_idea_items(path):
    items = []
    walk_over_folder(path, "= {\n", "", "=", items)
    return list(set(items))


def hard_find(path, loc):
    for f in file_walk(path):
        for line in f:
            if any(s in line for s in st.strings):
                if not any(s in line for s in st.forbidden):
                    if line[line.find("=")+1:line.find("#")].strip() != "":
                        loc.append(line[line.find("=")+1:line.find("#")].strip())


def find_all_events_id(path):
    loc = list()
    hard_find(path, loc)
    return loc


def out_print(list1, list2):
    return list(set(list1).difference(list2))


def print_results(list1, list2, start):
    with open('output.txt', 'a') as f:
        f.write(start)
        for item in sorted(out_print(list1, list2)):
            f.write("%s\n" % item)
    f.close()


def pretty_print():
    open('output.txt', 'w')
    print_results(find_all_events_id(st.event_path), find_all_loc(st.loc_path), st.events_print)
    print_results(find_idea_items(st.idea_path), find_all_loc(st.loc_path), st.ideas_print)


pretty_print()
