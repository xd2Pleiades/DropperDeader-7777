#health_panel.py

from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Label, Collapsible

from data.templates.body import build_default_body


class HealthPanel(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.body = build_default_body()

    def compose(self) -> ComposeResult:
        yield Label("Health")

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