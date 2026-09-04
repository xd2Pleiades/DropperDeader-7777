# data/player_status.py
from __future__ import annotations
from dataclasses import dataclass, field

from data.templates.body import BodyPart, build_default_body
from data.templates.personality import Personality, Traits


# ---REFERENCE DICTS--------------------------

PERSONAL_INFORMATION = {
    "Registration Number": "...",
    "First Name": "...",
    "Middle Name": "...",
    "Last Name": "...",
    "Age": "...",
    "Date of Birth": "...",
    "Planet of Origin": "...",
    "District of Origin": "...",
    "Microdistrict of Origin": "...",
    "Current Planet": "Karo",
    "Current District": "...",
    "Current Microdistrict": "...",
}

BASE_STATS = {
    # PHYSICAL
    "PHYSIQUE": "...",
    "STRENGTH": "...",
    "ENDURANCE": "...",
    "AGILITY": "...",
    "DEXTERITY": "...",
    # COGNITIVE
    "PERCEPTION": "...",
    "INTELLECT": "...",
    "MEMORY": "...",
    # SOCIAL/MENTAL
    "COMPOSURE": "...",
    "EMPATHY": "...",
    "CHARISMA": "...",
    "WILLPOWER": "...",
    "FOCUS": "...",
}

# ---STAGES------------------------------

MOOD_STAGE = [
    "Bliss", "Content", "Okay", "Stressed", "Depressed", "Hopeless"
]
TACTICAL_STAGES = [
    "Fearless", "Alert", "Cautious", "Suppressed", "Hunker"
]
HUNGER_STATE = [
    "Satiated", "Full", "Natural", "Peckish", "Hungry", "Starving", "Malnourished",
]
HYDRATION_STATE = [
    "Hydrated", "Quenched", "Natural", "Thirsty", "Parched", "Dehydrated", "Critically Dehydrated"
]


# ---CHARACTER--------------------------

@dataclass
class Character:
    # --- Identity ---
    name: str = ""
    registration_number: str = ""
    sex: str = ""
    age: int = 0
    dob: str = ""
    planet: str = ""
    district: str = ""
    microdistrict: str = ""
    occupation: str = ""
    blood_type: str = ""

    # --- Base Stats ---
    physique: int = 0
    strength: int = 0
    endurance: int = 0
    agility: int = 0
    dexterity: int = 0
    perception: int = 0
    intellect: int = 0
    memory: int = 0
    composure: int = 0
    empathy: int = 0
    charisma: int = 0
    willpower: int = 0
    focus: int = 0

    # --- Vitals / Needs ---
    trauma: int = 0
    stress: int = 2
    control: int = 2
    mood: int = 2
    tactical: int = 1
    hunger: int = 2
    hydration: int = 2
    fatigue: int = 2
    stamina: int = 2
    pain: int = 2
    hygiene: int = 2
    bladder: int = 1
    shit: int = 1
    body_temperature: float = 34.5

    # --- Health ---
    build: str = ""
    fitness: str = ""
    conditions: list = field(default_factory=list)
    body: list[BodyPart] = field(default_factory=build_default_body)

    # --- Personality & Traits ---
    personality: Personality = field(default_factory=Personality)
    traits: Traits = field(default_factory=Traits)