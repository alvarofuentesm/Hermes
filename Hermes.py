'''
Hermes class file
'''
from multipledispatch import dispatch

from Services.RemoteServices import RemoteServices
from Services.LocalServices import LocalServices

from ipyaladin import Aladin
from ipywidgets import Layout, Box, widgets

from astropy.visualization import astropy_mpl_style
import matplotlib.pyplot as plt



valid_search = ['cone_search', 'box_search']

class HermesClassError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('calling str')
        if self.message:
            return 'HermesClassError, {0} '.format(self.message)
        else:
            return 'HermesClassError has been raised'

class Hermes():
    def __init__(self):
        self.filters = {'search_type': None, 'ra/dec': [None, None], 'local_services' : []}
        self.data_query  = None
        self.local_query = None
        
    @dispatch(str)
    def addFilter(self, search_type = None):
        if (search_type in valid_search):
            self.filters['search_type'] = {'type' : search_type}
        else:
            raise HermesClassError('search_type is invalid')
    
    @dispatch(str, str)
    def addFilter(self, param_name, value):
        if (param_name == 'ra'):
            self.filters['ra/dec'][0] = value
        elif (param_name == 'dec'):
            self.filters['ra/dec'][1] = value

    @dispatch(str, float)
    def addFilter(self, param_name, value):
        # TO-DO: match search_type with param_name. Determine if box_search and radius is allowed or not.
        if (param_name == 'radius'):
            self.filters['search_type']['radius'] = value
        
        elif (param_name == 'width'):
            self.filters['search_type']['width'] = value
        elif (param_name == 'height'):
            self.filters['search_type']['height'] = value
        else:
            raise HermesClassError('filter is invalid')
    
    def startQuery(self): # start the query
        local_services = LocalServices(self.filters['local_services'])
        self.local_query = local_services.startQuery()

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

    def getTables(self, service_name, type_data):
        data_ = self.data_query[service_name][type_data].copy()
        return data_

    def getLocalTables(self, dummy = None):
        return self.local_query

    def addLocalService(self, path, column_available = True, separator = ',',  column_names = [], header = None):
        # TO-DO: check path existence in os or already in filters
        self.filters['local_services'].append( {'path': path, 'column_available': column_available, 'separator': separator,  'column_names': column_names, 'header': header} )

    def getLocalServices(self):
        return self.filters['local_services']

    def saveHermes(self, name = '',):
        import json        
        if name == '':
            with open('save.Hermes', 'w') as fout:
                print(self.filters)
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

    def generateVisualization(self, type = 'sky'):
        if (type == 'sky'):
            # TO-DO: generalizar (por ahora ocupa SIMBAD)
            #my_target = self.data_query['SIMBAD']['MAIN_ID'][0]
            my_target = self.getTables('SIMBAD', 'timeseries')[0]['data']['MAIN_ID'][0]
            
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

        elif (type == "spectrum"):
            # TO-DO: generalizar (por ahora ocupa MAST)
            plt.style.use(astropy_mpl_style)

            print(len(self.getTables('MAST', 'spectrum')))
            for i in range(len(self.getTables('MAST', 'spectrum'))):
                data = self.getTables('MAST', 'spectrum')[i]['data']
                if (len(data.shape) == 2):            
                    plt.figure()
                    #plt.title( )
                    plt.imshow(data, cmap='viridis')
                    plt.colorbar()
                    plt.show()

    def addTable(self, data):
        pass
