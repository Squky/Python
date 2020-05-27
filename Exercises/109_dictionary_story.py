
# Dictionary basics :D

#1 - Define a dictionary call story1, it should have the followign keys:
        # 'start', 'middle' and 'end'

#2 - Print the entire dictionary

#3 - Print the type of your dictionary

#4 - Print only the keys

#4 - print only the values

#5 - print the individual values using the keys (individually, lots of printi commands)

#6 - Now let's add a new key:value pair.
    # 'hero': yourSuperHero

story1 = {

        "start" : "This is the start of the dictionary",
        "middle" : "This is the middle of the values",
        "end" : "This is the final value",

    }

print(story1)

print("The type of my dictionary: ",type(story1))
print('\n')

print("The keys of my dictionary: ",story1.keys())
print('\n')
print("The Values of my dictionary: ",story1.values())

print("\n")
print(story1["start"])
print(story1["middle"])
print(story1["end"])

story1["Epilogue"] = "This is the epilogue."

print(story1["Epilogue"])