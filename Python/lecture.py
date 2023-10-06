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

print("Hello my name is {}{}".format(firstname,lastname))
print(f"Hello my name is {firstname}{lastname}")
