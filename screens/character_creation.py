#character_creation.py
"""
Character creation page
"""
from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, Button, Label, TabbedContent, TabPane, Input
from textual.containers import Horizontal, VerticalScroll
import random

from data.name import generate_name
from data.dob import generate_dob, format_dob, MIN_AGE, MAX_AGE
from data.dist import generate_origin, generate_district, LOCATIONS
from data.registration import generate_registration_number, PLANET_CODES


class CharacterCreation(Screen):

    CSS = """
    TabbedContent {
        width: 60%;
        border: wide white;
    }
    #advancement_pane {
        width: 40%;
    }
    .gen_button{
        width: 20%;
        color: white;
    }
    """

    # the scenario screen (Karo / Duris / outer_rings), not be hardcoded.
    DEFAULT_DISTRICT = "karo"
    DEFAULT_PLANET = "karo"  # this tab is specifically "Karo SSA Registration"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._generated_dob_str: str = ""
        self._origin_district_num: int = 0
        self._origin_region: str = ""

    def compose(self) -> ComposeResult:
        yield Header()
        yield Button("Back", id="back")
        with Horizontal():
            with TabbedContent():
                with TabPane("Karo SSA Registration", id="tab_ssa"):
                    with VerticalScroll():
                        yield Label("Registration Number:", classes="reg_number")
                        yield Label("", id="reg_number_value")

                        yield Label("Full Legal Name:", classes="field-label")
                        yield Input(placeholder="Enter First Name:", id="first_name")
                        yield Input(placeholder="Enter Middle Name:", id="middle_name")
                        yield Input(placeholder="Enter Last Name:", id="last_name")
                        yield Button("Generate Random Name", id="gen_name", classes="gen_button")

                        yield Label("Sex:", classes="field-label")
                        yield Label("", id="sex_value")
                        yield Button("Male", id="male_button", classes="gen_button")
                        yield Button("Female", id="female_button", classes="gen_button")

                        yield Label("Age:", classes="field-label")
                        yield Input(placeholder="Enter age", id="age")
                        yield Button("Random Age", id="gen_age", classes="gen_button")

                        yield Label("Date of Birth:", classes="field-label")
                        yield Label("", id="birth_date_value")
                        # Doesn't accept 80 years before and after 7777.
                        yield Button("Generate Date of Birth", id="gen_dob", classes="gen_button")

                        yield Label("Planet & District of Origin", classes="field-label")
                        yield Label("", id="district_origin_value")
                        yield Button("Generate District of Origin", id="gen_district_origin", classes="gen_button")

                        yield Label("Current District", id="current_district_label")
                        yield Label("", id="current_district_value")
                        yield Button("Generate Current District", id="gen_district_current", classes="gen_button")

                with TabPane("Personal Health Status", id="phs"):
                    with VerticalScroll(id="phs_scroll"):
                        yield Label("Vitals:", id="vitals")
            with VerticalScroll(id="advancement_pane"):
                yield Label("Age 16 decisions")
                # ... content for age 16 ...
                yield Label("Age 20 decisions")
                # ... content for age 20 ...
                yield Label("Age 30 decisions")
                # ... content for age 30 ...
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id

        if button_id == "back":
            # NOTE: switch_screen expects either a Screen instance or the
            # name a screen was *registered* under (via SCREENS = {...} or
            # install_screen). Confirm "scenario" is actually registered
            # under that name in dropperdeader.py / App before relying on
            # this — otherwise this raises at runtime instead of navigating.
            self.app.switch_screen("scenario")
            self.notify("Back to scenario screen.")

        elif button_id == "gen_name":
            full_name = generate_name(self.DEFAULT_DISTRICT, include_middle=True)
            parts = full_name.split(" ")
            first, middle, last = (parts + ["", "", ""])[:3] if len(parts) >= 3 else (parts[0], "", parts[-1])
            self.query_one("#first_name", Input).value = first
            self.query_one("#middle_name", Input).value = middle
            self.query_one("#last_name", Input).value = last

        elif button_id == "male_button":
            self.query_one("#sex_value", Label).update("Male")

        elif button_id == "female_button":
            self.query_one("#sex_value", Label).update("Female")

        elif button_id == "gen_age":
            age = random.randint(MIN_AGE, MAX_AGE)
            self.query_one("#age", Input).value = str(age)

        elif button_id == "gen_dob":
            age_raw = self.query_one("#age", Input).value.strip()
            if not age_raw:
                self.notify("Enter or generate an age first.", severity="warning")
                return
            try:
                age = int(age_raw)
            except ValueError:
                self.notify("Age must be a whole number.", severity="error")
                return
            if not (MIN_AGE <= age <= MAX_AGE):
                self.notify(f"Age must be between {MIN_AGE} and {MAX_AGE}.", severity="error")
                return

            dob = generate_dob(min_age=age, max_age=age)
            dob_str = format_dob(dob)
            self._generated_dob_str = dob_str
            self.query_one("#birth_date_value", Label).update(dob_str)

        elif button_id == "gen_district_origin":
            district, microdistrict = generate_origin(self.DEFAULT_DISTRICT)
            self._origin_district_num = int(district.split()[-1])
            self._origin_region = self.DEFAULT_DISTRICT
            self.query_one("#district_origin_value", Label).update(f"{district} / {microdistrict}")

            # Auto-generate RN now that district is finalized
            first = self.query_one("#first_name", Input).value.strip()
            last = self.query_one("#last_name", Input).value.strip()
            if not first or not last or not self._generated_dob_str:
                self.notify("RN will generate once name and date of birth are also set.", severity="information")
                return
            middle = self.query_one("#middle_name", Input).value.strip()
            full_name = " ".join(part for part in (first, middle, last) if part)
            rn = generate_registration_number(
                planet=self.DEFAULT_PLANET,
                region=self._origin_region,
                district_num=self._origin_district_num,
                full_name=full_name,
                dob_str=self._generated_dob_str,
            )
            self.query_one("#reg_number_value", Label).update(rn)

        elif button_id == "gen_district_current":
            # Current district isn't tied to where the character was born —
            # pick any region at random, independent of District of Origin.
            current_region = random.choice(list(LOCATIONS.keys()))
            district, microdistrict = generate_origin(current_region)
            self.query_one("#current_district_value", Label).update(f"{district} / {microdistrict}")