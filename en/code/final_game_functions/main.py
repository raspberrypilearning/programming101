stranger_secrets = ['there is gold to the west',
                    'there is danger to the north',
                    'there is a village to the south'
                    'there is a river to the east']

def explore(gold, gold_value, health, health_drop):
    print('You explore and find some gold')
    gold += gold_value
    health -= health_drop
    return gold, health


def talk(gold, gold_value, health, health_drop, stranger_secrets, player_information):
    print('You talk to a stranger and they sell you a secret')
    gold -= gold_value
    health -= health_drop
    secret = stranger_secrets.pop(0)
    player_information.append(secret)
    for secret in player_information:
        print(f'You know that {secret}')
    return gold, health


def rest(gold, health):
    print('You rest to regain some energy')
    health += 10
    return health


def check_player(gold, health, finished):
    if health < 0:
        print(f'You are too weak to continue')
        finished = True
    elif gold > 200:
        print(f'You are rich and have decided to go home')
        finished = True
    return finished

def main():
    # Set up character
    gold = 0
    health = 50
    player_information = []
    character = input("What is your character's name ")
    print(f'Welcome to the adventure {character}.')
    difficulty = input("What difficulty level would you like to play? ")
    gold_value = 100 / int(difficulty)
    health_drop = 1 * int(difficulty)
    print(f'The gold you find will be worth {gold_value} point.')
    print(f'Your health will drop by {health_drop} points each turn.')
    # Play game
    finished = False
    while not finished:
        finished = check_player(gold, health, finished)
        if not finished:
            print(f'You have {gold} gold and {health} health.')
            player_choice = input("What do you want to do? (explore/talk/rest/quit)> ")
            if player_choice == "explore":
                gold, health = explore(gold, gold_value, health, health_drop)
            elif player_choice == "talk":
                gold, health = talk(gold, gold_value, health, health_drop, stranger_secrets, player_information)
            elif player_choice == "rest":
                health = rest(gold, health)
            elif player_choice == "quit":
                print('Good bye')
                finished = True
            else:
                print(f'I do not understand the command {player_choice}')

if __name__ == "__main__":
    main()
        
