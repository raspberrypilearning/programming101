gold_value = 100
health_drop = 1 * difficulty
print(f'{character} is on a quest to find gold and secrets.')
gold_value = gold_value / difficulty
print("Welcome to The Adventure")
difficulty = int(input(f"What difficulty level should {character} play? (1-10) "))
print(f'The gold you find will be worth {gold_value} points.')
character = input("What is your character's name? ")
print(f'Your health will drop by {health_drop} points each turn.')
