while True:
    print("\n---Options---")
    print("Enter 'roll' to roll a die")

    import random #for random int
    import time #for sleep function

    def roll_dice():
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

    user_input = input(": ")
    if user_input == "quit":
        break

    elif user_input == "roll":
        roll_dice()