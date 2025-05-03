# x = [5, 8, 9, 5]
# ordered, allow duplicated value, changable
# y = (5, 2, 3, 5)
# y[0] = 4
# print(y)
#ordered, indexed, allow duplicated value, unchangable
#fixed data

# thistuple = tuple(("apple", "banana",[1, 0], "cherry"))
# thistuple[2][0] = 50
# print(thistuple)
# x = ("apple", "banana", "cherry")
# y = list(x)
# y[0] = "orange"
# y.append("hhhh")
# y.remove("banana")
# x = tuple(y)
# print(x)
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

# tuple unpack
# task
