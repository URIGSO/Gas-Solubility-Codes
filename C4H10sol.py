def C4H10sol(S,T):
    """
    #Solubility of an Aromatic Hydrocarbon: Anthracene
    #Author: Jacob P. Strock
    #Version 1.1, Updated Feb. 09 2018
    
    #Description: Solubility of Anthracene in Seawater derived from the experimental data published by Whitehouse (1983). 
    #The equation for solubility was estimated as:
    #    Solubility = a * (1/Salinity)/(1/Salinity + b) * e^(c * Temperature)
    #    whereby a, b , and c (39.07, 0.1034, 0.07524) are statistically derived constants from a non-linear regression of the average solubility values per each temperature 
    #    and salinity treatment datum published by Whitehouse (1983). a * (1/Salinity)/(1/Salinity + b) resembles a Michaelis-Menten relationship where a represents the 
    #    maximum solubility and b the Michealis constant (where solubility is 1/2 max). The solubility relationship with temperature is described in the exponential component
        
    #Input: Temperature (*C), Salinity (ppt)
    #Output: Solubility in nm/L
    
    #Whitehouse, B. The effects of temperature and salinity on the aqueous solubility of polynuclear aromatic hydrocarbons. Marine Chemistry, 14 (1984): 319-332.
    """

    import numpy
    global SolubilityCalc
    a=39.07
    b=0.01034
    c=0.07524
    SolubilityCalc = a * (1/S)/(1/S + b) * numpy.exp(c * T)
    return SolubilityCalc
