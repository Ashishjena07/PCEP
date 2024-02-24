# num = 124.5264646
# print("%.2f"%num)
# print(round(num,3))
# print(f"{.2}f".format(num))

x = int(input("enter the discount:"))
y = int(input("enter the amount:"))
z = y*(x/100)
print("discount amount:",z)
print("remain amount:",y-z)