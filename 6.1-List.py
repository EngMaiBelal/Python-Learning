# Array in programming
# container store multivalues

myList = ["apple", "banana", "orange", "apple"]
# print(myList)
# print(myList[-1]) # indexed
# length = index + 1
# print(len(myList))
# print(myList) # ordered
# myList[0] = "orange"
# print(myList) # changable Immutable
# print(myList) # allow duplicated value
# myList2 = list(("HTMl", "JS", "Python"))
# print(myList2)
# print(type(myList2))
# ///////////////

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[-3:-1] = ["blackcurrant", "watermelon"]
# print(thislist)


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango", "banana"]
# thislist[6:8] = ["blackcurrant", "watermelon"]
# thislist[2:4] = ""
# thislist.insert(2, "watermelon", "ppp")
# thislist.append("kkkkk")
# thislist.clear() # Empty list
# del thislist[0] 
# del thislist # delete list completely
# thislist.pop(1)
thislist.remove("banana")
print(thislist)

# len(thislist)

#########################################################
# https://www.w3schools.com/python/python_lists_add.asp