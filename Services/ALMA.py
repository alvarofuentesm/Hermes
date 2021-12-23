from astroquery.alma import Alma


if __name__ == '__main__':
    import astropy.units as u
    import astropy.coordinates as coord
    
    
    test_coords = coord.SkyCoord('12:26:27.011 +31:13:20.55', unit=(u.hourangle, u.deg))
    test_radius = 10*u.arcsec
    test_height = 5*u.arcsec
    test_width = 30*u.arcsec

    ##
    if False: 
        orionkl = coord.SkyCoord('5:35:14.461 -5:21:54.41', frame='fk5',
                                unit=(u.hour, u.deg))
        result = Alma.query_region(orionkl, radius=0.034*u.deg)
        print(result)
        uid_url_table = Alma.get_data_info(result['obs_id'])
        
        # Extract the data with tarball file size < 1GB
        #small_uid_url_table = uid_url_table[uid_url_table['content_length'] < 10**9]
        small_uid_url_table = uid_url_table[uid_url_table['content_length'] < 10]
        # get the first 10 files...
        tarball_files = uid_url_table[uid_url_table['content_type'] == 'application/x-tar']
        print(tarball_files)
        #filelist = Alma.download_and_extract_files(tarball_files[1]['access_url'])
    
    if False:
        galactic_center = coord.SkyCoord(0*u.deg, 0*u.deg,
                                        frame='galactic')
        gc_data = Alma.query_region(galactic_center, 1*u.deg)
        print(len(gc_data))
        print(gc_data)
    
    orionkl = coord.SkyCoord('5:35:14.461 -5:21:54.41', frame='fk5',
                                unit=(u.hour, u.deg))
    result = Alma.query_region(orionkl, radius=0.034*u.deg)
    print(result['member_ous_uid'])
    uid_url_table = Alma.get_data_info(result['obs_id'][0:40])

    small_uid_url_table = uid_url_table[uid_url_table['content_length'] < 10**9]
    print(small_uid_url_table)
    
    tarball_files = small_uid_url_table[small_uid_url_table['content_type'] == 'application/x-tar']
    print(tarball_files)

    filelist = Alma.download_and_extract_files(tarball_files[1:10]['access_url'])
    print(filelist)
    '''
    print(uid_url_table.columns)
    print(uid_url_table['access_url'])

    files = Alma.download_and_extract_files(list(set(uid_url_table['access_url'])))
    '''


    if False:
        from astroquery.alma import Alma
        from astroquery.splatalogue import Splatalogue
        from astroquery.simbad import Simbad
        from astropy import units as u
        from astropy import constants
        from spectral_cube import SpectralCube

        m83table = Alma.query_object('M83', public=True)
        print(m83table.columns)
        m83urls = Alma.get_data_info(m83table['obs_id'])
        # Sometimes there can be duplicates: avoid them with
        # list(set())
        # also, to save time, we just download the first one
        print(m83urls['URL'])
        m83files = Alma.download_and_extract_files(list(set(m83urls['URL']))[0])
        m83files = m83files
        print("A")

        Simbad.add_votable_fields('rv_value')
        m83simbad = Simbad.query_object('M83')
        rvel = m83simbad['RV_VALUE'][0]*u.Unit(m83simbad['RV_VALUE'].unit)

        for fn in m83files:
            if 'line' in fn:
                cube = SpectralCube.read(fn)
                # Convert frequencies to their rest frequencies
                frange = u.Quantity([cube.spectral_axis.min(),
                                    cube.spectral_axis.max()]) * (1+rvel/constants.c)

                # Query the top 20 most common species in the frequency range of the
                # cube with an upper energy state <= 50K
                lines = Splatalogue.query_lines(frange[0], frange[1], top20='top20',
                                                energy_max=50, energy_type='eu_k',
                                                only_NRAO_recommended=True)
                lines.pprint()

                # Change the cube coordinate system to be in velocity with respect
                # to the rest frequency (in the M83 rest frame)
                rest_frequency = lines['Freq-GHz'][0]*u.GHz / (1+rvel/constants.c)
                vcube = cube.with_spectral_unit(u.km/u.s,
                                                rest_value=rest_frequency,
                                                velocity_convention='radio')

                # Write the cube with the specified line name
                fmt = "{Species}{Resolved QNs}"
                row = lines[0]
                linename = fmt.format(**dict(zip(row.colnames, row.data)))
                vcube.write('M83_ALMA_{linename}.fits'.format(linename=linename))