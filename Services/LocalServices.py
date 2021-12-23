
import pandas as pd
from astropy.table import QTable
import astropy.units as u

class LocalServices():
    def __init__(self, local_services):
        self.services = local_services
        #self.query_parameters = {}
    
    def startQuery(self):
        data_full = {}

        data_full['timeseries'] = []

        for manifest in self.services:
            print(manifest['path'])
            if (manifest['column_available']):
                data_ = pd.read_csv(manifest['path'])
            else:
                data_ = pd.read_csv(manifest['path'], header = None)
                print(data_)
                data_.columns = manifest['column_names']
            
            table = {}
            table['data'] = QTable.from_pandas(data_)
            table['header'] = None

            data_full['timeseries'].append(table)
        
        return data_full