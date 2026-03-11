from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich.align import Align
from colorama import init, Fore
import math

init(autoreset=True)

console = Console()

console.print(
    Panel(
        Align.center("[bold cyan]Tile Cost Calculator[/bold cyan]\nCalculate tiles needed and total cost"),
        border_style="bright_blue",
    )
)

# Input section
tiles_price = float(Prompt.ask("[green]Enter tile price (each)[/green]"))
tile_area = float(Prompt.ask("[green]Enter tile area (sq ft)[/green]"))
room_width = float(Prompt.ask("[green]Enter room width (ft)[/green]"))
room_height = float(Prompt.ask("[green]Enter room height (ft)[/green]"))


def calculate_cost(tile_price, tile_area, room_width, room_height):

    room_area = room_width * room_height
    tiles_needed = math.ceil(room_area / tile_area)
    total_cost = tiles_needed * tile_price

    return room_area, tiles_needed, total_cost


room_area, tiles_needed, total_cost = calculate_cost(
    tiles_price, tile_area, room_width, room_height
)

# Result table
table = Table(title="Calculation Result", show_lines=True)

table.add_column("Metric", style="cyan", justify="center")
table.add_column("Value", style="magenta", justify="center")

table.add_row("Room Area", f"{room_area} sq ft")
table.add_row("Tile Area", f"{tile_area} sq ft")
table.add_row("Tiles Needed", str(tiles_needed))
table.add_row("Price per Tile", f"${tiles_price}")
table.add_row("Total Cost", f"${total_cost}")

console.print(table)

console.print(
    Panel(
        f"{Fore.YELLOW}Total tiles required: {tiles_needed}\nTotal cost: ${total_cost}",
        title="Summary",
        border_style="green",
    )
)