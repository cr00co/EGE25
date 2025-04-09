# c1 - счетчик ходов +1, с2 - счетчик ходов *2
def f(x, end, c1, c2):
    if x == end: return 1
    if x > end: return 0
    s = 0
    if c1 < 3:
        s += f(x + 1, end, c1 + 1, 0)
    if c2 < 3:
        s += f(x*2, end, 0, c2 + 1)
    return s
print(f(5, 299, 0, 0))
