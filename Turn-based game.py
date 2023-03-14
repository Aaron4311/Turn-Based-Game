import time
import random


class Character:
    def __init__(self, name, health, attack, defense, special):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.special = special  # Place where all stats of characters are identified


class Allies(Character):  # Allies class inherited from character class
    ally = []
    def __init__(self, name, health, attack, defense, special):
        super().__init__(name, health, attack, defense, special)
        Allies.ally.append(self.name + self.health + self.attack + self.defense + self.special)  # The list to see and use the stats of all allies


class Villains(Character): #Villains class inherited from character class
    villain = []
    def __init__(self, name, health, attack, defense, special):
        super().__init__(name, health, attack, defense, special)
        Villains.villain.append(self.name + self.health + self.attack + self.defense + self.special)  # The list to see and use the stats of all villains


class Weapon:
    weapons = []
    def __init__(self, name, block_chance, description, damage_rate):
        self.name = name
        self.block_chance = block_chance
        self.description = description
        self.damage_rate = damage_rate # Place where all stats of weapons are identified
        Weapon.weapons.append(self.name + self.block_chance + self.description + self.damage_rate) # The list to see and use the stats of all weapons

# Norse gods as allies
Thor = Allies("Thor", " 560", " 550", " 530", " Mighty Hammer")
Odin = Allies("Odin", " 480", " 470", " 540", " Knowledge")
Loki = Allies("Loki", " 450", " 470", " 415", " Trickery")
Balder = Allies("Balder", " 780", " 340", " 800", " Rage of Aesir")
Tyr = Allies("Tyr", " 480", " 520", " 510", " Super Strength")
Freya = Allies("Freya", " 430", " 490", " 410", " Wings of the Valkyrie")

# Greek gods as villains
Zeus = Villains("Zeus", " 550", " 560", " 470", " Lightning Strike")
Ares = Villains("Ares", " 440", " 570", " 510", " Super Strength")
Athena = Villains("Athena", " 310", " 300", " 260", " Strategy")
Poseidon = Villains("Poseidon", " 520", " 490", " 480", " Earth-Shaking")
Hades = Villains("Hades", " 515", " 500", " 530", " Controlling Flame")
Nyx = Villains("Nyx", " 400", " 490", " 410", " Shadow")

# Weapons
Sword = Weapon("Sword", " 3", " :_Strong_and_low_block_chance", " 0.15")
Axe = Weapon("Axe", " 4", " :_Powerful_but_high_block_chance", " 0.18")
Spear = Weapon("Spear", " 2", " :_Fast_but_deals_low_damage", " 0.13")


def start(): # First screen that welcomes the player
    print("\n"
          "Welcome to the arena warrior,\n" 
          "Choose which side you will fight for\n"
          "Allies / Villains (to quit press q)")
    while True:
        choice = input("  1    /    2\n") # Asks player to which side to play as
        if choice.lower() == "q":
            quit()
        elif choice.lower() == "1":
            print("Choose an ally\n")
            while True:
                for ally in Allies.ally:
                    print(ally.split(" ")[0])
                choice2 = input("(For random choice press 'r')\n") # If player chooses allies, it displays all allies for player to select
                if choice2.lower() == "r": # The choice can be made randomly
                    return random.choice(Allies.ally).split(" ")[0] # Sends the choices to the next function
                elif choice2.capitalize() in [i.split(" ")[0] for i in Allies.ally]:
                    return choice2.lower() # Sends the choices to the next function
                else:
                    print(f"There is no such ally as {choice2}\n" # If player entered an incorrect name, it warns the player
                          f"Make your choice again\n")

        elif choice.lower() == "2":
            print("Choose a villain\n")
            while True:
                for villain in Villains.villain:
                    print(villain.split(" ")[0])
                choice2 = input("For random choice press 'r'\n") # If player chooses villains, it displays all villains for player to select
                if choice2.lower() == "r": # The choice can be made randomly
                    return random.choice(Villains.villain).split(" ")[0] # Sends the choices to the next function
                elif choice2.capitalize() in [i.split(" ")[0] for i in Villains.villain]:
                    return choice2.lower() # Sends the choices to the next function
                else:
                    print(f"There is no such villain as {choice2},\n" # If player entered an incorrect name, it warns the player
                          f"Make your choice again\n")
        else:
            print("You must choose a side between these two")


