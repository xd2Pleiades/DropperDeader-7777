# main_menu
"""
Main Menu UIX
"""
from textual.app import ComposeResult
from textual.containers import Vertical
from textual.screen import Screen
from textual.widgets import Header, Footer, Button, Label


class MainMenu(Screen):
    CSS = """
    Screen {
        align: center middle;
    }

    #menu {
        height: auto;
        width: 60;
        margin: 4 8;
        background: $panel;
        border: tall $background;
        padding: 1 2;
    }

    #title {
        text-style: bold;
        text-align: center;
        width: 100%;
        margin-bottom: 1;
    }

    #lore {
        text-align: center;
        width: 100%;
        margin-bottom: 2;
    }

    Button {
        width: 100%;
        margin-top: 1;
    }
    """

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        yield Header()

        # LORE DESCRIPTION
        with Vertical(id="menu"):
            yield Label("Welcome to DropperDeader:7777", id="title")
            yield Label(
                "Karo is cold, overcrowded, and polluted. Forgotten by the Federation, fifty-three trillion people live under its governance."
                "\n"
                "\n You are one of them."
                "\n"
                "\n Nobody promised you a life worth living"
                "\n"
                "\n You have to fight for it."
                "\n",
                id="lore")
            yield Button("Play", id="play")
            yield Button("Quit", id="quit")

        yield Footer()

    def action_toggle_dark(self) -> None:
        self.app.theme = (
            "textual-dark" if self.app.theme == "textual-light" else "textual-light"
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "play":
            self.app.switch_screen("scenario")
            self.notify("Those who moved forward with the stars... Seek a new hell.")
        elif event.button.id == "quit":
            self.app.exit()
