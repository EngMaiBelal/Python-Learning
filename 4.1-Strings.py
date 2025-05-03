# Multiline string
# x = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(x)

#########################################
# Strings are Arrays
y = "Hello, Ahmed"  # postion, index 0--> 11
                    # length = 12
# print(y[7])
# print(len(y))
################################################
# slicing

# print(y[2:10])
# print(y[:10])  #Hello, Ahm  == print(y[0:10])  
# print(y[2:])  # == print(y[2:12])

# y = "Hello, Ahmed"
# print(y[-5:-1]) # Ahme

########################################
# modify
# y = "Hi, AhmEd"
# x = y.lower()
# print(x)

# print("hello, ahmed") # 20times
#############################33
# a = "                                Hello, World! "
# print(a.strip())
# print(a.strip()+"hi")
# print(a)

# a = "Hello, World!, Hello"
# print(a.replace("Hello","Hi"))


# Regular Expression Regex (search)
########################################################################
# age = 36
# txt = "My name is John, I am " + str(age)
# txt = f"My name is John, I am {age}" 

# print(txt)

########################################################################
# x = 20
# print(f"my age is {x:.5f}")





# text = "lorem lorem 'lorem' lorem"
# text2 = "lorem lorem       'lorem' lorem"
# text = "lorem lorem \"lorem\" lorem"
# text = "https:\\www.google.com"
text = "My name is \n mai"
text = """My name is 
mai"""

print(text)