def weapon_choice(): # Player chooses his weapons here
    warrior = start() # Recieves and saves choices from previous functions as variables
    print("Choose a weapon\n")
    while True:
        for _weapon in [i.split(" ")[0] + i.split(" ")[2] for i in Weapon.weapons]:
            print(_weapon.replace("_"," ")) # Displays all weapons and their descriptions
        choice = input("(For random choice press 'r')\n") # Player chooses which weapon to use
        if choice.lower() == "r":  # The choice can be made randomly
            return warrior + " " + random.choice(Weapon.weapons).split(" ")[0] # Sends the choices to the next function
        elif choice.capitalize() in [i.split(" ")[0] for i in Weapon.weapons]:
            return warrior + " " + choice # Sends the choices to the next function
        else:
            print(f"There is no such weapon as {choice},\n" # If player entered an incorrect name, it warns the player
                  f"Make your choice again\n")





def enemy(): # Player chooses his enemy and enemy's weapon
    warrior_and_weapon = weapon_choice() # Recieves and saves choices from previous functions as variables
    warrior,weapon_ = warrior_and_weapon.split(" ")[0],warrior_and_weapon.split(" ")[1] # Seperates warrior and weapon names
    ally = [i.split(" ")[0] for i in Allies.ally] # The list that holds allies' names
    villain = [i.split(" ")[0] for i in Villains.villain] # The list that holds villains' names
    if warrior.capitalize() in ally: # Checks if player chose allies

        # The part where player chooses his enemy
        while True:
            print("Choose your enemy\n")
            for enemy in villain:
                print(enemy) # Display villain names for player to select as his enemy
            choice = input("(For random choice press 'r')\n")
            if choice.lower() == "r": # The choice can be made randomly
                random_ = f"{random.choice(villain)} {warrior} {weapon_}" # Makes a random choice and saves it
                break
            elif choice.capitalize() in villain:
                random_ = f"{choice.capitalize()} {warrior.capitalize()} {weapon_.capitalize()}" # Saves player's choice
                break
            else:
                print(f"There is no such enemy as {choice},\n"  # If player entered an incorrect name, it warns the player
                     f"Make your choice again")

        # The part where player chooses his enemy's weapon
        while True:
            print("Choose your enemy's weapon")
            for enemy_weapon in Weapon.weapons:
                print((enemy_weapon.split(" ")[0] + enemy_weapon.split(" ")[2]).replace("_"," "))  # Displays all weapons and their descriptions
            choice = input("(For random choice press 'r')\n")
            if choice.lower() == "r": # The choice can be made randomly
                return random_ + " " + random.choice([i.split(" ")[0] for i in Weapon.weapons]) # Sends the choices to the next function
            elif choice.capitalize() in [i.split(" ")[0] for i in Weapon.weapons]:
                return random_  + " " + choice.capitalize() # Sends the choices to the next function
            else:
                print(f"There is no such weapon as {choice},\n" # If player entered an incorrect name, it warns the player
                      f"Make your choice again\n")

    elif warrior.capitalize() in villain: # Checks if player chose villains

        # The part where player chooses his enemy
        while True:
            print("Choose your enemy\n")
            for enemy_ in ally:
                print(enemy_) # Display villain names for player to select as his enemy
            choice = input("(For random choice press 'r')\n")
            if choice.lower() == "r": # The choice can be made randomly
                random_ = f"{random.choice(ally)} {warrior} {weapon_}"  # Saves player's choice
                break
            elif choice.capitalize() in ally:
                random_ = f"{choice.capitalize()} {warrior.capitalize()} {weapon_.capitalize()}" # Saves player's choice
                break
            else:
                print(f"There is no such enemy as {choice},\n"  # If player entered an incorrect name, it warns the player
                      f"Make your choice again")

        # The part where player chooses his enemy's weapon
        while True:
            print("Choose your enemy's weapon")
            for enemy_weapon in [i.split(" ")[0] for i in Weapon.weapons]:
                print(enemy_weapon) # Displays all weapons for player to choose for his enemy
            choice = input("(For random choice press 'r')\n")
            if choice.lower() == "r": # The choice can be made randomly
                return random_ + " " + random.choice([i.split(" ")[0] for i in Weapon.weapons]) # Sends the choices to the next function
            elif choice.capitalize() in [i.split(" ")[0] for i in Weapon.weapons]:
                print(random_ + " " + choice)
                return random_ + " " + choice.capitalize() # Sends the choices to the next function
            else:
                print(f"There is no such weapon as {choice},\n" #If player entered an incorrect name, it warns the player
                      f"Make your choice again\n")

