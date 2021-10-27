num1 = int(input("Enter the first number: "));
num2 = int(input("Enter the second number: "));
num3 = int(input("Enter the Third number: "));
def find_Biggest1():  # function definition
    if (num1 > num2):
        if (num1 > num3):
            largest = num1
        else:
            largest = num3
    elif num2 > num3:
            largest = num2

    else:
            largest = num3

    print("Largest number is: ", largest)

find_Biggest1();#function defination