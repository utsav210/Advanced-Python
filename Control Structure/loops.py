'''
Challenge/Task:
1. Write a function print_even_numbers that takes a limit as an argument.
2. Use a for loop to print all even numbers up to the limit.
3. Write another function countdown that takes a starting number as an argument.
4. Use a while loop to print a countdown from the starting number to 0.
'''
# Function to print all even numbers up to the limit
def print_even_numbers(limit):
    # Iterate over the range from 0 to limit
    for number in range(0, limit + 1):
        # Check if the number is even
        if number % 2 == 0:
            print(number)

# Function to print a countdown from the starting number to 0
def countdown(start):
    # Continue the loop as long as start is greater than or equal to 0
    while start >= 0:
        print(start)
        start -= 1

if __name__ == "__main__":
    print("Even numbers up to 25:")
    print_even_numbers(25)  # Should print even numbers from 0 to 20

    print("\nCountdown from 5:")
    countdown(5)  # Should print countdown from 5 to 0
