import random

SYLLABLES = {
    "karo": {
        "onset": ["V", "S", "M", "R", "L", "T", "D", "N", "K"],
        "vowel": ["a", "e", "i", "o", "au", "ie", "ei"],
        "coda": ["n", "l", "r", "s", "ne", "la", "ric", "va", ""],
    },
    "duris": {
        "onset": ["Br", "Dr", "Kr", "Th", "V", "K", "F", "Or", "M"],
        "vowel": ["a", "e", "o", "u", "ae"],
        "coda": ["k", "sh", "th", "ck", "n", "rr", "st", ""],
    },
    "outer_rings": {
        "onset": ["Gr", "Kr", "Sc", "Vr", "Tob", "Nim", "Rue", "Ash"],
        "vowel": ["a", "i", "u", "ix", "ak"],
        "coda": ["x", "k", "sh", "n", "rl", "aw", "am", ""],
    },
}

LAST_NAME_SYLLABLES = {
    "karo": {"onset": ["Van", "Sol", "Kas", "Mar", "On", "Far"], "mid": ["ta", "he", "tre", "ro", "di"],
             "end": ["ger", "im", "el", "ow", "ine"]},
    "duris": {"onset": ["Dun", "Ach", "Kes", "Bra", "Volk", "Sa"], "mid": ["mo", "ter", "sle", "nt", "de"],
              "end": ["re", "berg", "ler", "ner", "e"]},
    "outer_rings": {"onset": ["Hal", "Cr", "Ban", "Fer", "Wren", "Dac"], "mid": ["low", "ic", "tam", "ro", "lo"],
                    "end": ["way", "k", "m", "w", "e"]},
}


def _build_syllabic(pool: dict, n_syllables: int = 2) -> str:
    parts = []
    for i in range(n_syllables):
        parts.append(random.choice(pool["onset"] if i == 0 else pool["vowel"]))
        if i == 0:
            parts.append(random.choice(pool["vowel"]))
    parts.append(random.choice(pool["coda"]))
    return "".join(parts).capitalize()


def _build_surname(pool: dict) -> str:
    return (random.choice(pool["onset"]) + random.choice(pool["mid"]) + random.choice(pool["end"]))


def generate_name(district: str, include_middle: bool = True) -> str:
    """
    :param district: key into SYLLABLES/LAST_NAME_SYLLABLES ('karo', 'duris', 'outer_rings')
    :param include_middle: whether to include a middle name
    :raises KeyError: if district isn't recognized
    """
    syl_pool = SYLLABLES[district]
    sur_pool = LAST_NAME_SYLLABLES[district]

    parts = [_build_syllabic(syl_pool, n_syllables=random.choice([2, 2, 3]))]
    if include_middle:
        parts.append(_build_syllabic(syl_pool, n_syllables=2))
    parts.append(_build_surname(sur_pool))
    return " ".join(parts)
