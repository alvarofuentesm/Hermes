'''
Hermes class file
'''
from multipledispatch import dispatch

from Services.RemoteServices import RemoteServices

class Hermes():
    def __init__(self, dummy = {"test": "helloWorld", "test2": [1,2,3], "test3": ["1", "2", "3"]}):
        self.dummy = dummy
        self.filters = {'search_type': None, 'ra/dec': [None, None]}
        self.data_query  = None

    @dispatch(str)
    def addFilter(self, search_type = None):
        # TO-DO: verify search_type is valid
        if (search_type == 'cone_search'):
            self.filters['search_type'] = {'type' : 'cone_search'}
    
    @dispatch(str, str)
    def addFilter(self, param_name, value):
        if (param_name == 'ra'):
            self.filters['ra/dec'][0] = value
        elif (param_name == 'dec'):
            self.filters['ra/dec'][1] = value

    @dispatch(str, float)
    def addFilter(self, param_name, value):

        if (self.filters['search_type'] is None):
            return # TO-DO: manejar esto
        
        if (param_name == 'radius'):
            self.filters['search_type']['radius'] = value

        # TO-DO: width, height (box search)

    def startQuery(self): # start the query
        # Hacerlo síncrono
        remote_services = RemoteServices()
        remote_services.addQuery(self.filters)
        self.data_query = remote_services.startQuery()

        return self.data_query

    def getDataQuery(self):
        return self.data_query

    def getInitFileName(self):
        #return self.init_filename
        pass
        
    def getFilters(self):
        return self.filters
        
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
