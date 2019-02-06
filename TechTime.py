import os

tech_placement = "/home/max/.local/share/Paradox Interactive/Hearts of Iron IV/mod/Blackice-hoi4/common/technologies"
tech_vanilla_placement = "/home/max/.local/share/Steam/steamapps/common/Hearts of Iron IV/common/technologies"


def find_all_tech_time(path):
    loc = list()
    for root, dirs, files in os.walk(path):
        for name in files:
            f = open(os.path.join(root, name), 'r')
            for line in f:
                    if "research_cost" in line:
                        loc.append(line[line.find("=")+1:line.find("#")].strip())
    loc.remove("")
    return loc


def sum_all_time(time_list):
    sum = 0
    for item in time_list:
        sum += float(item)
    return sum


def find_bice_time():
    all_bice_time = list()
    all_bice_time.extend(find_all_tech_time(tech_placement))
    all_bice_time = list(filter(None, all_bice_time))
    return sum_all_time(all_bice_time)


def find_vanila_time():
    all_vanila_time = list()
    all_vanila_time.extend(find_all_tech_time(tech_vanilla_placement))
    all_vanila_time = list(filter(None, all_vanila_time))
    return sum_all_time(all_vanila_time)


def find_coefficient():
    a = find_bice_time()
    b = find_vanila_time()
    c = a/b
    return c

def print_results():
    print("\n" * 1)
    print("All bice tech time: %d" % int(round(find_bice_time())))
    print("All vanila tech time: %d" % int(round(find_vanila_time())))
    print("Coefficient : %f" % find_coefficient())


print_results()

