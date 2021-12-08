# https://astroquery.readthedocs.io/en/latest/mast/mast.html

from astroquery.mast import Observations
    
if __name__ == '__main__':
    '''
    ['BEFS', 'EUVE', 'FUSE', 'GALEX', 'HLA', 'HLSP', 'HST', 'HUT', 'IUE', 'JWST', 
    'K2', 'K2FFI', 'Kepler', 'KeplerFFI', 'PS1', 'SPITZER_SHA', 'SWIFT', 'TESS', 
    'TUES', 'WUPPE']
    '''
    print(Observations.list_missions())