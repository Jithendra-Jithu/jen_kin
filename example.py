# example.py

# Function to greet the user
def greet(name):
    return f"Hello, {name}!"

# Main function to execute the program
if __name__ == "__main__":
    user_name = input("Enter your name: ")
    greeting_message = greet(user_name)
    print(greeting_message)
