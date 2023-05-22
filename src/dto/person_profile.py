from dataclasses import dataclass
from datetime import date

from utils import calculate_age


@dataclass(frozen=True)
class PersonProfile:
    name: str | None
    description: str | None
    birth_date: date | None
    death_date: date | None

    @property
    def age(self) -> int | None:
        if self.birth_date:
            return calculate_age(self.birth_date, self.death_date)
        return None
    
    def __rich_repr__(self):
        if self.name:
            yield self.name.title()
        if self.description:
            yield "Description", self.description
        if self.birth_date:
            yield "Birthdate", self.birth_date.strftime("%d-%m-%Y")
        if self.death_date:
            yield "Death date", self.death_date.strftime("%d-%m-%Y")
        yield "age", self.age, None
