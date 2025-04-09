from fnmatch import*

for x in range(61, 10**6 + 1, 61):
    if fnmatch(str(x), '5*9?*2?'):
        if (x % 2 != 0) and (x % 19 != 0):
            print(x)