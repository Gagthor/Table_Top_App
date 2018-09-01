#practice_player.py
class Test_Player():
    while True:

        print("Options:")
        print("Enter 'stats' to show stats")
        print("Enter 'show items' to show items")
        print("Enter 'add items' to show items")
        print("Enter 'roll' to roll 1d20")
        
        #Player Stats
        Strength = (20)
        Dexterity = (18)
        Constitution = (16)
        Intelligence = (14)
        Wisdom = (12)
        Charisma = (10)

        def roll_dice():    
            import random #for random int
            import time #for sleep function

            die_number = int(input("\nHow many die?: "))
            die_type = int(input("\nWhat type of die?: d"))
            min = 1
            max = die_type
            roll = random.randint(min, die_type) * die_number

            print('Rolling the die...')
            time.sleep(1)
            
            print('\nYou rolled a ' + str(roll))

            if roll == max:
                print('Critical hit!')

            elif roll == min:
                print('Critical fail!')

            print('\n')
            break
            
        user_input = input(": ")
        if user_input == "quit":
            break

        elif user_input == "roll":
            roll_dice()
            
        #User input
        user_input = input(": ")
        if user_input == "quit":
            break
        
        #Show Stats
        elif user_input == "stats":
            print("\n", "---Stats---")
            if Strength <= (11):
                print("Str: " + str(Strength) + " + 0")
            elif Strength <= (13):
                print("Str: " + str(Strength) + " + 1")
            elif Strength <= (15):
                print("Str: " + str(Strength) + " + 2")
            elif Strength <= (17):
                print("Str: " + str(Strength) + " + 3")
            elif Strength <= (19):
                print("Str: " + str(Strength) + " + 4")
            elif Strength >= (20):
                print("Str: " + str(Strength) + " + 5")

            if Dexterity <= (11):
                print("Dex: " + str(Dexterity) + " + 0")
            elif Dexterity <= (13):
                print("Dex: " + str(Dexterity) + " + 1")
            elif Dexterity <= (15):
                print("Dex: " + str(Dexterity) + " + 2")
            elif Dexterity <= (17):
                print("Dex: " + str(Dexterity) + " + 3")
            elif Dexterity <= (19):
                print("Dex: " + str(Dexterity) + " + 4")
            elif Dexterity >= (20):
                print("Dex: " + str(Dexterity) + " + 5")

            if Constitution <= (11):
                print("Con: " + str(Constitution) + " + 0")
            elif Constitution <= (13):
                print("Con: " + str(Constitution) + " + 1")
            elif Constitution <= (15):
                print("Con: " + str(Constitution) + " + 2")
            elif Constitution <= (17):
                print("Con: " + str(Constitution) + " + 3")
            elif Constitution <= (19):
                print("Con: " + str(Constitution) + " + 4")
            elif Constitution >= (20):
                print("Con: " + str(Constitution) + " + 5")

            if Wisdom <= (11):
                print("Wis: " + str(Wisdom) + " + 0")
            elif Wisdom <= (13):
                print("Wis: " + str(Wisdom) + " + 1")
            elif Wisdom <= (15):
                print("Wis: " + str(Wisdom) + " + 2")
            elif Wisdom <= (17):
                print("Wis: " + str(Wisdom) + " + 3")
            elif Wisdom <= (19):
                print("Wis: " + str(Wisdom) + " + 4")
            elif Wisdom >= (20):
                print("Wis: " + str(Wisdom) + " + 5")

            if Intelligence <= (11):
                print("Int: " + str(Intelligence) + " + 0")
            elif Intelligence <= (13):
                print("Int: " + str(Intelligence) + " + 1")
            elif Intelligence <= (15):
                print("Int: " + str(Intelligence) + " + 2")
            elif Intelligence <= (17):
                print("Int: " + str(Intelligence) + " + 3")
            elif Intelligence <= (19):
                print("Int: " + str(Intelligence) + " + 4")
            elif Intelligence >= (20):
                print("Int: " + str(Intelligence) + " + 5")

            if Charisma <= (11):
                print("Cha: " + str(Charisma) + " + 0")
            elif Charisma <= (13):
                print("Cha: " + str(Charisma) + " + 1")
            elif Charisma <= (15):
                print("Cha: " + str(Charisma) + " + 2")
            elif Charisma <= (17):
                print("Cha: " + str(Charisma) + " + 3")
            elif Charisma <= (19):
                print("Cha: " + str(Charisma) + " + 4")
            elif Charisma >= (20):
                print("Cha: " + str(Charisma) + " + 5")

            print("\n")

        #Show Items
        #elif user_input == "show items":

        #roll
        elif user_input == "roll":
            roll_dice()
