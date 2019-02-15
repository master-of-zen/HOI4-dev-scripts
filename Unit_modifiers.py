import parse_lib
import settings
import UnitClass


def read_all():
    for file in parse_lib.file_walk(settings.units_path):
        read_unit(file)


def read_unit(file):
    item = UnitClass
    item.unit_name = file
    print(item.unit_name)


read_all()