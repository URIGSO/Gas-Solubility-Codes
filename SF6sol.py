#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
    Gas Solubility Package for Python
        Version 1.1 Mar 21, 2017
        Maintainer:  Brice Loose, Graduate School of Oceanography, URI.
        Email: bloose@uri.edu
        
    #=========================================================================
    # SF6sol   Solubility of SF6 in sea water
    #=========================================================================         
    # USAGE:  concSF6 = SF6sol(S,T, Moist)
              Author:  Samuel Gartzman, Graduate School of Oceanography, URI.
              Email: sgartzman@uri.edu

    #
    # DESCRIPTION:
    #    Solubility (saturation) of Sulfur hexafluoride (SF6) in sea water 
    #    at 1-atm pressure of air including saturated water vapor
    #
    # INPUT:  (if S and T are not singular they must have same dimensions)
    #   S = salinity    [PSS]
    #   T = temperature [degree C]
    #
    # OUTPUT:
    #   concSF6 = solubility of SF6  [mol/Kg]
    # 
    #
    # REFERENCE:
    # Busenberg and Plummer (2008), Dating groundwater with trifluoromethyl 
    # sulfurpentafluoride (SF5CF3), sulfur hexafluoride (SF6), CF3Cl (CFC-13),
    # and CF2Cl2 (CFC-12).  WATER RESOURCES RESEARCH, VOL. 44, W02431, 
    # doi:10.1029/2007WR006150, 2008
    #
    # DISCLAIMER:
    #    This software is provided "as is" without warranty of any kind.  
    #=========================================================================
"""

def SF6sol(S, T):

    import numpy as np

    #----------------------
    # Check input parameters
    #----------------------

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
        print "SF6sol: S & T must have same dimensions or be singular"
        return

    #------
    # BEGIN
    #------
    # convert T to scaled temperature
    T = np.add(T,273.15)
    
    a1 = -82.16390000
    a2 = 120.15200000
    a3 = 30.63720000
    
    b1 = 0.02932010
    b2 = -0.03519740
    b3 = 0.00740056
    
    lnC= a1 + a2*(100/T) + a3*np.log(T/100) + np.multiply(S,(b1+b2*(T/100)+b3*(T/100)**2))
    sol=np.exp(lnC)
    return sol