# -*- coding: utf-8 -*-
"""
    Gas Solubility Package for Python
        Version 1.0 Feb 16, 2017
        Maintainer: Brice Loose (bloose@uri.edu)
            
    % Solubility of CFC 12 in sea water
    %=========================================================================
    % Version 1.2 4/4/2005
    %          Author: Kristpher Krasnosky (URI Graduate School of Oceanography
               Email: kkrasnosky@uri.edu
    %
    % USAGE:  concF12 = F12sol(S,T)
    %
    % DESCRIPTION:
    %    Solubility (saturation) of CFC 12 in sea water
    %    at 1-atm pressure of air including saturated water vapor
    %
    % INPUT:  (if S and T are not singular they must have same dimensions)
    %   S = salinity    [PSS]
    %   T = temperature [degree C]
    %
    % OUTPUT:  Bunsen solubility coefficient (vol_gas / vol_liquid) at
    % at one atmosphere and the temperature and salinity given by T,S
    % (inputs).
    % 
    %
    %
    % DISCLAIMER:
    %    This software is provided "as is" without warranty of any kind.  
    %=========================================================================

"""
def F12sol(S, T, args='vol'):

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
        print "F12sol: S & T must have same dimensions or be singular"
        return

    #------
    # BEGIN
    #------
    
    T = np.add(273.15,T)
    #T=[x+273.15 for x in T]
    #T = T + 273.15

    if args == 'mas':
        
        a1 = -220.2120000;
        a2 = 301.8695000;
        a3 = 114.8533000;
        a4 = -1.3916500;
    
        b1 = -0.1477180;
        b2 = 0.0931750;
        b3 = -0.0157340;
        
        lnC = a1 + np.divide(a2*100,T) + a3*np.log(np.divide(T,100)) + np.divide(np.multiply(a4,np.power(T,2)),10000) + S*(b1 + np.divide(np.multiply(b2,T),100) + b3*np.power(np.divide(T,100),2));
    
    elif mass_or_vol == 'vol':
    

        a1 = -124.4395;
        a2 = 185.4299;
        a3 = 51.6383;
    
        b1 = -0.149779;
        b2 = 0.094668;
        b3 = -0.0160043;
        
        lnC = a1 + np.divide(a2*100,T) + a3*np.log(np.divide(T,100)) + S*(b1 + b2*np.divide(T,100) + b3*np.power(np.divide(T,100),2));
        
    else:
        raise ValueError('Invalid selection of mass_or_vol  enter "mas" or "vol" for third parameter')
    
    return np.exp(lnC)
    
    
#    
#    # convert T to scaled temperature
#    temp_S = np.log(np.subtract(298.15,T) / np.add(273.15,T))
#    
#    # constants from Table 4 of Hamme and Emerson 2004
#    A0_ar = 2.79150
#    A1_ar = 3.17609
#    A2_ar = 4.13116
#    A3_ar = 4.90379
#    B0_ar = -6.96233e-3
#    B1_ar = -7.66670e-3
#    B2_ar = -1.16888e-2
#
#    # Eqn (1) of Hamme and Emerson 2004
#    conc_Ar = np.exp(A0_ar + A1_ar * temp_S + A2_ar * np.power(temp_S,2) + A3_ar*np.power(temp_S,3) + S * (B0_ar + B1_ar * temp_S + B2_ar * np.power(temp_S,2)))
#              a1 + a2*100./T + a3*log(T/100) + a4*T.^2/10000 + S.*[b1 + b2*T/100 + b3*(T/100).^2];
#    return conc_Ar

    