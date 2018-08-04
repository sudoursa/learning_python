from math import sqrt


def is_prime(x):
    """
    Takes a given int(x) and determines if it is a prime number
    :param x: integer to perform the operation on
    :return: Returns True if x is prime and False if x is not prime
    """
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def first(iterable):
    """
    Take the iterable object and returns the first object or raises a ValueError if the iterable is empty
    :param iterable: any iterable object
    :return: Returns the first object in the provided iterable
    """
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("Iterable is empty")


def gen123():
    yield 1
    yield 2
    yield 3


def gen246():
    print("About to yield 2")
    yield 2
    print("About to yield 4")
    yield 4
    print("About to yield 6")
    yield 6


def take(count, iterable):
    """
    Take items from the front of an iterable.

    :param count: The maximum number of items to retrieve
    :param iterable: The source series.
    :yields: At most 'count' items from 'iterable.'
    """
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def run_take():
    items = [2, 4, 6, 8, 10]
    for item in take(3, items):
        print(item)


def distinct(iterable):
    """
    Return unique items by eliminating duplicates.

    :param iterable: The source series.
    :yields: Unique elements in order from 'iterable'.
    """
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)


def run_distinct():
    items = [5, 7, 7, 6, 5, 5]
    for item in distinct(items):
        print(item)


def run_pipeline():
    items = [3, 6, 6, 2, 1, 1]
    for item in take(3, distinct(items)):
        print(item)


if __name__ == '__main__':
    # print([x for x in range(101) if is_prime(x)])
    #
    # iterable1 = ['Spring', 'Summer', 'Autumn', 'Winter']
    # iterator = iter(iterable1)
    #
    # print(next(iterator))
    # print(next(iterator))
    # print(next(iterator))
    # print(next(iterator))
    #
    # g = gen123()
    # print(g)
    # print(next(g))
    # print("extra")
    # for x in g:
    #     print(x)
    #
    # h = gen246()
    # next(h)
    # print(next(h))
    # for x in h:
    #     continue

    # run_take()
    # run_distinct()
    run_pipeline()
