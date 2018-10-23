store = []


def sort_by_last_letter(strings):
    def last_letter(s):
        return s[-1]

    store.append(last_letter)
    print(last_letter)
    return sorted(strings, key=last_letter)


g = 'global'


def outer(p='param'):
    l = 'local'

    def inner():
        print(g, p, l)

    inner()


# closures occur by remembering the objects that were in use by a local function

def enclosing():
    x = 'closed over'

    def local_func():
        print(x)

    return local_func


# not sure why this doesn't actually work
lf = enclosing()
lf()
