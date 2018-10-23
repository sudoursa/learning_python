import functools


# this example shows that the __name__ and __doc__ values are replace when using a decorator

def noop(f):
    def noop_wrapper():
        return f()

    return noop_wrapper


@noop
def hello():
    "Print a well-known message"
    print("Hello, world!")


print(hello.__name__)
print(hello.__doc__)
help(hello)
print('-' * 10)


# this example shows how to fix that issue


def noopv2(f):
    def noop_wrapper():
        return f()

    noop_wrapper.__name__ = f.__name__
    noop_wrapper.__doc__ = f.__doc__
    return noop_wrapper


@noopv2
def hellov2():
    "Print a well-known message"
    print("Hello, world!")


print(hellov2.__name__)
print(hellov2.__doc__)
help(hellov2)
print('-' * 10)


# there is a tool to handle this already import statement at top for functools


def noopv3(f):
    @functools.wraps(f)
    def noop_wrapper():
        return f()

    return noop_wrapper


@noopv3
def hellov3():
    "Print a well-known message"
    print("Hello, world!")


print(hellov3.__name__)
print(hellov3.__doc__)
help(hellov3)
print('-' * 10)
