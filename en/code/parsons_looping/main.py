command = input("Welcome to the program that has been coded to calculate an average. Would you like to continue?")
print("Hi, this program will ask you to enter numbers and calculate the average of those numbers.")

if command == "yes":
    result = total / how_many
    how_many = int(input("How many numbers? "))
    total = 0
    for number_count in range(how_many):
        number = int(input(f"Enter number {number_count + 1}: "))  # Adjusted index to start from 1
        total += number
    print("Error!")
else:
    print(f"The average = {result}")