# Function to calculate the minimum number of pizzas required
def min_pizzas_required(N, X):

    total_slices = N * X


    min_pizzas = total_slices // 4
    if total_slices % 4 != 0:
        min_pizzas =  min_pizzas + 1

    return min_pizzas



T = int(input("Enter the number of test cases: "))


for _ in range(T):

    N, X = map(int, input().split())


    print(min_pizzas_required(N, X))
#Q