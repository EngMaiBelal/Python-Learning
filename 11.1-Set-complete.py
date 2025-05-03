# Join 2 sets
# The union() and update() methods joins all items from both sets.
# The intersection() method keeps ONLY the duplicates.
# The difference() method keeps the items from the first set that are not in the other set(s).
# The symmetric_difference() method keeps all items EXCEPT the duplicates.

# thisset = {"apple", "banana", "cherry"}
# tropical = ("pineapple", "mango", "papaya")
# thisset.update(tropical)  # set datatype
# print(thisset)
# print(tropical)

# set1 = {"a", "b", "c", 1, 2, 8}
# set2 = {1, 2, 3}
# set3 = set1.intersection(set2)
# set3 = set1 & set2
# print(set3)

# set3 = set2.difference(set1) # 3
# set4 = set1.difference(set2) # a,b,c,8 # -
# set5 = set2.symmetric_difference(set1) # ^
# set6 = set2.union(set1) # set1 | set2

# print(set3)
# print(set4)
# print(set5)
# print(set6)

# x = {"a", "b", "c"}
# y = (1, 2, 3)

# z = x.union(y)
# print(z)
# you can join set with (tuple, set, list)  must start with set with this method
# can you change the intial set by methodName_update()
set1 = {0, False, 'a', 'b', 'B'}
print(set1)