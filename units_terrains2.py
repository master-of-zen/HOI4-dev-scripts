import os
from settings import units_path

_ignore = {"equipments", "upgrades", "resources", "type", "can_convert_from", "categories", "need", "sub_units", "#"}
_terrains = {"jungle", "forest", "marsh", "urban", "fort", "river", "amphibious", 'desert', 'capital', 'hills', 'plains',
            'densecity', 'mountain'}


def _file_walk(path):
    for root, dirs, files in os.walk(path):
        for name in files:
            yield open(os.path.join(root, name), 'r+')


def unit_terrains2(path):
    path = os.path.join(path, 'common', 'units')
    for item in _terrains:
        with open('terrains/' + item + '.txt', "w+") as f:
            f.write(str(item.upper()) + "\n")
            for file in _file_walk(path):
                if any(item in line for line in file for item in _terrains):
                    do_print = False
                    temp = set(_terrains)
                    temp.remove(item)
                    for line in file:
                        ln = line[:line.find("#")].strip()
                        if "= {" in ln:
                            do_print = False
                            if not any(s in ln for s in _terrains):
                                if not any(s in ln for s in _ignore):
                                    f.write("\n#" + ln[:ln.find("=")] + "\n")
                        if do_print and "}" not in ln:
                            f.write(ln.strip() + "\n")
                        elif item in ln:
                            do_print = True
                        elif "}" in ln:
                            do_print = False


if __name__ == '__main__':
    unit_terrains2(units_path)
