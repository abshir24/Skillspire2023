# 1.Ask the user for number of units sold and assign it to the variable units_sold.
# 2.Run conditions on the user input (if else statements) to determine 
# the discount on the total price. Store percentage into variable
# 3. Calculate the total cost. 
# Which is (quanity * price) - (quanity * price * discount)
# 4. Print the total cost to the user.

user_input = int( input("Enter the number of units sold: ") )
discount = 0

if user_input >= 10 and user_input <= 19:
    discount = .2
elif user_input >= 20 and user_input <= 49:
    discount = .3
elif user_input >= 50 and user_input <= 99:
    discount = .4
elif user_input >= 100:
    discount = .5
else:
    discount = 0

total_cost = (user_input * 99) - (user_input * 99 * discount)

print("The total cost is:$", total_cost )