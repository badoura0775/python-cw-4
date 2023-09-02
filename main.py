def my_name():
    print("my name is Badreya")
my_name()

def my_meal(food,drink):
    print(f"I like to eat {food} while drinking {drink}")
my_meal("cookies","coffe")

def cube(number):
    return number**3


def by_three(number):
    if number%3==0:
        return cube(number)
    else:
        return False
three= by_three(6)#cube
print(three)