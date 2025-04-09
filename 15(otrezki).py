for x in [k * 0.25 for k in range(-10000, 10000)]:
    P = 55 <= x <= 100
    Q = 66 <= x <= 129
    A = 0
    f = P <= ((Q and (not A)) <= (not P))
    if f != 1:
        print(x)