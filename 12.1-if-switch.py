
nat = input("what is your nationality? ")

match nat:
    case "egyption":
        print('you are from Egypt')
    case "indian":
        print('you are from India')
    case _:
        print('please focus')















# If statment --> equality, values range
# x = 6
# y = 4

# if x > y :
#     print("x is greater than y")
# elif x == y:
#     print("x equal y")
# else:
#     print("x is less than y")






# Write aprogram to ask user about langauge that he wants to learn
    # JavaScript --> web developer,
    # Python --> Data scientist,
    # PHP --> backend developer,
    # HTML --. frontend developer,
    # Java --> mobile developer
    # else -->problems

lang = input("What's the programming language you want to learn? ")

match lang:
    case "JavaScript":
        print("You can become a web developer.")

    case "Python":
        print("You can become a Data Scientist")

    case "PHP":
        print("You can become a backend developer")

    case "HTML":
        print("You can become a frontend developer")

    case "Java":
        print("You can become a mobile app developer")
    case _:
        print("The language doesn't matter, what matters is solving problems.")
















