"""
Code checker for HOI4 mods
"""

import settings
import parse


def get_key_line(file, key, start_f, end_f):
    lines = []
    for line in parse.have_key(file, key):
        lines.append(line[line.find(start_f):line.find(end_f)].strip())
    return lines


def walk_over_folder(path, key, start_f, end_f, lines):
    for file in parse.file_walk(path):
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
    for f in parse.file_walk(path):
        for line in f:
            if any(s in line for s in settings.strings):
                if not any(s in line for s in settings.forbidden):
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
    print_results(find_all_events_id(settings.event_path), find_all_loc(settings.loc_path), settings.events_print)
    print_results(find_idea_items(settings.idea_path), find_all_loc(settings.loc_path), settings.ideas_print)


pretty_print()
