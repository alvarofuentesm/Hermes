'''
Hermes class file
'''

#import de servicios

class Hermes():
    def __init__(self, dummy = {"test": "helloWorld", "test2": [1,2,3], "test3": ["1", "2", "3"]}):
        self.dummy = dummy

    def addFilter(self, filters = {} ):
        #self.filters = filters
        pass

    def startQuery(self): # start the query
        # Hacerlo síncrono
        pass

    def getInitFileName(self):
        #return self.init_filename
        pass
        
    def getFilters(self):
        #return self.filters
        pass

    def saveHermes(self, path = ''):
        # guardar estado de objeto en archivo .hermes
        return 

    def loadHermes(self,  init_filename = None):
        # guardar estado de objeto en archivo .hermes
        return 

    def generateVisualization(self):
        pass 

    def addTable(self, data):
        pass
