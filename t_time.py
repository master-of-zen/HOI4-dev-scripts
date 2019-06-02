import os
from time import time
from tech_time import f_tech_time
from settings import bice_path

time1 = time()


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
    with open('tech_time_output.txt', 'w') as f:
        tech_path = path + 'common/technologies'
        mod = get_research_time(tech_path)
        mod = sorted(mod, key=lambda tup: tup[1], reverse=True)
        f.write(f'All tech time {f_tech_time()}\n\n')
        f.write(f'Tech times per file\n')
        for i in mod:
            f.write(f'{i[1]} = {i[0]}\n')


if __name__ == '__main__':
    t_time(bice_path)
