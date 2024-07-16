from World1 import *

"""
This program shows different shapes which can be built in the Shapes module. 
We can see here how they can be rotated in various ways.

We have a blue, cylindrical pillar and a cuboid comprised of smaller cubes.
Notice that the pillar is rotating about it's own axis. 
It's axis is then being rotated.

____Visit World1 module to see how the inputs are scaled to coordinate the motion___

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
    M = [[[1,6,0],[0,0,0], [0,0,40], [0,30,0], [0,0,0]], 
            [[0,0,0], [0,0,0]]]
    object_pos = M[0]
    camera_pos = M[1]       # Note that here we can adjust lie colour...
    line_colour = (0,0,200) # ...and more besides in the following demos. 
    def __init__(self):
        self.run = True

    def main(self):
        ob, cam = self.object_pos, self.camera_pos
                # Adjust the following boolean variables as desired
        wireframe, colours = False, False
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    self.run=False
                # World's display function calls Screen class to render shapes
            World(self).display(wireframe,colours,flatten=False)
                # third and fourth elements rotate world
                # note the cuboid is stationary inside rotating frame
            ob[3][0] += 1 
                # Set object spinning 
            ob[4][1] += 2 
            pygame.display.update() 
        pygame.quit()  
App().main()

