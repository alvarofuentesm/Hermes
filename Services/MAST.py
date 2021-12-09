# https://astroquery.readthedocs.io/en/latest/mast/mast.html
# https://mast.stsci.edu/api/v0/_c_a_o_mfields.html

from astroquery.mast import Observations

class QueryMAST():
    def startQuery(self, query_parameters):
        print("Start query MAST")
        if (query_parameters['search_type']['type'] == 'cone_search'):
            table = Observations.query_criteria(coordinates = query_parameters['coordinates'],
                                     radius = query_parameters['search_type']['radius'],  dataproduct_type = "timeseries")
        else:
            table = None
        # TO-DO: box search
        return table
    

if __name__ == '__main__':
    import numpy as np
    import astropy.units as u
    import astropy.coordinates as coord

    '''
    ['BEFS', 'EUVE', 'FUSE', 'GALEX', 'HLA', 'HLSP', 'HST', 'HUT', 'IUE', 'JWST', 
    'K2', 'K2FFI', 'Kepler', 'KeplerFFI', 'PS1', 'SPITZER_SHA', 'SWIFT', 'TESS', 
    'TUES', 'WUPPE']
    '''

    test_coords = coord.SkyCoord('12:26:27.011 +31:13:20.55', unit=(u.hourangle, u.deg))
    test_radius = 10*u.arcsec

    print(Observations.list_missions())

    table = Observations.query_criteria(coordinates = test_coords, radius = test_radius,  dataproduct_type = "timeseries")
    print(table)
    print(np.unique(table['provenance_name']))