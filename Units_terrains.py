import parse_lib
import settings

with open("terrain_mod.txt", "w+") as f:
    for file in parse_lib.file_walk(settings.units_path):
        fl = str(file)
        f.write("\n"+ fl[fl.find("s/")+ 2:fl.find(".txt")] + "\n\n")
        do_print = False
        for line in file:
            line = line[:line.find("#")]
            if "}" not in line and do_print == True:
                f.write("\t" + line.strip() + "\n")
            elif "}" in line:
                do_print = False
            if any(s in line for s in settings.terrains):
                do_print = True
            if not any(s in line for s in settings.ignore):
                if "= {" in line:
                    if not any(s in line for s in settings.terrains):
                        f.write("\n#" + line[:line.find("=")].strip() + "\n")
                    else:
                        f.write("\n" + line[:line.find("=")].strip() + "\n")








