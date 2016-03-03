import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import gridspec
from matplotlib import rc
rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
mpl.rcParams['font.size'] = 20.0

import readsmart
from .make_noise import make_noise
from .teleplanstar import Telescope, Planet, Star

def planetzoo(name='earth', telescope=Telescope(), planet=Planet(), itime=10.0, planetdir = '/astro/users/jlustigy/Models/coronagraph/planets/', plot=True, savedata=False, saveplot=False, ref_lam=0.55):
    '''
    planet choices: 
        earth, venus, archean,
        earlymars, hazyarchean, earlyvenus,
        jupiter, saturn, uranus, neptune, mars,
        fstarozone
    star choices (for now):
    sun, f2v
    '''

    whichplanet = name
    startype = planet.star
    tag = name

    if True:
        
        if whichplanet == 'earth':
            fn = 'earth_quadrature_radiance_refl.dat'
            model = np.loadtxt(planetdir+fn, skiprows=8)
            lamhr = model[:,0] 
            radhr = model[:,1] 
            solhr = model[:,2] 
            reflhr = model[:,3]
            Ahr   = np.pi*(np.pi*radhr/solhr) # hi-resolution reflectivity
            planet.Rp    = 1.0     # Earth radii
            planet.r     = 1.0     # semi-major axis (AU) 

        if whichplanet == 'venus':
            fn = 'Venus_geo_albedo.txt'
            model = np.loadtxt(planetdir+fn) 
            lamhr = model[:,0] 
            Ahr   = model[:,1]
            planet.Rp    = 0.95     #Earth radii
            planet.r     = 0.72     #semi-major axis (AU)

        if whichplanet == 'archean':
            fn = 'ArcheanEarth_geo_albedo.txt'
            model = np.loadtxt(planetdir+fn) 
            lamhr = model[:,0] 
            Ahr   = model[:,1]     	
            planet.Rp    = 1.0     #Earth radii
            planet.r     = 1.0     #semi-major axis (AU)

        if whichplanet == 'earlymars':
            fn = 'EarlyMars_geo_albedo.txt'
            model = np.loadtxt(planetdir+fn) 
            lamhr = model[:,0] 
            Ahr   = model[:,1]
            planet.Rp    = 0.53     #Earth radii
            planet.r     = 1.52     #semi-major axis (AU)

        if whichplanet == 'hazyarchean':
            fn = 'Hazy_ArcheanEarth_geo_albedo.txt'
            model = np.loadtxt(planetdir+fn) 
            lamhr = model[:,0] 
            Ahr   = model[:,1]     	
            planet.Rp    = 1.0     #Earth radii
            planet.r     = 1.0     #semi-major axis (AU)

        if whichplanet == 'earlyvenus':
            fn = 'EarlyVenus_geo_albedo.txt'
            model = np.loadtxt(planetdir+fn) 
            lamhr = model[:,0] 
            Ahr   = model[:,1]
            planet.Rp    = 0.95     #Earth radii
            planet.r     = 0.72     #semi-major axis (AU)

        if whichplanet == 'jupiter':
            fn = planetdir+'Jupiter_geo_albedo.txt'
            model = np.loadtxt(planetdir+fn) 
            lamhr = model[:,0] 
            Ahr   = model[:,1]
            planet.Rp    = 10.86     #Earth radii
            planet.r     = 5.20     #semi-major axis (AU)

        if whichplanet == 'saturn':
            fn = planetdir+'Saturn_geo_albedo.txt'
            model = np.loadtxt(planetdir+fn) 
            lamhr = model[:,0] 
            Ahr   = model[:,1]
            planet.Rp    = 9.00     #Earth radii
            planet.r     = 9.54     #semi-major axis (AU)

        if whichplanet == 'uranus':
            fn = 'Uranus_geo_albedo.txt'
            model = np.loadtxt(planetdir+fn) 
            lamhr = model[:,0] 
            Ahr   = model[:,1]
            planet.Rp    = 3.97     #Earth radii
            planet.r     = 19.19     #semi-major axis (AU)


        if whichplanet == 'warmuranus':
            fn = 'Uranus_geo_albedo.txt'
            model = np.loadtxt(planetdir+fn) 
            lamhr = model[:,0] 
            Ahr   = model[:,1]
            planet.Rp    = 3.97     #Earth radii
            planet.r     = 5.20     #semi-major axis (AU)
        
        if whichplanet == 'warmneptune':
            fn = 'Neptune_geo_albedo.txt'
            model = np.loadtxt(planetdir+fn) 
            lamhr = model[:,0] 
            Ahr   = model[:,1]
            planet.Rp    = 3.97     #Earth radii
            planet.r     = 5.20     #semi-major axis (AU)

        if whichplanet == 'neptune':
            fn = 'Neptune_geo_albedo.txt'
            model = np.loadtxt(planetdir+fn) 
            lamhr = model[:,0] 
            Ahr   = model[:,1]
            planet.Rp    = 3.85     #Earth radii
            planet.r     = 30.07     #semi-major axis (AU)


        if whichplanet == 'mars':
            fn = 'Mars_geo_albedo.txt'
            model = np.loadtxt(planetdir+fn) 
            lamhr = model[:,0] 
            Ahr   = model[:,1]
            planet.Rp    = 0.53     #Earth radii
            planet.r     = 1.52     #semi-major axis (AU)

        if whichplanet == 'fstarozone':
            print('fstarozone functionality not yet added') 
            #fn = 'fstarcloudy.sav'
            #fn = 'F2V_5.e-1fCO2_1.e6H2Volc_1.e10BIF.out_toa.rad'
            #READCOL, 'planets/'+fn, lamhr, wnhr, sunhr, fluxhr
            #restore, 'planets/'+fn
            #lamhr = reverse(wl_)
            #ahr = reverse(cloudyalb_)
            #Ahr = (2/3.) * fluxhr/(sunhr/2.) #geometric albedo & phase corrections
            #Rp    = 1.0     #Earth radii
            #r     = 1.72    #semi-major axis (AU)



    # star parameters
    if startype == '':
        Teff  = 5780.   #Sun-like Teff (K)
        Rs    = 1.      #star radius in solar radii
    if  startype == 'sun':
        Teff  = 5780.   #Sun-like Teff (K)
        Rs    = 1.      #star radius in solar radii
    if  startype == 'f2v':
        Teff  = 7050.   #Sun-like Teff (K)
        Rs    = 1.3      #star radius in solar radii
    
    star = Star(Teff=Teff, Rs=Rs)
 
    # Shawn: "I don't like noise.  It makes me sad."

    lam, dlam, A, q, Cratio, cp, csp, cz, cez, cD, cR, cth, DtSNR \
        = make_noise(Ahr, lamhr, telescope, planet, star, COMPUTE_LAM=True)

    # Calculate background photon count rate
    cb = (cz + cez + csp + cD + cR + cth)
    
    # Calculate the SNR of observation
    time = itime * 3600. # Convert hours to seconds
    SNR = calc_SNR(time, cp, cb)
    
    # Generate noisy spectrum by drawing data points from a normal distribution
    spec, sig = draw_noisy_spec(A, SNR)

    
    if plot:

        wlhr = lamhr
    
        # Set string for plot text
        if itime > 2.0:
            timestr = "{:.0f}".format(itime)+' hours'
        else:
            timestr = "{:.0f}".format(itime*60)+' mins'
        plot_text = r'Distance = '+"{:.1f}".format(planet.distance)+' pc'+\
        '\n Integration time = '+timestr
    
        # If a reference wavelength is specified then return the SNR at that wl 
        # corresponding to the integration time given
        if ref_lam:
            ireflam = find_nearest(lam,ref_lam)
            ref_SNR = SNR[ireflam] 
            plot_text = plot_text + '\n SNR = '+"{:.1f}".format(ref_SNR)+\
                ' at '+"{:.2f}".format(lam[ireflam])+r' $\mu$m'    
        
        # Plot observed spectrum; save pdf if saveplot=True 
        lammin,lammax = np.min(lam)-0.1, np.max(lam)+0.1
        Amin, Amax = np.min(A)-np.max(sig)*1.1, np.max(A)+np.max(sig)*1.1
        tmin = np.min(Ahr[(wlhr > lammin) & (wlhr < lammax)])
        tmax = np.max(Ahr[(wlhr > lammin) & (wlhr < lammax)])
        if tmin < Amin: Amin = tmin
        if tmax > Amax: Amax = tmax
        plot_tag = 'observed_'+tag+'.pdf'
        fig = plt.figure(figsize=(15,10))
        gs = gridspec.GridSpec(1, 1) 
        ax0 = plt.subplot(gs[0])
        ax0.plot(wlhr, Ahr, alpha=0.5, c='k')
        if telescope.mode != 'Imaging':
            ax0.plot(lam, A, alpha=0.7, color='orange', drawstyle='steps-mid', lw=2.0)
        else:
            ax0.plot(lam, A, 'o', alpha=0.7, color='orange', ms = 10.0)
            telescope.filter_wheel.plot(ax=ax0)
        ax0.errorbar(lam, spec, yerr=sig, fmt='o', color='k', ms=10.0)
        ax0.set_ylabel('Reflectivity')
        ax0.set_xlabel('Wavelength [$\mu$m]')
        ax0.set_title(tag)
        ax0.set_xlim([lammin,lammax])
        ax0.set_ylim([Amin, Amax])
        #ax0.set_ylim([-0.01,1.01])
        ax0.text(0.99, 0.99, plot_text,\
             verticalalignment='top', horizontalalignment='right',\
             transform=ax0.transAxes,\
             color='black', fontsize=20)
        # Save plot if saveplot==True
        if saveplot:
            fig.savefig(plot_tag)
            print 'Saved: '+plot_tag
        fig.show()
    
    # Save Synthetic data file (wavelength, albedo, error) if savedata=True
    if savedata:
        data_tag = 'observed_'+tag+'.txt'
        y_sav = np.array([lam,spec,sig])
        np.savetxt(data_tag, y_sav.T)
        print 'Saved: '+data_tag
    
    # Return Synthetic data and high-res spec
    
    return lam, spec, sig
    
