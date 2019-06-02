import parse_lib
from settings import equipment_path, ignore


def f_air_cost(path):
    with open("all_ic.txt", "w+") as f:
        for file in parse_lib.file_walk(path):
            fl = str(file)
            f.write("\n\n" + fl[fl.find("equipment") + 10:fl.find(".txt")] + ":\n\n")
            temp = ""
            for line in file:
                if not any(s in line for s in ignore):
                    if "= {" in line:
                        temp = (line[:line.find("=")].strip())
                    elif "build_cost_ic" in line:
                        f.write(line[line.find("=") + 1:line.find("#")].strip() + " = " + temp + "\n")


if __name__ == '__main__':
    f_air_cost(equipment_path)