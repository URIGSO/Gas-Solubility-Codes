# -*- coding: utf-8 -*-
"""
Saturation Vapor Pressure Package for Python
        Version 1.0 May 21, 2017
        Author:  Samuel Gartzman, Graduate School of Oceanography, URI.
        Email: sgartzman@uri.edu
% function es = sat_vp(T),
%- INPUT:
%-  1) Temperature in Deg. C
%- OUTPUT:
%-  1) vapor pressure in mb
%- calculate the saturation vapor pressure.  below T = 0 C
"""



def sat_vp(T):
    
    import numpy as np
    
    Lf = 2.453e6 # (J/kg)
    Rv = 461.     # (J/kg)
    
    if (T <= 0):
    
        Tk = 273.15+T
        
        # es in hPa
        loges =  -7.90298*(373.16/Tk-1) + 5.02808*np.log10(373.16/Tk) - 1.3816e-7*(1011.344*(1-Tk/373.16)-1) + 8.1328e-3*(10**-3.49149*(373.16/Tk-1)-1)+ np.log10(1013.246)
        es = 10**loges
        
    else:
        Tk = 273.15+T
        loges = Lf/Rv*(1./273.15 - 1./Tk)
        es = 6.11*np.exp(loges)
    return es

