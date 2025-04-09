def f(a, b, c, m):
    if a+b+c >= 150: return m % 2 == 0
    if m == 0: return 0
    h = [f(a+16,b,c,m-1), f(a,b+16,c,m-1), f(a,b,c+16,m-1), f(a+32,b,c,m-1), f(a,b+32,c,m-1), f(a,b,c+32,m-1), f(a*2,b,c,m-1), f(a,b*2,c,m-1), f(a,b,c*2,m-1)]
    return any(h) if m % 2 != 0 else all(h)

print('19)', [s for s in range(1, 67) if f(6, 2*s, 3*s, 1)])
print('20)', [s for s in range(1, 67) if not f(6, 2*s, 3*s, 1) and f(6, 2*s, 3*s, 3)])
print('19)', [s for s in range(1, 67) if not f(6, 2*s, 3*s, 2) and f(6, 2*s, 3*s, 4)])
