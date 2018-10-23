import time


def make_timer():
    last_called = None

    def elapsed():
        nonlocal last_called
        now = time.time()
        if last_called is None:
            last_called = now
            return None
        result = now - last_called
        last_called = now
        return result

    return elapsed


# demonstrates that the passed function and related calls maintain state from last time it was called

t = make_timer()
print(t())

time.sleep(3)
print(t())

time.sleep(5)
print(t())
