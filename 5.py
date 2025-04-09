def f(n):
    x = ''
    while n > 0:
        x += str(n % 5)
        n //= 5
    return x[::-1]

for n in range(1, 1000):
    R = f(n)
    if (int(R) % 5) % 2 == 0:
        R += f(sum(int(i) for i in R))
    if (int(R) % 5) % 2 != 0:
        R = '21' + R

    if int(R, 5) <= 320:
        print(n)