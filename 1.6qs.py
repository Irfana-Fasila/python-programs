# Function to reverse the digits of a number
def reverse_number(n):
    return int(str(n)[::-1])
def is_palindrome(n):
    return str(n) == str(n)[::-1]
def make_palindrome(n):
    while not is_palindrome(n):
        reversed_n = reverse_number(n)
        n += reversed_n
        print(f"Intermediate sum: {n}")
    return n

number = int(input("Enter a number: "))
palindrome = make_palindrome(number)
print(f"The palindrome is: {palindrome}")
