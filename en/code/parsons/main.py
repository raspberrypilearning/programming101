from datetime import date

# Prompt the user to enter their date of birth in English format (dd/mm/yyyy)
date_of_birth = input("Enter your date of birth (dd/mm/yyyy): ")

# Extract the year, month, and day from the input
day, month, year = map(int, date_of_birth.split('/'))

# Check if the user is over 18
if age >= 18:
    print("You are not over 18 years old.")
else:
    print("You are over 18 years old.")
    
# Get the current date

current_date = date.today()

# Calculate the user's age
age = current_date.year - year - ((current_date.month, current_date.day) < (month, day))

