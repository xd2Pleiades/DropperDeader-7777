#health_panel.py
from textual.app import ComposeResult
from textual.widget import Widget
from textual.containers import VerticalScroll
from textual.widgets import Label, Collapsible


class HealthPanel(Widget):

    def compose(self) -> ComposeResult:
        yield Label("Health")

        with Collapsible(title="Overall Health Status"):
            with VerticalScroll():
                yield Label("insert HealthStatus")
                yield Label("insert FitnessStatus")
                yield Label("Height:")
                yield Label("Weight:")
                yield Label("BMI:")
                yield Label("insert BMI Classification")

        with Collapsible(title="Vitals"):
            with VerticalScroll():
                yield Label("Heart rate:")
                yield Label("Blood Pressure: Systolic")
                yield Label("Blood Pressure: Diastolic")
                yield Label("Body Temperature:")
                yield Label("insert BreathingState")
                yield Label("Oxygen Saturation:")

        with Collapsible(title="Body Build"):
            with VerticalScroll():
                yield Label("insert Strength")
                yield Label("insert Musculature")
                yield Label("Body Fat:")
                yield Label("Body Fat Composition:")
                yield Label("insert BodyBuild")

        with Collapsible(title="Body Regions"):
            with VerticalScroll():

                with Collapsible(title="Head"):
                    yield Collapsible(title="Skull")
                    yield Collapsible(title="Face")
                    yield Collapsible(title="Jaw")

                    with Collapsible(title="Neck"):
                        yield Collapsible(title="Throat")

                with Collapsible(title="Torso"):
                    yield Collapsible(title="Chest")
                    yield Collapsible(title="Abdomen")
                    yield Collapsible(title="Back")
                    yield Collapsible(title="Pelvis")

                with Collapsible(title="Shoulders"):
                    with Collapsible(title="Right"):
                        yield Label("insert R Shoulder info")
                        yield Collapsible(title="R Elbow")
                        yield Collapsible(title="R Wrist")
                        yield Collapsible(title="R Hand")

                    with Collapsible(title="Left"):
                        yield Label("insert L Shoulder info")
                        yield Collapsible(title="L Elbow")
                        yield Collapsible(title="L Wrist")
                        yield Collapsible(title="L Hand")

                with Collapsible(title="Legs"):
                    with Collapsible(title="Right"):
                        yield Collapsible(title="R Thigh")
                        yield Collapsible(title="R Knee")
                        yield Collapsible(title="R Lower Leg")
                        yield Collapsible(title="R Ankle")
                        yield Collapsible(title="R Foot")

                    with Collapsible(title="Left"):
                        yield Collapsible(title="L Thigh")
                        yield Collapsible(title="L Knee")
                        yield Collapsible(title="L Lower Leg")
                        yield Collapsible(title="L Ankle")
                        yield Collapsible(title="L Foot")