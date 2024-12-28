# Basic Python script demonstrating essential functionalities

# Function to greet the user
def greet_user():
    print("Hello! Welcome to the basic Python test script.")

# Function to demonstrate basic arithmetic operations
def arithmetic_operations():
    print("\nArithmetic Operations")
    # Initialize two numbers for arithmetic
    a = 10
    b = 5
    # Perform and display basic operations
    print(f"Addition: {a} + {b} = {a + b}")
    print(f"Subtraction: {a} - {b} = {a - b}")
    print(f"Multiplication: {a} * {b} = {a * b}")
    print(f"Division: {a} / {b} = {a / b}")

# Function to demonstrate string manipulations
def string_operations():
    print("\nString Operations")
    # Sample string for operations
    text = "Python is fun!"
    print(f"Original text: {text}")
    # Convert the string to uppercase
    print(f"Uppercase: {text.upper()}")
    # Convert the string to lowercase
    print(f"Lowercase: {text.lower()}")
    # Reverse the string using slicing
    print(f"Reversed: {text[::-1]}")

# Function to demonstrate basic list operations
def list_operations():
    print("\nList Operations")
    # Create a sample list
    numbers = [1, 2, 3, 4, 5]
    print(f"Original list: {numbers}")
    # Append a new element to the list
    numbers.append(6)
    print(f"List after appending 6: {numbers}")
    # Remove a specific element from the list
    numbers.remove(2)
    print(f"List after removing 2: {numbers}")
    # Calculate and display the sum of list elements
    print(f"Sum of list: {sum(numbers)}")

# Function to demonstrate file operations
def file_operations():
    print("\nFile Operations")
    # Specify the file name
    filename = "test_file.txt"
    # Open the file in write mode and write content to it
    with open(filename, "w") as file:
        file.write("This is a test file created by the Python script.\n")
    print(f"File '{filename}' created and written to.")
    # Open the file in read mode and read its content
    with open(filename, "r") as file:
        content = file.read()
    print(f"Content of '{filename}':\n{content}")

# Main function to call all other functions
def main():
    greet_user()  # Call the greeting function
    arithmetic_operations()  # Call the arithmetic operations function
    string_operations()  # Call the string operations function
    list_operations()  # Call the list operations function
    file_operations()  # Call the file operations function

# Execute the main function when the script is run directly
if __name__ == "__main__":
    main()
