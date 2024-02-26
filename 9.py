#Given your birthday, in the format "DD-MM-YYYY", write a function that calculates how many days have passed since your birthday (without counting the days in your birth year and the current year, so just whole years).
#The function takes your birthday as a parameter in string format.
#Do not import anything, use only what we learned in class
def years_alive(day, month, year):
    current_day = 26
    current_month = 2
    current_year = 2024

    # Calculate the  of whole years passed between birthday and current date
    years_passed = current_year - year - 1

    return years_passed

