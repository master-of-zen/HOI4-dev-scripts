import parse_lib
import settings

with open("all_ic.txt", "w+") as f:
    for file in parse_lib.file_walk(settings.equipment_path):
        fl = str(file)
        f.write("\n\n" + fl[fl.find("equipment") + 10:fl.find(".txt")] + ":\n\n")
        temp = ""
        for line in file:
            if not any(s in line for s in settings.ignore):
                if "= {" in line:
                    temp = (line[:line.find("=")].strip())
                elif "build_cost_ic" in line:
                    f.write(line[line.find("=") + 1:line.find("#")].strip() + " = " + temp + "\n")