def generate_observation(wlhr, Ahr, itime, telescope, planet, star,
                         ref_lam=0.55, tag='', plot=True, saveplot=False, savedata=False):    
    """
    Parameters
    ----------
    wlhr : float
        Wavelength array (microns)
    Ahr : float
        Geometric albedo spectrum array
    itime : float
        Integration time (hours)
    telescope : Telescope
        Telescope object
    planet : Planet
        Planet object
    star : Star 
        Star object
    tag : string
        ID for output files
    plot : boolean
        Set to True to make plot
    saveplot : boolean
        Set to True to save the plot as a PDF
    savedata : boolean
        Set to True to save data file of observation
    
    Returns
    -------
    lam : array
        Wavelength grid of observed spectrum
    spec : array
        Albedo grid of observed spectrum
    sig : array
        One sigma errorbars on albedo spectrum
    
    Output
    ------
    If saveplot=True then plot will be saved
    If savedata=True then data will be saved
    """
    
    # Skip call_noise and just call: noise 
    lam, dlam, A, q, Cratio, cp, csp, cz, cez, cD, cR, cth, DtSNR = \
        make_noise(Ahr, wlhr, telescope, planet, star, wantsnr=10.0, COMPUTE_LAM=True)
        
    # Calculate background photon count rate
    cb = (cz + cez + csp + cD + cR + cth)
    
    # Calculate the SNR of observation
    time = itime * 3600. # Convert hours to seconds
    SNR = calc_SNR(time, cp, cb)
    
    # Generate noisy spectrum by drawing data points from a normal distribution
    spec, sig = draw_noisy_spec(A, SNR)

    
    if plot:
    
        # Set string for plot text
        if itime > 2.0:
            timestr = "{:.0f}".format(itime)+' hours'
        else:
            timestr = "{:.0f}".format(itime*60)+' mins'
        plot_text = r'Distance = '+"{:.1f}".format(planet.distance)+' pc'+\
        '\n Integration time = '+timestr
    
        # If a reference wavelength is specified then return the SNR at that wl 
        # corresponding to the integration time given
        if ref_lam:
            ireflam = find_nearest(lam,ref_lam)
            ref_SNR = SNR[ireflam] 
            plot_text = plot_text + '\n SNR = '+"{:.1f}".format(ref_SNR)+\
                ' at '+"{:.2f}".format(lam[ireflam])+r' $\mu$m'    
        
        # Plot observed spectrum; save pdf if saveplot=True 
        lammin,lammax = np.min(lam)-0.1, np.max(lam)+0.1
        Amin, Amax = np.min(A)-np.max(sig)*1.1, np.max(A)+np.max(sig)*1.1
        tmin = np.min(Ahr[(wlhr > lammin) & (wlhr < lammax)])
        tmax = np.max(Ahr[(wlhr > lammin) & (wlhr < lammax)])
        if tmin < Amin: Amin = tmin
        if tmax > Amax: Amax = tmax
        plot_tag = 'observed_'+tag+'.pdf'
        fig = plt.figure(figsize=(15,10))
        gs = gridspec.GridSpec(1, 1) 
        ax0 = plt.subplot(gs[0])
        ax0.plot(wlhr, Ahr, alpha=0.5, c='k')
        if telescope.mode != 'Imaging':
            ax0.plot(lam, A, alpha=0.7, color='orange', drawstyle='steps-mid', lw=2.0)
        else:
            ax0.plot(lam, A, 'o', alpha=0.7, color='orange', ms = 10.0)
            telescope.filter_wheel.plot(ax=ax0)
        ax0.errorbar(lam, spec, yerr=sig, fmt='o', color='k', ms=10.0)
        ax0.set_ylabel('Reflectivity')
        ax0.set_xlabel('Wavelength [$\mu$m]')
        ax0.set_xlim([lammin,lammax])
        ax0.set_ylim([Amin, Amax])
        #ax0.set_ylim([-0.01,1.01])
        ax0.text(0.99, 0.99, plot_text,\
             verticalalignment='top', horizontalalignment='right',\
             transform=ax0.transAxes,\
             color='black', fontsize=20)
        # Save plot if saveplot==True
        if saveplot:
            fig.savefig(plot_tag)
            print 'Saved: '+plot_tag
        fig.show()
    
    # Save Synthetic data file (wavelength, albedo, error) if savedata=True
    if savedata:
        data_tag = 'observed_'+tag+'.txt'
        y_sav = np.array([lam,spec,sig])
        np.savetxt(data_tag, y_sav.T)
        print 'Saved: '+data_tag
    
    # Return Synthetic data and high-res spec
    
    return lam, spec, sig
    

