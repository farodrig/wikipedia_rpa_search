from dataclasses import dataclass
from datetime import date
from typing import Optional

from utils import calculate_age


@dataclass(frozen=True)
class PersonProfile:
    name: Optional[str]
    description: Optional[str]
    birth_date: Optional[date]
    death_date: Optional[date]

    @property
    def age(self) -> Optional[int]:
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
