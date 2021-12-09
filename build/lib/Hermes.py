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

    def saveHermes(self,name = '', path = ''):
        import json        
        if name == '':
            with open('save.Hermes', 'w') as fout:
                json.dump(self.dummy, fout)
        else:
            with open('{}.Hermes'.format(name) , 'w') as fout:
                json.dump(self.dummy, fout)        
        return 

    def loadHermes(self, filename):
        import json 
        file=open(filename,"r")
        data = json.load(file)            
        self.dummy=data
        # guardar estado de objeto en archivo .hermes
        return 

    def generateVisualization(self):
        pass 

    def addTable(self, data):
        pass

a=Hermes()
a.saveHermes()
input()
a.loadHermes("save.Hermes")
print(a.dummy)