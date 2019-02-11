from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

# #Vertical line
# draw_line(0,0,0,500,screen,color)
#
# #Horizontal line
# draw_line(0,0,500,0,screen,color)
#
# #Line with slope 1
# draw_line(0,0,500,500,screen,color)
#
# #Line with slope -1
# draw_line(0,500,500,0,screen,color)
#
# #Octant 1 line
# draw_line(0,0,500,300,screen,color)
#
# #Octant 2 line
# draw_line(0,0,250,500,screen,color)
#
# # #Octant 7 line
# draw_line(0,500,475,0,screen,color)
#
# #Octant 8 line
# draw_line(0,500,500,250,screen,color)

for i in range(0,500):
    x = 50+i
    if(x % 25 == 0):
        draw_line(0,0,x,500,screen,color)


display(screen)
save_extension(screen, 'img.png')
