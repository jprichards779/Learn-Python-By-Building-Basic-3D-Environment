from World2 import *

"""
This program shows wheels which rotate about their own axis and 
are moving in the World frame's x-direction.
The world is itself oriented with respect to the viewer/camera. 


____Visit World2 module to see how the inputs are scaled to coordinate the motion___

Notice how the program speeds up after a few seconds.
This is because previous coordinates are being revisited, as we would expect with 
periodic motion and rotations. The program stores visitted data in dictionaries
so that calculations aren't unnecessarily repeated. 

The initial slowing arises from the need to check if a data point exists or not to avoid 
overwriting. This is might be overkill following recent modifications I made. 
The idea was to stop the globally scoped dictionaries overwriting and/or getting too large 
becuase this visibly slowed the frame rate, defeating their whole purpose. 
"""


class App: 
    M = [[[0,10,1],[-90,0,0], [70,0,0], [0,0,0], [0,0,0]], 
            [[0,0,0], [0,0,10]]]
    object_pos = M[0]
    camera_pos = M[1]
    line_colour=(0,0,255)
    def __init__(self):
        self.run = True
    def main(self):
        ob, cam = self.object_pos, self.camera_pos
        wireframe, colours = False, True
        while self.run and ob[1][0] < 60:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    self.run=False
            World2(self).display(wireframe,colours,flatten=False)
            ob[1][0] += 2
            ob[4][1] += 2
            pygame.display.update() 
        pygame.quit()  
App().main()