def smart_observation(radfile, itime, telescope, planet, star,
                         ref_lam=0.55, tag='', plot=True, saveplot=False, savedata=False):   
    """Uses coronagraph noise model to create an observation of high resolution SMART output.
    
    Parameters
    ----------
    radfile : string
        Location and name of file to be read in
    itime : float
        Integration time (hours)
    telescope : Telescope
        Telescope object
    planet : Planet
        Planet object
    star : Star 
        Star object
    tag : string
        ID for output files
    plot : boolean
        Set to True to make plot
    saveplot : boolean
        Set to True to save the plot as a PDF
    savedata : boolean
        Set to True to save data file of observation
    
    Returns
    ----------
    lam : array
        Wavelength grid of observed spectrum
    spec : array
        Albedo grid of observed spectrum
    sig : array
        One sigma errorbars on albedo spectrum
    rwl : array
        Wavelength grid of SMART output
    Ahr : array
        Albedo grid of SMART output
    
    Output
    ---------
    If saveplot=True then plot will be saved
    If savedata=True then data will be saved
    """

    # Read-in .rad file
    wlhr, wno, solar_spec, TOA_flux, rad_streams = readsmart.rad(radfile,getdata=True)
    
    # Calculate Hi-res reflectivity spectrum
    Ahr = (TOA_flux / solar_spec) * np.pi / planet.Phi
    
    # Skip call_noise and just call: noise 
    lam, dlam, A, q, Cratio, cp, csp, cz, cez, cD, cR, cth, DtSNR = \
        make_noise(Ahr, wlhr, telescope, planet, star, wantsnr=10.0, COMPUTE_LAM=True)
        
    # Calculate background photon count rate
    cb = (cz + cez + csp + cD + cR + cth)
    
    # Calculate the SNR of observation
    time = itime * 3600. # Convert hours to seconds
    SNR = calc_SNR(time, cp, cb)
    
    # Generate noisy spectrum by drawing data points from a normal distribution
    spec, sig = draw_noisy_spec(A, SNR)

    if plot:
    
        # Set string for plot text
        if itime > 2.0:
            timestr = "{:.0f}".format(itime)+' hours'
        else:
            timestr = "{:.0f}".format(itime*60)+' mins'
        plot_text = r'Distance = '+"{:.1f}".format(planet.distance)+' pc'+\
        '\n Integration time = '+timestr
    
        # If a reference wavelength is specified then return the SNR at that wl 
        # corresponding to the integration time given
        if ref_lam:
            ireflam = find_nearest(lam,ref_lam)
            ref_SNR = SNR[ireflam]  
            plot_text = plot_text + '\n SNR = '+"{:.1f}".format(ref_SNR)+\
                ' at '+"{:.2f}".format(lam[ireflam])+r' $\mu$m'    
        
        # Plot observed spectrum; save pdf if saveplot=True 
        lammin,lammax = np.min(lam)-0.1, np.max(lam)+0.1
        Amin, Amax = np.min(A)-np.max(sig)*1.1, np.max(A)+np.max(sig)*1.1
        tmin = np.min(Ahr[(wlhr > lammin) & (wlhr < lammax)])
        tmax = np.max(Ahr[(wlhr > lammin) & (wlhr < lammax)])
        if tmin < Amin: Amin = tmin
        if tmax > Amax: Amax = tmax
        #ymin,ymax = np.min(A), np.max(A)
        plot_tag = 'observed_smart_'+tag+'.pdf'
        fig = plt.figure(figsize=(15,10))
        gs = gridspec.GridSpec(1, 1) 
        ax0 = plt.subplot(gs[0])
        ax0.plot(wlhr, Ahr, alpha=0.5, c='k')
        if telescope.mode != 'Imaging':
            ax0.plot(lam, A, alpha=0.7, color='orange', drawstyle='steps-mid', lw=2.0)
        else:
            ax0.plot(lam, A, 'o', alpha=0.7, color='orange', ms = 10.0)
            telescope.filter_wheel.plot(ax=ax0)
        ax0.errorbar(lam, spec, yerr=sig, fmt='o', color='k', ms=10.0)
        ax0.set_ylabel('Reflectivity')
        ax0.set_xlabel('Wavelength [$\mu$m]')
        ax0.set_xlim([lammin,lammax])
        ax0.set_ylim([Amin, Amax])
        #ax0.set_ylim([-0.01,ymax+0.1])
        #ax0.set_ylim([-0.01,1.01])
        ax0.text(0.99, 0.99, plot_text,\
             verticalalignment='top', horizontalalignment='right',\
             transform=ax0.transAxes,\
             color='black', fontsize=20)
        # Save plot if saveplot==True
        if saveplot:
            fig.savefig(plot_tag)
            print 'Saved: '+plot_tag
        fig.show()
    
    # Save Synthetic data file (wavelength, albedo, error) if savedata=True
    if savedata:
        data_tag = 'observed_smart_'+tag+'.txt'
        y_sav = np.array([lam,spec,sig])
        np.savetxt(data_tag, y_sav.T)
        print 'Saved: '+data_tag
    
    # Return Synthetic data and high-res spec
    
    return lam, spec, sig, wlhr, Ahr
    
def calc_SNR(itime, cp, cb, poisson=2.):
    
    cnoise = cp + poisson*cb
    SNR = cp*itime / np.sqrt(cnoise*itime)
    
    return SNR

def draw_noisy_spec(spectrum, SNR, apparent=False):
    
    if apparent:
        # Scale geometric albedo to apparent albedo (as if lambertian sphere) for quadrature
        scale = 3.*np.pi/2.
    else:
        scale = 1.0  
    
    # Compute "sigma"
    sigma = scale * spectrum / SNR
    # Draw data points from normal distribution    
    spec_noise = np.random.randn(len(spectrum))*sigma + scale*spectrum
    
    return spec_noise, sigma

def find_nearest(array,value):
    idx = (np.abs(array-value)).argmin()
    return idx
