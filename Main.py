"""
Code checker for HOI4 mods
"""
import os
import Settings

all_loc = list()
all_id = list()


def get_key_line(file, key, start_f, end_f):
    lines = []
    for line in file:
        if key in line:
            lines.append(line[line.find(start_f):line.find(end_f)].strip())
    return lines


def find_all_loc():
    loc = list()
    for root, dirs, files in os.walk(Settings.loc_path):
        for name in files:
            f = open(os.path.join(root, name), 'r')
            loc.extend(get_key_line(f, ":0", "", ":0"))
    return list(set(loc))


def find_idea_items(path):
    items = list()
    for root, dirs, files in os.walk(path):
        for name in files:
            f = open(os.path.join(root, name), 'r')
            items.extend(get_key_line(f, "= {\n", "", "="))
    return list(set(items))


def find_all_events_id():
    strings = ("name", "desc", "title")
    forbidden = ("{", "}", "/", '"')
    loc = list()
    for root, dirs, files in os.walk(Settings.event_path):
        for name in files:
            f = open(os.path.join(root, name), 'r')
            for line in f:
                if any(s in line for s in strings):
                    if not any(s in line for s in forbidden):
                        if line[line.find("=")+1:line.find("#")].strip() != "":
                            loc.append(line[line.find("=")+1:line.find("#")].strip())
    return loc


def out_print(list1, list2):
    return list(set(list1).difference(list2))


def print_results(list1, list2):
    with open('output.txt', 'a') as f:
        for item in sorted(out_print(list1, list2)):
            f.write("%s\n" % item)
    f.close()


def pretty_print():
    open('output.txt', 'w')
    with open('output.txt', 'a') as f:
        f.write("All Events with missing localisation :" + "\n" * 10)
    print_results(find_all_events_id(), find_all_loc())
    with open('output.txt', 'a') as f:
        f.write("\n" * 10 + "All ideas with missing localisation :" + "\n" * 10)
    print_results(find_idea_items(Settings.idea_path), find_all_loc())


pretty_print()