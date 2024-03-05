# def add (a,b):
#     print("addition:",a+b)
#
# a = int(input("enter a no"))
# b = int(input("enter a no"))
# add(a,b)

# def printer(name="user",age=None):
#     print(f"Hello {name},your age is {age}")
#
# printer(name="Ashish")

# def printer(name:str="",age:int=0):
#     if isinstance(name, str) and isinstance(age, int):
#         print(f"Hello {name},your age is {age}")
#     else:
#         print("Type error")
#
# printer(age=20)

def op(a,b):
    c= a+b
    print("ADD:",c)
    d = a-b
    print("SUB:",d)
    e = a*b
    print("MUL:",e)
    f = a/b
    print("DIV:",f)
    t = c+d+e+f
    print("Total sum:",t)

a=int(input("enter the ist number:"))
b=int(input("enter the 2nd number:"))
op(a,b)
