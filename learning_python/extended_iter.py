# import datetime
# import time
#
# t = datetime.datetime.now
#
# i = iter(t, None)
# next(i)
#
# while True:
#     print(i)
#     time.sleep(3)
#     next(i)

# Not sure why the above doesn't work returns the following traceback:

# Traceback (most recent call last):
#   File "/extended_iter.py", line 7, in <module>
#     next(i)
# StopIteration

with open('ending_file.txt', 'rt') as f:
    for line in iter(lambda: f.readline().strip(), 'END'):
        print(line)
