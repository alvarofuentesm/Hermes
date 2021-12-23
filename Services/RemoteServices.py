
from .MAST import QueryMAST
from .OAC import QueryOAC
from .SIMBAD import QuerySIMBAD
from .IRSA import QueryIRSA

import astropy.units as u
import astropy.coordinates as coord


astroquery_services = [
    # https://astroquery.readthedocs.io/en/latest/oac/oac.html
    {'service_name': 'OAC', 'catalogues' : [], 'description': 'Open Astronomy Catalog REST API for easy access to data of supernovae, Tidal Disruption Events (TDEs) and kilonovae. '}, 
    # https://astroquery.readthedocs.io/en/latest/mast/mast.html
    {'service_name': 'MAST', 'catalogues' : [], 'description': 'Barbara A. Mikulski Archive for Space Telescopes (MAST)'},
    # https://astroquery.readthedocs.io/en/latest/ipac/irsa/irsa.html
    #{'service_name': 'IRSA', 'catalogues' : ['ptf_lightcurves'], 'description': 'Different types of queries on the catalogs present in the IRSA general catalog service'},
    # https://astroquery.readthedocs.io/en/latest/simbad/simbad.html
    {'service_name': 'SIMBAD', 'catalogues' : [], 'description': 'Simbad service'}
]

allowed_search_types = {
    'cone_search': ['OAC', 'IRSA', 'MAST', 'SIMBAD'],
    'box_search': ['OAC', 'IRSA'] 
}


class RemoteServices():
    def __init__(self):
        self.services = {}
        self.query_parameters = {}

        for service in astroquery_services:
            service_name = service['service_name']
            service_class = globals()[f'Query{service_name}']
            self.services[service_name] = service_class()

        print(self.services)
    
    def addQuery(self, filters):
        for param in filters:
            if (param == 'ra/dec'):
                ra = filters[param][0]
                dec = filters[param][1]
                self.query_parameters['coordinates'] = coord.SkyCoord(f'{ra} {dec}', unit=(u.hourangle, u.deg))

            elif (param == 'search_type'):
                self.query_parameters['search_type'] = {}
                self.query_parameters['search_type']['type'] = filters['search_type']['type'] 
                if (filters['search_type']['type'] == 'cone_search'):
                    self.query_parameters['search_type']['radius'] = filters['search_type']['radius']*u.arcsec
                elif (filters['search_type']['type'] == 'box_search'):
                    self.query_parameters['search_type']['height'] = filters['search_type']['height']*u.arcsec
                    self.query_parameters['search_type']['width'] = filters['search_type']['width']*u.arcsec

                
    def startQuery(self):
        data = {}
        for service_instance in self.services:
            print(service_instance)
            if (service_instance in allowed_search_types[self.query_parameters['search_type']['type']]):
                data[service_instance] = self.services[service_instance].startQuery(self.query_parameters)

        return data


