f = open('6.txt')
s = [int(i) for i in f]
count = 0
l = []
for i in range(len(s) - 2):
    if (s[i] % 2 != 0 and s[i + 1] % 2 != 0 and s[i + 2] % 2 != 0) and sum([(max(s[i], s[i + 1], s[i + 2])), (min(s[i], s[i + 1], s[i + 2]))]) < 0:
        count += 1
        l.append(sum([s[i], s[i + 1], s[i + 2]]))
print(count, min(l))
