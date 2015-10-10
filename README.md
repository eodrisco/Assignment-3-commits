# Assignment-3-commits
Python Programming, Databases, and Version Control Assignment;
Use sqlite3 module to connect to renewable database and table "location".
Numpy module used for arithmetic of database values. Using fetchall, push database into an multidimensional array called X. Multidimensional array allow for arithmatic between each cell in array.
The distance between 2 points in 2D is sqrt(x2-x1)^2+(y2-y1)^2. Cmath required for this calculation. 
Use while loop to calculate distances of every location. On each loop, calculate distance of current location (value of i) to each plant against.
For each loop, each location is given a weight. Start with the sum of the weight at zero and increment for each loop.
Weight of a location is production tonnage divided by distance from current location in loop.
Distance to current location to itself must be zero. If statement is used work around this. Ie if distance is 0, then this must be current location. For current location weight will be equal to tonnage at this location. 
On final loop each final summed weight is added into an array. The max number in this array is the best location for new plant. 
Use another loop to create an array with latitude and longitude of new plant location. Print decision of new plant location and its latitude and  
longitude. To calculate which port is nearest to new plant location, connect to renewable database and table "ports".
Push table into an array Y. Create a "port" array to calculate distances from best location to each port.
Finally create another array and use another loop to calculate the nearest port. Print nearest Port number and distance to Port.

