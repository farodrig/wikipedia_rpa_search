from collections.abc import Callable
from datetime import date
from typing import TypeVar

from dateutil.relativedelta import relativedelta
from rich.progress import Progress

T = TypeVar('T')

def progress_display(
    elements: list[T],
    general_description: str, 
    procedure: Callable[[T], None],
    element_description: Callable[[T], str] | None,
    **kwargs,
):
    with Progress() as progress:
        task = progress.add_task(general_description, total=len(elements), **kwargs)
        for element in elements:
            if element_description:
                progress.console.print(element_description(element))
            procedure(element)
            progress.advance(task)


def calculate_age(start_date: date, end_date: date | None) -> int:
    age = relativedelta(end_date or date.today(), start_date)
    return age.years
