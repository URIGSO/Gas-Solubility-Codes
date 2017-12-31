######## Solubility Code for Argon for R

### Version 1.0 --- February 17, 2017
### Author: Monique LaFrance Bartley, Graduate School of Oceanography, University of Rhode Island
### Email: mlafrance@uri.edu

### Calculates solubility (Bunsen Coefficient) of Argon in sea water

### INPUT: T = temperature in degrees C and S = salinity in psu.
### OUTPUT:  bunsen coefficient at given T and S 

### REFERENCE -- Equation and constants for calculating Argon solubility are found in 
# Pilson, M.E.Q. 2013. An Introduction to the Chemistry of the Sea, 2nd ed. 
# Cambridge University Press, 524 pages, ISBN: 9781139603034.

### DISCLAIMER: This code is provided "as is" without warrenty of any kind. 


## Defining function and constants 
argon_sol <- function(T, S){
  
  A0 <- 2.79150
  A1 <- 3.17609
  A2 <- 4.13116
  A3 <- 4.90379
  B0 <- -6.96233e-3
  B1 <- -7.66670e-3
  B2 <- -1.16888e-2
  
  
  Temp <- log((298.15-T)/(T + 273.15))
  
  agsol.x <- exp((A0 + A1*Temp + A2*(Temp^2)+A3*(Temp^3)) + S*(B0 +B1*(Temp)+ B2*(Temp)^2))
  
  agsol <- c(agsol.x)
  
  return(agsol)
}


## Plotting data using salinity and temperature data from CLIVAR survey section A20 during Cruise ID 33AT20120419 
# Data from CTD cast 25 used
# Data can be downloaded at: http://cchdo.ucsd.edu

#Sal25<-CTD25v2$CTDSAL
#argon_solubility <- argon_sol(CTD25v2$CTDTMP, Sal25)
#argon_solubility  ## these are the solubiitiy at the various temps and salinities, correct? 


#plot(argon_solubility~CTD25v2$CTDTMP, xlab="Temperature (C)", ylab="[Ag] (umol/kg)", main = "Argon Equilibrium Solubility as a Function of Temperature", col = "darkgreen", cex=1)

