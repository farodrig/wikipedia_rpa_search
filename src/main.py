import json
from pathlib import Path
from typing import Annotated, List

from rich import print, progress
from rich.console import Console
from robots.wikipedia_robot import PersonWikipediaRobot
from typer import Context, Exit, Option, Typer

from config import SCIENTISTS, SRC_PATH
from utils import progress_display

robot = PersonWikipediaRobot()
app = Typer(rich_markup_mode="rich")
error_console = Console(stderr=True)


@app.command()
def find_wikipedia_person_by_name(name: str):
    print(f"We are going to extract data from wikipedia for: {name}")
    person_data = robot.find_person(name)
    print(person_data)


@app.command()
def find_wikipedia_people_by_name(people: List[str] = SCIENTISTS):
    robot.say_hello()
    print(f"We are going to extract data from wikipedia for these people: {people}")

    progress_display(
        elements=people,
        general_description="Extracting people information...",
        element_description=lambda scientist: f"Extracting information about {scientist}...",
        procedure=find_wikipedia_person_by_name
    )
    robot.say_goodbye()


@app.command()
def find_wikipedia_people_from_file(
    file_path: Annotated[
        Path,
        Option(
            file_okay=True,
            dir_okay=False,
            readable=True,
            resolve_path=True,
        ),
    ] = SRC_PATH / "people_names.json"
):
    default_file_error_message = "File should contain a list of strings not empty"
    with progress.open(file_path, "rb") as file:
        try:
            people_names = json.load(file)
        except json.JSONDecodeError as e:
            error_console.print_exception()
            error_console.print(default_file_error_message)
            raise Exit(code=1)

    if not isinstance(people_names, list):
        error_console.print(default_file_error_message)
        raise Exit(code=1)
    if len(people_names) == 0:
        error_console.print(default_file_error_message)
        raise Exit(code=1)
    if any(map(lambda name: not isinstance(name, str), people_names)):
        error_console.print(default_file_error_message)
        raise Exit(code=1)
    find_wikipedia_people_by_name(people_names)


@app.callback(invoke_without_command=True)
def main(ctx: Context):
    if ctx.invoked_subcommand is None:
        find_wikipedia_people_by_name()


if __name__ == "__main__":
    app()
