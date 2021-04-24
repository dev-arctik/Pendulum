
import pygame
import math

pygame.init()
win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Simple Pendulum")



m = 7  #suspended mass
l = 200 #length of the rope
a = math.pi/2  #angle of rope w.r.t. the Y axis
av = 0 #angular velocity
aa = 0 # angular acceleration
g = 0.009 #Gravity simulation

x0 = 250
y0 = 50




def draw():
    pygame.draw.circle(win, (250,250,250), (x0,y0), 2)      #Fix circle
    pygame.draw.line(win, (250,0,0), (x0,y0), (x,y), 3)   #Pendulum
    pygame.draw.circle(win, (250,250,0), (int(x),int(y)), m)      #mass
    

    


run = True
while run:
    pygame.time.delay(50)
    win.fill((0,0,0))
    for event in pygame.event.get():
        #print (event)
        if event.type == pygame.QUIT:
            run = False

    #angle calculation
    aa = -m*g*math.sin(a)
    av = av+aa
    av = av*0.99
    a = a+av
    
    
    x = x0 + (l*math.sin(a))
    y = y0 + (l*math.cos(a))

    
    draw()

    
    pygame.display.update()


pygame.quit()
