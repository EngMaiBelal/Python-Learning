mytuple = (2, 'ahmed' ,10)
# why dictionary
# x = {
#     'key1' : 'value1',
#     'key2' : 'value2'
# }
# ordered, chanagable, No duplicated (key:value pairs) overwrite
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "model2": "Mustang",
#   "year": 2024,
#   "year": 1964
# }
# print(thisdict['brand'])
# print(len(thisdict))


thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
# print(thisdict['colors'][1])
# print(type(thisdict))


thisdict = dict(
  brand = "Ford",
  electric = False,
  year = 1964,
  colors = ["red fruit", "white fruit", "blue fruit"]
)
# print(type(thisdict))
print(thisdict['colors'][1])
print(thisdict['colors'][0])
print(thisdict['colors'][2])
# loop 4 (print('hello')) # prevent the repeated code
# print('hello')
# print('hello')
# print('hello')
