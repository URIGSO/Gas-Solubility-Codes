# -*- coding: utf-8 -*-
"""
Gas Solubility Package for Python
    Version 3.0 Mar 24, 2019
    Author:  Brice Loose, Graduate School of Oceanography, URI.
    Email: bloose@uri.edu
    #
    # USAGE:  import Solubility as S
    #         Solubility.Hesol(33,0) gives solubility at S = 33, T = 0
    #
    #
    # 
    # DISCLAIMER:
    #    This software is provided "as is" without warranty of any kind. 
    #    A portion of the functions included here were ported from Roberta Hamme's
    #    Matlab Solubility functions. Roberta Hamme (rhamme@ucsd.edu)
    #=========================================================================      
"""

#import numpy as np
from .Hesol import *
from .Nesol import *
from .Arsol import *
from .KRsol import *
from .Xesol import *
from .O2sol import *
from .N2sol import *
from .SF6sol import *
from .F12sol import *
from .CH4sol import *
from .CCL4sol import *
from .C4H10sol import *

__all__ = ['Hesol','Nesol','Arsol','KRsol','Xesol','O2sol','N2sol','N2Osol','SF6sol','F12sol','CH4sol','CCL4sol','C4H10sol']