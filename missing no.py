# Read the list of integers
input_numbers = input("enter a no") .split()
numbers = [int(num) for num in input_numbers]#conver the data type into string type to  integer type
originalsum = sum(range(1,101))
sumoftotalnoofinput = sum(numbers)
missedno = originalsum - sumoftotalnoofinput
print(missedno)