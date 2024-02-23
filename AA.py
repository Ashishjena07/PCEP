def sumofcube(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i ** 3
    return sum


n = int(input("Enter the number: "))
result = sumofcube(n)
# print(result)


if  n <= 4 :
    print(result)
else:
    print("Error")  # AA QUESTIONS