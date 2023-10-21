def oneFinder(binary_string):
    number_of_ones = binary_string.count('1')
    return number_of_ones

testString = '111000111000111'
result = oneFinder(testString)
print(f" In the string {testString}, there are {result} occurrences of '1'.")

def my_push(x, li):
    return [x] + li
print(my_push(1, [2,3,4]))

def my_pop(li):
    li.pop(0)
    return li
print(my_pop([1,2,3,4]))