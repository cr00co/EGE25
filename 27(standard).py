clustersA = [[], []]
clustersB = [[], [], []]

# Если есть аномалии, то эти области pass
for line in open('fileA.txt'):
    x, y = [float(k) for k in line.replace(',', '.').split()]
    if y > 5:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])

for line in open('fileB.txt'):
    x, y = [float(k) for k in line.replace(',', '.').split()]
    if y < -2:
        clustersB[0].append([x, y])
    elif x > 3:
        clustersB[1].append([x, y])
    else:
        clustersB[2].append([x, y])

def d(A, B):
    x1, y1 = A
    x2, y2 = B
    return max(abs(x2 - x1), abs(y2 - y1))

def center(cl):
    m = []
    for p in cl:
        sm = sum(d(p, p1) for p1 in cl)
        m.append([sm, p])
    return min(m)[1]

centersA = [center(cl) for cl in clustersA]
centersB = [center(cl) for cl in clustersB]
pxA = sum(x for x, y in centersA) / 2 * 100000
pyA = sum(y for x, y in centersA) / 2 * 100000
pxB = sum(x for x, y in centersB) / 3 * 100000
pyB = sum(y for x, y in centersB) / 3 * 100000

print(int(pxA), int(pyA))
print(int(pxB), int(pyB))