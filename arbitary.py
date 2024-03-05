# def printer(*args):
#     print(args)
#
# printer(1,2,3,4,5,"hello",['list1','list2'])

def printer(*args,**kargs):
    print(f"args: {args}\nkwargs: {kargs}")

printer(1,2,3,4,5.3,name="Ashish",age=20,dept="CSE")