import os
from settings import bice_path

_ignore = {"equipments", "upgrades", "resources", "type", "can_convert_from", "categories", "need", "sub_units", "#",
           'add_stats', 'add_average_stats'}


def _file_walk(path):
    for root, dirs, files in os.walk(path):
        for name in files:
            yield open(os.path.join(root, name), 'r+')


def f_ic_cost(path):
    path = os.path.join(path, 'common', 'units', 'equipment')
    with open("all_ic.txt", "w+") as f:
        for file in _file_walk(path):
            if 'upgrades' in str(file):
                continue
            fl = str(file)
            f.write(("\n\n# " + fl[fl.find("equipment") + 10:fl.find(".txt")].capitalize() + ":\n\n").upper())
            temp = ""
            pass_second = False
            for line in file:
                if not any(s in line for s in _ignore):
                    if pass_second:
                        if '}' in line:
                            pass_second = False
                            continue
                        else:
                            continue
                    elif 'multiply_stats' in line or 'add_average_stats' in line:
                        pass_second = True
                        continue
                    elif "= {" in line:
                        temp = (line[:line.find("=")].strip())
                    elif "build_cost_ic" in line:
                        f.write(line[line.find("=") + 1:line.find("#")].strip() + " = " + temp + "\n")


if __name__ == '__main__':
    f_ic_cost(bice_path)
