#Types of Arguments in Python
# 1.Default Arguments
# 2.Keyword Arguments
# 3.Positional Arguments
# 4.Arbitrary Arguments

#using default arguments 
print("Using Default Arguments:")
def fun1(name,age=18):
    print("Name:",name)
    print("Age:",age)
fun1("Alice")  # Age will take the default value of 18

#uding keyword arguments
print("\nUsing Keyword Arguments:")
def fun2(name,age):
    print("Name:",name)
    print("Age:",age)
fun2(age=25,name="Bob")  # Arguments can be passed in any order

#using positional arguments
print("\nUsing Positional Arguments:")
def fun3(name,age):
    print("Name:",name)
    print("Age:",age)   
fun3("Charlie",30)  # Arguments must be passed in the correct order

#using arbitrary arguments
print("\nUsing Arbitrary Arguments:")
def fun4(*args,**kwargs):
    for arg in args:
        print("Arg:",arg)
    for key,value in kwargs.items():
        print(f"{key}: {value}")    
fun4(1,2,3,name="David",age=40)  # Can accept any number of positional and keyword arguments