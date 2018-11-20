values = [x / (x -y)
          for x in range(100)
          if x > 50
          for y in range(100)
          if x - y != 0]

# is the same as:

values = []
for x in range(100):
    if x > 50:
        for y in range(100):
            if x - y != 0:
                values.append(x / (x - y))
