# SIMPLEST - Restaurant Waiter Helper

# User Stories
#1
# AS a User I want to be able to see the menu in a formated way, so that I can order my meal.

#2
# AS a User I want to be able to order 3 times, and have my responses added to a list so they aren't forgotten

#3
# As a user, I want to have my order read back to me in formated way so I know what I ordered.

# DOD
# its own project on your laptop and Github
# be git tracked
# have 5 commits mininum!
# has documentation
# follows best practices

# starter code
menu = ['falafel', 'hummus', 'couscous', 'bacalhau a bras']
food_order = []
print("Items on today's Menu: ")
for i in menu:
    print(i.capitalize())
order_nums= 3
order =[]
while order_nums != 0:

    userinput = input("What would you like to order? ")
    userinput = userinput.lower()
    while(menu.count(userinput)<1):
        print("Not on the menu! ")
        userinput = input("What would you like to order? ")


    order.append(userinput)
    print("You order so far: ")
    for i in order:
        print(i)
    order_nums -= 1
    print("You can order ", order_nums, "more times")
    print()


# I need to print each item from the list
# print(menu[0])
# before I print I need to make them all capitalized
#  print everything