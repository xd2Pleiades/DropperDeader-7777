from __future__ import annotations
import json
import random
from pathlib import Path

# PP-RRRR-DD-NNNN-NNNN-CC
#   PP    = planet code
#   RRRR  = region code
#   DD    = district code
#   NNNN-NNNN = random serial
#   CC    = checksum

PLANET_CODE = "01"  # TODO: only one known planet right now (Lebenikl?) —
                     # extend this to a dict once more planets exist.

REGION_CODES = {
    "karo": "0001",
    "duris": "0002",
    "outer_rings": "0003",
}

# Where issued RNs are tracked so they're never reused, even across runs.
_STORE_PATH = Path(__file__).parent / "issued_registration_numbers.json"


def _load_issued() -> set[str]:
    if not _STORE_PATH.exists():
        return set()
    with open(_STORE_PATH, "r", encoding="utf-8") as f:
        return set(json.load(f))


def _save_issued(issued: set[str]) -> None:
    with open(_STORE_PATH, "w", encoding="utf-8") as f:
        json.dump(sorted(issued), f, indent=2)


def _checksum(digits_only: str) -> str:
    """Simple mod-100 checksum over every digit preceding it in the RN."""
    total = sum(int(ch) for ch in digits_only if ch.isdigit())
    return f"{total % 100:02d}"


def generate_registration_number(region: str, district_num: int) -> str:
    """
    Builds a unique SSA registration number: PP-RRRR-DD-NNNN-NNNN-CC.
    Retries against the persisted issued-number store until a fresh
    serial is found, then records it so it's never issued again.

    :param region: key into REGION_CODES ('karo', 'duris', 'outer_rings')
    :param district_num: numeric district id, e.g. 11
    :raises KeyError: if region isn't recognized
    """
    if region not in REGION_CODES:
        raise KeyError(f"Unknown region: {region}")

    region_code = REGION_CODES[region]
    district_code = f"{district_num % 100:02d}"
    issued = _load_issued()

    while True:
        serial_a = f"{random.randint(0, 9999):04d}"
        serial_b = f"{random.randint(0, 9999):04d}"
        digits_only = f"{PLANET_CODE}{region_code}{district_code}{serial_a}{serial_b}"
        checksum = _checksum(digits_only)
        candidate = f"{PLANET_CODE}-{region_code}-{district_code}-{serial_a}-{serial_b}-{checksum}"

        if candidate not in issued:
            issued.add(candidate)
            _save_issued(issued)
            return candidate