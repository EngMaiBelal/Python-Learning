# Join Lists
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# list3 = list1 + list2
# # print(list3)


# list2.extend(list1)
# print(list2)
# list = ['banana', 'apple']
# list.append('orange')
# print(list)

# list1 = [20,1 , 34, -3, 40.5, 0, True, 1, False]
# list1.sort()

# print(list1)

# thislist = ["orange", "mango", "kiwi", "Pineapple", "banana"]
# # thislist = ["orange", 0, "kiwi", "Pineapple", "banana"] # str, int 
# thislist.sort(reverse = True)
# thislist.sort()
# print(thislist)

# thislist = ["banana", "Orange","orange", "kiwi","Kiwi", "cherry"]
# thislist.sort(key = str.lower)
# print(thislist)


# thislist = ["orange", "mango", "kiwi", "Pineapple", "banana"]
# # thislist = ["orange", 0, "kiwi", "Pineapple", "banana"] # str, int 
# thislist.sort(reverse = True)
# sort--> allpha

# thislist = ["orange", "mango", "kiwi", "Pineapple", "banana"]
# thislist = ["orange", 2 , "kiwi", "Pineapple", 1]
# thislist.reverse() # mirror
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# # mylist = thislist  # by reference 
# # thislist[0] = "omar"

# mylist = thislist.copy() # by value
# thislist[0] = "omar"

# print(mylist)
# print(thislist)




# thislist = list(("apple", "banana", "cherry"))
# print(thislist)

thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist) # constructor
mylist = thislist[:]      # slice operator
print(mylist)


