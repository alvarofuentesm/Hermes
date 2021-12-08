from astroquery.simbad import Simbad
from astroquery.vizier import Vizier
from astropy import coordinates
from astropy import units as u
import astropy.coordinates as coord

if False:
    result_table = Simbad.query_object("m [1-9]", wildcard=True)
    print(result_table)


    result_table = Simbad.query_region("m81", radius=0.1 * u.deg)
    # another way to specify the radius.
    result_table = Simbad.query_region("m81", radius='0d6m0s')
    print(result_table)

if False:
    v = Vizier(keywords=['stars:white_dwarf'])

    c = coordinates.SkyCoord(0, 0, unit=('deg', 'deg'), frame='icrs')
    result = v.query_region(c, radius=2*u.deg)

    print(len(result))

    print(result[0].pprint())


if False:
    from astroquery.oac import OAC
    metadata = OAC.query_object("GW170817")
    print(metadata)


    photometry = OAC.query_object("GW170817", quantity="photometry",
                                    attribute=["time", "magnitude",
                                                "e_magnitude", "band",
                                                "instrument"])

    print(photometry)


    ra = 197.45037
    dec = -23.38148
    test_coords = coord.SkyCoord(ra=ra, dec=dec, unit=(u.deg, u.deg))
    test_radius = 10*u.arcsec
    test_height = 10*u.arcsec
    test_width = 10*u.arcsec

    photometry = OAC.query_region(coordinates=test_coords,
                                    radius=test_radius,
                                    quantity="photometry",
                                    attribute=["time", "magnitude",
                                                "e_magnitude", "band",
                                                "instrument"])

    print(photometry)

#To get back all Observations containing TESS Mission light curves from sector 14

if False:
    from astroquery.mast import Observations
    obs = Observations.query_criteria(obs_collection = 'TESS', sequence_number = [14], dataproduct_type = "timeseries")

    print(obs)

if True:
    from astroquery.mast import Observations
    print(Observations.list_missions())