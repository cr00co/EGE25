def f(x, end, move_n = 0, r = False):
    if x == end and r: 
        return 1
    if x > end or x == 18: 
        return 0
    # Считаем только пути содержащие 6 на пути
    if x == 6: 
        r = True
    # h - ходы, move - номер хода
    h = f(x*2, end, 2, r)
    if move_n != 1:
        h += f(x*3, end, 3, r)
    if move_n != 2:
        h += f(x+4, end, 1, r)
    return h
    
print(f(2, 296))


