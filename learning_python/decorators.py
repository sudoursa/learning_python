# replace, enhance, or modify existing functions
# does not change the original function definition
# calling code does not need to change
# decorators mechanism uses the modified function's original name


# example
# the following is not using a decorator, which is not scalable or easily maintained

def vegetable():
    return ascii('blomkål')


def animal():
    return ascii('bjørn')


def mineral():
    return ascii('stål')


# the following using a decorator to accomplish the same thing


def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)

    return wrap


@escape_unicode
def vegetablev2():
    return 'blomkål'


@escape_unicode
def animalv2():
    return 'bjørn'


@escape_unicode
def mineralv2():
    return 'stål'


print(vegetable())
print(animal())
print(mineral())
print('using decorators')
print(vegetablev2())
print(animalv2())
print(mineralv2())


class CallCount:
    def __init__(self, f):
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.f(*args, **kwargs)


@CallCount
def hello(name):
    print('Hello, {}'.format(name))


hello('Fred')
hello('Wilma')
hello('Betty')
hello('Barney')
print(hello.count)


class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args, **kwargs)

        return wrap


tracer = Trace()


@tracer
def rotate_list(l):
    return l[1:] + [l[0]]


l = [1, 2, 3]
l = rotate_list(l)
print(l)
l = rotate_list(l)
print(l)
l = rotate_list(l)
print(l)
tracer.enabled = False
l = rotate_list(l)
print(l)
l = rotate_list(l)
print(l)

# multiple decorator example

tracer.enabled = True  # resetting tracer value


@tracer
@escape_unicode
def norwegian_island_maker(name):
    return name + 'øy'


print(norwegian_island_maker('Llama'))
print(norwegian_island_maker('Python'))
print(norwegian_island_maker('Troll'))

tracer.enabled = False

print(norwegian_island_maker('Tracerless'))


class IslandMaker:
    def __init__(self, suffix):
        self.suffix = suffix

    @tracer
    def make_island(self, name):
        return name + self.suffix


tracer.enabled = True  # resetting tracer value

im = IslandMaker(' Island')
print(im.make_island('Python'))
print(im.make_island('Llama'))
