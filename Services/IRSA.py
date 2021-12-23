# https://astroquery.readthedocs.io/en/v0.1-0/irsa.html
# https://astroquery.readthedocs.io/en/v0.1-0/_generated/astroquery.irsa.core.Irsa.html#astroquery.irsa.core.Irsa.query_region
# https://irsa.ipac.caltech.edu/cgi-bin/Gator/nph-dd
# https://irsa.ipac.caltech.edu/workspace/TMP_3SAToV_4699/Gator/irsa/25122/tbview.html
from astroquery.ipac.irsa import Irsa

class QueryIRSA():
    def __init__(self):
        self.available_data_types = ['timeseries']

    def startQuery(self, query_parameters):
        print("Start query IRSA")
        print("Start query SIMBAD")
        full_data = {}
        for type in self.available_data_types: 
            print("query ", type)
            full_data[type] = []

            if (type == "timeseries"):
                my_catalog = 'ptf_lightcurves'
            else:
                my_catalog = ''

            if (query_parameters['search_type']['type'] == 'cone_search'):
                table = Irsa.query_region( query_parameters['coordinates'],
                        catalog = my_catalog, spatial='Cone',
                        radius=query_parameters['search_type']['radius'])
            elif (query_parameters['search_type']['type'] == 'box_search'):
                table = Irsa.query_region( query_parameters['coordinates'],
                        catalog = my_catalog, spatial='Box',
                        width=query_parameters['search_type']['width'])
            else:
                continue 
            
            # TO-DO: box search
            data_ = {}
            data_["header"] = None
            data_["data"] = table.copy()
            full_data[type].append( data_.copy() )
 
        return full_data

if __name__ == '__main__':
    import astropy.units as u
    import numpy as np
    import astropy.coordinates as coord

    #Irsa.print_catalogs()
    '''
    ptf_lightcurves                 PTF Lightcurve Table
    ptf_sources                     PTF Sources Catalog
    ptf_objects                     PTF Objects
    '''
    #https://irsa.ipac.caltech.edu/workspace/TMP_3SAToV_4699/Gator/irsa/25122/tbview.html
    '''
    table = Irsa.query_region("20h 49m 20.07s -01d 04m 43.3s",
                    catalog='ptf_lightcurves', spatial='Box',
                    width=5 * u.arcsec)
    '''
    ra = 312.333629
    dec = -1.078686
    #ra = 197.45037
    #dec = -23.38148
    #test_coords = coord.SkyCoord(ra=ra, dec=dec, unit=(u.deg, u.deg))
    #test_coords = coord.SkyCoord('21:23:32.16 -53:01:36.08', unit=(u.hourangle, u.deg))
    test_coords = coord.SkyCoord('12:26:27.011 +31:13:20.55', unit=(u.hourangle, u.deg))
    test_radius = 10*u.arcsec
    test_height = 5*u.arcsec
    test_width = 5*u.arcsec

    
    #table = Irsa.query_region(test_coords,
    #                catalog='ptf_lightcurves', spatial='Box',
    #                width=test_width)
    table = Irsa.query_region(test_coords,
                    catalog='ptf_lightcurves', spatial='Cone',
                    radius=test_radius)

    print(table)

    #print(table.columns)   # Dict of table columns (access by column name, index, or slice)
    print(table.colnames)  # List of column names
    print(table.columns) 
    print(len(table))      # Number of table rows

    #print(table.meta)      # Dict of meta-data

    print(np.unique(table['oid'])) # oid: Unique object identifier