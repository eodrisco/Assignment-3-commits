import sqlite3
import numpy as np
import cmath

#connect to renewable database and table location
connection = sqlite3.connect('renewable.db') # create a "connection"
cursor = connection.execute('select * from location')
l = connection.cursor()
l.execute("SELECT * FROM location")
# push database into an array X
X = np.array(cursor.fetchall())
# use shape funtion to define lenght of while loop in line number 20
shape = X.shape

#each location to be weighted. Start with the sum of the weight at zero.
sum_weight1 = 0
sum_weight2 = 0
sum_weight3 = 0
sum_weight4 = 0
sum_weight5 = 0
sum_weight6 = 0
sum_weight7 = 0
sum_weight8 = 0
sum_weight9 = 0
sum_weight10 = 0 
# Need to calculate the distance for each location against every other location.
# this is done using a while loop. Once location is calcluated.
# weight of that location is production tonnage diveded by weight
i  = 0
while i < shape[0]:
    # distance to location1 
    distance1 = (cmath.sqrt((X[i,0]-X[0+i,0])*(X[i,0]-X[0,0])+(X[i,1]-X[0,1])*(X[i,1]-X[0,1])))
    # weighting each prodution facility is tonnage divide by distance
    # distance to current location is zero. If loop to work aroung this.
    if distance1 == 0:
         weight1 = X[i,2]
    else: 
         weight1 = X[i,2]/cmath.sqrt((X[i,0]-X[0,0])*(X[i,0]-X[0,0])+(X[i,1]-X[0,1])*(X[i,1]-X[0,1]))
    # distane to location 2 with thats location's weight     
    distance2 = cmath.sqrt((X[i,0]-X[1,0])*(X[i,0]-X[1,0])+(X[i,1]-X[1,1])*(X[i,1]-X[1,1])) 
    if distance2 == 0:
         weight2 = X[1,2]  
    else: 
         weight2 = X[1,2]/cmath.sqrt((X[i,0]-X[1,0])*(X[i,0]-X[1,0])+(X[i,1]-X[1,1])*(X[i,1]-X[1,1]))
    distance3 = cmath.sqrt((X[i,0]-X[2,0])*(X[i,0]-X[2,0])+(X[i,1]-X[2,1])*(X[i,1]-X[2,1])) 
    if distance3 == 0:
         weight3 = X[2,2]  
    else: 
         weight3 = X[2,2]/cmath.sqrt((X[i,0]-X[2,0])*(X[i,0]-X[2,0])+(X[i,1]-X[2,1])*(X[i,1]-X[2,1])) 
    distance4 = cmath.sqrt((X[i,0]-X[3,0])*(X[i,0]-X[3,0])+(X[i,1]-X[3,1])*(X[i,1]-X[3,1])) 
    if distance4 == 0:
         weight4 = X[3,2]  
    else: 
         weight4 = X[3,2]/cmath.sqrt((X[i,0]-X[3,0])*(X[i,0]-X[3,0])+(X[i,1]-X[3,1])*(X[i,1]-X[3,1])) 
    distance5 = cmath.sqrt((X[i,0]-X[4,0])*(X[i,0]-X[4,0])+(X[i,1]-X[4,1])*(X[i,1]-X[4,1]))
    if distance5 == 0:
         weight5 = X[4,2]  
    else: 
         weight5 = X[4,2]/cmath.sqrt((X[i,0]-X[4,0])*(X[i,0]-X[4,0])+(X[i,1]-X[4,1])*(X[i,1]-X[4,1])) 
    distance6 = cmath.sqrt((X[i,0]-X[5,0])*(X[i,0]-X[5,0])+(X[i,1]-X[5,1])*(X[i,1]-X[5,1])) 
    if distance6 == 0:
         weight6 = X[5,2]  
    else: 
         weight6 = X[5,2]/cmath.sqrt((X[i,0]-X[5,0])*(X[i,0]-X[5,0])+(X[i,1]-X[5,1])*(X[i,1]-X[5,1])) 
    distance7 = cmath.sqrt((X[i,0]-X[6,0])*(X[i,0]-X[6,0])+(X[i,1]-X[6,1])*(X[i,1]-X[6 ,1])) 
    if distance7 == 0:
         weight7 = X[6,2]  
    else: 
         weight7 = X[6,2]/cmath.sqrt((X[i,0]-X[6,0])*(X[i,0]-X[6,0])+(X[i,1]-X[6,1])*(X[i,1]-X[6,1])) 
    distance8 = cmath.sqrt((X[i,0]-X[7,0])*(X[i,0]-X[7,0])+(X[i,1]-X[7,1])*(X[i,1]-X[7,1])) 
    if distance8 == 0:
         weight8 = X[7,2]  
    else: 
         weight8 = X[7,2]/cmath.sqrt((X[i,0]-X[7,0])*(X[i,0]-X[7,0])+(X[i,1]-X[7,1])*(X[i,1]-X[7,1])) 
    distance9 = cmath.sqrt((X[i,0]-X[8,0])*(X[i,0]-X[8,0])+(X[i,1]-X[8,1])*(X[i,1]-X[8,1])) 
    if distance9 == 0:
         weight9 = X[8,2]    
    else: 
         weight9 = X[8,2]/cmath.sqrt((X[i,0]-X[8,0])*(X[i,0]-X[8,0])+(X[i,1]-X[8,1])*(X[i,1]-X[8,1])) 
    distance10 = cmath.sqrt((X[i,0]-X[9,0])*(X[i,0]-X[9,0])+(X[i,1]-X[9,1])*(X[i,1]-X[9,1])) 
    if distance10 == 0:
         weight10 = X[9,2]  
    else: 
         weight10 = X[9,2]/cmath.sqrt((X[i,0]-X[9,0])*(X[i,0]-X[9,0])+(X[i,1]-X[9,1])*(X[i,1]-X[9,1])) 
    # weight of each location will increment for each loop 
    sum_weight1 = weight1 + sum_weight1
    sum_weight2 = weight2 + sum_weight2
    sum_weight3 = weight3 + sum_weight3
    sum_weight4 = weight4 + sum_weight4
    sum_weight5 = weight5 + sum_weight5
    sum_weight6 = weight6 + sum_weight6
    sum_weight7 = weight7 + sum_weight7
    sum_weight8 = weight8 + sum_weight8
    sum_weight9 = weight9 + sum_weight9
    sum_weight10 = weight10 + sum_weight10
    i = i + 1
