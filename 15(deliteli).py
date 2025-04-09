def f(x, y, A): return (x < A) or (y < A) or ((x * y) % 4 == 0) or (2*x + 3*y != 100)

print(min(A for A in range(0, 200) if all(f(x,y,A) == 1 for x in range(0, 300) for y in range(0, 300))))