num1 = int(input("the first number:"))
num2 = int(input("the second number:"))
num3 = int(input("the third number:"))
def func1(*mylist):
    for num in mylist:
        print(num)

    if(num1 > num2):
        if(num1 > num3):
            largest = num1
        else:
            largest = num3
    elif(num2 > num3):
        largest = num2
    else:
        largest = num3
    print("the largest number is" , largest)

func1()