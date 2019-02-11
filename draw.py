from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    if(x0 > x1):
        draw_line(x1,y1,x0,y0,screen,color)
        return
    deltaY = y1-y0
    deltaX = x1-x0

    #If line doesn't exist
    if(deltaX ==0 and deltaY == 0):
        return

    #If line is vertical
    if(deltaX == 0 and deltaY != 0):
        for i in range(y0, y1):
            plot(screen, color, x0, i)
        return

    m = deltaY/deltaX

    #Octant 1
    if(m >= 0 and m <= 1):
        x = x0
        y = y0
        a = y1-y0
        b = -(x1-x0)
        d = 2*a + b
        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:
                y += 1
                d += 2*b
            x += 1
            d += 2*a
        return

    #Octant 2
    if(m > 1):
        x = x0
        y = y0
        a = y1-y0
        b = -(x1-x0)
        d = a + 2*b
        while y <= y1:
            plot(screen, color, x, y)
            if d < 0:
                x += 1
                d += 2*a
            y += 1
            d += 2*b
        return

    #Octant 7
    if(m <= -1):
        x = x0
        y = y0
        a = y1-y0
        b = -(x1-x0)
        d = a + 2*b
        while y >= y1:
            plot(screen, color, x, y)
            if d > 0:
                x += 1
                d += 2*a
            y -= 1
            d -= 2*b
        return

    #Octant 8
    if(m < 0 and m > -1):
        x = x0
        y = y0
        a = y1-y0
        b = -(x1-x0)
        d = 2*a + b
        while x <= x1:
            plot(screen, color, x, y)
            if d < 0:
                y -= 1
                d -= 2*b
            x += 1
            d += 2*a
        return
