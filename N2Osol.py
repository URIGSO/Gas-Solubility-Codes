# -*- coding: utf-8 -*-
"""
    Gas Solubility Package for Python
        Version 1.1 Mar 21, 2017
        Maintainer:  Brice Loose, Graduate School of Oceanography, URI.
        Email: bloose@uri.edu

    Many of the functions included here were ported from Roberta Hamme's
    Matlab Solubility functions. Roberta Hamme (rhamme@uvic.ca)
    
    % Arsol   Solubility of Ar in sea water
    %=========================================================================
    % N2Osol Version 1.2 4/4/2005
    %          Author: Scott Hara, (scott_hara@my.uri.edu ) 
    %          URI Graduate School of Oceanography 
    %
    % USAGE:  concN2O = N2Osol(S,T,args)
    %
    % DESCRIPTION:
    %    Solubility of N2O in sea water
    %    at 1-atm pressure of air including saturated water vapor
    %
    % INPUT:  (if S and T are not singular they must have same dimensions)
    %   S = salinity    [PSS]
    %   T = temperature [degree C]
        *args = 'vol'. Optional parameter
    %
    % OUTPUT:
    %   concN2O = solubility of N2O  [umol/kg] 
    #   Nitrous Oxide solubility in either
    #   mol/liter or mol/kg, depending on
    #   *args.
    % 
    %
    % REFERENCE:
    %        Weiss and Price (1980) Nitrous oxide solubility in water and 
             seawater, Marine Chemistry, Vol. 8 pp. 347-359.

    %
    % DISCLAIMER:
    %    This software is provided "as is" without warranty of any kind.  
    %=========================================================================

"""
import numpy as np

def N2Osol(S,T, args='vol'):
    # Input: Single value or set of Nx1 arrays.
    # T = Temperature, Kelvin
    # S = Salinity, PSU
    # 
    # *args = 'vol'. Optional parameter
    #
    # Output: 
    # Nitrous Oxide solubility in either
    # mol/liter or mol/kg, depending on
    # *args.
    # SOURCE:  Weiss and Price (1980) Nitrous
    # oxide solubility in water and seawater,
    # Marine Chemistry, Vol. 8 pp. 347-359.


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
        print "Arsol: S & T must have same dimensions or be singular"
        return

    T = np.add(273.16,T)
    
    print args

    # if an argument is specified use mol/liter.
    # Otherwise assume inputs are in mol/kg.
    if args == 'vol':
        # mol/liter
        a1 = -165.8806;
        a2 = 222.8743;
        a3 = 92.0792;
        a4 = -1.48425;
        
        b1 = -0.056235;
        b2 = 0.031619;
        b3 = -0.0048472;
    else:
        # mol/kg
        a1 = -168.2549;
        a2 = 226.0894;
        a3 = 93.2817;
        a4 = -1.48693;
        
        b1 = -0.060361;
        b2 = 0.033765;
        b3 = -0.0051862;

    # Calculate solubility per n2o_solubility.m script
    b1b2=np.add(b1,np.multiply(b2,np.divide(T,100)))
    #print b1b2
    b3coeff=np.multiply(np.power(T/100.0,2),b3)
    #print b3coeff
    bsum=np.add(b1b2,b3coeff)
    #print bsum
    lnC = a1 + np.divide(a2*100.0,T) + \
     np.multiply(a3,np.log(T/100.0)) + \
    np.multiply(a4,np.power(T/100.0,2)) + \
      np.multiply(S,bsum)
    #print lnC
    return np.exp(lnC)


def main():
    # test to confirm function accepts both
    # arrays and singular values
    # for T and S
    # T in Kelvin, S in psu
    T=np.array([273.0, 278.0, 283.0]) - 273.16
    S=np.array([25, 30, 35])
    n2osol=n2o_solubility(T,S)
    print n2osol
    T=273.0
    S=0.05
    n2osol_single=n2o_solubility(T,S)
    print n2osol_single


if __name__ == '__main__':
      main()