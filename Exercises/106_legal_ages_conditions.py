age = 19
driver_lisence = True


# - You can vote and drive

user_input=""
print("Type 'exit' to quit the loop: ")
while user_input !="exit":              ## Start of while loop which asks the user for input until "exit" is inputted

    user_input = input("Exit? ")        ## Asks User if they want to exit.
    if (user_input == "exit"):          ## Checks if the user inputted 'exit'. If so, breaks the while loop and exits
        break


    age = int(input("Please enter your age: "))                         ## Asks user for their age and casts it as int
    drv_lic_input = (input("Do you have a driver license? (Y/N)"))      ## Asks user for if they have a driver license.


    if(drv_lic_input.lower()=="y"):             ## Checks for if the user said they have driver license
        driver_lisence = True                   ## and updates the 'driver_lisence' variable accordingly
    else:
        driver_lisence = False


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