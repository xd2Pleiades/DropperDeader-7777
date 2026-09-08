# data/body.py
"""
Body part, limb, and anatomical component dataclasses for DropperDeader.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum


# ---CONDITION ENUMS----------------------------

class WoundSeverity(Enum):
    GRAZE = "Graze"
    LIGHT = "Light"
    FLESH = "Flesh"
    DEEP = "Deep"
    LETHAL = "Lethal"
    DEADLY = "Deadly"


class WoundType(Enum):
    SLASH = "Slash"
    PIERCE = "Pierce"
    BLUNT = "Blunt"
    FIRE = "Fire"


class OrganCondition(Enum):
    HEALTHY = "Healthy"
    DAMAGED = "Damaged"
    INFLAMED = "Inflamed"
    INFECTED = "Infected"
    FAILING = "Failing"
    NECROTIC = "Necrotic"


class MuscleCondition(Enum):
    HEALTHY = "Healthy"
    STRAINED = "Strained"
    TORN = "Torn"
    ATROPHIED = "Atrophied"
    NECROTIC = "Necrotic"


class VesselCondition(Enum):
    HEALTHY = "Healthy"
    NARROWED = "Narrowed"
    RUPTURED = "Ruptured"
    SEVERED = "Severed"


class TissueCondition(Enum):
    HEALTHY = "Healthy"
    BRUISED = "Bruised"
    LACERATED = "Lacerated"
    OPEN_WOUND = "Open Wound"
    INFECTED = "Infected"
    NECROTIC = "Necrotic"


class BoneCondition(Enum):
    INTACT = "Intact"
    FRACTURED = "Fractured"
    SHATTERED = "Shattered"


# ---WOUND--------------------------------------

@dataclass
class Wound:
    wound_type: WoundType
    severity: WoundSeverity
    bleed_rate: int = 0
    pain_penalty: int = 0
    treated: bool = False
    infected: bool = False


# ---ANATOMICAL COMPONENTS----------------------

@dataclass
class Organ:
    name: str
    condition: OrganCondition = OrganCondition.HEALTHY


@dataclass
class Muscle:
    name: str
    condition: MuscleCondition = MuscleCondition.HEALTHY


@dataclass
class BloodVessel:
    name: str
    condition: VesselCondition = VesselCondition.HEALTHY
    blood_volume: float = 100.0       # percentage of normal volume
    red_cell_count: float = 100.0     # percentage of normal
    white_cell_count: float = 100.0   # percentage of normal
    platelet_count: float = 100.0     # percentage of normal


@dataclass
class Tissue:
    name: str
    condition: TissueCondition = TissueCondition.HEALTHY


@dataclass
class Bone:
    name: str
    condition: BoneCondition = BoneCondition.INTACT


# ---BODY PART----------------------------------

@dataclass
class BodyPart:
    name: str
    organs: list[Organ] = field(default_factory=list)
    muscles: list[Muscle] = field(default_factory=list)
    vessels: list[BloodVessel] = field(default_factory=list)
    tissues: list[Tissue] = field(default_factory=list)
    bones: list[Bone] = field(default_factory=list)
    wounds: list[Wound] = field(default_factory=list)


# ---DEFAULT BODY-------------------------------

def build_default_body() -> list[BodyPart]:
    """Returns a full default human body with all parts and components at healthy baseline."""
    return [
        BodyPart(
            name="Head",
            organs=[Organ("Brain"), Organ("Eyes"), Organ("Ears")],
            muscles=[Muscle("Facial Muscles"), Muscle("Jaw Muscles")],
            vessels=[BloodVessel("Temporal Artery")],
            tissues=[Tissue("Scalp"), Tissue("Skin")],
            bones=[Bone("Cranium")],
        ),
        BodyPart(
            name="Jaw",
            organs=[Organ("Teeth")],
            muscles=[Muscle("Masseter")],
            tissues=[Tissue("Gums"), Tissue("Skin")],
            bones=[Bone("Mandible")],
        ),
        BodyPart(
            name="Neck",
            organs=[Organ("Trachea"), Organ("Esophagus")],
            muscles=[Muscle("Neck Muscles")],
            vessels=[BloodVessel("Carotid Artery"), BloodVessel("Jugular Vein")],
            tissues=[Tissue("Skin")],
            bones=[Bone("Cervical Spine")],
        ),
        BodyPart(
            name="Chest",
            organs=[Organ("Heart"), Organ("Lungs")],
            muscles=[Muscle("Pectorals"), Muscle("Intercostals")],
            vessels=[BloodVessel("Aorta"), BloodVessel("Pulmonary Artery")],
            tissues=[Tissue("Skin")],
            bones=[Bone("Ribs"), Bone("Sternum")],
        ),
        BodyPart(
            name="Abdomen",
            organs=[Organ("Liver"), Organ("Kidneys"), Organ("Stomach"), Organ("Intestines"), Organ("Spleen")],
            muscles=[Muscle("Abdominals")],
            vessels=[BloodVessel("Abdominal Aorta"), BloodVessel("Vena Cava")],
            tissues=[Tissue("Skin")],
        ),
        BodyPart(
            name="Upper Back",
            muscles=[Muscle("Trapezius"), Muscle("Lats")],
            tissues=[Tissue("Skin")],
            bones=[Bone("Thoracic Spine"), Bone("Scapula")],
        ),
        BodyPart(
            name="Lower Back",
            organs=[Organ("Spine"), Organ("Pelvis")],
            muscles=[Muscle("Lower Back Muscles")],
            tissues=[Tissue("Skin")],
            bones=[Bone("Lumbar Spine"), Bone("Pelvis")],
        ),
        # --- LEFT SIDE ---
        BodyPart(
            name="Shoulder (L)",
            muscles=[Muscle("Deltoid"), Muscle("Rotator Cuff")],
            vessels=[BloodVessel("Subclavian Artery")],
            tissues=[Tissue("Skin")],
            bones=[Bone("Clavicle")],
        ),
        BodyPart(
            name="Upper Arm (L)",
            muscles=[Muscle("Bicep"), Muscle("Tricep")],
            vessels=[BloodVessel("Brachial Artery")],
            tissues=[Tissue("Skin")],
            bones=[Bone("Humerus")],
        ),
        BodyPart(
            name="Forearm (L)",
            muscles=[Muscle("Forearm Muscles")],
            vessels=[BloodVessel("Radial Artery"), BloodVessel("Ulnar Artery")],
            tissues=[Tissue("Skin")],
            bones=[Bone("Radius"), Bone("Ulna")],
        ),
        BodyPart(
            name="Hand (L)",
            muscles=[Muscle("Hand Muscles")],
            vessels=[BloodVessel("Palmar Arch")],
            tissues=[Tissue("Skin")],
            bones=[Bone("Carpals"), Bone("Metacarpals")],
        ),
        BodyPart(
            name="Thigh (L)",
            muscles=[Muscle("Quadriceps"), Muscle("Hamstrings")],
            vessels=[BloodVessel("Femoral Artery")],
            tissues=[Tissue("Skin")],
            bones=[Bone("Femur")],
        ),
        BodyPart(
            name="Knee (L)",
            vessels=[BloodVessel("Popliteal Artery")],
            tissues=[Tissue("Skin"), Tissue("Cartilage")],
            bones=[Bone("Patella")],
        ),
        BodyPart(
            name="Lower Leg (L)",
            muscles=[Muscle("Calf Muscles")],
            vessels=[BloodVessel("Tibial Artery")],
            tissues=[Tissue("Skin")],
            bones=[Bone("Tibia"), Bone("Fibula")],
        ),
        BodyPart(
            name="Foot (L)",
            muscles=[Muscle("Foot Muscles")],
            vessels=[BloodVessel("Dorsalis Pedis")],
            tissues=[Tissue("Skin")],
            bones=[Bone("Tarsals"), Bone("Metatarsals")],
        ),
        # --- RIGHT SIDE ---
        BodyPart(
            name="Shoulder (R)",
            muscles=[Muscle("Deltoid"), Muscle("Rotator Cuff")],
            vessels=[BloodVessel("Subclavian Artery")],
            tissues=[Tissue("Skin")],
            bones=[Bone("Clavicle")],
        ),
        BodyPart(
            name="Upper Arm (R)",
            muscles=[Muscle("Bicep"), Muscle("Tricep")],
            vessels=[BloodVessel("Brachial Artery")],
            tissues=[Tissue("Skin")],
            bones=[Bone("Humerus")],
        ),
        BodyPart(
            name="Forearm (R)",
            muscles=[Muscle("Forearm Muscles")],
            vessels=[BloodVessel("Radial Artery"), BloodVessel("Ulnar Artery")],
            tissues=[Tissue("Skin")],
            bones=[Bone("Radius"), Bone("Ulna")],
        ),
        BodyPart(
            name="Hand (R)",
            muscles=[Muscle("Hand Muscles")],
            vessels=[BloodVessel("Palmar Arch")],
            tissues=[Tissue("Skin")],
            bones=[Bone("Carpals"), Bone("Metacarpals")],
        ),
        BodyPart(
            name="Thigh (R)",
            muscles=[Muscle("Quadriceps"), Muscle("Hamstrings")],
            vessels=[BloodVessel("Femoral Artery")],
            tissues=[Tissue("Skin")],
            bones=[Bone("Femur")],
        ),
        BodyPart(
            name="Knee (R)",
            vessels=[BloodVessel("Popliteal Artery")],
            tissues=[Tissue("Skin"), Tissue("Cartilage")],
            bones=[Bone("Patella")],
        ),
        BodyPart(
            name="Lower Leg (R)",
            muscles=[Muscle("Calf Muscles")],
            vessels=[BloodVessel("Tibial Artery")],
            tissues=[Tissue("Skin")],
            bones=[Bone("Tibia"), Bone("Fibula")],
        ),
        BodyPart(
            name="Foot (R)",
            muscles=[Muscle("Foot Muscles")],
            vessels=[BloodVessel("Dorsalis Pedis")],
            tissues=[Tissue("Skin")],
            bones=[Bone("Tarsals"), Bone("Metatarsals")],
        ),
    ]