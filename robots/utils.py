from datetime import date
from typing import Optional

from dateutil.relativedelta import relativedelta

def calculate_age(start_date: date, end_date: Optional[date]) -> int:
    age = relativedelta(end_date or date.today(), start_date)
    return age.years
