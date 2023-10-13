import random

# 1. Prompt the user for a value between 1 and 6

# 2. Emulate a dice rolling session.

# 3. If the user rolls the number that they were prompted for then print 
# "You have successfully rolled (number that they chose)"

# 4. You must also print out the number of tries that it took the user to 
# roll that number.


user_input = int( input("Pick a number between 1 and 6: ") )

dice_roll = random.randint(1,6)

number_of_rolls = 1

while user_input != dice_roll: 
    print("You rolled a " + str(dice_roll) + " and you picked a " + str(user_input) + ".Try again!")
    user_input = int( input("Pick a number between 1 and 6: ") )
    dice_roll = random.randint(1,6)
    number_of_rolls += 1

print("You have successfully rolled a ",  user_input ,  "! You Win!")
print("It took you ", number_of_rolls, " tries!")
