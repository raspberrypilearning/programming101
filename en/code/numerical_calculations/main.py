# Print a welcome message explaining the purpose of the program
print("Hi, this program will ask you to enter two numbers, calculate the addition of those two numbers and output the result.")

# Prompt the user to enter the first number and store it in the variable 'input1'
input1 = int(input("Enter number 1"))

# Prompt the user to enter the second number and store it in the variable 'input2'
input2 = int(input("Enter number 2"))

# Calculate the sum of the two numbers and store the result in the variable 'result'
result = input1 + input2

# Print the result of the addition using an f-string
print(f"The result of {input1} + {input2} is {result}")