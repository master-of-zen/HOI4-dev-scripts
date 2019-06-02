
from settings import terrains, ignore, units_path


def unit_terrains2(path):
    for item in terrains:
        with open('terrains/' + item + '.txt', "w+") as f:
            f.write(str(item.upper()) + "\n")
            for file in parse_lib.file_walk(path):
                if any(item in line for line in file for item in terrains):
                    do_print = False
                    temp = set(terrains)
                    temp.remove(item)
                    for line in file:
                        ln = line[:line.find("#")].strip()
                        if "= {" in ln:
                            do_print = False
                            if not any(s in ln for s in terrains):
                                if not any(s in ln for s in ignore):
                                    f.write("\n#" + ln[:ln.find("=")] + "\n")
                        if do_print and "}" not in ln:
                            f.write(ln.strip() + "\n")
                        elif item in ln:
                            do_print = True
                        elif "}" in ln:
                            do_print = False


if __name__ == '__main__':
    unit_terrains2(units_path)