# Best location is the location with max summed weight  at end of loop statement
all_weights = np.array([sum_weight1, sum_weight2, sum_weight3, sum_weight4, sum_weight5, sum_weight6 , sum_weight7, sum_weight8, sum_weight9, sum_weight10])  
max_weight = (all_weights.max())
#loop to creat an array with latitude and longitude of best location.
i = 0
while i < 10:
    if  max_weight == all_weights[i]:
        # to avoid calling a location 0, ie first location is 1. list of locations is 1-10 instead of 0-9
        best_plant = i + 1
        print "best plant is number %s" % best_plant
        best_plant_lat = round(X[i,0], 2)
        #print "best plant lat %s" % best_plant_lat
        best_plant_long = round(X[i,1], 2)
        #print "best plant long %s" % best_plant_long
        best_plant_loc = [best_plant_lat, best_plant_long]      
        print "best plant location is %s" % best_plant_loc
    else:
# do not need else to have a function, so d = 5         
        d = 5
    i = i + 1
#connect to renewable database and table location
cursor = connection.execute('select * from ports')
p = connection.cursor()
p.execute("SELECT * FROM ports")
# push database into an array Y
Y = np.array(cursor.fetchall())
#create a "port" array to calcuate distances from best location to each port.
port = [0,0,0]
i  = 0
while i < 3:
      #distance to best location to each port
      port[i]= cmath.sqrt((best_plant_loc[0]-Y[i,0])*(best_plant_loc[0]-Y[i,0])+(best_plant_loc[1]-Y[i,1])*(best_plant_loc[1]-Y[i,1])) 
      #print Z[i]
      i = i + 1
# creat an array to calulate the nearest port
Port_Dist = np.array(port)
Min_Port_Dist = (Port_Dist.min())

i = 0
while i < 3:
    if  Min_Port_Dist == port[i]:
        Near_Port = i + 1
        print "Nearest Port to Best Plant Location is number %s" % Near_Port
        print "Distance to nearest Port is %s" % round(Min_Port_Dist, 2)
    else:
        d = 5
    i = i + 1
     
     