print("Hi, this program will ask you to enter two numbers and perform a calculation using them.")
command = input("Would you like to add or divide?")

if command == "add":
    print("Let's add some numbers.")
    input1 = input("Number 1> ")
    input2 = input("Number 2> ")
    number1 = int(input1)
    number2 = int(input2)
    result = number1 + number2
    print(f"{input1} + {input2} = {result}")
else:
    print("There is an error. Please enter 'add' or 'divide' when prompted")