def pre_fight(): # Sets everything before fight
    _enemy_warrior_weapon_enemyweapon = enemy() # Recieves and saves choices from previous functions as variables
    _enemy,warrior,weapon_,enemy_weapon =  _enemy_warrior_weapon_enemyweapon.split(" ")[0], _enemy_warrior_weapon_enemyweapon.split(" ")[1],\
    _enemy_warrior_weapon_enemyweapon.split(" ")[2],_enemy_warrior_weapon_enemyweapon.split(" ")[3]  #Seperates player's character, player's weapon, enemy's name and enemy's weapon
    you_are = ""

    if warrior.capitalize() in [i.split(" ")[0] for i in Allies.ally]:
        you_are = "Ally" # Changes "you_are" variable as Ally (if player chose allies)
    elif warrior.capitalize() in [i.split(" ")[0] for i in Villains.villain]:
        you_are = "Villain" # Changes "you_are" variable as Villain (if player chose villains)
    _your_stats = "" # This variable holds player's stats if player chose villains
    your_stats_ = "" # This variable holds player's stats if player chose allies

    if you_are == "Ally":
        for stats in Allies.ally:
            if warrior.capitalize() in stats:
                _your_stats = stats # Updates "_your_stats" variable
        for stats in Villains.villain:
            if _enemy in stats: # Confirms enemy's name is in the villains list
                return f"{_enemy} {warrior} {weapon_} {enemy_weapon} {_your_stats} {you_are}" # Sends the choices to the next function

    elif you_are == "Villain":
        for stats in Villains.villain:
            if warrior.capitalize() in stats:
                your_stats_ = stats # Updates "your_stats" variable
        for stats in Allies.ally:
            if _enemy in stats: # Confirms enemy's name is in the Allies list
                return f"{_enemy} {warrior} {weapon_} {enemy_weapon} {your_stats_} {you_are}" # Sends the choices to the next function


