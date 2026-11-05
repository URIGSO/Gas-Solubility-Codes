# -*- coding: utf-8 -*-
"""
Gas Solubility Package for Python
        Version 1.0 May 8, 2017
        Author:  Samuel Gartzman, Graduate School of Oceanography, URI.
        Email: sgartzman@uri.edu

    Many of the functions included here were ported from Brice Loose's
    Matlab Solubility functions. Brice Loose (bloose@uri.edu)
    
    % CO2sol   Solubility of CO2 in sea water
    %=========================================================================
    %
    % USAGE:  [Ko] = CO2sol(S,T)
    %
    % DESCRIPTION:
    %    Solubility (saturation) of Carbon dioxide (CO2) in sea water
    %    
    %
    % INPUT:  (if S and T are not singular they must have same dimensions)
    %   S = salinity    [PSS]
    %   T = temperature [degree C]
    %
    % OUTPUT:
    %   Ko = Ko, where C_liquid = Ko*Pp,  Pp = gas partial pressure
    %   [mols/L/atm]
    % 
    %
    % REFERENCE:
    %    Weiss, R.F, (1974).  Carbon Dioxide in water and seawater: The
    %    Solubility of a non-ideal gas.  Marine Chemistry V.2, pp.203-15
    %
    % DISCLAIMER:
    %    This software is provided "as is" without warranty of any kind.  
    %=========================================================================

"""
def CO2sol(S, T):

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
        print ("CO2sol: S & T must have same dimensions or be singular")
        return

    #------
    # BEGIN
    #------
    
    # convert T to scaled temperature
    temp_S = T + 273.15
    
    # constants from Table 4 of Hamme and Emerson 2004
    a1 = -58.0931
    a2 = 90.5069
    a3 = 22.2940

    b1 = 0.027766
    b2 = -0.025888
    b3 = 0.0050578


    # Eqn (1) of Hamme and Emerson 2004
    lnKo = a1 + a2 * 100.0/temp_S + a3 * np.log(temp_S/100.0) + S * (b1 + b2*temp_S/100.0 + b3*(temp_S/100)**2)
    Ko = np.exp(lnKo)
    return Ko