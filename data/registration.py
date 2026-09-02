from __future__ import annotations
import hashlib

# PP-RRRR-DD-NNNN-NNNN-CC
#   PP    = planet code (one of the 8 Federation planets)
#   RRRR  = region code (administrative region *within* that planet —
#           for Karo specifically this reuses dist.py's karo/duris/outer_rings
#           scheme; note "duris" here is a Karo-internal region and is a
#           different thing from the planet Duris below — same name,
#           different level. Worth renaming one of them to avoid confusion.)
#   DD    = district code
#   NNNN-NNNN = serial, deterministically derived from the character's
#               own data (name + DOB + district) so no two characters
#               with different data can collide, and no external
#               file/db is needed to track "used" numbers.
#   CC    = checksum, computed purely from the digits before it — the
#           whole number is arithmetically self-validating.

PLANET_CODES = {
    "karo": "01",
    "utrique": "02",
    "caogo": "03",
    "duris": "04",       # the PLANET Duris (see naming-collision note above)
    "oro": "05",
    "baifvis": "06",
    "bafwerk": "07",
    "latro": "08",
}

REGION_CODES = {
    "karo": "0001",
    "duris": "0002",     # Karo-internal region, NOT the planet
    "outer_rings": "0003",
}


def _checksum(digits_only: str) -> str:
    """
    Mod-97 checksum over the full numeric body. Anyone holding just the
    final RN can re-derive this from its own digits and confirm it's
    well-formed — no external record needed.
    """
    return f"{int(digits_only) % 97:02d}"


def _derive_serial(full_name: str, dob_str: str, district_num: int) -> tuple[str, str]:
    """
    Turns (name, DOB, district) into an 8-digit serial via SHA-256.
    Deterministic: the same character always gets the same serial, and
    two different characters need a hash collision to get the same one
    — astronomically unlikely at this digit count, but not impossible;
    see note in generate_registration_number.
    """
    seed = f"{full_name.strip().lower()}|{dob_str}|{district_num}"
    digest = hashlib.sha256(seed.encode("utf-8")).hexdigest()
    numeric = int(digest, 16) % 10**8
    serial = f"{numeric:08d}"
    return serial[:4], serial[4:]

# TODO: Generate DD on the correct district & should force the player to generate planet, district and microdistrict first

def generate_registration_number(
    planet: str,
    region: str,
    district_num: int,
    full_name: str,
    dob_str: str,
) -> str:
    """
    :param planet: key into PLANET_CODES
    :param region: key into REGION_CODES
    :param district_num: numeric district id, e.g. 11
    :param full_name: the character's full name, used to derive the serial
    :param dob_str: the character's formatted date of birth string
    :raises KeyError: if planet or region isn't recognized
    :raises ValueError: if full_name or dob_str is empty (nothing to derive from)

    NOTE on "no duplicate IDs": without a persisted registry, uniqueness
    is only as strong as (a) no two characters sharing identical name +
    DOB + district, and (b) no SHA-256 collision in an 8-digit space.
    Two characters with the *same* name, DOB, and district will get the
    *same* RN — if that's a real scenario in your game (twins, common
    names), this alone won't catch it. Say so if you want a persisted
    fallback check re-added just for that edge case.
    """
    if planet not in PLANET_CODES:
        raise KeyError(f"Unknown planet: {planet}")
    if region not in REGION_CODES:
        raise KeyError(f"Unknown region: {region}")
    if not full_name.strip():
        raise ValueError("full_name is required to derive a registration number")
    if not dob_str.strip():
        raise ValueError("dob_str is required to derive a registration number")

    planet_code = PLANET_CODES[planet]
    region_code = REGION_CODES[region]
    district_code = f"{district_num % 100:02d}"
    serial_a, serial_b = _derive_serial(full_name, dob_str, district_num)

    digits_only = f"{planet_code}{region_code}{district_code}{serial_a}{serial_b}"
    checksum = _checksum(digits_only)

    return f"{planet_code}-{region_code}-{district_code}-{serial_a}-{serial_b}-{checksum}"


def is_valid_registration_number(rn: str) -> bool:
    """Recomputes the checksum from the RN's own digits — no lookup needed."""
    parts = rn.split("-")
    if len(parts) != 6:
        return False
    planet_code, region_code, district_code, serial_a, serial_b, checksum = parts
    digits_only = f"{planet_code}{region_code}{district_code}{serial_a}{serial_b}"
    if not digits_only.isdigit() or not checksum.isdigit():
        return False
    return _checksum(digits_only) == checksum