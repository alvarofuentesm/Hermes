'''
Hermes class file
'''
from multipledispatch import dispatch

from Services.RemoteServices import RemoteServices

from ipyaladin import Aladin
from ipywidgets import Layout, Box, widgets


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
        
    def saveHermes(self, path = '',name = '',):
        import json        
        if name == '':
            with open('save.Hermes', 'w') as fout:
                json.dump(self.filters, fout)
        else:
            with open('{}.Hermes'.format(name) , 'w') as fout:
                json.dump(self.filters, fout)        
        return

    def loadHermes(self,    filename=''):
        import json         
        if filename != '':            
            file=open(filename,"r")
        else:
            file=open("save.Hermes","r")
        data = json.load(file)
        self.filters=data
        # guardar estado de objeto en archivo .hermes
        return 
        return 

    def generateVisualization(self, type = 'sky'):
        if (type == 'sky'):
            # TO-DO: generalizar (por ahora ocupa SIMBAD)
            my_target = self.data_query['SIMBAD']['MAIN_ID'][0]
            
            aladin = Aladin(layout=Layout(width='50%'), target=my_target, fov=0.2)


            button = widgets.Button(description="Select")
            def on_button_clicked(b):
                aladin.rectangular_selection()

            button.on_click(on_button_clicked)
            table_info = widgets.HTML(layout=Layout(height='auto', overflow='auto'))


            box_layout = Layout(display='flex',
                                flex_flow='row',
                                align_items='stretch',
                                width='100%',
                                position='relative',
                                overflow='hidden',
                                height='100vh',
                                margin='-100px 0 0 0',
                                padding='100px 0 0 0 '
                            )
            box = Box(children=[aladin, button, table_info], layout=box_layout)
            return box


    def addTable(self, data):
        pass
