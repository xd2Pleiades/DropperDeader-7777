#scenario
"""
Scenario selection page
"""
from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, Button, Label
from textual.containers import VerticalScroll, Horizontal
from data.scenarios import SCENARIOS


class Scenario(Screen):
    CSS = """
    #layout {
        width: 100%;
        height: 100%;
    }

    #scenario_list {
        width: 30%;
        height: 100%;
        border: tall $background;
        padding: 1 2;
    }

    #description {
        width: 70%;
        height: 100%;
        border: tall $background;
        padding: 2 4;
    }

    #desc_title {
        text-style: bold;
        width: 100%;
        margin-bottom: 1;
    }

    #desc_text {
        width: 100%;
        margin-bottom: 2;
    }

    #desc_start {
        width: 100%;
        color: $text-muted;
    }

    Button {
        width: 100%;
        margin-top: 1;
    }

    #regiment_661 {
        color: $error;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal(id="layout"):
            with VerticalScroll(id="scenario_list"):
                yield Label("Select a scenario.", id="text")
                yield Button("New Drop", id="new_drop")
                yield Button("Inherited Debt", id="inherited_debt")
                yield Button("The Undocumented", id="the_undocumented")
                yield Button("Corporate Transfer", id="corporate_transfer")
                yield Button("Third Generation", id="third_generation")
                yield Button("Ration Runner", id="ration_runner")
                yield Button("The Witness", id="witness")
                yield Button("Corrupt", id="corrupt")
                yield Button("Prodigal & Loyal Son", id="prodigal_son")
                yield Button("Alone", id="alone")
                yield Button("Regiment 661", id="regiment_661")
                yield Button("Main Menu", id="main_menu")
            with VerticalScroll(id="description"):
                yield Label("", id="desc_title")
                yield Label("Select a scenario to see its description.", id="desc_text")
                yield Label("", id="desc_start")
                yield Button("Start", id="start")
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "start":
            if self.selected_scenario is None:
                self.notify("Select a scenario first.", severity="warning")
                return
            if SCENARIOS[self.selected_scenario]["playable"] is None:
                self.notify("Select a playable scenario first.", severity="warning")
                return
            self.notify("He has sought the abyss.")
            self.app.switch_screen("character_creation")
        elif event.button.id == "main_menu":
            self.app.switch_screen("main_menu")
            self.notify("Back to main menu.")
        elif event.button.id in SCENARIOS:
            scenario = SCENARIOS[event.button.id]
            self.selected_scenario = event.button.id
            self.query_one("#desc_title", Label).update(scenario["title"])
            self.query_one("#desc_text", Label).update(scenario["description"])
            start_with = "\n".join(f"- {s}" for s in scenario["start_with"])
            self.query_one("#desc_start", Label).update(f"Start with:\n{start_with}")

    def __init__(self):
        super().__init__()
        self.selected_scenario = None