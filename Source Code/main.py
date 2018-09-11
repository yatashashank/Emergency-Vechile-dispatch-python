# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 20:44:58 2018

@author: somar
"""


import csv
import dijkstra

#We need to mention __name__ as main as we are importing methods from other classes

if __name__ == '__main__':

 
    # Reading the datasets.

    #Reading the distances csv file 
    reader = csv.DictReader(open('ZipcodeDistances2.csv', encoding='utf-8-sig'))
    distances = []
    for line in reader:
        distances.append(line)
   
    #Reading the vehicles csv file 
 
    vehicleReader2 = csv.DictReader(open('EmergencyVehicle.csv', encoding='utf-8-sig'))
    vehicles = []
    for line in vehicleReader2: 
        vehicles.append(line)
    
    #Adding availability to all the vehicles as TRUE
    for vehicle in vehicles:
        vehicle['AVAILABILITY'] = True
    
    # Simplyfing the code by declaring the Dijkstra Graph to g
    g = dijkstra.Graph()
    
    for distance in distances:
        #Adding the vertices to graph witrh respect to zipcodes
        if not distance['ZIPCODE1'] in g.get_vertices():
            g.add_vertex(int(distance['ZIPCODE1']))

        if not distance['ZIPCODE2'] in g.get_vertices():
            g.add_vertex(int(distance['ZIPCODE2']))

        #Adding the edges of vertices based on the distance between the vertices 
        g.add_edge(int(distance['ZIPCODE1']),int( distance['ZIPCODE2']), int(distance['DISTANCE']))

"""
    print('Graph data:')
    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print('( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w)))

"""
def dispatch(vehicle_type, zipcode):

        unassigned_vehicles = [v for v in vehicles if int(v['T']) == vehicle_type and v['AVAILABILITY']]

        
        if len(unassigned_vehicles) > 0:
            g.reset_vertices() #vertex's distance = infinityvi; vextex.visited = False; vertex.previous = None will be done in reset_vertices() method
            place = g.get_vertex(zipcode) #Returns vert_dict
            dijkstra.dijkstra(g, place) #passing the graph object and place into DIJKSTRA's method in Dijkstra's file

            #Calculating and  storing the list of distances for all the available vehicles done by adding vertex and getting distance
            for vehicle in unassigned_vehicles:
                vehicle['DISTANCE'] = g.get_vertex(int(vehicle['ZIPCODE'])).get_distance()

            #Sorting the list of all the available vehicles, based on key with inline function Lambda(sorts based on Distances)
            #The below contains list of KEY, VALUE pairs
            unassigned_vehicles = sorted(unassigned_vehicles, key=lambda k: k['DISTANCE'])
        
#        vehicles[vehicles.index(availability[0])]['AVAILABILITY'] = False  
        print ("The ID of assigned vehicle is " + unassigned_vehicles[0]['SNUM'] + " and the shortest distance from the requested ZIPCODE is " + str(unassigned_vehicles[0]['DISTANCE']) )
        return 

#Dynamicaly requesting the service 
        
print("HELLO !, Do You like to resquest the Emergency vehicle")
decision = input('Y or N ' + '\n')
request = 'Y'
if decision == 'Y':
    while (request == 'Y'):
        vehicle_type = input('Type of Vehicle You are Requesting:' + '\n' + 'Fire Engine = 1,' + '\n' + 'Ambulance = 2,' + '\n' + 'Police = 3' + '\n' )
        while vehicle_type not in  ['1','2','3']:
            vehicle_type = input('You have entered an invalid type, Re-enter type of Vehicle:')
        zipcode = input('Enter the zipcode of the area' + '\n')
        dispatch(int(vehicle_type),int(zipcode))
        request = input('\n' + 'Do you like to have another request (Y/N)')
    print('thanku')    
else: 
    print('This is not the proper one you are searching for!!')