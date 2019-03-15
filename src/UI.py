'''
Created on Nov 15, 2017

@author: Ale
'''
from Operations import *

def initList(flightList):
    flightList.append(('0B3002', '45', 'Cluj-Napoca', 'London'))
    flightList.append(('0A3333', '30', 'Cluj-Napoca', 'Berlin'))
    flightList.append(('0BBBBB', '100', 'London', 'Munchen'))
    flightList.append(('0C5634', '25', 'Cluj-Napoca', 'Paris'))
    flightList.append(('0D67A4', '90', 'Barcelona', 'Bucharest'))
    flightList.append(('0CCC67', '45', 'Cluj-Napoca', 'Bucharest'))
    flightList.append(('0A8973', '75', 'Madrid', 'London'))
    flightList.append(('0B3004', '50', 'Rome', 'Cluj-Napoca'))
    flightList.append(('0B3554', '65', 'London', 'Venice'))
    flightList.append(('0B3000', '30', 'Berlin', 'Targu-Mures'))
    
def printList(flightList):
    for f in flightList:
        print("Code: " + f[0] + " Duration: " + f[1] + " Departure city: " + f[2] + " Destination city: " + f[3])
        
def start():
    flightList = []
    initList(flightList)
    
    while True:
        option = raw_input("Enter an option: ")
        
        if option == '1':
            print("You chose to add a flight")
            code = raw_input("Code: ")
            duration = raw_input("Duration: ")
            departure = raw_input("Departure city: ")
            destination = raw_input("Destination city: ")
            if checkAndAdd(flightList, code, duration, departure, destination) == True:
                print("Flight added")
            else:
                print("Invalid parameters. Flight not added")
        elif option == '2':
            print("You chose to update a flight")
            code = raw_input("Code: ")
            newDuration = raw_input("New duration: ")
            updateFlight(flightList, code, newDuration)
        elif option == '3':
            print("You chose to reroute flights for a given destination")
            destination = raw_input("Destination city: ")
            newDestination = raw_input("New destination city: ")
            if checkAndReroute(flightList, destination, newDestination) == True:
                print("Flight/s rerouted")
            else:
                print("Invalid parameters. Modification not made")
        elif option == '4':
            print("Show all flights with a given departure city")
            departure = raw_input("Departure city: ")
            auxList = sortByDuration(flightList, departure)
            printList(auxList)
        elif option == '5':
            printList(flightList)
        elif option == '0':
            print("Exited the program")
            break
        else:
            print("Invalid option")
        
start()

