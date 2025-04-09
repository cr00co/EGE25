for i in range(100812, 100924):
    ds = set() # Делители числа
    for d in range(1, int(i**0.5)+1):
        if i % d == 0:
            ds.add(d)
            ds.add(i//d)
        
        if len(ds) > 6:
            break
    if len(ds) == 6:
        ds = sorted(list(ds))
        print(ds[-2], ds[-1])