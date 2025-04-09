from itertools import*

def f(x,y,z,w): return ((x <= y) <= z) or (not w)

for x1,x2,x3,x4,x5,x6,x7 in product([0,1], repeat=7):
    table = (
        (x1,0,x2,0),
        (1,x3,x4,x5),
        (0,1,x6,x7)
    )
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, t))) for t in table] == [0,0,0]:
                print(*p)