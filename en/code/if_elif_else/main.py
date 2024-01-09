# Get input from the user
response = input("Are you over the age of 13? ")

# Check different responses
if response == "yes":
    # If the user is over 13
    print("That's great! 👋 Welcome to your new video streaming service.")
elif response == "no":
    # If the user is under 13
    print("")
else:
    # If the user enters something other than "yes" or "no"
    print("Invalid response. Please enter 'yes' or 'no'.")

print("Please wait")