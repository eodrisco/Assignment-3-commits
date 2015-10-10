import sqlite3
import numpy as np
import cmath

connection = sqlite3.connect('renewable.db') # create a "connection"
cursor = connection.execute('select * from location')
l = connection.cursor()
l.execute("SELECT * FROM location")
X = np.array(cursor.fetchall())
# print(X)
#using shape function to calculate lenght of location array
shape = X.shape
#print shape
#print shape[0]
sum_weight = np.zeros(shape[0])
distance = np.zeros(shape[0])
weight = np.zeros(shape[0])
#print sum_weight

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

i  = 0
while i < shape[0]:
    # distance to location1 
    # distance to loc1 is distance from loc1 to each other location multiplied by production of that plant
    distance1 = cmath.sqrt((X[i,0]-X[0+i,0])*(X[i,0]-X[0,0])+(X[i,1]-X[0,1])*(X[i,1]-X[0,1]))
    print "distance 1 is %s" % distance1  
    # weighting each prodution facility is tonnage divide by distance
    # distance to current location is zero. If loop to work aroung this.
    if distance1 == 0:
         weight1 = X[i,2]
    else: 
         weight = X[i,2]/cmath.sqrt((X[i,0]-X[0,0])*(X[i,0]-X[0,0])+(X[i,1]-X[0,1])*(X[i,1]-X[0,1]))
         print weight1
    #sum weight of each location     
    distance2 = cmath.sqrt((X[i,0]-X[1,0])*(X[i,0]-X[1,0])+(X[i,1]-X[1,1])*(X[i,1]-X[1,1])) 
    print "distance 2 is %s" % distance2  
    if distance2 == 0:
         weight2 = X[1,2]  
         print weight2
    else: 
         weight2 = X[1,2]/cmath.sqrt((X[i,0]-X[1,0])*(X[i,0]-X[1,0])+(X[i,1]-X[1,1])*(X[i,1]-X[1,1]))
         #print weight2     
    distance3 = cmath.sqrt((X[i,0]-X[2,0])*(X[i,0]-X[2,0])+(X[i,1]-X[2,1])*(X[i,1]-X[2,1])) 
    print "distance 3 is %s" % distance3  
    if distance3 == 0:
         weight3 = X[2,2]  
         #print weight3
    else: 
         weight3 = X[2,2]/cmath.sqrt((X[i,0]-X[2,0])*(X[i,0]-X[2,0])+(X[i,1]-X[2,1])*(X[i,1]-X[2,1])) 
         #print weight3
    distance4 = cmath.sqrt((X[i,0]-X[3,0])*(X[i,0]-X[3,0])+(X[i,1]-X[3,1])*(X[i,1]-X[3,1])) 
    if distance4 == 0:
         weight4 = X[3,2]  
         #print weight4
    else: 
         weight4 = X[3,2]/cmath.sqrt((X[i,0]-X[3,0])*(X[i,0]-X[3,0])+(X[i,1]-X[3,1])*(X[i,1]-X[3,1])) 
         #print weight4
    distance5 = cmath.sqrt((X[i,0]-X[4,0])*(X[i,0]-X[4,0])+(X[i,1]-X[4,1])*(X[i,1]-X[4,1]))
    #print distance5
    if distance5 == 0:
         weight5 = X[4,2]  
         #print weight5
    else: 
         weight5 = X[4,2]/cmath.sqrt((X[i,0]-X[4,0])*(X[i,0]-X[4,0])+(X[i,1]-X[4,1])*(X[i,1]-X[4,1])) 
         #print weight5
    distance6 = cmath.sqrt((X[i,0]-X[5,0])*(X[i,0]-X[5,0])+(X[i,1]-X[5,1])*(X[i,1]-X[5,1])) 
    if distance6 == 0:
         weight6 = X[5,2]  
         #print weight6
    else: 
         weight6 = X[5,2]/cmath.sqrt((X[i,0]-X[5,0])*(X[i,0]-X[5,0])+(X[i,1]-X[5,1])*(X[i,1]-X[5,1])) 
         #print weight6
    distance7 = cmath.sqrt((X[i,0]-X[6,0])*(X[i,0]-X[6,0])+(X[i,1]-X[6,1])*(X[i,1]-X[6 ,1])) 
    if distance7 == 0:
         weight7 = X[6,2]  
         #print weight7
    else: 
         weight7 = X[6,2]/cmath.sqrt((X[i,0]-X[6,0])*(X[i,0]-X[6,0])+(X[i,1]-X[6,1])*(X[i,1]-X[6,1])) 
         #print weight7
    distance8 = cmath.sqrt((X[i,0]-X[7,0])*(X[i,0]-X[7,0])+(X[i,1]-X[7,1])*(X[i,1]-X[7,1])) 
    if distance8 == 0:
         weight8 = X[7,2]  
         #print weight8
    else: 
         weight8 = X[7,2]/cmath.sqrt((X[i,0]-X[7,0])*(X[i,0]-X[7,0])+(X[i,1]-X[7,1])*(X[i,1]-X[7,1])) 
         #print weight8
    distance9 = cmath.sqrt((X[i,0]-X[8,0])*(X[i,0]-X[8,0])+(X[i,1]-X[8,1])*(X[i,1]-X[8,1])) 
    if distance9 == 0:
         weight9 = X[8,2]  
         #print weight9
    else: 
         weight9 = X[8,2]/cmath.sqrt((X[i,0]-X[8,0])*(X[i,0]-X[8,0])+(X[i,1]-X[8,1])*(X[i,1]-X[8,1])) 
         #print weight9
    distance10 = cmath.sqrt((X[i,0]-X[9,0])*(X[i,0]-X[9,0])+(X[i,1]-X[9,1])*(X[i,1]-X[9,1])) 
    if distance10 == 0:
         weight10 = X[9,2]  
         #print weight10
    else: 
         weight10 = X[9,2]/cmath.sqrt((X[i,0]-X[9,0])*(X[i,0]-X[9,0])+(X[i,1]-X[9,1])*(X[i,1]-X[9,1])) 
         #print weight10     
    sum_weight1 = weight1 + sum_weight1
    print "sum weight is %s" % sum_weight1 
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
    


