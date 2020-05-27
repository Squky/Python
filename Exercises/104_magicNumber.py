# Magic number game!
# I want you to use operators
# equate something

# As a user, I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not.



# We should define/assign number to a variable called magic_number
# magic_number =

# I need to ask user for input

import random

user_number= int(input("Guess a number: "))
magic_numm= random.randint(1,100)
# I need to check if this input matches a magic_number

if user_number== magic_numm:
    print("Well Done!, You guessed correctly and have won!")
else:
    print("PSYKE! Thats the wrong number!")
print(magic_numm)

# I need to let the user know if the response was write or not
#self five

