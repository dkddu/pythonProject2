import turtle,time
def drawgap():
    turtle.penup()
    turtle.fd(5)
def drawline(draw):
    drawgap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    turtle.right(90)
def drawdigits(digits):
    turtle.pencolor()
    drawline(True) if digits in [2,3,4,5,6,8,9] else drawline(False)
    drawline(True) if digits in [0,1,3,4,5,6,7,8,9] else drawline(False)
    drawline(True) if digits in [0, 2, 3, 5, 6, 8] else drawline(False)
    drawline(True) if digits in [0, 2, 5, 6, 8] else drawline(False)
    turtle.left(90)
    drawline(True) if digits in [0, 4, 5, 6, 8, 9] else drawline(False)
    drawline(True) if digits in [0, 2, 3, 5, 6,7, 8, 9] else drawline(False)
    drawline(True) if digits in [0,1, 2, 3, 4, 7, 8, 9] else drawline(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def drawdate(date):
    turtle.pencolor("red")
    for i in date:
        if i=="-":
            turtle.write('时',font=("Arial",18,"normal"))
            turtle.pencolor("green")
        elif i=="=":
            turtle.write('分', font=("Arial", 18, "normal"))
            turtle.pencolor("blue")
        elif i=="+":
            turtle.write("秒",font=("Arial",18,"normal"))
        else:
            drawdigits(eval(i))

def main():
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.fd(-300)
    drawdate(time.strftime("%H-%M=%S+",time.gmtime()))
main()