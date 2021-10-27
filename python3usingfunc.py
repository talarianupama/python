def inputInfo() :
    userName = input("user_name")
    userAge = input("Age of the user")
    return (userName , userAge)

def find_Year_When_Age_100(name , age) :
    currentYear = 2021
    age = 100 - int(age)
    currentYear == age
    print( name ,"is going to be 100 by", currentYear)

if __name__ == "__main__":
    userName , userAge = inputInfo()
    print(find_Year_When_Age_100(userName , userAge))

