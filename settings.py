"""
File for all literals
"""

"""Paths"""

idea_path = "/home/max/.local/share/Paradox Interactive/Hearts of Iron IV/mod/Blackice-hoi4/common/ideas"
event_path = "/home/max/.local/share/Paradox Interactive/Hearts of Iron IV/mod/Blackice-hoi4/events/"
loc_path = "/home/max/.local/share/Paradox Interactive/Hearts of Iron IV/mod/Blackice-hoi4/localisation/"
units_path = "/home/max/.local/share/Paradox Interactive/Hearts of Iron IV/mod/Blackice-hoi4/common/units"
test_path = "/home/max/PycharmProjects/bice_grenight_code_check/test"
equipment_path = "/home/max/.local/share/Paradox Interactive/Hearts of Iron IV/mod/Blackice-hoi4/common/units/equipment"
"""Strings"""

strings = ("name", "desc", "title")
forbidden = ("{", "}", "/", '"', "has")
date_key = ("date <", "date >")
ignore = {"equipments", "upgrades", "resources", "type", "can_convert_from", "categories", "need", "sub_units", "#"}
terrains = {"jungle", "forest", "marsh", "urban", "fort", "river", "amphibious", 'desert', 'capital', 'hills', 'plains',
            'densecity', 'mountain'}

"""Prints"""

events_print = "All Events with missing localisation :" + "\n" * 5
ideas_print = "\n" * 5 + "All ideas with missing localisation :" + "\n" * 5

