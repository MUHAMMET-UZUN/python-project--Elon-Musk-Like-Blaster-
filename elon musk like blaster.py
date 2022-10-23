import turtle, random
import winsound

window = turtle.Screen()
window.bgcolor('black')
window.title('Elon Musk Like Blaster')
window.bgpic('uzay.gif')
window.setup(width=600, height=600)

turtle.register_shape('oyuncu.gif')
turtle.register_shape('dusman.gif')
turtle.register_shape('ates.gif')

oyuncu = turtle.Turtle()
oyuncu.color('yellow');
oyuncu.speed(0)
oyuncu.shape('oyuncu.gif')
oyuncu.setheading(90)
oyuncu.penup()
oyuncu.goto(0,-250)
oyuncuhizi = 20

ates = turtle.Turtle()
ates.color('green');
ates.speed(0)
ates.shape('ates.gif')
ates.setheading(90)
ates.penup()
ates.goto(0,-240)
ateshizi = 10
ates.hideturtle()
ates.turtlesize(1,1)
ateskontrol = True

yaz = turtle.Turtle()
yaz.color('white');
yaz.speed(0)
yaz.penup()
yaz.goto(0,200)
yaz.hideturtle()

def atesgit():
    y = ates.ycor()
    y = y + ateshizi
    ates.sety(y)
    #ateş etme sesi eklenecekl

def sola_git():
    x = oyuncu.xcor()
    x = x - oyuncuhizi
    if x < -300:
        x = -300
    oyuncu.setx(x)

def saga_git():
    x = oyuncu.xcor()
    x = x + oyuncuhizi
    if x > 300:
        x = 300
    oyuncu.setx(x)

def yukari_git():
    y = oyuncu.ycor()
    y = y + oyuncuhizi
    if y > 270:
        y = 270
    oyuncu.sety(y)

def asagi_git():
    y = oyuncu.ycor()
    y = y - oyuncuhizi
    if y < -270:
        y = -270
    oyuncu.sety(y)

def ates_et():
    global ateskontrol
    x = oyuncu.xcor()
    y = oyuncu.ycor() + 20
    ates.goto(x,y)
    ates.showturtle()
    ateskontrol = True

hedefler = []

for i in range(7):
    hedefler.append(turtle.Turtle())

for hedef in hedefler:
    hedef.color('red')
    hedef.speed(0)
    hedef.turtlesize(1,1)
    hedef.shape('dusman.gif')
    hedef.penup()
    hedef.setheading(90)
    x = random.randint(-250,250)
    y = random.randint(-180,260)
    hedef.goto(x,y)


window.listen()
window.onkey(asagi_git,'Down')
window.onkey(yukari_git,'Up')
window.onkey(sola_git,'Left')
window.onkey(saga_git,'Right')
window.onkey(ates_et,'space')

while True:
    if ateskontrol:
        atesgit()
    
    for hedef in hedefler:
        y = hedef.ycor()
        y = y - 2
        hedef.sety(y)
        if hedef.distance(ates) < 20:
            ates.hideturtle()
            hedef.hideturtle()
            hedefler.pop(hedefler.index(hedef))
            #düşman yok olma sesi eklenecek

        if hedef.ycor() < -270 or hedef.distance(oyuncu) < 20:
            yaz.write('YOU LOSER XD!!', align = 'center', font = ('Comic Sans', 24, 'bold'))


    if len(hedefler) == 0:
        yaz.write('Congratulations! YOU WON', align = 'center', font = ('Comic Sans', 24, 'bold'))
