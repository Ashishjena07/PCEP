# Generator function to generate squares of numbers
def generate_squares(n):
    for i in range(1, n + 1):
        yield i * i

# Main function to demonstrate generator usage
def main():
    n = int(input("Enter the number of squares to generate: "))
    print("Generating squares of numbers from 1 to", n)

    # Using the generator to iterate over generated squares
    for square in generate_squares(n):
        print(square)

if __name__ == "__main__":
    main()
