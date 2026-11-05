# -*- coding: utf-8 -*-
"""
    Gas Solubility Package for Python
        Version 1.0 Feb 16, 2016
        Author:  Brice Loose, Graduate School of Oceanography, URI.
        Email: bloose@uri.edu
    
    % ch4_solubility   Solubility of Methane in sea water
    %=========================================================================
    % - Calculate solubility (Bunsen Coefficient) of methane in sea water.
    %- OUTPUT:  Bunsen solubility coefficient (vol/vol) and temperature and 
    %- salinity given by T,S (inputs).
    %
    %
    %- SOURCE:  Yamamoto, S. et al. (1976) Solubility of Methane in Distilled 
    %- Water and Seawater, Journal of Chemical Engineering Data, Vol. 21(1).
    % DISCLAIMER:
    %    This software is provided "as is" without warranty of any kind.  
    %=========================================================================
"""
def ch4_solubility(T, S):

    import numpy as np


    T = np.add(T,273.16)

    
    a1 = -67.1962;
    a2 = 99.1624;
    a3 = 27.9015;
    a4 = 0;
    
    b1 = -0.072909;
    b2 = 0.041674;
    b3 = -0.0064603;

    lnC = a1 + a2*100/T + a3*np.log(T/100) + a4*T/100+ S *(b1 + b2*T/100 + b3*np.power((T/100),2));

    sol = np.exp(lnC);
    
    # Add a conversion from L/L to mol/L using ideal gas law.
    
    return sol

    