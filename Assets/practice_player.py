class Test_Player():
    
    #Makes the program run until stopped
    while True:
        print("\n---Options---")
        print("Enter 'player' to show the player menu")
        print("Enter 'roll' to roll some dice")
           
        #dice rolling command
        def roll_dice():    
            while True:
                
                import random #for random int
                import time #for sleep function

                die_number = int(input("\nHow many die?: "))
                die_type = int(input("How many sides on the die?: " + str(die_number) + "d"))

                min = 1
                max = die_type
                
                #calculates the sum of your roll
                roll = random.randint(min, die_type) * die_number

                print('Rolling the die...')
                time.sleep(1)
                print('\nYou rolled a ' + str(roll))
                continue_input = input("\nPress 'Enter' to continue")

                #if its a 1d20 roll then allow for critical hit/fail
                if die_number == int(1):
                    if die_type == int(20):
                        if roll == max:
                            print('Critical hit!')
                        elif roll == min:
                            print('Critical fail!')

                #ask the user if they would like to roll again
                print('\nRoll again?')
                reroll_input = input("\n: ") 
                if reroll_input == "yes":
                    roll_dice()
                elif reroll_input == "no":
                    break
                else:
                    break

        #show player stats
        def player_menu():
            
            #player stats
            name = 'Player'
            race = 'Thing'
            age = 'Whatever'
            game_class = 'Warrior'
            level = (1)

            Strength = (14)
            Dexterity = (16)
            Constitution = (11)
            Intelligence = (13)
            Wisdom = (12)
            Charisma = (19)

            while True:
                print("\n---Player Options---")
                print("Enter 'create' to reroll charcter")
                print("Enter 'stats' to view stats\n")

                #character creation steps 
                player_menu_input = input(": ") 
                if player_menu_input == ('create'):
                    print('\n---Character Creation---')
                    name = input("Enter name: ")
                    race = input("Enter race: ")
                    age = input("Enter age: ")
                    game_class = input("Enter class: ")
                    level = input("Enter level: ")
                    print('\n')

                #show stats using charcter creation info
                elif player_menu_input == ('stats'):

                    print("\n---Stats---")
                    print('Name: ', name)
                    print('Race: ', race)
                    print('Age: ', age)
                    print('\nClass: ', 'lvl',str(level),game_class,'\n')

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
                    
                    continue_input = input("\nPress 'Enter' to continue")
                
                else:
                    break

        #main menu input commands
        menu_input = input("\n: ")
        
        if menu_input == "player":
            player_menu()
        elif menu_input == "roll":
            roll_dice()
        elif menu_input == "quit":
            raise SystemExit

        #Makes the program wait for input after printing the available options
        user_input()