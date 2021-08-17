# import turtle
# t = turtle.Turtle()
# shapeInput = input('circle and square or triangle, what is your favorite shape?:')
# colorInput = input('What color will it be? :')
# t.fillcolor(colorInput)
# t.begin_fill()
# if shapeInput == 'circle':
#     r=float(input("radius :"))
#     t.circle(r)
# elif shapeInput == 'square':
#     a = float(input("side length :"))
#     for x in range(4):
#         t.fd(a)
#         t.rt(90)
# elif shapeInput == 'triangle' :
#     l = float(input("side length :"))
#     for x in range(3):
#         t.fd(l)
#         t.lt(120)
# else:
#     print("Sorry, I don't have this shape :(")
# t.end_fill()
# wn = turtle.Screen()
# wn.bgcolor("black")
# wn.title("Your shape")
# turtle.done()