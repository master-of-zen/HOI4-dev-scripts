import os
from time import time
from TechTime import find_bice_time, find_vanila_time, find_coefficient
tech_placement = "/home/max/.local/share/Paradox Interactive/Hearts of Iron IV/mod/blackice_v4.0/common/technologies"
tech_vanilla_placement = "/home/max/.local/share/Steam/steamapps/common/Hearts of Iron IV/common/technologies"

time1 = time()


def find_tech_time(path):
    all_times = []
    for root, dirs, files in os.walk(path):
        for name in files:
            f = open(os.path.join(root, name), 'r')
            file_time = []
            for line in f:
                if "research_cost = " in line and 'xp' not in line:
                    file_time.append(line[line.find('=') + 1:line.find("#")].strip())
            file_time = list(filter(None, file_time))
            file_time = round(sum(list(map(float, file_time))), 2)
            all_times.append((name, file_time))
    return all_times


with open('tech_time_output.txt', 'w') as f:

    bice = find_tech_time(tech_placement)
    vanila = find_tech_time(tech_vanilla_placement)
    bice = sorted(bice, key=lambda tup: tup[1], reverse=True)
    vanila = sorted(vanila, key=lambda tup: tup[1], reverse=True)
    f.write(f'Coefficient {find_coefficient()}\n\n')
    f.write(f'All Bice time {find_bice_time()}\n\n')
    f.write(f'Bice Tech times per file\n')
    for i in bice:
        f.write(f'{i}\n')

    f.write('\n')
    f.write(f'All Vanila time {find_vanila_time()}\n\n')
    f.write(f'Vanila Tech times per file\n\n')
    f.write('\n')

    for i in vanila:
        f.write(f'{i}\n')




print(time() - time1)