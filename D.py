def is_cycle(a, b):
    for i in range(len(a)):
        if a == b:
            return i
        i += 1
        a = a[1:] + a[0]
    return -1
a = input()
b = input()
print(is_cycle(a, b))
