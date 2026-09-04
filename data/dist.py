import random
import string


def _generate_microdistrict_code(district_num: int) -> str:
    """Builds a code like MD-11-987Z: district number + 3 digits + 1 uppercase letter."""
    digits = "".join(random.choices(string.digits, k=3))
    letter = random.choice(string.ascii_uppercase)
    return f"MD-{district_num}-{digits}{letter}"


LOCATIONS = {
    "karo": {"district_range": (1, 20)},  # Capital — Federal State
    "utrique": {"district_range": (21, 40)},  # Corporate Federative State
    "caogo": {"district_range": (41, 60)},  # Democratic Federative State
    "duris": {"district_range": (61, 80)},  # Corporate Federative State
    "oro": {"district_range": (81, 100)},  # Theocracy — Aristocratic State
    "baifvis": {"district_range": (101, 120)},  # Federal State
    "bafwerk": {"district_range": (121, 140)},  # Federal State
    "latro": {"district_range": (141, 160)},  # Theocracy — Aristocratic State
}


def generate_district(region: str) -> str:
    """
    :param region: planet key into LOCATIONS ('karo', 'utrique', 'caogo', 'duris', 'oro', 'baifvis', 'bafwerk', 'latro')
    :return: a district label, e.g. 'District 11'
    :raises KeyError: if planet isn't recognized
    """
    low, high = LOCATIONS[region]["district_range"]
    return f"District {random.randint(low, high)}"


def generate_origin(region: str) -> tuple[str, str]:
    """
    :param region: planet key into LOCATIONS ('karo', 'utrique', 'caogo', 'duris', 'oro', 'baifvis', 'bafwerk', 'latro')
    :return: (district_label, microdistrict_code) pair, e.g. ('District 11', 'MD-11-987Z')
    :raises KeyError: if region isn't recognized
    """
    low, high = LOCATIONS[region]["district_range"]
    district_num = random.randint(low, high)
    district_label = f"District {district_num}"
    microdistrict_code = _generate_microdistrict_code(district_num)
    return district_label, microdistrict_code
