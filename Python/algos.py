def arr_to_dict(arr):
    dictionary = {}
    for x in arr:
        dictionary[str(x)] = x
    return {str(x):x for x in arr}


# print(arr_to_dict([1,2,3]))

def check_phone_book(phonebook, name):
    return phonebook[name]
print(check_phone_book({ "Jim": 5555555, "Bill":2222222}, "Bob"))

def remove_duplicate(arr):
    dup_dict = {}
    for x in arr:
        if str(x) not in dup_dict.keys():
            dup_dict[str(x)] = 0
        dup_dict[str(x)] += 1
    for key, value in dup_dict.items():
        if value > 1:
            for _ in range(value - 1):
                arr.remove(int(key))
    return arr
print(remove_duplicate([1,2,1,2,3,3,4,4,4,4,4,4]))

dictionary = {
    
}