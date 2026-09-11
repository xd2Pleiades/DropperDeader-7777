#health_panel.py

from textual.app import ComposeResult
from textual.containers import VerticalScroll
from textual.widget import Widget
from textual.widgets import Label, Collapsible, Input

from data.templates.body import build_default_body


class HealthPanel(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.body = build_default_body()

    def compose(self) -> ComposeResult:
        yield Label("Health")
        with VerticalScroll():
            with Collapsible(title="Overall Health Condition"):
                yield Label(
                    f"Health Status:{health_status}"
                )
                yield Label(
                    f"Fitness Status:{fitness_status}"
                )
                yield Label(
                    "Height"
                )
                yield Input(
                    placeholder="Enter Height",
                )
                yield Label(
                    "Weight"
                )
                yield Input(
                    "Enter Weight",
                )
                yield Label(
                    "BMI"
                )
                yield Input(
                    "Enter BMI",
                )
                yield Label(
                    f"{BMI_classification}"
                )
            with Collapsible(title="Vitals"):
                yield Label(
                    f"Heart Rate:{bpm} bpm"
                )
                yield Label(
                    f"Blood Pressure:{systolic} mmHg / {diastolic} mmHg"
                )
                yield Label(
                    f"Body Temperature:{body_temperature}C"
                )
                yield Label(
                    f"Respiratory rate: {breathes_pm} per minute"
                )
                yield Label(
                    f"Oxygen saturation: {oxygen_saturation}%"
                )
            with Collapsible(title="Body Build"):
                yield Label(
                    f"Strength: {strength}"
                )
                yield Label(
                    f"Musculature: {muscles}"
                )
                yield Label(
                    f"Body fat: {body_fat}"
                    f"\n Body fat Composition: {body_fat_comp}%"
                )
            with Collapsible(
                    title="Body Regions",
                    collapsed=False,
            ):
                for body_part in self.body:
                    with Collapsible(title=body_part.name):

                        if body_part.organs:
                            with Collapsible(title="Organs"):
                                for organ in body_part.organs:
                                    yield Label(
                                        f"{organ.name}: {organ.condition.value}"
                                    )

                        if body_part.muscles:
                            with Collapsible(title="Muscles"):
                                for muscle in body_part.muscles:
                                    yield Label(
                                        f"{muscle.name}: "
                                        f"{muscle.condition.value}"
                                    )

                        if body_part.vessels:
                            with Collapsible(title="Blood Vessels"):
                                for vessel in body_part.vessels:
                                    yield Label(
                                        f"{vessel.name}: "
                                        f"{vessel.condition.value}"
                                    )

                        if body_part.tissues:
                            with Collapsible(title="Tissues"):
                                for tissue in body_part.tissues:
                                    yield Label(
                                        f"{tissue.name}: "
                                        f"{tissue.condition.value}"
                                    )

                        if body_part.bones:
                            with Collapsible(title="Bones"):
                                for bone in body_part.bones:
                                    yield Label(
                                        f"{bone.name}: "
                                        f"{bone.condition.value}"
                                    )

                        if body_part.wounds:
                            with Collapsible(title="Wounds"):
                                for wound in body_part.wounds:
                                    yield Label(
                                        f"{wound.wound_type.value} - "
                                        f"{wound.severity.value}"
                                    )