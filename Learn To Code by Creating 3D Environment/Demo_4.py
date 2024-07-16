from World3 import * 

"""
This program shows the sheet class which has had it's vertices 
scaled to form a 3D parabola. It's possible to fluctuate the constant used to scale 
this. Similarly, wave like behaviour can be achieved with some careful thought. 


____Visit World3 module to see how the inputs are scaled to coordinate the motion___

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
    M = [[[0,15,-8],[0,0,0], [0,0,0], [0,0,0], [0,0,0]], 
            [[0,0,0], [0,0,-15]]]
    object_pos = M[0]
    camera_pos = M[1]
    line_colour = (0,255,0)
    sheet_colour = (0,0,150)

    def __init__(self):
        self.run = True
    def main(self):
        ob, cam = self.object_pos, self.camera_pos
        wireframe, colours = False, True
        # wireframe, colours = False, False
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    self.run=False
            World3(self).display(wireframe,colours,flatten=False)
            ob[2][0] += 0.5
            # ob[4][1] += 3
            pygame.display.update() 
        pygame.quit()  
App().main()




