from typing import List

from rich import print
from robots.wikipedia_robot import PersonWikipediaRobot
from typer import Context, Typer

from config import SCIENTISTS
from utils import progress_display

robot = PersonWikipediaRobot()
app = Typer(rich_markup_mode="rich")


@app.command()
def find_wikipedia_person_by_name(name: str):
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

@app.callback(invoke_without_command=True)
def main(ctx: Context):
    if ctx.invoked_subcommand is None:
        find_wikipedia_people_by_name()


if __name__ == "__main__":
    app()
