import datetime

def has_13th_friday(month, year):
    try:
        # Create a date object for the 13th day of the given month and year
        date = datetime.date(year, month, 13)
        
        # Check if the 13th day is a Friday (Friday corresponds to day number 4)
        return date.weekday() == 4
    except ValueError:
        # Handle invalid input 
        return False

month = 7  # july
year = 2023

if has_13th_friday(month, year):
    print(f"The 13th of {datetime.date(year, month, 1).strftime('%B')} {year} is a Friday!")
    print(True)
else:
    print(f"The 13th of {datetime.date(year, month, 1).strftime('%B')} {year} is not a Friday.")
    print(False)
