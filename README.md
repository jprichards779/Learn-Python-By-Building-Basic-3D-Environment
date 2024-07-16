

Motivation
______________________________________________________________________________________________

      - Learn how to use Object Oriented Programming (OOP), exerrcise these skills 
        and to improve my programming skills to a degree that my previous projects didn't. 
      
      - Optimise the performance of my code, reaching beyond my comfort zone to do so,
        and pull my skillset upwards and deepen my understanding



Context
_______________________________________________________________________________________________

      I implemented my first piece of coding syntax 3 years ago. I subsequently tested out my 
      and developed understanding by creating several basic gaming projects, first relying on 
      command-line prompt, then using Pygame's GUI afterwards. 

      By now I knew some of the basics about OOP, but for me to gain a more solid 
      understanding of these data structures, I would have to build an interesting project 
      which would allow me to experiment with the various ways they can be used.
      I already and a mathematical intuition about the creation of 3D holograms and derived 
      my own formulae for it in Excel (Yes! You can draw 3D cubes in Excel).

      Creating a 3D environment was the just the start, the real challenge was how to 
      get shapes to carry out complex motion without using any mathematical help online. 
      The only help I incorporated into my project centered around Python concepts and 
      pygame documentation / video intros to pygame.
      
      Also would like to give a big thanks to Python Institute and Tech with Tim for 
      sharing their projects and providing inspiration for a novice like me. 


      
Project Timeline
_______________________________________________________________________________________________
      
      Early 2022
            I created the first draft of this project, which only consisted of procedural code. 
            Once I felt ready the code was eventually overhalled to adopt Object Oriented 
            Programming.
      
      Early 2023 
            I had adopted extra functionality, allowing the shapes to be rotated and moved in 
            unison or independently. 
             This update abandoned the need to colour the shapes, focussing more on getting 
            the basics right. The result was monochromatic, transparent shapes.
             Around this time I noticed how the order of rotational transforms could give you a 
            different result. 
             Some axes of rotation remain fixed to the world frame while some remain local. 
            To account for this, I built a tilt() function in which the order of these 
            transformations could be set according to the desired affect. 
            This shouldn't have surprised me because in linear algebra, matrix transforms 
            don't commute (well..most of the time / or at least not here).
      
      Winter 2023 
            I realised this format had hidden a problem from view. The shapes were not drawn in 
            the correct order when rotated. 
             This was fixed by calculating the average radial distance of each side for each shape and 
            using lists to reorder the sequence of sides by average radial distance. 
             This dramatically slowed the program down for shapes such as cylinders, 
            consisting of many points to form a curve. 
            
      Spring 2024
            Storing these distances and shape data as key value pairs in a dictionary, speeded 
            this program back up to its initial rate. 
             As the project has grown in size, I have modified it several times to help remove 
            any code that was naively introduced when my confidence and understanding was less 
            than it presently is. There is still work to do, and that might later take the form 
            of me starting again from scratch, with he overall layout being informed by the 
            lessons learned. 

The format of this whole project was overhalled about 3 times as it grew in complexity and 
my knowledge improved. Much time was spent second guessing whether there was a better way 
to do it, but this has been the best my skillset and availability will allow. 





Layout 
________________________________________________________________________________________________

      The Project is broken up into Demo files, containing the main event loop. Information for 
      each is fed in from corresponding World module, containing a World class which contains 
      all of the shape data. 
      The packages folder contains all the modules which contain the underpinning calculation 
      functionality. 
      My approach has been to create object motion by simply feeding numerical position data 
      into the world class in the main loop, just to demonstrate what can be achieved visually.
      
      The motion is adjusted using the following argument:   

            object_pos = [ [ x, y, z ], [ x, y, z ], [a1,a2,a3], [a1,a2,a3], [a1,a2,a3] ]
      
            - First element is the World distance 
            - Second element is the group motion/position in World's coordinate frame
            - Third and fourth elements form an angle matrix. 
              Two elements allow greater rotation flexibility. 
              Both rotate world about the centre/origin  i.e  the second element. 
            - Fifth element rotates individual shapes about their own centre. Another angle could be 
              added to improve flexibility but for it remains like this for now to stop the array 
              becoming larger than it already is. 

      The Demos will show it all in action. The shapes are built out of a cubic( ) function. 
      This returns the vertices of a cube, each of which can be scaled separately and connected 
      to form more complex shapes. 

      Scale factors for each corner at set to [1,1,1] by default. 
      A scale factor of [2,1,1] would double the x component. 
      Doubling all components would double the coordinate values of the position vector which 
      originates at the centre of the cube. 


General Thoughts
________________________________________________________________________________________________

      My thoughts on where to improve have come with the benefit of hindsight 
      and growing confidence in programming. I now know there are so may ways I could or 
      should have done this differently and here are some of them:

            If I could start with the knowledge I had now, I would focus more on making the 
            program more interactive, whereby the user can draw / retreave shapes as required
            on screen as opposed to building the world programatically. 

            The number of calculations needed per vertex is just huge. 
            Really, a project such as this need sto be completed in C++ or JavaScript 
            which are much faster than Python. This is mainly because (I think this is correct)
            Python code gets compiled during runtime, unlike the former which is precompiled as the 
            code is written and stored in memory. 
            
            Python has some libraries which help get around this.
            Use of NumPy library to create arrays from the outset. All shape attributes should be controllable from the 
            App class. 
            Some of this can be done already, but more is needed besides.
            Need to find ways of duplicating data points instead of recalculating for each instance. 
            I am considering potential solutions to this but for now my priority is demonstrating 
            where my coding ability is at as well as a possible way to create a 
            basic virtual environment.

            In a previous iteration of the project, side minimising algorithm was used to remove 
            sides which meet and are invisible to the user. 
            At present, the cubic2( ) function allows users to specify sides to include. 
            The aim of both is to minimise calculations to be completed, but a more consistent / 
            unified way of doing this is needed. 

            I have implemented some memoizaton into the program but these are more useful 
            for cylcical motion where spatial coordinates are revisitted.
            Motion can be initially gittery before the all data is collected in 
            dictionaries, in which case, calculation outouts are simply revisitted, 
            saving the need for recalculating. 
            The effects of this can be seen in Demo4, where we have a rotating parabolic sheet.
            At first, rotation is slow, but then it suddenly speeds right up. 

            The program slows down the greater the number of shapes. Introducing duplication 
            techniques could be first approach and then some multiplrocessing from Python's
            multiprocessing library. Apparently the effects would still be minimla compared to 
            executing in C++.
            
            The calculations needed to contually re-determine the order by which shapes are overlayed 
            slowed the program down. However the use of dictionary structures to record 
            data instead of lists has speeded it back up to its original speed, 
            with this extra functionality on top. 



      
