# colors = {'red', 'blue', 'green', 'red'}
# print(colors)
# print(colors[0])
# unchangable, unordered, unindexed, duplicated value not allowed

# colors = ['red', 'blue', 'green']
# colors = ('red', 'blue', 'green')
# print(colors[0])
# Id --> register 

# thisset = {"apple", "banana", "cherry"}
# print("banana" in thisset) # True, false # to list, tuple, set
# print("banana" not in thisset)

# _________________________________________________________________________________________
# Once a set is created, you cannot change its items, but you can add new items.
# 1- Change Item
# thisset = {"apple", "banana", "cherry"}
# print(thisset)
# mylist = list(thisset)
# # print(mylist)
# mylist[0] = "hhhhh"
# thisset = set(mylist)
# print(thisset)


# thisset = {"apple", "banana", "cherry"}
# thisset.add("orange")
# print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = ("pineapple", "mango", "papaya")

thisset.update(tropical)  # set datatype
print(thisset)
# print(tropical)

# thisset.remove("banana")
# thisset.remove("cherry")
# print(thisset)

# discard() will NOT raise an error. --> item not found
# remove() will raise an error. --> item not found

# thisset = {"apple"}
# print(type(thisset))

# myset = {'apple', 'orange', 'banana'}
# myset.pop() # last element
# print(myset)

