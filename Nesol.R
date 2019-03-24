# Solubility of Ne in sea water
#=========================================================================
#  2/1/18
#            Original Author: Roberta C. Hamme (Scripps Inst of Oceanography)
# translating/editing author: Joseph D. Zottoli (URI GSO)
#
# USAGE:  eqsolubility(S,t)
#
# DESCRIPTION:
#    Solubility (saturation) of neon (Ne) in sea water
#    at 1-atm pressure of air including saturated water vapor
#
# INPUT:  (if S and t are not singular they must have same dimensions)
#   S = salinity    (PSS)
#   t = temperature (degree C)
#
# OUTPUT:
#   conc_Ne = solubility of Ne  [umol/kg] 
# 
# AUTHOR:  Joseph Zottoli (jzottoli@uri.edu)
#
# REFERENCE:
#    Roberta Hamme and Steve Emerson, 2004.
#    "The solubility of neon, nitrogen and argon in distilled water and seawater."
#    Deep-Sea Research I, 51(11), p. 1517-1528.
#
# DISCLAIMER:
#    This software is provided "as is" without warranty of any kind.  

#start function
eqsolubility=function(S,te){ 
  conc_Ne<<-NA
  if(length(S)!=length(te)) stop("S and te must be of same length")
  temp_S=rep(NA,length(te)) 
  
  for (i in 1:length(te)){
    # convert T to scaled temperature
    
    temp_S[i] = log((298.15 - te[i])/(273.15 + te[i]))
    
    # Eqn (1) of Hamme and Emerson 2004 with constants from table 4 inserted
    conc_Ne[i] = exp(2.18156 + 1.29108*(temp_S[i]) + 2.12504*temp_S[i]^2 + S[i]*(-5.94737e-3 + -5.13896e-3*temp_S[i]))
    
    # Convert from nmol/kg to umol/kg
    conc_Ne[i] <<- conc_Ne[i]/1000
    
  }
  print(conc_Ne)
}

eqsolubility(35,te=10)#shows equllibrium solubility of one temop and salinity

eqsolubility(c(35,33,27,38,30),te=c(10,15,25,20,10))#shows equllibrium solubility of 10 combinations

eqsolubility(c(35,33),te=c(20,10,5))#shows that vectors must be of same length

