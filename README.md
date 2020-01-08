# Transformation-2D-geometric-objects
python code of linear transformations of 2D geometric Objects
Input
The first contains the word ‘disc’ or ‘polygon’ denoting the figure you have to use.
If the word is ‘disc’, the next line contains three space-separated integers a b r as specified
above.
If the word is ‘polygon’, the next two lines contain space separated lists X[] and Y[] of equal
length, denoting the x-y co-ordinates of the vertices of the polygon.
The next few lines contain a single query each, denoting the transformation you have to perform.
Each query will be of the form:
- S x y : scale the object by a factor of x along the x-axis, and y along the y-axis.
- R theta : rotate the object by angle theta(in degrees, 0 <= theta <= 360) in the
counter-clockwise direction about the origin.
- T dx dy : translate the object by dx units along the x-axis, and by dy units along the y-axis.
Each transformation has to be performed on the shape obtained as a result of all the previous
transformations, ie the effect of the transformations should be cumulative.
The final line of the input contains the word ‘quit’, denoting that no further transformations are
required and you should exit the program.
Output
Plot the input object according to the input specifications.
For each transformation,
- print the new resulting parameters(a b r for disc and x[] y[] for polygon) of the object in the
format specified in the input.
- update the plot to show the new object position.
