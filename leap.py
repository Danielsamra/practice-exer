def is_leap_year(year):
    # Leap year is divisible by 4
    if year % 4 == 0:
        # If divisible by 100, it should also be divisible by 400
        if year % 100 == 0:
            return year % 400 == 0
        
            return True
    else:
        return False

# Example usage:
year_to_check = 2024
if is_leap_year(year_to_check):
    print(f"{year_to_check} is a leap year.")
else:
    print(f"{year_to_check} is not a leap year.")
