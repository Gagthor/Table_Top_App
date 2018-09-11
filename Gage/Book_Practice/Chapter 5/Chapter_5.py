'''
#voting.py
age = 17

if age >= 18:
    print("You can vote, sure.")
    print("Have you registered yet or...?")
else:
    print("Nope, no voting for you.")
    print("You can register wha=en you turn 18, though.")


###################################################################


#amusement_park.py

age = 8

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age > 18:
    price = 1000

print("Your price is $" + str(price) + ".")


###################################################################


#toppings.py

requested_toppings = ['mushroom', 'extra cheese']

if 'mushroom' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding gross meat.")
if 'extra cheese' in requested_toppings:
    print("Makin' it thicc.")

print("\nPizza's done!")


###################################################################


#SuperNerdFunTime.py

zones = ['nerd', 'geek', 'pony']
requested_zone = ['nerd']

for zone in zones:
    if zone == 'nerd':
        print("Sounds about right.")


###################################################################


#1d20_roll.py
import random #for random int
import time #for sleep function

class Random_1d20:
    def randomroll(self):  
        
        #min / max value for dice roll
        min = 1
        max = 20
        roll = random.randint(min, max)

        #prints roll after sleeping fro 2 seconds
        print('Rolling the die...')
        time.sleep(2)
        print(str(roll) + '\n')
        
        #prints critical fail or hit
        if roll == 20:
            print('Critical hit!\n')
        
        elif roll == 1:
            print('Critical fail!\n')

#calls class
roll_1d20 = Random_1d20()
roll_1d20.randomroll()


###################################################################


#Kyles_calculator.py
class Calculator:
    def Kyles_Calculator(self):    
        while True:

            print("Options:")
            print("Enter 'add' to add two numbers")
            print("Enter 'subtract' to subtract two numbers")
            print("Enter 'multiply' to multiply two numbers")
            print("Enter 'divide' to divide two numbers")
            print("Enter 'quit' to end the program")

            user_input = input(": ")
            if user_input == "quit":
                break

            elif user_input == "add":
                num1 = float(input("\nEnter a number: "))
                num2 = float(input("Enter another number: "))
                result = str(num1 + num2)
                print("\nThe answer is " + result + "\n")

            elif user_input == "subtract":
                num1 = float(input("\nEnter a number: "))
                num2 = float(input("Enter another number: "))
                result = str(num1 - num2)
                print("\nThe answer is " + result + "\n")

            elif user_input == "multiply":
                num1 = float(input("\nEnter a number: "))
                num2 = float(input("Enter another number: "))
                result = str(num1 * num2)
                print("\nThe answer is " + result + "\n")

            elif user_input == "divide":
                num1 = float(input("\nEnter a number: "))
                num2 = float(input("Enter another number: "))
                result = str(num1 / num2)
                print("\nThe answer is " + result + "\n")

            else:
                print("Unknown input")

Runthatshit = Calculator()
Runthatshit.Kyles_Calculator()
'''

###################################################################


#alien.py
Roque_stats = { 'Str': 16, 
                'Dex': 15,
                'Con': 14,
                'Int': 13,
                'Wis': 12,
                'Cha': 11} 

print(Roque_stats['Str'])