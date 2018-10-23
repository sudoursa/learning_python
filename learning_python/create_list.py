def check_non_negative(index):
    def validator(f):
        def wrap(*args):
            if args[index] < 0:
                raise ValueError(
                    'Argument {} must be non-negative.'.format(index))
            return f(*args)
        return wrap
    return validator


# the below example decorator is actually a call to a function that returns a decorator i.e. validator()
# remember that a decorator is a callable that takes a callable and returns a callable

@check_non_negative(1)
def create_list(value, size):
    return [value] * size


A = create_list('a', 3)
print(A)
B = create_list('b', -6)
print(B)
