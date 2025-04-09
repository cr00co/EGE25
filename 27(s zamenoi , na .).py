# Смена "," на "." в файлах
# A
with open('27_A_2__4uxf2.txt', 'r') as file:
    content = file.read()

updated_content = content.replace(',', '.')

with open('27_A_2__4uxf2.txt', 'w') as file:
    file.write(updated_content)
# B
with open('27_B_2__4uxf3.txt', 'r') as file:
    content = file.read()

updated_content = content.replace(',', '.')

with open('27_B_2__4uxf3.txt', 'w') as file:
    file.write(updated_content)

# Основной код
clustersA = [[], [], [], [], []]
clustersB = [[], [], []]

for string in open('27_A_2__4uxf2.txt'):
    x, y = [float(k) for k in string.split()]
    if x < -34:
        clustersA[0].append([x, y])
    if -19 > x > -34:
        clustersA[1].append([x, y])
    if  0 > x > -19:
        clustersA[2].append([x, y])
    if y < 0 and x > 0:
        clustersA[3].append([x, y])
    if x > 0 and y > 0:
        clustersA[4].append([x, y])
    
for string in open('27_B_2__4uxf3.txt'):
    x, y = [float(k) for k in string.split()]
    if x < -30:
        clustersB[0].append([x, y])
    if y > -15:
        clustersB[1].append([x, y])
    if x > 20:
        clustersB[2].append([x, y])

def d(A, B):
    x1, y1 = A
    x2, y2 = B
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def center(cl):
    m = []
    for t in cl:
        sm = sum(d(t, p) for p in cl)
        m.append([sm, t])
    return min(m)[1]

centersA = [center(cl) for cl in clustersA]
centersB = [center(cl) for cl in clustersB]
apx = sum(x for x, y in centersA) / 5 * 1000
apy = sum(y for x, y in centersA) / 5 * 1000
bpx = sum(x for x, y in centersB) / 3 * 1000
bpy = sum(y for x, y in centersB) / 3 * 1000

print(int(apx), int(apy))
print('=====')
print(int(bpx), int(bpy))