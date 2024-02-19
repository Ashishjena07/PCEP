def process_data(data):
    for item in data:
        # Check if item meets some condition
        if condition_met(item):
            # Perform some action
            process(item)
        else:
            # Placeholder for when condition is not met
            pass

def condition_met(item):
    # Dummy condition for demonstration
    return item > 5

def process(item):
    # Dummy process for demonstration
    print(f"Processing item: {item}")

# Example usage
data = [1, 6, 3, 8, 2]
process_data(data)
