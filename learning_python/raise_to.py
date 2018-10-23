# function factories


def raise_to(exp):
    def raise_to_exp(x):
        return pow(x, exp)
    return raise_to_exp


# the above function creates a closure
square = raise_to(2)
print(square.__closure__)

# when an object equals a function it becomes callable just like any other function

print(square(5))
print(square(9))
print(square(1234))

# this works the same when the function is defined otherwise

cube = raise_to(3)
print(cube(3))
print(cube(10))
print(cube(23))
