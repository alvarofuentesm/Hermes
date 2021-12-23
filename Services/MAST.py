# https://astroquery.readthedocs.io/en/latest/mast/mast.html
# https://mast.stsci.edu/api/v0/_c_a_o_mfields.html

from astroquery.mast import Observations

class QueryMAST():
    def __init__(self):
        self.available_data_types = ['timeseries', 'spectrum']

    def startQuery(self, query_parameters):
        print("Start query MAST")
        if (query_parameters['search_type']['type'] == 'cone_search'):
            table = Observations.query_criteria(coordinates = query_parameters['coordinates'],
                                     radius = query_parameters['search_type']['radius'],  dataproduct_type = "timeseries")
        else:
            table = None
        
        return table
    

if __name__ == '__main__':
    import numpy as np
    import astropy.units as u
    import astropy.coordinates as coord
    from astropy.io import fits

    from astropy.visualization import astropy_mpl_style
    import matplotlib.pyplot as plt

    plt.style.use(astropy_mpl_style)


    '''
    ['BEFS', 'EUVE', 'FUSE', 'GALEX', 'HLA', 'HLSP', 'HST', 'HUT', 'IUE', 'JWST', 
    'K2', 'K2FFI', 'Kepler', 'KeplerFFI', 'PS1', 'SPITZER_SHA', 'SWIFT', 'TESS', 
    'TUES', 'WUPPE']
    '''

    test_coords = coord.SkyCoord('12:26:27.011 +31:13:20.55', unit=(u.hourangle, u.deg))
    test_radius = 10*u.arcsec

    print(Observations.list_missions())

    #type = "spectrum" 
    type = "timeseries"
    #table = Observations.query_criteria(coordinates = test_coords, radius = test_radius,  dataproduct_type = "timeseries")
    table = Observations.query_criteria(coordinates = test_coords, radius = test_radius,  dataproduct_type = type)
    print(table)
    print(np.unique(table['provenance_name']))

    print(len(table))
    print(len(table[0:10]))
    data_products_by_obs = Observations.get_product_list(table[0]) # the first one
    print(data_products_by_obs)

    manifest = Observations.download_products(data_products_by_obs)

    print(manifest)

    for i, filename in enumerate(manifest['Local Path']):
        if (filename.endswith('.fits') ):
            hdul = fits.open(filename)  # open a FITS file
            data = hdul[1].data
            print(data)
            if (data is None):
                hdul.close()
                continue    
            print(filename)
            #print(hdul[1].name)
            print(hdul[1].header)
            print(data.shape)
            if (len(data.shape) == 2):
                plt.figure()
                plt.title(manifest['obs_id'][i] + '\n' + manifest['dataproduct_type'][i])
                plt.imshow(data, cmap='viridis')
                plt.colorbar()
                plt.show()
            if (type == "timeseries"):
                print(data.columns)

            hdul.close()