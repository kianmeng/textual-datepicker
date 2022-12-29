from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Header, Footer, Label

from textual_datepicker import DateSelect


class DropdownApp(App):
    CSS = """
    #main_container {
        padding: 2 5;
    }

    #main_container > Label {
        margin: 3 1 1 1;
    }
    """

    BINDINGS = [
        ("f10", "app.quit", "Exit")
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Vertical(
            Label("Date:"),
            DateSelect(
                placeholder="please select",
                format="YYYY-MM-DD",
                picker_mount="#main_container"
            ),

            id="main_container"
        )


if __name__ == "__main__":
    app = DropdownApp()
    app.run()
