def timetaken(x,y):
    fp=y//2
    r=x-y
    tt=fp+r

    return (tt)

x,y =map(int,input().split())

print(timetaken(x,y))
