import parse_lib
import settings

for item in settings.terrains:
    with open('terrains/' + item + '.txt', "w+") as f:
        search = str(item)
        f.write(str(item.upper()) + "\n")
        for file in parse_lib.file_walk(settings.units_path):
            if any(item in line for line in file for item in settings.terrains):
                do_print = False
                temp = set(settings.terrains)
                temp.remove(item)
                for line in file:
                    ln = line[:line.find("#")].strip()
                    if "= {" in ln:
                        do_print = False
                        if not any(s in ln for s in settings.terrains):
                            if not any(s in ln for s in settings.ignore):
                                f.write("\n#" + ln[:ln.find("=")] + "\n")
                    if do_print and "}" not in ln:
                        f.write(ln.strip() + "\n")
                    elif item in ln:
                        do_print = True
                    elif "}" in ln:
                        do_print = False

