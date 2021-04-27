player = input("Hi there! What is your name? ")
print('Nice to meet you, {}. Welcome to the world of POKEMON! \nHere you will fight in a battle against other pokemon.'.format(player))
# ---NOTE--- need to have all gifs in the same folder as this python project file
# pip install random
# pip install requests
# pip install pyglet
import random
import requests
import pyglet

# ----- generating random pokemon ------
num_rounds=0 # for keeping track of the number of rounds
scores = {"You": 0, "Opponent": 0} # this dictionary stores scores
play_again = "yes"
def round():
# A function that generates 3 random pokemon and stores their info
    def possible_pokemon():
    # Create two lists
    # One for the three random numbers to be generated
    # One for storing the info about the three pokemon once generated
        random_pokemons = []
        random_choice = []
    # Repeat random number generation three times and store number in random_choice list
        for chosen_pokemon in range(3):
            chosen_pokemon = random.randint(1, 151)
            random_choice.append(chosen_pokemon)
    # Retrieve information for all three pokemon generated in the previous for loop
        for pokemon in random_choice:
            url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon)
            response = requests.get(url)
            pokemon = response.json()
    # Create variables for the information needed for the game
            name = pokemon['name']
            id = pokemon['id']
            height = pokemon['height']
            weight = pokemon['weight']
    # Store that information in a dictionary
            info_pokemon = {'name': name, 'id': id, 'height': height, 'weight': weight}
    # Add the three dictionaries to the list previously created. The list now store all three pokemons info.
            random_pokemons.append(info_pokemon)
    # Ends the programme and outputs the information requested. In this case, the two lists.
        return random_pokemons, random_choice
    random_pokemons, random_choice = possible_pokemon()
    just_names = [i['name'] for i in random_pokemons if 'name' in i]
    print("Let's play! You have been given these pokemon:")
    for name in just_names: # prints items in the list without the brackets
        print(name)
    chosen_fighter = input('I choose you, ')
    def user_choice():
        fighter = {}
        for each_dictionary in random_pokemons:
            if chosen_fighter in each_dictionary['name']:
                print('Nice choice! You are fighting with {}.'.format(chosen_fighter))
                temporary_fighter = {'name': each_dictionary['name'], 'id': each_dictionary['id'], 'height': each_dictionary['height'], 'weight': each_dictionary['weight']}
                fighter.update(temporary_fighter)
        return fighter
    def opponent_pokemon(): # generates a random pokemon for the opponent
      pokemon_number = random.randint(1, 151)
      url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
      response = requests.get(url)
      pokemon = response.json()
      return {
      'name': pokemon['name'],
      'id': pokemon['id'],
      'height': pokemon['height'],
      'weight': pokemon['weight'],
      }
# ----- GIFS-----
    def winner():
        # pick an animated gif file you have in the working directory (same folder as this project file)
        ag_file = "happy.gif"
        animation = pyglet.resource.animation(ag_file)
        sprite = pyglet.sprite.Sprite(animation)
        # create a window and set it to the image size
        win = pyglet.window.Window(width=sprite.width, height=sprite.height)
        @win.event
        def on_draw():
            win.clear()
            sprite.draw()
        pyglet.app.run()

    def loser():
        ag_file = "sad.gif"
        animation = pyglet.resource.animation(ag_file)
        sprite = pyglet.sprite.Sprite(animation)
        win = pyglet.window.Window(width=sprite.width, height=sprite.height)
        @win.event
        def on_draw():
            win.clear()
            sprite.draw()
        pyglet.app.run()

    def draw():
        ag_file = "peace.gif"
        animation = pyglet.resource.animation(ag_file)
        sprite = pyglet.sprite.Sprite(animation)
        win = pyglet.window.Window(width=sprite.width, height=sprite.height)
        @win.event
        def on_draw():
            win.clear()
            sprite.draw()
        pyglet.app.run()
# ---------THE GAME---------
    def game_on():
        my_fighter = user_choice()
        opponent_fighter = opponent_pokemon()
        print("Your opponent is fighting with {}.".format(opponent_fighter['name']))
        chosen_stat = input('What do you want to compete on? \nWhoever gets the highest value - wins. Choose id, weight or height: ')
        opponent_stat = opponent_fighter[chosen_stat]
        print('Trainer {} sent out {} against an enemy {}'.format(player, my_fighter['name'], opponent_fighter['name']))
        chosen_stat_value = my_fighter[chosen_stat]
        if chosen_stat == 'weight' and chosen_stat_value > opponent_stat:
            print('Your pokemon is heavier than {}. Congratulations! You Win!'.format(opponent_fighter['name']))
            scores["You"] += 1 # adding a point to the scores dictionary
            winner()
        elif chosen_stat == 'weight' and chosen_stat_value < opponent_stat:
            print('Oh no! Your pokemon was crushed by the heavy {}. You Lose...'.format(opponent_fighter['name']))
            scores["Opponent"] += 1
            loser()
        elif chosen_stat == 'height' and chosen_stat_value > opponent_stat:
            print('Your pokemon is taller than {}. Congratulations! You Win!'.format(opponent_fighter['name']))
            scores["You"] += 1
            winner()
        elif chosen_stat == 'height' and chosen_stat_value < opponent_stat:
            print("Oh no! Your {} is too short and couldn't reach the tall {}.\nYou Lose...".format(my_fighter['name'],opponent_fighter['name']))
            scores["Opponent"] += 1
            loser()
        elif chosen_stat == 'id' and chosen_stat_value > opponent_stat:
            print('Your pokemon is way cooler than {}. Congratulations! You Win!'.format(opponent_fighter['name']))
            scores["You"] += 1
            winner()
        elif chosen_stat == 'id' and chosen_stat_value < opponent_stat:
            print("Oh no! Your {} got intimidated by {} and ran away. You Lose...".format(my_fighter['name'],opponent_fighter['name']))
            scores["Opponent"] += 1
            loser()
        else:
            print("It's a draw!")
            draw()
    game_on()
# loops the game until the user does not say 'yes'
while play_again == "yes":
    round()
    num_rounds+=1
    play_again = input("Would you like to play again? - yes/no: ")
else:
    print("Good game! Rounds played: {}.\n---SCOREBOARD---".format(num_rounds))
    # prints scores from the dictionary without the brackets
    for key, value in scores.items():
        print("{}: {}".format(key, value))
close=input("Press enter to exit") # exits the program
# THE END