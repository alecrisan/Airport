'''
Created on Nov 15, 2017

@author: Ale
'''

def checkAndAdd(flightList, code, duration, departure, destination):
    """
    checks if the user entered valid input
    input: the list, code, duration, departure city, destination city
    output: True if the adding was done
            False otherwise (duration was less than 20, the length of the other strings was < 3)
    """
    if duration.isdigit() == True:
        if int(duration) < 20:
            return False
        
    if len(code) < 3 or len(departure) < 3 or len(destination) < 3:
            return False
    
    flightList.append((code, duration, departure, destination))
    return True

def updateFlight(flightList, code, newDuration):
    """
    Modifies the duration of a given flight
    input: the list, the code of the flight and the new duration
    output: the modified list
    """
    for i in range(0, len(flightList)):
        f = flightList[i]
        if f[0] == code:
            flightList.append((f[0], newDuration, f[2], f[3]))
            flightList.remove(f)
            break
    return flightList
        
def checkAndReroute(flightList, destination, newDestination):
    """
    checks if the user entered valid input
    input: the list, the destination, and the new destination
    output: True if there was at least one flight modified
            False otherwise(the length of the strings was < 3, or there weren't any flights to change)
    """
    ok = 0
    if len(newDestination) < 3 or len(destination) < 3:
        return False
    for i in range(0, len(flightList)):
        f = flightList[i]
        if f[3] == destination:
            ok = 1
            flightList.append((f[0], f[1], f[2], newDestination))
            flightList.remove(f)
    if ok == 1:
        #at least one flight was changed
        return True
    
def sortByDuration(flightList, departure):
    """
    We put in a list only the flights with the given departure city
    And then we sort it by duration (increasing)
    input: the list, the departure city
    output: the new list
    """
    auxList = []
    for i in range(0, len(flightList)):
        f = flightList[i]
        if f[2] == departure:
            auxList.append((f))
    for i in range(0, len(auxList) - 1):
        f1 = auxList[i]
        for j in range(i + 1, len(auxList)):
            f2 = auxList[j]
            if int(f1[1]) > int(f2[1]):
                f1, f2 = f2, f1
    
    return auxList
    
    
    