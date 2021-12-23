# https://astroquery.readthedocs.io/en/v0.1-0/sdss.html
from astroquery.sdss import SDSS

if __name__ == '__main__':
    import astropy.units as u
    import astropy.coordinates as coord

    test_coords = coord.SkyCoord('12:26:27.011 +31:13:20.55', unit=(u.hourangle, u.deg))
    test_radius = 10*u.arcsec
    test_height = 5*u.arcsec
    test_width = 30*u.arcsec      

    xid = SDSS.query_region(coordinates=test_coords, radius = test_radius, spectro=True)
    print(xid)
    
