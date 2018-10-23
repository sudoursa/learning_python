# demonstrate that local functions do not modify global variables

message = 'global'

def enclosing():
    message = 'enclosing'

    def local():
        message = 'local'

    print('enclosing message:', message)
    local()
    print('enclosing message:', message)


print('global message:', message)
enclosing()
print('global message:', message)


# demonstrate that the global variable can be changed when using the global keyword

def enclosingv2():
    message = 'enclosing'

    def local():
        global message
        message = 'local'

    print('enclosing message:', message)
    local()
    print('enclosing message:', message)


print('global message:', message)
enclosingv2()
print('global message:', message)


# demonstrate that the enclosing variable can be changed with the nonlocal keyword

message = 'global'  # resetting global message because v2 edits it


def enclosingv3():
    message = 'enclosing'

    def local():
        nonlocal message
        message = 'local'

    print('enclosing message:', message)
    local()
    print('enclosing message:', message)


print('global message:', message)
enclosingv3()
print('global message:', message)
