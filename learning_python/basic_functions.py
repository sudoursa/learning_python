def hypervolume(*args):
    print(args)
    print(type(args))


def hypervolumev2(*lengths):
    i = iter(lengths)
    v = next(i)
    for length in i:
        v *= length
    return v
    # has the problem of exposing details when called wtih zero arguments


def hypervolumev3(length, *lengths):
    v = length
    for item in lengths:
        v *= item
    return v
    # this make the function require 1 argument and allows a more defining error message


def tag(name, **kwargs):
    print(name)
    print(kwargs)
    print(type(kwargs))


def tagv2(name, **attributes):
    result = '<' + name
    for key, value in attributes.items():
        result += ' {k}="{v}"'.format(k=key, v=str(value))
    result += '>'
    return result
