# -*- coding: utf-8 -*-
"""
    Gas Solubility Package for Python
        Version 1.0 Feb 16, 2016
        Author:  Brice Loose, Graduate School of Oceanography, URI.
        Email: bloose@uri.edu

    Many of the functions included here were ported from Roberta Hamme's
    Matlab Solubility functions. Roberta Hamme (rhamme@uvic.ca)
    
    % O2sol   Solubility of O2 in sea water
    %=========================================================================
    % O2sol Version 1.1 4/4/2005
    %          Author: Roberta C. Hamme (Scripps Inst of Oceanography)
    %
    % USAGE:  concO2 = O2sol(S,T)
    %
    % DESCRIPTION:
    %    Solubility (saturation) of oxygen (O2) in sea water
    %    at 1-atm pressure of air including saturated water vapor
    %
    % INPUT:  (if S and T are not singular they must have same dimensions)
    %   S = salinity    [PSS]
    %   T = temperature [degree C]
    %
    % OUTPUT:
    %   concO2 = solubility of O2  [umol/kg] 
    % 
    % AUTHOR:  Roberta Hamme (rhamme@ucsd.edu)
    %
    % REFERENCE:
    %    Hernan E. Garcia and Louis I. Gordon, 1992.
    %    "Oxygen solubility in seawater: Better fitting equations"
    %    Limnology and Oceanography, 37, pp. 1307-1312.
    %
    % DISCLAIMER:
    %    This software is provided "as is" without warranty of any kind.  
    %=========================================================================
"""
def O2sol(S, T):

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
        print ("O2sol: S & T must have same dimensions or be singular")
        return

    #------
    # BEGIN
    #------
    
    # convert T to scaled temperature
    temp_S = np.log(np.subtract(298.15,T) / np.add(273.15,T))
    
    # constants from Table 1 of Garcia & Gordon for the fit to Benson and Krause (1984)
    A0_o2 = 5.80871; 
    A1_o2 = 3.20291;
    A2_o2 = 4.17887;
    A3_o2 = 5.10006;
    A4_o2 = -9.86643e-2;
    A5_o2 = 3.80369;
    B0_o2 = -7.01577e-3;
    B1_o2 = -7.70028e-3;
    B2_o2 = -1.13864e-2;
    B3_o2 = -9.51519e-3;
    C0_o2 = -2.75915e-7;
    
    # Corrected Eqn (8) of Garcia and Gordon 1992
    conc_O2 = np.exp(A0_o2 + A1_o2 * temp_S + A2_o2 * np.power(temp_S,2) + A3_o2 * np.power(temp_S,3) + A4_o2*np.power(temp_S,4) + A5_o2 * np.power(temp_S,5) + S*(B0_o2 + B1_o2 * temp_S + B2_o2 * np.power(temp_S,2) + B3_o2 * np.power(temp_S,3) + C0_o2*np.power(S,2)))

    return conc_O2

    