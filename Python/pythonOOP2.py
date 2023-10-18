# 1. Gambling game. Create a Boxer class that has size, 
# strength, wins and losses properties. Make sure to use the CONSTRUCTOR function 
# to give values to all these properties.

# 2. In the class create a function that displays the boxer’s stats 
# (Size, Strength, Wins, Losses). 

# 3.Create 2 Boxer objects and print out all the information on both boxers.

# 4. Then use the input function to prompt the user to choose which boxer 
# they would like to bet on.

# 5. If the user chooses the boxer that has the best properties in size strength and 
# wins and losses then the user wins their bet. Other wise the user loses.

class Boxer:
    def __init__(self, size, strength, wins, losses):
        self.size = size
        self.strength = strength 
        self.wins = wins
        self.losses = losses
    
    def display_stats(self):
        print("Height(in cm):", self.size)
        print("Strength:", self.strength)
        print("Wins:", self.wins)
        print("Losses:", self.losses)
    
    def getTotalStats(self):
        return self.size + self.strength + self.wins + self.losses

boxer1 = Boxer(186, 96, 50, 0)

boxer2 = Boxer(183, 93, 46, 2)

print("-------------Boxer 1-------------")
boxer1.display_stats()
print("---------------------------------")

print("-------------Boxer 2-------------")
boxer2.display_stats()
print("----------------------------------")

user_input = int( input("Which boxer would you like to bet on? (1 or 2): ") )

betterBoxer = None

if(boxer1.getTotalStats() > boxer2.getTotalStats()):
    betterBoxer = 1
else:
    betterBoxer = 2

if(user_input == betterBoxer):
    print("You win!")
else:
    print("You lose!")

    


