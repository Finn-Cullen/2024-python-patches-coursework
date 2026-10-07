from graphix import Point,Rectangle,Polygon,Text,Window,time

# core variables : basically the most important variables for the program
size = int(input("how big should the pattern be? "))
X_dimention = 500 # screen X size
Y_dimention = 500 # screen Y size
spacing = ((X_dimention / size)/5) # size of a patch shape (each patch is made of smaller shapes)
# storing variables : stores data that will be used everywhere
win = Window("window", X_dimention,Y_dimention)
col_check = ["red","green","blue","magenta","orange","purple"]
patch_index = 0
A = 3 # A is just a placeholder so that it can be overwritten by the patches later on
patches = [A]*(size*size)

decide = True
while(decide):  # gets the colours and checks they are valid
    print("Valid colours are red, green, blue, magenta,orange and purple")
    colours = [input("whats your colours? ") ,input("whats your colours? ") ,input("whats your colours? ") ]
    if(colours[0] != colours[1] and colours[0] != colours[2] and colours[1] != colours[2]):
        check = 0
        for I in range(len(colours)):
            for II in range(len(col_check)):
                if(col_check[II] == colours[I]):
                    check += 1
        if(check > 2):
            decide = False
        else:
            print("sorry, something must have gone wrong")

# functions
def draw_patch_1(X,Y,colour): # takes input for its starting position and colour
    point_A = Point(int(X),int(Y))
    point_B = Point(int(X + spacing * 5),int(Y + spacing * 5)) # sets the points
    rect = Rectangle(point_A,point_B) # draws rectangle
    rect.fill_colour = colour
    rect.outline_colour = colour # fills colour
    patches[patch_index] = [rect]
    rect.draw(win)

def draw_patch_3(start_X,start_Y,colour): # takes input for its starting position and colour
    patch_array = [start_X]*5*6
    patch_array_index = 0
    for Y in range(5):
        for X in range(6):
            point_A = Point(int(start_X + (X * spacing + spacing / 2)),int(start_Y + (Y * spacing + spacing))) # bottom point
            point_B = Point(int(start_X + (X * spacing)),int(start_Y + (Y * spacing))) # top left
            point_C = Point(int(start_X + (X * spacing + spacing)),int(start_Y + (Y * spacing))) # bottom top
            if(Y % 2 == 1): # offsets odd rows so to make the pattern
                point_A.move(-int(spacing/2),0)
                point_C.move(-int(spacing/2),0)
                if(point_B.x > start_X):
                    point_B.move(-int(spacing/2),0)
                if(point_C.x > start_X + spacing * 5):
                    point_C.move(-int(spacing/2),0)

            tri = Polygon(points=[point_A,point_B,point_C]) # makes triangle
            tri.fill_colour = colour
            patch_array[patch_array_index] = tri
            patch_array_index += 1
            if(point_C.x - 1<= start_X + spacing * 5): # stops it from drawing triangles outside the patch
                tri.draw(win) # the -1 gives it leeway at different sizes as int() can prove to be strange at times
    patches[patch_index] = patch_array

def draw_patch_2(start_X,start_Y,colour): # takes input for its starting position and colour
    patch_array = [start_X]*5*5*2
    patch_array_index = 0
    for X in range(5):
        for Y in range(5): # unfortunatly python/graphix doesnt like any numbers that are the product of a calculation, thus i have to use int() on everything or else it breaks
            point_A = Point(int(start_X + (X * spacing + spacing)),int(start_Y + (Y * spacing + spacing)))
            point_B = Point(int(start_X + (X * spacing)),int(start_Y + (Y * spacing))) # points are made for drawing
            rect = Rectangle(point_A,point_B)
            text_point = Point(int(start_X + (X * spacing + spacing / 2)),int(start_Y + (Y * spacing + spacing / 2)))
            text = Text(text_point,"hi!")
            rect.outline_colour = colour
            text.fill_colour = colour # sets colour
            if(int(10 * (5/size)) <= 4):
                text.size = 5 # 4 is the smallest allowed size of text
            else:
                text.size = int(10 * (5/size)) # scales text with patch size
            patch_array[patch_array_index] = text
            patch_array_index += 1
            patch_array[patch_array_index] = rect
            patch_array_index += 1
            text.draw(win)
            rect.draw(win)
    patches[patch_index] = patch_array

def make_patches(): # patch_check, 1=clear,2=P,3=F
    for Y in range(size):
        colour_check = 1 # colour check controls what colour goes around the X
        for X in range(size):
            patch_check = 0 # patch check controls what patch gets drawn
            chosen_colour = "" # holds the colour to be used
            if(colour_check == -1): # fills in the rest of the pattern
                chosen_colour = colours[1]
            if(colour_check == 1 or Y == (size-1) / 2):
                chosen_colour = colours[2]
            if(X == Y or X + Y == size-1): # draws the X
                colour_check = -colour_check
                chosen_colour = colours[0]
                patch_check = 2 # Hi squares
            if(X == 0 or Y == 0 or X == size-1 or Y == size-1):
                patch_check = 1 # blank square
            elif(patch_check != 2):
                patch_check = 3 # triangles

            if(patch_check == 1):
                draw_patch_1(X*spacing*5,Y*spacing*5,chosen_colour)
            if(patch_check == 2):
                draw_patch_2(X*spacing*5,Y*spacing*5,chosen_colour)
            if(patch_check == 3):
                draw_patch_3(X*spacing*5,Y*spacing*5,chosen_colour)
            global patch_index
            patch_index += 1

