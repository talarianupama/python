a=int(input("please enter first number: "))
b=int(input("please enter second number: "))
c=int(input("please enter third number: "))
if(a > b) and (a > c):
    largest = a
elif(b > a) and (b > c):
    largest = b
else:
    largest = c
print("the largest number is",largest)