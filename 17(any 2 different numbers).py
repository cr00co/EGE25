l = [int(i) for i in open('17.txt')]
c = 0
mn = 10**100
for i in range(len(l)-1):
    for j in range(i+1, len(l)):
        if (((l[i] + l[j]) % 18 == 0) + ((l[i] * l[j]) % 18 == 0)) == 1:
            c += 1
            mn = min(mn, l[i] * l[j])
print(c, mn)