def fight():
    _enemy_warrior_weapon_enemyweapon = pre_fight() # Recieves and saves choices from previous functions as variables
    _enemy, warrior, weapon_, enemy_weapon,your_stats,you_are = _enemy_warrior_weapon_enemyweapon.split(" ")[0], _enemy_warrior_weapon_enemyweapon.split(" ")[1],\
    _enemy_warrior_weapon_enemyweapon.split(" ")[2],_enemy_warrior_weapon_enemyweapon.split(" ")[3],\
    _enemy_warrior_weapon_enemyweapon.split(" ")[4:-1],_enemy_warrior_weapon_enemyweapon.split(" ")[-1] # Seperates player's character, weapon and stats, enemy's name and weapon, and player's team
    Special = {"Thor": 2, "Odin": 1.5, "Loki": 1.4, "Balder": 1.5, "Tyr": 2, "Freya": 1.4, "Zeus": 1 * 4, "Ares": 2,"Athena": 1.5, "Poseidon": 1.8, "Hades": 1.6, "Nyx": 2} # Coefficients of all characters' special ability
    enemy_stats = " " #This variable holds enemy's stats (this will be updated later)
    void = ""

    for special in your_stats[4:]:
        void = void + " " + special #This variable holds player's special ability as string

    if you_are == "Villain":
        for enemy_stats_ in Allies.ally:
            if _enemy in enemy_stats_:
                enemy_stats = enemy_stats_.split(" ") # Updates enemy's stats
    elif you_are == "Ally":
        for enemy_stats_ in Villains.villain:
            if _enemy in enemy_stats_:
                enemy_stats = enemy_stats_.split(" ") # Updates enemy's stats
    enemy_void = ""
    for enemy_special in enemy_stats[4:]:
        enemy_void = enemy_void + " " + enemy_special # This variable holds enemy's special ability as string
    time.sleep(0.1)

    #Displays both characters' name and their stats
    print(f" {warrior.capitalize()}     VS                 {_enemy.capitalize()}\n"
          f"\n"
          f"  {warrior.capitalize()}                   {_enemy.capitalize()}\n Health: {your_stats[1]}             {enemy_stats[1]}\n Attack: {your_stats[2]}             {enemy_stats[2]}\n Defense: {your_stats[3]}            {enemy_stats[3]}\n")
    time.sleep(1)

    #A head or tails choice to decide who is starting first
    print("Time to decide who is starting first")
    while True:
        print("Heads or Tails?")
        choice = input(" 1   /   2\n")
        if choice != "1" and choice != "2":
            print("Choose again")
        else:
            break

    heads_tails = "12" # %50 probability

    print("Coin has flipped...")
    time.sleep(1.5)
    chosen = "" # This variable holds if player chose heads or tails
    not_chosen = "" # This variable holds the one that player's choice's opposite

    if choice == "1":
        chosen = "Heads"
        not_chosen = "Nails"
    elif choice == "2":
        chosen = "Nails"
        not_chosen = "Heads"

    starting = 0 # This variable decides who is starting first and whose turn to attack
    if random.choice(heads_tails) == choice: # Selects head or tails by %50 chance
        print(f"It's {chosen}, You are starting first")
        starting += 1

    else:
        print(f"It's {not_chosen}, Your enemy is starting first")
        starting += 0

    time.sleep(1)
    weapon_damage_rate = [float(i.split(" ")[-1]) for i in Weapon.weapons if weapon_ in i] # Hold weapon damage rate
    weapon_block_rate = [int(i.split(" ")[1]) for i in Weapon.weapons if weapon_ in i] # Hold weapon block rate
    enemy_weapon_damage_rate = [float(i.split(" ")[-1]) for i in Weapon.weapons if enemy_weapon in i] # Holds enemy's weapon's damage rate
    enemy_weapon_block_rate = [float(i.split(" ")[1]) for i in Weapon.weapons if enemy_weapon in i] # Holds enemy's weapon's block rate
    chance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # This helps to both player and enemy to block at weapon's block rate

    # Battle begins
    def arena(starting):
        your_health = int(your_stats[1]) # Holds player's health
        enemy_health = int(enemy_stats[1]) # Holds enemy's health
        enemy_starting_health = int(enemy_stats[1]) # Enemy's base health (This will be used to decide when special ability will be used)
        special_count = 0 # Counts special ability uses (Can only be used for once)
        enemy_special_count = 0 # Counts enemy's special ability uses (Can only be used for once)

        while True:
            if starting == 1: # If its player's turn to attack;
                while True:
                    if enemy_health > 0:
                        print("--------------------------------------------------------------\n")
                        if special_count == 0:
                            attack = input("To attack press enter (for special attack press 'S')\n") # If special ability has not been used, player sees this message
                        else:
                            attack = input("To attack press enter \n") # If special ability has been used, player sees this message

                        if attack.lower() == "s":
                            if special_count >= 1:
                                print("You have already used your special attack") # Warns the player that he will not be able to use the special ability for second time


                            else:
                                print(f"{warrior} has used {void} ability\n")  # Player uses his special attack
                                time.sleep(1.5)
                                print(f"{warrior} has dealt {round(((int(your_stats[1]) * (float(weapon_damage_rate[0]*Special[warrior.capitalize()])))), 2)} damage to {_enemy}\n") # Prints how much damage player is done to his enemy
                                time.sleep(1.5)
                                enemy_health -= round(int(your_stats[1]) * (float(weapon_damage_rate[0]*Special[warrior.capitalize()])), 3) # Updates enemy's health
                                print(f"Remaining Health {round(enemy_health, 4)}\n")
                                special_count += 1
                                starting = 0
                                if enemy_health <= 0: # If enemy's health went under zero after this attack, it ends the battle and asks player to what to do
                                    print("You have won")
                                    while True:
                                        choice = input(
                                            f"Dare to fight against {_enemy} again / Select characters / Quit \n"
                                            f"                1                 /         2         /    3    \n")
                                        if choice == "1":
                                            arena(starting)
                                        elif choice == "2":
                                            fight()
                                        elif choice == "3":
                                            quit()
                                        else:
                                            print("Select valid numbers")
                                break

                        if attack == "":
                            print(f"{warrior} has attacked with the {weapon_}\n")
                            time.sleep(1.5)
                            if random.choice(chance) > int(weapon_block_rate[0]):
                                print(f"{warrior} has dealt {round((int(your_stats[1])*float(weapon_damage_rate[0])),2)} damage to {_enemy}\n") # Prints how much damage player is done to his enemy
                                time.sleep(1.5)
                                enemy_health -=  round(int(your_stats[1]) * float(weapon_damage_rate[0]),3) # Updates enemy's health
                                print(f"Remaining Health {round(enemy_health,4)}\n")
                                starting = 0
                                if enemy_health <= 0: # If enemy's health went under zero after this attack, it ends the battle and asks player to what to do
                                    print("You have won")
                                    while True:
                                        choice = input(
                                            f"Dare to fight against {_enemy} again / Select characters / Quit \n"
                                            f"                1                 /         2         /    3    \n")

                                        if choice == "1":
                                            arena(starting)
                                        elif choice == "2":
                                            fight()
                                        elif choice == "3":
                                            quit()
                                        else:
                                            print("Select valid numbers")
                                break
                            else:
                                if enemy_health <= 0:  # If enemy's health is under zero despite blocking, it ends the battle and asks player to what to do
                                    print("You have won")
                                    while True:
                                        choice = input(
                                            f"Dare to fight against {_enemy} again / Select characters / Quit \n"
                                            f"                1                 /         2         /    3    \n")
                                        if choice == "1":
                                            arena(starting)
                                        elif choice == "2":
                                            fight()
                                        elif choice == "3":
                                            quit()
                                        else:
                                            print("Select valid numbers")
                                print(f"{_enemy} has successfuly blocked {warrior}'s attack,\n"
                                      f"{warrior} has done no damage")
                                starting = 0
                                break
                        else:
                            print("You have to attack")
                            break

            if starting == 0: # If its enemy's turn to attack;
                while True:
                    if your_health > 0:
                        time.sleep(1.5)
                        print("--------------------------------------------------------------\n")
                        time.sleep(0.75)
                        print(f"{_enemy} has attackted with the {enemy_weapon}\n")
                        time.sleep(1.5)
                        if random.choice(chance) > int(enemy_weapon_block_rate[0]):
                            print(f"{_enemy} has dealt {round((int(enemy_stats[1])*float(enemy_weapon_damage_rate[0])),3)} damage to {warrior}\n") # Prints how much damage enemy is done to you
                            time.sleep(1.5)
                            your_health -= round((int(enemy_stats[1])*float(enemy_weapon_damage_rate[0])),2) # Updates player's health
                            print(f"Your remaining Health {round(your_health,4)}\n")

                            if your_health <= 0: # If player's health went under zero after this attack, it ends the battle and asks player to what to do
                                print("You have lost")
                                while True:
                                    choice = input(
                                        f"Dare to fight against {_enemy} again / Select characters / Quit \n"
                                        f"                1                 /         2         /    3    \n")
                                    if choice == "1":
                                        arena(starting)
                                    elif choice == "2":
                                        fight()
                                    elif choice == "3":
                                        quit()
                                    else:
                                        print("Select valid numbers")
                            starting = 1
                            time.sleep(1.5)
                            break
                        else:
                            if your_health <= 0:  # If player's health is under zero despite blocking, it ends the battle and asks player to what to do
                                print("You have lost")
                                while True:
                                    choice = input(
                                        f"Dare to fight against {_enemy} again / Select characters / Quit \n"
                                        f"                1                 /         2         /    3    \n")
                                    if choice == "1":
                                        arena(starting)
                                    elif choice == "2":
                                        fight()
                                    elif choice == "3":
                                        quit()
                                    else:
                                        print("Select valid numbers")
                            print(f"{warrior} has successfuly blocked {_enemy}'s attack\n"
                                  f"{_enemy} has done no damage")

                        if enemy_health < enemy_starting_health//2 and enemy_special_count == 0: # If enemy's health is below than it's 1/2 health, enemy uses his special ability
                            print(f"{_enemy} has used {enemy_special} ability\n")
                            time.sleep(1.5)
                            print(f"{_enemy} has dealt {round((int(enemy_stats[1])*(float(enemy_weapon_damage_rate[0]))*Special[_enemy.capitalize()]),3)} damage to {warrior}\n") # Prints how much damage enemy is done to you
                            your_health -= round((int(enemy_stats[1])*(float(enemy_weapon_damage_rate[0])*Special[_enemy.capitalize()])),3) # Updates player's health
                            time.sleep(1.5)
                            print(f"Remaining Health {round(your_health,4)}\n")
                            enemy_special_count += 1
                            if your_health <= 0: # # If player's health went under zero after this attack, it ends the battle and asks player to what to do
                                print("You have lost")
                                while True:
                                    choice = input(
                                        f"Dare to fight against {_enemy} again / Select characters / Quit \n"
                                        f"                1                 /         2         /    3    \n")
                                    if choice == "1":
                                        arena(starting)
                                    elif choice == "2":
                                        fight()
                                    elif choice == "3":
                                        quit()
                                    else:
                                        print("Select valid numbers")
                        time.sleep(1.5)
                        starting = 1
                        break
    arena(starting)
fight()
