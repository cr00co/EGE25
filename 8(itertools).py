from itertools import*

w = 'РАСЧЕСКА'

c = 0
s = set()
for j in range(3, 7):
    for i in product(w, repeat=j):
        x = ''.join(i)
        s.add(x)
print(len(s))
    