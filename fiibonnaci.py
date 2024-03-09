# def fibonacci_of(n):
#     if n in {0, 1}:
#         return n
#     return fibonacci_of(n - 1) + fibonacci_of(n - 2)
# for n in range(15):
#     print(fibonacci_of(n), end=" ")

def fibonacci_of(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0,1]
    else:
        fib_list = fibonacci_of(n-1)
        fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list
number_of_terms = int(input("Enter the number: "))
fibonacci_series = fibonacci_of(number_of_terms-1)
print(f"Fibonacci series upto {number_of_terms} terms: {fibonacci_series}")