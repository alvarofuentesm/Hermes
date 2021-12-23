# https://astroquery.readthedocs.io/en/latest/oac/oac.html
# https://astroquery.readthedocs.io/en/latest/api/astroquery.oac.OACClass.html#astroquery.oac.OACClass

from astroquery.oac import OAC

class QueryOAC():
    def __init__(self):
        self.available_data_types = ['timeseries']

    def startQuery(self, query_parameters):
        print("Start query OAC")
        full_data = {}
        for type in self.available_data_types: 
            print("query ", type)
            full_data[type] = []

            if (query_parameters['search_type']['type'] == 'cone_search'):
                table = OAC.query_region(coordinates=query_parameters['coordinates'],
                                    radius = query_parameters['search_type']['radius'],
                                    quantity="photometry",
                                    attribute=["time", "magnitude",
                                                "e_magnitude", "band",
                                                "instrument"])

            elif (query_parameters['search_type']['type'] == 'box_search'):
                table = OAC.query_region(coordinates=query_parameters['coordinates'],
                                    width = query_parameters['search_type']['width'],
                                    height = query_parameters['search_type']['height'],
                                    quantity="photometry",
                                    attribute=["time", "magnitude",
                                                "e_magnitude", "band",
                                                "instrument"])

            else:
                continue
            
            data_ = {}
            data_["header"] = None
            data_["data"] = table.copy()
            full_data[type].append( data_.copy() )


        return full_data


if __name__ == '__main__':
    import astropy.units as u
    import astropy.coordinates as coord
    

    #metadata = OAC.query_object("GW170817")
    
    #print(metadata)

    '''
    photometry = OAC.query_object("GW170817", quantity="photometry",
                                  attribute=["time", "magnitude",
                                             "e_magnitude", "band",
                                             "instrument"])
    '''
    
    #ra = 312.333629
    #dec = -1.078686
    # catalog?ra=21:23:32.16&dec=-53:01:36.08&radius=2
    # 12:26:27.011 +31:13:20.55
    
    #ra = 197.45037
    #dec = -23.38148
    #test_coords = coord.SkyCoord(ra=ra, dec=dec, unit=(u.deg, u.deg)) 
    test_coords = coord.SkyCoord('12:26:27.011 +31:13:20.55', unit=(u.hourangle, u.deg))
    test_radius = 10*u.arcsec
    test_height = 5*u.arcsec
    test_width = 30*u.arcsec
    photometry_table = OAC.query_region(coordinates=test_coords,
                                  #width=test_width, height=test_height, # box
                                  radius = test_radius, # cone
                                  quantity="photometry",
                                  attribute=["time", "magnitude",
                                             "e_magnitude", "band",
                                             "instrument"])

    print(photometry_table.columns)

        

