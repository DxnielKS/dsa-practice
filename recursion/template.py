"""
A recursive function calls itself with smaller instances of a identically architected problem as the initial problem.

It consists of:

- a base case which is when the recursion stops and the call stack starts to resolve from the bottom up
- the recursive call which calls the same function again with an altered state

"""


# Example 1: factorial function
    
def factorial(number):

    # base case
    if number==1:
        return 1
    
    # calling the function again with one less than the number
    return number * factorial(number-1)