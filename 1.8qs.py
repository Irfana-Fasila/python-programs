# Dictionary to store calculated factorials
factorial_cache = {}

def factorial(n):
    if n in factorial_cache:
        return factorial_cache[n]
    
    if n == 0 or n == 1:
        factorial_cache[n] = 1
    else:
        factorial_cache[n] = n * factorial(n - 1)
    
    return factorial_cache[n]

def main():
    while True:
        try:
            number = int(input("Enter a non-negative integer to find its factorial (or a negative number to exit): "))
            if number < 0:
                break
            result = factorial(number)
            print(f"The factorial of {number} is {result}.")
            print(f"Factorial cache: {factorial_cache}")
        except ValueError:
            print("Invalid input. Please enter a non-negative integer.")

if __name__ == "__main__":
    main()
