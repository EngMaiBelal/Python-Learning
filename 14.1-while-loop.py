#For loop challenge2

#The code below displays the answers to the...
#2 times table. Change it to display the..
#answers to the 3 times table


#For loop challenge4(GCSECS.COM)

#The code below is mixed up and has 1 error
#It should ask the user to enter a times table
#It should then display the times table
#Also, you may need to fix indentation

# number = int(input("Enter a times table: "))
# print("showing the",number,"times table")
# for i in range(1,13):
#   print(i ,"x", number, "=", i*number)
# ____________________________________________________________________
# Loop by index
# ____________________________________________________________________
# fruits = ('apple', 'orange', 'banana', 'cherry')
# for x in fruits:
#     print(x)

# for i in range(2):
#     print(fruits[i])



# fruits = ['apple', 'orange', 'banana', 'cherry']
# i = 0 # start
# while i < len(fruits): # condition
#   print(fruits[i])
#   i += 1 #step

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x, y in thisdict.items():
    print(x, y)

# for x in thisdict: #keys
#   print(x)
#   print(thisdict[x])  
#   print(thisdict) 
# print(thisdict.values())
# for x in thisdict.values():
#   print(x)