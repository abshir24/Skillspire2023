# Use a for loop to count from 1-100. For every number that is odd print 
# “FIZZ” for every number 
# that is even print “BUZZ”

for i in range(1,11):
    if(i % 2 == 0):
        print("BUZZ")
    else:
        print("FIZZ")



# Create a list variable with 5 numbers and find the minimum, 
# maximum and average of all those numbers. 
# Then print them out.

# [1,2,3,4,5] -> min: 1, max: 5, avg: 3

num_list = [1,2,3,4,5]
# print("min: ", min(num_list))
# print("max: ", max(num_list))
# print("avg:", sum(num_list)/len(num_list))


# find minimum and maximum
min_num = num_list[0]
max_num = num_list[0]
sum_num = 0

for num in num_list:
    sum_num += num

    if(num < min_num):
        min_num = num

    if(num > max_num):
        max_num = num


# print("min: ", min_num)
# print("max: ", max_num)
# print("avg:", sum_num/len(num_list))