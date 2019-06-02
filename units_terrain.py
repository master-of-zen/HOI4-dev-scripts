import os
from settings import units_path, terrains, ignore


def file_walk(path):
    for root, dirs, files in os.walk(path):
        for name in files:
            yield open(os.path.join(root, name), 'r+')


def unit_terrain_modifiers(path):
    with open("terrain_mod.txt", "w+") as f:
        for file in file_walk(path):
            fl = str(file)
            f.write("\n"+ fl[fl.find("s/") + 2:fl.find(".txt")] + "\n\n")
            do_print = False
            for line in file:
                line = line[:line.find("#")]
                if "}" not in line and do_print == True:
                    f.write("\t" + line.strip() + "\n")
                elif "}" in line:
                    do_print = False
                if any(s in line for s in terrains):
                    do_print = True
                if not any(s in line for s in ignore):
                    if "= {" in line:
                        if not any(s in line for s in terrains):
                            f.write("\n#" + line[:line.find("=")].strip() + "\n")
                        else:
                            f.write("\n" + line[:line.find("=")].strip() + "\n")


if __name__ == '__main__':
    unit_terrain_modifiers(units_path)






