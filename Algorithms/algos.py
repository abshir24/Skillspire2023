def oneFinder(binary_string):
    number_of_ones = binary_string.count('1')
    return number_of_ones

testString = '111000111000111'
result = oneFinder(testString)
print(f" In the string {testString}, there are {result} occurrences of '1'.")