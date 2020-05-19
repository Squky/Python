age = 19
driver_lisence = True


# - You can vote and drive

user_input=""
print("Type 'exit' to quit the loop: ")
while user_input !="exit":
    user_input = input("Exit? ")
    age = int(input("Please enter your age: "))

    if(age > 19 and driver_lisence == True):
        print("You can vote and drive")
    elif(age>19):
        print("You can vote")
    elif(age>=16 and driver_lisence==True):
        print("You can drive")
    elif(16<age<18):
        print("You can't legally drink but your mates/uncles might have your back...")
    else:
        print("You're too young! Go back to school.")

# - You can vote
# - You can driver
# - you can't leagally drink but your mates/uncles might have your back (bigger 16)
# - Your too young, go back to school!


 #  as a user I should be able to keep being prompted for input until I say 'exit'