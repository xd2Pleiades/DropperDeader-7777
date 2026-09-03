import random
import string


def _generate_microdistrict_code(district_num: int) -> str:
    """Builds a code like MD-11-987Z: district number + 3 digits + 1 uppercase letter."""
    digits = "".join(random.choices(string.digits, k=3))
    letter = random.choice(string.ascii_uppercase)
    return f"MD-{district_num}-{digits}{letter}"


LOCATIONS = {
    "karo": {"district_range": (1, 20)},
    "duris": {"district_range": (21, 40)},
    "outer_rings": {"district_range": (41, 60)},
}


def generate_district(region: str) -> str:
    """
    :param region: key into LOCATIONS ('karo', 'duris', 'outer_rings')
    :return: a district label, e.g. 'District 11'
    :raises KeyError: if region isn't recognized
    """
    low, high = LOCATIONS[region]["district_range"]
    return f"District {random.randint(low, high)}"


def generate_origin(region: str) -> tuple[str, str]:
    """
    :param region: key into LOCATIONS ('karo', 'duris', 'outer_rings')
    :return: (district_label, microdistrict_code) pair, e.g. ('District 11', 'MD-11-987Z')
    :raises KeyError: if region isn't recognized
    """
    low, high = LOCATIONS[region]["district_range"]
    district_num = random.randint(low, high)
    district_label = f"District {district_num}"
    microdistrict_code = _generate_microdistrict_code(district_num)
    return district_label, microdistrict_code


# TODO: Fix, include all planets add planet codes and their districts
"""
Federation of Octavosol / Emergency Assembly Union
EAU MEMBERS
Dominant Species
Theme/Inspiration 
Capital Karo
Homo Sapiens Sapiens
Federal State
Planet State of Utrique
Homo Sapiens Sapiens
Corporate Federative State
Planet State of Caogo
Neo-Homo Sapien Habilis
Democratic Federative State
Planet State of Duris
Homo Sapiens Sapiens
Corporate Federative State
Theocracy of Oro
Neo-Sapiens Mars
Aristocratic State
Planet State of Baifvis
Homo Sapiens Sapiens
Federal State
Planet State Bafwerk
Homo Sapiens Sapiens
Federal State
Theocracy Latro
 Sons of Mars
Aristocratic State
"""
