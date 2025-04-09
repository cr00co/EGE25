# алфавит данной сс
alph = '0123456789ABCDEF'

# значения выражения в 7-ой сс
l = []
# суммы цифр чисел в 7-ой сс
l_sums = []
# иксы, для нахождения наименьшего, который дает сумму цифр выражения в 7-ой - 34
xs = []
# значения выражения в 10-ой сс
l_ten = []

# функция перевода в 7-ую сс
def f(n):
    x = ''
    while n > 0:
        x += str(n % 7)
        n //= 7
    return x[::-1]

# перебор возможных иксов(в данном случае цифры 16-ой сс)
for x in alph:
    z = int(f'9AC{x}36', 16) + int(f'5CD{x}DA', 16)
    l.append(f(z))
    l_ten.append(z)
    xs.append(x)

# суммы цифр чисел(значения выражения) в 7-ой сс
for i in l:
    l_sums.append(sum(int(j) for j in str(i)))

print(l_sums)
print(l_ten)
print(xs)
