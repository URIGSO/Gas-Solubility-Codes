"""
    Gas Solubility Package for Python
        Version 3.6.1 Createed 8 Feb 2018
        Author:  Lisa De Pace, Graduate School of Oceanography, URI.
        Email: lmdepace@my.uri.edu 
       
    #=========================================================================
    # CCL4  Solubility of CCL4 in sea water
    #=========================================================================
    #
    # USAGE:  concCCL4 = CCL4sol(S,T)
    #
    # DESCRIPTION:
    #    Solubility (saturation) of carbon tetrachloride (CCL4) in sea water 
    #       with moist air 
    #
    #
    # INPUT:  (if S and T are not singular they must have same dimensions)
    #   S = salinity    [PSU]
    #   T = temperature [degree C]
    #
    # OUTPUT:
    #   concCCL4= solubility of CCL4  [micromol/(kg*atm)] 
    #   
    # 
    # AUTHOR:  Lisa De Pace (URI) modeled off of Brice Loose code for HeSol
    #
    # REFERENCE:
    #   Bullister, J., & Wisegarver, D. (1998). 
    #  The solubility of carbon tetrachloride in water and seawater. 
    #  Deep Sea Research, Part 1(45), 1285–1302. 
    #
    # DISCLAIMER:
    #    This software is provided "as is" without warranty of any kind.  
    #=========================================================================
"""

def CCL4sol(S, T):

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
        print('CCL4: S & T must have same dimensions or be singular')
        return

    #------
    # BEGIN
    #------

    # convert T to scaled temperature
    T_abs = np.add(T,273.15)

    a1= -149.163
    a2= 228.998
    a3= 63.0162
    b1= -0.405112
    b2=  0.267558
    b3= -0.0450331


    # Eqn (5) of Bullister and Wisegarver 
    
    conc_CCL4 = np.exp(a1 + (a2*(100/T_abs))+ (a3*(np.log(T_abs/100))) + (S*(b1 + b2*(T_abs/100)+ b3*np.power((T_abs/100),2))))
    conc_CCL4= conc_CCL4*1000000

    return conc_CCL4