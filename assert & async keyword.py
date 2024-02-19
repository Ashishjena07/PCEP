import asyncio

# Function to check if a number is positive
def check_positive(number):
    assert number > 0, "Number should be positive"

# Asynchronous function to print a message after a delay
async def print_message():
    await asyncio.sleep(2)
    print("Async message printed after a delay")

def main():
    try:
        # Test assert statement
        check_positive(5)  # This will not raise an AssertionError

        # Uncomment the line below to test assert with a negative number
        # check_positive(-5)  # This will raise an AssertionError

        # Test asynchronous function
        asyncio.run(print_message())

    except AssertionError as e:
        print("Assertion Error:", e)

if __name__ == "__main__":
    main()
