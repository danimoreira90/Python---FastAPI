from datetime import date

def calculate_days_until_birthday(birthday: date) -> int:
    today = date.today()
    this_year_birthday = birthday.replace(year=today.year)
    
    if this_year_birthday < today:
        this_year_birthday = this_year_birthday.replace(year=today.year + 1)
    
    return (this_year_birthday - today).days