# Practice strings
# Welcome to Sparta - exercise
# Version 1 specs - with concatenation
# define a variable name, and assign a string
# prompt the user for input and ask the user for his/her name
# re assign the original variable this this input
# use concatenation to print a welcome message and use methods to format the name/input (remove white spaces)
# Version 2 - with interpolation
# ask the user for a first name, save it in a variable
# ask the user for a last name, save it in a variable
# use interpolation to print the message

# Calculate year of birth
# gather details on age and name
# print something like
# OMG <person>, you are <age> years old so you were born in <year>

var1 = "This is a string"
user_name =input("What is your name? ")

var1 = user_name

welcome_message = "Welcome!Hope you are well " + var1
print(welcome_message.strip())

fName = input("What is your first name? ")
lName = input("..and your last name? ")


print("Hello {} {}".format(fName,lName))
###
import datetime
age = int(input("Please input your age: \n"))
print("OMG ", fName, "you're ", age, "years old so you were born in " ,(2020-age) )