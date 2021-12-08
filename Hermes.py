'''
Hermes class file
'''

class Hermes():
    def __init__(self, filters = {}, init_filename = None):
        self.filters = filters
        self.init_filename = init_filename

        if (init_filename is not None): # Carga desde archivo .hermes
            pass
        
        else: # busqueda por filtros
            pass


    def getInitFileName(self):
        return self.init_filename

    def getFilters(self):
        return self.filters

    def saveHermes(self, path = ''):
        # guardar estado de objeto en archivo .hermes
        return 

    def generateVisualization(self):
        pass 

    def addTable(self, data):
        pass
