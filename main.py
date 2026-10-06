from datetime import date

from age_tools import make_greeting, calculate_age, year_turning

name = input("What is your name? ")
birth_year_text = input("What year were you born? ")
birth_year = int(birth_year_text)

current_year = date.today().year
age = calculate_age(birth_year, current_year)

print(make_greeting(name))
print(f"You are about {age} years old.")
print(f"You turn 100 in the year {year_turning(100, birth_year)}.")