def undraw_patch(mouse_X,mouse_Y):
    for I in range(len(patches[mouse_X + (mouse_Y * size)])):
        patches[mouse_X + (mouse_Y * size)][I].undraw()
    patches[mouse_X + (mouse_Y * size)] = [Point(0,0)]

def swap_colour(mouse_X,mouse_Y,inp_col):
    if(len(patches[mouse_X + (mouse_Y * size)]) < 35):
        for I in range(len(patches[mouse_X + (mouse_Y * size)])):
            patches[mouse_X + (mouse_Y * size)][I].fill_colour = colours[inp_col]
            patches[mouse_X + (mouse_Y * size)][I].outline_colour = colours[inp_col]
    else: # exception needed for HI! squares
        for I in range(len(patches[mouse_X + (mouse_Y * size)])):
            patches[mouse_X + (mouse_Y * size)][I].outline_colour = colours[inp_col]

def swap_patch(mouse_X,mouse_Y,inp_patch,chosen_colour):
    undraw_patch(mouse_X,mouse_Y)
    global patch_index
    patch_index = mouse_X + (mouse_Y * size)
    if(inp_patch == 1):
        draw_patch_1(mouse_X*spacing*5,mouse_Y*spacing*5,chosen_colour)
    if(inp_patch == 2):
        draw_patch_2(mouse_X*spacing*5,mouse_Y*spacing*5,chosen_colour)
    if(inp_patch == 3):
        draw_patch_3(mouse_X*spacing*5,mouse_Y*spacing*5,chosen_colour)

def move_patch(mouse_X,mouse_Y,move_vect):
    new_pos_X = mouse_X + move_vect[0]
    new_pos_Y = mouse_Y + move_vect[1]
    if(new_pos_X > -1 and new_pos_Y > -1 and new_pos_Y < size and new_pos_X < size and patches[mouse_X + move_vect[0] + ((mouse_Y + move_vect[1]) * size)][0].is_drawn() == False): # ensures it cant go out of bounds
        for timer in range(int(spacing*5)): # animates movement
            time.sleep(0.01)
            for I in range(len(patches[mouse_X + (mouse_Y * size)])):
                patches[mouse_X + (mouse_Y * size)][I].move(move_vect[0],move_vect[1])
        pA = patches[mouse_X + (mouse_Y * size)]
        pB = patches[mouse_X + move_vect[0] + ((mouse_Y + move_vect[1]) * size)] # swaps position in the array
        patches[mouse_X + (mouse_Y * size)] = pB
        patches[mouse_X + move_vect[0] + ((mouse_Y + move_vect[1]) * size)] = pA

make_patches() # makes patches and such

# main loop
while(True):
    print("list of commands : ")
    print("LMB : select patch")
    print("- : deselect patch") # "minus"
    print("WASD : move selected patch") # "wasd"
    print("up/down : scroll through colours") # "Up Down"
    print("left/right : scroll through patches") # "Left Right"
    print("P : erases patch") # "p"
    print("esc : closes program") # "Escape"
    
    point = win.get_mouse()
    mouse_X = int(point.x // (spacing * 5)) # gets mouse coords
    mouse_Y = int(point.y // (spacing * 5))

    point_a = Point(int(mouse_X * spacing*5),int(mouse_Y * spacing*5))
    point_b = Point(int(spacing*5) + int(mouse_X * spacing*5),int(spacing*5) + int(mouse_Y * spacing*5))

    outline = Rectangle(point_b,point_a) # makes outline
    outline.draw(win)
    outline.outline_width = 3


    key_str = ""

    # sets patch and colour
    for I in range(len(colours)):
        if(patches[mouse_X + (mouse_Y * size)][0].fill_colour == colours[I]): # grabs colour
            colour_save = I
    if(len(patches[mouse_X + (mouse_Y * size)]) == 1):
        patch_save = 1
    elif(len(patches[mouse_X + (mouse_Y * size)]) > 35): # pacth is detected via array size
        patch_save = 3
    else:
        patch_save = 2
    # sets patch and colour

    while(key_str != "minus"):
        key_str = win.check_key()

        if(key_str == "Escape"): # close window
            win.close()

        # movement
        if(key_str == "w"):
            move_patch(mouse_X,mouse_Y,[0,-1])
        if(key_str == "a"):
            move_patch(mouse_X,mouse_Y,[-1,0])
        if(key_str == "s"):
            move_patch(mouse_X,mouse_Y,[0,1])
        if(key_str == "d"):
            move_patch(mouse_X,mouse_Y,[1,0])
        # movement

        # undraw
        if(key_str == "p"):
            undraw_patch(mouse_X,mouse_Y)
        # undraw

        # colour change
        if(key_str == "Up"):
            colour_save += 1
            if(colour_save > 2):
                colour_save = 0
            swap_colour(mouse_X,mouse_Y,colour_save)
        if(key_str == "Down"):
            colour_save -= 1
            if(colour_save < 0):
                colour_save = 2
            swap_colour(mouse_X,mouse_Y,colour_save)
        # colour change

        # patch change
        if(key_str == "Left"):
            patch_save -= 1
            if(patch_save < 1):
                patch_save = 3
            swap_patch(mouse_X,mouse_Y,patch_save,colours[colour_save])
            outline.undraw()
            outline.draw(win)
        if(key_str == "Right"):
            patch_save += 1
            if(patch_save > 3):
                patch_save = 1
            swap_patch(mouse_X,mouse_Y,patch_save,colours[colour_save])
            outline.undraw()
            outline.draw(win)
        # patch change

    outline.undraw() # undraws outline when the patch is deselected

#for I in range(len(patches[mouse_X + (mouse_Y * size)])):