import os
from time import time
from TechTime import find_bice_time, find_vanila_time, find_coefficient
from settings import tech_vanilla_placement as vanila_path, tech_placement as bice_path

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


with open('tech_time_output.txt', 'w') as f:

    bice = get_research_time(bice_path)
    vanila = get_research_time(vanila_path)
    bice = sorted(bice, key=lambda tup: tup[1], reverse=True)
    vanila = sorted(vanila, key=lambda tup: tup[1], reverse=True)
    f.write(f'Coefficient {find_coefficient()}\n\n')
    f.write(f'All Bice time {find_bice_time()}\n\n')
    f.write(f'Bice Tech times per file\n')
    for i in bice:
        f.write(f'{i[1]} = {i[0]}\n')

    f.write('\n')
    f.write(f'All Vanila time {find_vanila_time()}\n\n')
    f.write(f'Vanila Tech times per file\n\n')
    f.write('\n')

    for i in vanila:
        f.write(f'{i[1]} = {i[0]}\n')


print(time() - time1)