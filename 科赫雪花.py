import  turtle as t
def koch(size,n):
    if n==0:
        t.fd(size)
    else:
        for i in [0,60,-120,60]:
            t.left(i)
            koch(size/3,n-1)
def main():
    t.setup(600,600)
    t.penup()
    t.goto(-200,100)
    t.pensize(2)
    t.pendown()
    level = 4
    koch(400,level)
    t.right(120)
    koch(400,level)
    t.right(120)
    koch(400,level)
    t.hideturtle()
main()

