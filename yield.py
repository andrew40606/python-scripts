def my_range(x):
    i = 0
    while i < x:
        yield i
        i += 1

print(my_range(5))