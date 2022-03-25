from canvas import Canvas
from shapes import Rectangle, Square

#Get the canvas dimensions from the user
canvas_height = int(input("Enter the Canvas height: "))
canvas_width = int(input("Enter the Canvas width: "))

#select the color of the canvas
colors = {'white': (255, 255, 255), 'black': (0, 0, 0)}
canvas_color = input("Enter color for the canvas(white or black): ")

#create the canvas as per the users dimensions
user_canvas = Canvas(canvas_height, canvas_width, color=colors[canvas_color])

while True:
    shape_type = input("What do you like to draw(rectangle or square)? Enter quit to quit ")
    #if user enters a rectangle
    if shape_type.lower() == 'rectangle':
        rec_x = int(input("Enter the x coordinate of the rectangle: "))
        rec_y = int(input("Enter the y coordinate of the rectangle: "))
        rec_height = int(input("Enter the height of the rectangle: "))
        rec_width = int(input("Enter the width of the rectangle: "))
        rec_red = int(input("How much red you want in the rectangle: "))
        rec_blue = int(input("How much blue you want in the rectangle: "))
        rec_green = int(input("How much green you want in the rectangle: "))

        #create the rectangle
        r1 = Rectangle(rec_x, rec_y, rec_height, rec_width, [rec_red, rec_blue, rec_green])
        r1.draw(user_canvas)

    #if user has entered square
    if shape_type.lower() == 'square':
        sq_x = int(input("Enter the x coordinate of the square: "))
        sq_y = int(input("Enter the y coordinate of the square: "))
        sq_side = int(input("Enter the side of the square: "))
        sq_red = int(input("How much red you want in the square: "))
        sq_blue = int(input("How much blue you want in the square: "))
        sq_green = int(input("How much green you want in the square: "))

        #create the rectangle
        s1 = Square(sq_x, sq_y, sq_side, [sq_red, sq_blue, sq_green])
        s1.draw(user_canvas)

    #if user enters quit
    if shape_type.lower() == 'quit':
        break

filename = input("Enter the filename with which you want to save: ")
user_canvas.make(filename)
