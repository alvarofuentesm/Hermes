# https://astroquery.readthedocs.io/en/latest/oac/oac.html
# https://astroquery.readthedocs.io/en/latest/api/astroquery.oac.OACClass.html#astroquery.oac.OACClass

from astroquery.oac import OAC


if __name__ == '__main__':
    metadata = OAC.query_object("GW170817")
    print(metadata)

