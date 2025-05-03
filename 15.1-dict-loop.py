# _______________________________________________
# Dictinary
# _______________________________________________
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# # thisdict2 = thisdict.copy()
# thisdict2 = dict(thisdict)
# print(thisdict2)
# print(thisdict)
# thisdict['year'] = 2000 # update

# print(thisdict2)
# print(thisdict)






# print(thisdict['year']) # access
# thisdict['name'] = 'ahmed' # add
# print(thisdict)
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 2000
# }
# for i in thisdict.items():
#     print(type(i))

# the brand is ford





# for x, y in thisdict.items():
#     print(x, y)

# for x in thisdict: #keys
#   print(x)
#   print(thisdict[x])  
#   print(thisdict) 
# print(thisdict.values())
# for x in thisdict.values():
#   print(x)

# myfamily = {
#   "child1" : {
#               "name" : "Emil",
#               "year" : 2004
#             },
#   "child2" : {
#               "name" : "Tobias",
#               "year" : 2007
#             },
#   "child3" : {
#               "name" : "Linus",
#               "year" : 2011
#             }
# }
# print(myfamily['child3']['year'])
# print(myfamily['child2']['year'])
# print(myfamily['child1']['year'])




child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
print(myfamily)