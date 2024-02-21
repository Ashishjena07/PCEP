import timeit
from memory_profiler import profile

@profile
def process_data(data):
    processed_data = [item.upper() for item in data]
    return processed_data

@profile
def main():
    data = ["item " + str(i) for i in range(100)]

    execution_time = timeit.timeit(lambda: process_data(data), number=1)
    print(f"Execution time: {execution_time} seconds")

if __name__ == '__main__':
    main()