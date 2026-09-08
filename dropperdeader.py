# dropperdeader.py
"""
Screen Manager
"""
from textual.app import App

from screens.character_creation import CharacterCreation
from screens.main_menu import MainMenu
from screens.scenario import Scenario


class DropperDeader(App):
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    SCREENS = {
        "main_menu": MainMenu,
        "scenario": Scenario,
        "character_creation": CharacterCreation
    }

    def on_mount(self) -> None:
        self.push_screen("main_menu")
