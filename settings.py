"""
File for all literals
"""

"""Paths"""

idea_path = "/home/max/.local/share/Paradox Interactive/Hearts of Iron IV/mod/blackice_v4.0common/ideas"
event_path = "/home/max/.local/share/Paradox Interactive/Hearts of Iron IV/mod/blackice_v4.0events/"
loc_path = "/home/max/.local/share/Paradox Interactive/Hearts of Iron IV/mod/blackice_v4.0localisation/"
units_path = "/home/max/.local/share/Paradox Interactive/Hearts of Iron IV/mod/blackice_v4.0/common/units"
equipment_path = "/home/max/.local/share/Paradox Interactive/Hearts of Iron IV/mod/blackice_v4.0/common/units/equipment"
tech_placement = "/home/max/.local/share/Paradox Interactive/Hearts of Iron IV/mod/blackice_v4.0/common/technologies"
tech_vanilla_placement = "/home/max/.local/share/Steam/steamapps/common/Hearts of Iron IV/common/technologies"

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

