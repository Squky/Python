
# mr Miyagi trainee

# make a mr miyagi virtual assistant

# as a user I should be able to speak with mr miyagi and get appropriate response s as I go

# Ask for user input and depending on the response, mr Miyagi will respond.
#
# prompt user for input
# Evaluate each input and print the appropriate responses
# Follow these rules:
#
# every time you ask a question --> Mr. Miyagi responde with
    # --> 'questions are wise, but for now. Wax on, and Wax off!'
# every statement/question must start with Sensei, otherwise:
    # --> 'You are smart, but not wise - address me as Sensei please'
# every time you mention 'block' or 'blocking' --> Mr. Miyagi responde with
    # --> 'Remeber, best block, not to be there..'
# anything else you say:
    # --> 'do not lose focus. Wax on. Wax off.'


# Make it so you keep playing until we say: 'Sensei, I am at peace'
    # --> 'Sometimes, what heart know, head forget'

# your_response = input('(MR.Miyagi)... -.-')

#  EXTRA:
#  make it run continuously
#  consider best practices of functions - make this functional

your_response =""


def miyagi_resp_func(your_response):
    if (your_response.endswith("?")):
        print("Questions are wise, but for now. Wax on, and Wax off! ")
    elif(not your_response.capitalize().startswith("Sensei")):
        print("You are smart, but not wise - address me as Sensei please")
    elif (your_response.count("block") > 0 or your_response.count("blocking") > 0):
        print("Remeber, best block, not to be there..")
    else:
        print("Do not lose focus. Wax on. Wax off. ")

while your_response != 'Sensei, I am at peace':
    your_response = input("Say something to Mr. Miyagi: ")
    if(your_response=="Sensei, I am at peace"):
        break
    miyagi_resp_func(your_response)

print('Sometimes, what heart know, head forget')



