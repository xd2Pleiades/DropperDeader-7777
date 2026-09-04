# data/personality.py
"""
Traits and personality dataclasses for DropperDeader.
Personality follows the Big Five (OCEAN) model.
Traits are freeform strings with a 1-10 intensity score.
"""
from __future__ import annotations
from dataclasses import dataclass, field


# ---INTENSITY LABEL----------------------------

def intensity_label(value: int) -> str:
    """Derives a human-readable label from a 1-10 intensity value."""
    if value <= 1:
        return "Barely"
    elif value <= 3:
        return "Slight"
    elif value <= 5:
        return "Moderate"
    elif value <= 7:
        return "Notable"
    elif value <= 9:
        return "Strong"
    else:
        return "Extreme"


def describe_trait(name: str, value: int) -> str:
    """Returns a formatted trait description e.g. 'Strong Ambitious'"""
    return f"{intensity_label(value)} {name}"


# ---OCEAN PERSONALITY--------------------------

@dataclass
class Personality:
    """
    Big Five (OCEAN) personality model.
    Each axis is scored 1-10.
    """
    openness: int = 5           # curiosity, creativity, openness to experience
    conscientiousness: int = 5  # discipline, organization, dependability
    extraversion: int = 5       # sociability, assertiveness, positive emotion
    agreeableness: int = 5      # cooperation, trust, empathy
    neuroticism: int = 5        # emotional instability, anxiety, moodiness

    def describe(self) -> dict[str, str]:
        """Returns all five axes as labeled descriptions."""
        return {
            "Openness":          describe_trait("Openness", self.openness),
            "Conscientiousness": describe_trait("Conscientiousness", self.conscientiousness),
            "Extraversion":      describe_trait("Extraversion", self.extraversion),
            "Agreeableness":     describe_trait("Agreeableness", self.agreeableness),
            "Neuroticism":       describe_trait("Neuroticism", self.neuroticism),
        }


# ---TRAITS-------------------------------------

@dataclass
class Traits:
    """
    Freeform trait collection.
    Each trait is a string mapped to a 1-10 intensity value.
    e.g. {"Ambitious": 8, "Introverted": 3}
    """
    traits: dict[str, int] = field(default_factory=dict)

    def add(self, name: str, intensity: int) -> None:
        """Add or update a trait."""
        self.traits[name] = max(1, min(10, intensity))

    def remove(self, name: str) -> None:
        """Remove a trait if it exists."""
        self.traits.pop(name, None)

    def describe(self) -> list[str]:
        """Returns all traits as labeled descriptions."""
        return [describe_trait(name, value) for name, value in self.traits.items()]