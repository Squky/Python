# Define the following variables
# name, last_name, age, eye_color, hair_color
# name = ''
# last_name = ''
# eye_color = ''
# hair_color = ''
# age = ''
# Prompt user for input and Re-assign these

# Print them back to the user as conversation
# Example: 'Hello Jack! Welcome, your age is 26, your eyes are green and your hair color is black.

#Section 2 - Calculate in what year was the person born? and responde back.
# print something like: 'You said you we're 28 hence you were born in 1991!'

#Extra - Cast your input
#
import datetime

name = ''
last_name = ''
eye_color = ''
hair_color = ''
age = ''

fName = str(input("Please input your first name: \n"))
lName = str(input("Please input your last name: \n"))
eyeColour = str(input("Please input your eye colour: \n"))
hairColour = str(input("Please input your hair colour: \n"))
age = int(input("Please input your age: \n"))

print("Hello ",fName, lName, ". You have ", eyeColour, " eyes, ",hairColour, "and hair.")
print("You are ",age , " years old.")


def yearborn(age):    # Function- takes a number and uses it to calculate year born
    cur_year = datetime.datetime.now()
    born = cur_year.year - age
    return born
print("You were born in ", yearborn(age))