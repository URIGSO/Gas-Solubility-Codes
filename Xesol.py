# -*- coding: utf-8 -*-
"""
    Gas Solubility Package for Python
        Version 2.0 October, 2022
        Author:  Brice Loose, Graduate School of Oceanography, URI.
        Email: bloose@uri.edu

    These noble gas solubility functions are being updated to reflect the new
    solubility determinations for He, Ne, Ar, Kr, and Xe from 
    Jenkins et al., (2019).  These replace the prio relationships developed by
    Roberta Hamme.
    
    #=========================================================================
    # Hesol   Solubility of Kr in sea water
    #=========================================================================
    #
    # USAGE:  concNe = Xesol(S,T)
    #
    # DESCRIPTION:
    #    Solubility (saturation) of Xenon (Xe) in sea water 
    #    at 1-atm pressure of air including saturated water vapor
    #
    # INPUT:  (if S and T are not singular they must have same dimensions)
    #   S = salinity    [PSS]
    #   T = temperature [degree C]
    #
    # OUTPUT:
    #   concHe = solubility of Xe  [umol/kg] 
    # 
    #
    # REFERENCE:
    #    Jenkins, W., Lott, D.E., Cahill, K.L. (2019) A determination of 
    # atmospheric helium, neon, argon, krypton, and xenon solubility 
    # concentrations in water and seawater.  Marine Chemistry,
    # DOI: https://doi.org/10.1016/j.marchem.2019.03.007
    #
    # DISCLAIMER:
    #    This software is provided "as is" without warranty of any kind.  
    #=========================================================================
"""


def Xesol(S, T):

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
        print ("Xesol: S & T must have same dimensions or be singular")
        return

    #------
    # BEGIN
    #------

    # convert T to scaled temperature
    temp_abs = np.add(T,273.15)/100

    A1 = -224.5100
    A2 = 292.8234
    A3 = 157.6127
    A4 = -22.66895
    B1 = -0.084915
    B2 = 0.047996
    B3 = -0.0073595
    C1 = 6.69e-6

    # Eqn (2) of Weiss and Kyser
    conc_Xe = np.exp(A1 + (A2 / temp_abs) +
                     (A3 * np.log(temp_abs)) + 
                     (A4 * temp_abs) + S*(B1 +
                    (B2 * temp_abs) + 
                    (B3 * np.power(temp_abs,2))) + C1*S**2)

    
    return conc_Xe*1e6  # OUTPUT IN umol/kg

    