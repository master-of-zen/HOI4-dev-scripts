import os
from time import time
from settings import bice_path

time1 = time()


def find_all_tech_time(path):
    loc = list()
    for root, dirs, files in os.walk(path):
        for name in files:
            f = open(os.path.join(root, name), 'r')
            for line in f:
                    if "research_cost = " in line and 'xp' not in line:
                        loc.append(line[line.find("=")+1:line.find("#")].strip())
    return loc


def sum_all_time(time_list):
    count = 0
    for item in time_list:
        count += float(item)
    return count


def f_tech_time(path):
    all_tech_time = list()
    all_tech_time.extend(find_all_tech_time(path))
    all_tech_time = list(filter(None, all_tech_time))
    return int(sum_all_time(all_tech_time))


def get_research_time(path):
    all_times = []
    for root, dirs, files in os.walk(path):
        for name in files:
            f = open(os.path.join(root, name), 'r')
            ft = []
            for l in f:
                if "research_cost = " in l and 'xp' not in l:
                    ft.append(l[l.find('=') + 1:l.find("#")].strip())
            ft = list(filter(None, ft))
            ft = round(sum(list(map(float, ft))))
            all_times.append((name, ft))
    return all_times


def t_time(path):
    with open('tech_time.txt', 'w') as f:
        tech_path = os.path.join(path, 'common', 'technologies')
        mod = get_research_time(tech_path)
        mod = sorted(mod, key=lambda tup: -tup[1])
        all_tech_time = f_tech_time(tech_path)
        f.write(f'All tech time {all_tech_time}\n\n')
        f.write(f'Tech times per file\n')
        for i in mod:
            f.write(f'{i[1]} | {round((i[1]/all_tech_time) * 100, 1)}% = {i[0]}\n')


if __name__ == '__main__':
    t_time(bice_path)
