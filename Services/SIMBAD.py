# https://astroquery.readthedocs.io/en/latest/simbad/simbad.html

from astropy import coordinates
from astroquery.simbad import Simbad


class QuerySIMBAD():
    def startQuery(self, query_parameters):
        print("Start query SIMBAD")
        if (query_parameters['search_type']['type'] == 'cone_search'):
            table = Simbad.query_region(coordinates = query_parameters['coordinates'], 
                                            radius=query_parameters['search_type']['radius'])
        else:
            table = None    
        
        return table

if __name__ == '__main__':
    import astropy.units as u
    import astropy.coordinates as coord

    test_coords = coord.SkyCoord('12:26:27.011 +31:13:20.55', unit=(u.hourangle, u.deg))
    test_radius = 10*u.arcsec
    test_height = 5*u.arcsec
    test_width = 5*u.arcsec
    
    
    table = Simbad.query_region(coordinates = test_coords, radius=test_radius)
    print(table)


