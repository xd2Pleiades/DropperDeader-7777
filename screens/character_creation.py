#character_creation.py
"""
Character creation page

"""
from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, Button, Label, TabbedContent, TabPane, Input
from textual.containers import Horizontal, VerticalScroll

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

    def compose(self) -> ComposeResult:



        yield Header()

        yield Button("Back", id="back")

        with Horizontal():
            with TabbedContent():
                # SSA ------------------------------------------------------
                with TabPane("Karo SSA Registration", id="tab_ssa"):
                    with VerticalScroll():
                        yield Label("Registration Number:", classes="reg_number")
                        yield Button("Generate RN", classes="gen_button")

                        yield Label("Full Legal Name:", classes="field-label")
                        yield Input(placeholder="Enter First Name:", id="first_name")
                        yield Input(placeholder="Enter Middle Name:", id="middle_name")
                        yield Input(placeholder="Enter Last Name:", id="last_name")
                        yield Button("Generate Random Name", classes="gen_button")

                        yield Label("Sex:", classes="field-label")
                        yield Input(placeholder="Male or Female", id="sex")

                        yield Label("Date of Birth:", classes="field-label")
                        yield Input(placeholder="Enter Date of Birth:", id="birth_date")
                        # Doesn't accept 80 years before and after 7777.
                        yield Button("Generate Date of Birth", classes="gen_button")

                        yield Label("Planet & District of Origin", classes="field-label")
                        yield Button("Generate District of Origin", classes="gen_button")
                        yield Label("Current District", id="current_district")
                        yield Button("Generate Current District", classes="gen_button")

                with TabPane("Personal Health Status", id="phs"):
                    with VerticalScroll(id="phs_scroll"):
                        yield Label("Vitals:",id="vitals")

            with VerticalScroll(id="advancement_pane"):
                yield Label("Age 16 decisions")
                                # ... content for age 16 ...
                yield Label("Age 20 decisions")
                                # ... content for age 20 ...
                yield Label("Age 30 decisions")
                                # ... content for age 30 ...
        yield Footer()

    def on_button_pressed(self,event: Button.Pressed) -> None:
        if event.button.id == "back":
            self.app.switch_screen("scenario")
            self.notify("Back to scenario screen.")
        elif event.button.id == "":
            pass