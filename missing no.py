# Read the list of integers
# input_numbers = input("enter a no") .split()
# numbers = [int(num) for num in input_numbers]#conver the data type into string type to  integer type
# originalsum = sum(range(1,101))
# sumoftotalnoofinput = sum(numbers)
# missedno = originalsum - sumoftotalnoofinput
# print(missedno)

list_1 = [int(x)for x in input().split()]

list_data = (map(int,input().split()))
print(list_data)

for i in range(1,101):
    if i not in list_1:
        print(i)

n = 100
total = n*(n+1)//2
list_2 = sum(list_1)
print(total-list_2)
