from turtle import*

tracer(0)
left(90)
screensize(2000, 2000)
m = 50

for i in range(4):
    forward(10*m)
    right(90)
up()

for x in range(-20, 20):
    for y in range(-20, 20):
        dot(5, 'red')
        setpos(x * m, y * m)
done()