all_weights = np.array([sum_weight1, sum_weight2, sum_weight3, sum_weight4, sum_weight5, sum_weight6 , sum_weight7, sum_weight8, sum_weight9, sum_weight10]) 
max_weight = (all_weights.max())
#print "max_weight is %s" % max_weight
i = 0
while i < 10:
    if  max_weight == all_weights[i]:
        best_plant = i + 1
        print "best plant is number %s" % best_plant
        best_plant_lat = X[i,0]
        #print "best plant lat %s" % best_plant_lat
        best_plant_long = X[i,1]
        #print "best plant long %s" % best_plant_long
        best_plant_loc = [best_plant_lat, best_plant_long]      
        print "best plant location is %s" % best_plant_loc
    else:
        d = 5
    i = i + 1

cursor = connection.execute('select * from ports')
p = connection.cursor()
p.execute("SELECT * FROM ports")
Y = np.array(cursor.fetchall())
#print(Y)

Z = [0,0,0]
i  = 0
while i < 3:
      #distance to por11 
      #distance to loc1 is distance from loc1 to each other location multiplied by production of that plant
      Z[i]= cmath.sqrt((best_plant_loc[0]-Y[i,0])*(best_plant_loc[0]-Y[i,0])+(best_plant_loc[1]-Y[i,1])*(best_plant_loc[1]-Y[i,1])) 
      #print Z[i]
      i = i + 1
Port_Dist = np.array(Z)
Min_Port_Dist = (Port_Dist.min())

i = 0
while i < 3:
    if  Min_Port_Dist == Z[i]:
        Near_Port = i + 1
        print "Nearest Port to Best Plant Location is number %s" % Near_Port
        print "Distance to nearest Port is %s" % Min_Port_Dist
    else:
        d = 5
    i = i + 1
     
     