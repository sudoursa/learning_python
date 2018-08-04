""" A module for demonstrating exceptions."""
import sys
from math import log


def convert(s):
    """Convert to an integer and handle exceptions. While reusing the captured error and re-raising it"""
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("Conversion error: {}"
              .format(str(e)),
              file=sys.stderr)
        raise


def string_log(s):
    """More pythonic, converts the error code into a true exception, really we should be using those errors normally"""
    v = convert(s)
    return log(v)


def convert_v1(s):
    """Convert to an integer."""
    x = int(s)
    return x


def convert_v2(s):
    """Convert to an integer. Handle value errors. Fixed string issues."""
    try:
        x = int(s)
        print("Conversion succeeded! x =", x)
    except ValueError:
        print("Conversion failed!")
        x = -1
    return x


def convert_v3(s):
    """Convert to an integer. Handle value and type errors. Resolves other collection issues ex: list"""
    try:
        x = int(s)
        print("Conversion succeeded! x =", x)
    except ValueError:
        print("Conversion failed!")
        x = -1
    except TypeError:
        print("Conversion failed!")
        x = -1
    return x


def convert_v4(s):
    """Convert to an integer and handle exceptions. with print output"""
    x = -1
    try:
        x = int(s)
        print("Conversion succeeded! x =", x)
    except (ValueError, TypeError):
        print("Conversion failed!")
    return x


def convert_v5(s):
    """Convert to an integer and handle exceptions. Without printed output"""
    x = -1
    try:
        x = int(s)
    except (ValueError, TypeError):
        pass
    return x


def convert_v6(s):
    """Convert to an integer and handle exceptions. Without printed output or variables"""
    try:
        return int(s)
    except (ValueError, TypeError):
        return -1


def convert_v7(s):
    """Convert to an integer and handle exceptions. While reusing the captured error for standard out and an errcode"""
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("Conversion error: {}"
              .format(str(e)),
              file=sys.stderr)
        return -1