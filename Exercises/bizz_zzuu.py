




def upto(num):              ## Function which prints every number from 0 to the given number
    for i in range(0,num+1):
        if (i % 3 == 0 and i % 5 == 0):
            print("bizzuu")
        elif (i % 3 == 0):
            print("bizz")
        elif (i % 5 == 0):
            print("buzz")
        else:
            print(i)

def NegUpTo(num):           ## This function deals with negative inputs from the user
    for i in range(0,num-1,-1): ## it basically works in reverse (counting back up to 0)
        print(i)


def mult(num):
    if (num % 3 == 0 and num % 5 == 0):
        print("bizzuu")
    elif(num==0):
        upto(num)
    elif(num%3==0):
        print("bizz \n")
    elif(num%5==0):
        print("buzz \n")
    elif(num<0):
        NegUpTo(num)

    else:
        upto(num)


num =""

while(num!="penpinapplespen"):
    num = input("Please input a number: ")
    if(num == "penpinapplespen"):
        break

    else:
        try:
            mult(int(num))
        except ValueError:
            print("Sorry thats not a valid number. Try Again. \n")





