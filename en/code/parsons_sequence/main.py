print(f'The gold you find will be worth {gold_value} points.')
character = input("What is your character's name ")
print(f'{character} is on a quest to find gold and secrets.')
difficulty = input(f"What difficulty level should {character} play? (1-10) ")
gold_value = 100
print("Welcome to The Adventure")
print(f'Your health will drop by {health_drop} points each turn.')
health_drop = 1
health_drop = health_drop * difficulty
gold_value = gold_value / difficulty
