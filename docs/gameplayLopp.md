#character_creation.py
"""
Character creation page

"""
from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, Button, Label, TabbedContent, TabPane
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Collapsible

class CharacterCreation(Screen):

    def compose(self) -> ComposeResult:
        yield Header()
        with Collapsible(title="Character Status", collapsed=False): # UNAVAILABLE ONLY FOR GAMEPLAY
            yield Label("Time")
            yield Label("Weather")
            yield Label("Temperature")
            yield Label("No New Alerts") # Check as yield Label for {alerts} check your tablet
        with TabbedContent(initial="Personal Status"): # UNAVAILABLE ONLY FOR GAMEPLAY
            with TabPane("Personal Status", id="tab_status"):
                yield Label("Personal Status")
            with TabPane("Personal Finances", id="tab_finances"):
                yield Label("Personal Finances", id="finances")
        with Horizontal():
            with VerticalScroll(id="left"): # FOR FULL CHARACTER STATUSES & SKILLS
                yield Label("left side")
            with VerticalScroll(id="right"): # FOR CHARACTER CREATION AGE, DECISIONS EACH AGE ADVANCEMENT
                yield Label("right side")
        yield Footer()