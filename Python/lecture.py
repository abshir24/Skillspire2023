# x = 5

# if(x < 10):
#     print("cool")

string = "This is my first python string"
# when naming a string variable avoid using the name str because this is a pre-built function name

number = 1
integer = 5
# when naming a integer variable avoid using the name int because this is a pre-built function name

floating_point = 5.5

# when naming a floating point number avoid using the name float because this is a pre-built function name

boolean = True
boolean2 = False


# A list in python is almost identical to an array in javascript

python_list = [1,"hello",True,5.5]

# print( python_list[1] )

#Tuple: tuple - An immutable data type (can't be changed) that contains a group of values. Values can be mixed data types

tup = (1,2,3,4,5)
# print(tup[0])

# Dictionary: dict - A set of key value pairs. Each key is unique and associated with a value

dictionary = { 
    "key" : "value"
}

# print(dictionary["key"])

my_string = "Zeus"
my_string2 = " + Hera"

# String concatenation
my_string3 = my_string + my_string2

# print(my_string3)

firstname = "Tom"
lastname = "Hanks"

# print("Hello my name is {}{}".format(firstname,lastname))
# print(f"Hello my name is {firstname}{lastname}")


# Conditionals

# age = int ( input("How old are you?") )

# if age >= 18: 
#     print("You are old enough to have a driver's liscence in the US")
# else:
#     print("You are not old enough to have a driver's liscence in the US")


# Loops

# for a in [1,2,3,4,5]:
#     print(a)

# array = [1,2,3,4,5]

# for a in array:
#     array[a] = 2

# print(array)

# for i in range(0,101,2):
#     print(i)

# a = int( input("Enter a number: ") )

# while a > 0:
#     print(a)
#     a -=10

# print("DONE")
# a = int( input("Enter a number: ") )
# while a != 0:
#     a = int( input("Enter a number: ") )



# Collections

string = "string"
# print(string[0:4])

# listOfFruits = [100,200,300,4,5,6,7,8] # Creating a list of strings

# print(listOfFruits[2:6])


# for loops with lists

array = [1,2,3,4,5,6,7,8,9,10]

# for value in array:
#     print(value)



# for i in range(0,len(array)):
#     array[i]  = array[i] * 2

# print(array)


# array = [1,2,3,4,5,6,7,8,9,10]

# print(array[5:10])
# print(array[3:10])

# input ( or parameter) = number

# output (or return statement) = number * 2

# def test(number):
#     return number * 2

# outcome_function = test(2)

# print(outcome_function)

#  len(), range(), input(),sort(),reverse, round()

collection = [1,2,3,4,5]

length = len(collection)

# print(length)

# for i in range(0,10,2):
#     print(i)

# test = int( input('Enter a number:') )

# print(test)

# collection = [2,1,2,0,5,4]

# collection[0]

# collection.sort()

# collection[0] 

# print(collection)

# collection = [1,2,3,4,5]

# collection.reverse()

# print(collection)

# number = 5.6

# print(round(number))


class Car:
   def __init__(self, weight, color, make, model, year, top_speed):
       self.weight = weight
       self.color = color
       self.make = make
       self.model = model
       self.year = year
       self.top_speed = top_speed 


car1 = Car(4000,"green","Ford","Mustang",2019,210)

print("Color " + car1.color)

print("Make " + car1.make)

car2 = Car(12000, "Grey", "MAC", "Freightline", 2019, 160)

print("Color " + car2.color)
print("Make " + car2.make)

# car3 = Car()


 

# In the example above we create a class using the class keyword. Inside the body of the class we 
# declare the a variable and set it equal to 5. Notice the indentation.  After we exit the class block we 
# use a print statement to print the data that was stored in the x variable. This may not look like much due to the 
# fact that we are just using a class to store a variable. But classes can do so much more. 
# We're just laying down the ground work.