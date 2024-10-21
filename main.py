''' Write a program to calculate factorial of a number '''

# Define a function named 'factorial' that calculated the factorual of a number 'n'.
def factorial(n):
    # Check si n is 0.
    if n == 0:
        return 1 # if so returns to 1, as factorial of 0 is 1.
    else:
        # if n it's not 0, multiply n with factorial(n-1).
        return n * factorial(n - 1)

# This variable 'n' asks the user to put a number to compute the factorial.
n = int(input('Input a number to compute the factorial: '))

#prints the factorial of the number by calling the 'factorial' function.
print(factorial(n))