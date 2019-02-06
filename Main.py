"""
Code checker for HOI4 mods
"""
import os
import time


start = time. time()
idea_placement = "/home/max/.local/share/Paradox Interactive/Hearts of Iron IV/mod/Blackice-hoi4/common/ideas"
event_placement = "/home/max/.local/share/Paradox Interactive/Hearts of Iron IV/mod/Blackice-hoi4/events/"
loc_placement = "/home/max/.local/share/Paradox Interactive/Hearts of Iron IV/mod/Blackice-hoi4/localisation/"
all_loc = list()
all_id = list()
out_print = list()


def find_all_loc():
    loc = list()
    for root, dirs, files in os.walk(loc_placement):
        for name in files:
            f = open(os.path.join(root, name), 'r')
            for line in f:
                    if ":0" in line:
                        loc.append(line[:line.find(":0")].strip())
    return list(set(loc))


def find_idea_items(path):
    l = list()
    for root, dirs, files in os.walk(path):
        for name in files:
            f = open(os.path.join(root, name), 'r')
            for line in f:
                if "= {\n" in line:
                    l.append(line[:line.find("=")].strip())
    return list(set(l))


def find_all_events_id():
    strings = ("name", "desc", "title")
    forbidden = ("{", "}", "/", '"')
    loc = list()
    for root, dirs, files in os.walk(event_placement):
        for name in files:
            f = open(os.path.join(root, name), 'r')
            for line in f:
                if any(s in line for s in strings):
                    if not any(s in line for s in forbidden):
                        if line[line.find("=")+1:line.find("#")].strip() != "":
                            loc.append(line[line.find("=")+1:line.find("#")].strip())
    return loc


start = time. time()
all_loc.extend(find_all_loc())
end = time. time()
print(end - start, " Find all loc")

start = time. time()
all_id.extend(find_all_events_id())
end = time. time()
print(end - start, " Find all events")

start = time. time()
all_id.extend(find_idea_items(idea_placement))
end = time. time()
print(end - start, " Find all events")

start = time.time()
"""
for item in all_id:
    if item not in all_loc:
        out_print.append(item)
"""
out_print = list(set(all_id).difference(all_loc))

end = time. time()
print(end - start, " List stuff")

start = time. time()

with open('output.txt', 'w') as f:
    for item in sorted(out_print):
        f.write("%s\n" % item)
    f.close()
end = time. time()
print(end - start, " List stuff")

