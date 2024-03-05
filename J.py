for i in range(int(input())):
    x = int(input())
    print("Yes, LUNCH TIME") if x<=3 else print("No, IT IS NOT LUNCH TIME")


def is_lunchtime(x):
    return 11 <= x <= 16

# Input the number of test cases
t = int(input("Enter the number of test cases: "))

# Process each test case
for _ in range(t):
    # Input the current time
    x = int(input("Enter the current time (in hours): "))

    # Check if it's lunchtime and print the result
    if is_lunchtime(x):
        print("YES")
    else:
        print("NO")