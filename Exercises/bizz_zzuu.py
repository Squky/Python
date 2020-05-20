




def upto(num):
    for i in range(0,num+1):
        print(i)

def mult(num):
    if(num==0):
        upto(num)
    elif(num%3==0):
        print("bizz \n")


    elif(num%5==0):
        print("buzz \n")


    else:
        upto(num)


num =0

while(num!="penpinapplespen"):

    mult(int(num))
    num =0
    while (num!="penpinapplespen"):
        if num < 0:
            print("Sorry, whole numbers only  \n")
        try:
            num = int(input("Please input a whole number: "))
        except ValueError:
            print("Sorry thats not a valid number. \n")
        else:
            break





