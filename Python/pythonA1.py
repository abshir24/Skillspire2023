firstname = "Abshir"
lastname = "Mohamed"

fullname = f"{firstname} {lastname}" 

print(fullname.count(lastname))
print(fullname.find(lastname))
print(fullname.endswith(lastname))
print(lastname in fullname)

if(lastname in fullname):
    print("lastname exists")

# ALL METHODS ABOVE WORK FOR SOLVING PART 1


#Section 2
username = "abshir-253"

print(username.isalnum())