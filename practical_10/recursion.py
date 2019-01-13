"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    """Do...oipk it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)


# TODO: 1. write down what you think the output of this will be,
# Ans: 3
# TODO: 2. use the debugger to step through and see what's actually happening
# Ans: 3
# print(do_it(5))

"""
def do_something(n):
      # Print the squares of positive numbers from n down to 0.
    if n < 0:
        print(n ** 2)
    do_something (n - 1)

do_something(4)
"""

# TODO: 3. write down what you think the output of do_something(4) will be,
# Ans: Infinite
# TODO: 4. use the debugger to step through and see what's actually happening
#  The recursion method process to the -987 count

# TODO: 5. fix do_something() so that it works according to the docstring
def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n < 0:
        return
    print(n ** 2)
    do_something(n - 1)

do_something(4)


