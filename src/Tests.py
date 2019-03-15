'''
Created on Nov 15, 2017

@author: Ale
'''
from Operations import *

def testcheckAndAdd():
    flightList = []
    
    assert checkAndAdd(flightList, '0B3001', '45', 'Bucharest', 'Berlin')
    assert not checkAndAdd(flightList, '0B3001', '10', 'Bucharest', 'Berlin')
    assert not checkAndAdd(flightList, '0B3001', '45', 'Bu', 'Berlin')
    
def testupdateFlight():
    flightList = [('0B3001', '45', 'Bucharest', 'Berlin')]
    flightList2 = [('0B3003', '90', 'Cluj-Napoca', 'Berlin')]
    
    assert updateFlight(flightList, '0B3001', '90') == [('0B3001', '90', 'Bucharest', 'Berlin')]
    assert updateFlight(flightList2, '0B3003', '100') == [('0B3003', '100', 'Cluj-Napoca', 'Berlin')]
    
    
def testcheckAndReroute():
    flightList = [('0B3001', '45', 'Cluj-Napoca', 'Bucharest')]
    
    assert checkAndReroute(flightList, 'Bucharest', 'Berlin')
    assert not checkAndReroute(flightList, 'Bucharest', 'Be')
    
def testsortByDuration():
    flightList = []
    flightList.append(('0B3002', '45', 'Cluj-Napoca', 'London'))
    flightList.append(('0A3333', '30', 'Cluj-Napoca', 'Berlin'))
    flightList.append(('0BBBBB', '100', 'London', 'Munchen'))
    flightList.append(('0C5634', '25', 'Cluj-Napoca', 'Paris'))
    
    assert sortByDuration(flightList, 'Cluj-Napoca') == [('0C5634', '25', 'Cluj-Napoca', 'Paris'), ('0A3333', '30', 'Cluj-Napoca', 'Berlin') ,('0B3002', '45', 'Cluj-Napoca', 'London')]


def runAllTests():
    testcheckAndAdd()
    testupdateFlight()
    testcheckAndReroute()
    testsortByDuration()
    
runAllTests()