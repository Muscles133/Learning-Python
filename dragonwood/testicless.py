from rich import print
from rich.table import Table
from rich.console import Console

def show_colors():
    console = Console()
    table = Table(title="Rich Available Colors")
    table.add_column("Color Name", style="white")
    table.add_column("Sample Text", style="white")
    
    # Standard colors
    standard_colors = [
        "black", "red", "green", "yellow", "blue", "magenta", "cyan", "white",
        "bright_black", "bright_red", "bright_green", "bright_yellow",
        "bright_blue", "bright_magenta", "bright_cyan", "bright_white"
    ]
    
    # Named colors (some examples)
    named_colors = [
        "orange1", "orange3", "purple", "violet", "pink1", "deep_pink2",
        "steel_blue", "turquoise2", "green4", "sea_green2", "gold1",
        "sandy_brown", "dark_sea_green", "deep_sky_blue4", "dodger_blue2",
        "royal_blue1", "slate_blue3", "medium_purple", "dark_violet",
        "light_coral", "indian_red", "rosy_brown", "grey37", "grey50", "grey63",
        "grey74", "grey84", "grey93"
    ]
    
    # Add all colors to the table
    for color in standard_colors + named_colors:
        table.add_row(color, f"[{color}]This text is in {color}[/{color}]")
    
    console.print(table)

show_colors()