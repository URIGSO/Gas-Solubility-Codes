# -*- coding: utf-8 -*-
"""
    Gas Solubility Package for Python
        Version 1.1 Mar 21, 2017
        Maintainer:  Brice Loose, Graduate School of Oceanography, URI.
        Email: bloose@uri.edu

    Many of the functions included here were ported from Roberta Hamme's
    Matlab Solubility functions. Roberta Hamme (rhamme@uvic.ca)
    
    % N2sol   Solubility of N2 in sea water
    %=========================================================================
    % N2sol Version 1.2 4/4/2005
    # USAGE:  concSF6 = SF6sol(S,T, Moist)
              Author:  Samuel Gartzman, Graduate School of Oceanography, URI.
              Email: sgartzman@uri.edu
    %
    % USAGE:  concN2 = N2sol(S,T)
    %
    % DESCRIPTION:
    %    Solubility (saturation) of Nitrogen (N2) in sea water
    %    at 1-atm pressure of air including saturated water vapor
    %
    % INPUT:  (if S and T are not singular they must have same dimensions)
    %   S = salinity    [PSS]
    %   T = temperature [degree C]
    %
    % OUTPUT:
    %   concN2 = solubility of N2 [umol/kg] 
    % 
    %
    % REFERENCE:
    %    Roberta Hamme and Steve Emerson, 2004.
    %    "The solubility of neon, nitrogen and argon in distilled water and seawater."
    %    Deep-Sea Research I, 51(11), p. 1517-1528.
    %
    % DISCLAIMER:
    %    This software is provided "as is" without warranty of any kind.  
    %=========================================================================

"""
def N2sol(S, T):

    import numpy as np

    #----------------------
    # Check input parameters
    #----------------------
    #Python Takes care of this...

    # CHECK S,T dimensions and verify consistent
    if np.size(np.shape(T))>1:
        mt,nt=np.shape(T)
    else:
        mt = np.size(T)
        nt = 0
    if np.size(np.shape(S))>1:
        ms,ns=np.shape(S)
    else:
        ms = np.size(S)
        ns = 0

    # Check that T&S have the same shape or are singular
    if (ms != mt) or (ns != nt):
        print "N2sol: S & T must have same dimensions or be singular"
        return

    #------
    # BEGIN
    #------
    
    # convert T to scaled temperature
    temp_S = np.log(np.subtract(298.15,T) / np.add(273.15,T))
    
    # constants from Table 4 of Hamme and Emerson 2004
    A0_n2 = 6.42931
    A1_n2 = 2.92704
    A2_n2 = 4.32531
    A3_n2 = 4.69149
    B0_n2 = -7.44129e-3
    B1_n2 = -8.02566e-3
    B2_n2 = -1.46775e-2


    # Eqn (1) of Hamme and Emerson 2004
    conc_N2 = np.exp(A0_n2 + A1_n2 * temp_S + A2_n2 * np.power(temp_S,2) + A3_n2*np.power(temp_S,3) + S * (B0_n2 + B1_n2 * temp_S + B2_n2 * np.power(temp_S,2)))

    return conc_N2