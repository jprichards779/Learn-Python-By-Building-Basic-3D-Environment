from World4 import *

"""
NESTED ROTATION

This program shows something a bit more meaningful for the field of animation.
We can see wheels rotating in two ways, one about their own horizontal axis, and 
the other about the vertical world axis.
In other words, a rotating object inside a rotating frame. 
The effect is same as pivoting the camera about some central point. 

____Visit World4 module to see how the numerical inputs are scaled to coordinate the motion___

In this demo, more can be adjusted from the app class and makes it easier to play around 
with. 

It's often easy to forget that we are using a 2D template, because the geometry acting 
on the coordiantes is true to the geometry of light being focused onto our retinas. 
"""

class App: 
    # Initialise our world
    M = [[[2,20,-5],[0,0,0], [0,10,0], [0,0,0], [0,0,0]], 
            [[0,0,0], [-10,0,-15]]]
    object_pos = M[0]
    camera_pos = M[1]

    line_colour = (0,0,255)
    cylinder_colour = (0,0,50)
    sheet_colour = (100,100,100)
    def __init__(self):
        self.run = True
    def main(self):
        ob, cam = self.object_pos, self.camera_pos
        wireframe, colours = False, True
        while self.run and abs(ob[2][0]) <220:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    self.run=False
            World4(self).display(wireframe,colours,flatten=False)
            ob[1][0] += 1
            ob[2][0] += 1.5
            ob[4][1] += 1.5
            pygame.display.update() 
        pygame.quit()  
App().main()