######## Solubility Code for SF6 for R

### Version 1.0 --- February 17, 2017
### Author: Monique LaFrance Bartley and Chris McAleer, Graduate School of Oceanography, University of Rhode Island
### Email: mlafrance@uri.edu

### Calculates solubility (Bunsen Coefficient) of SF6 in sea water
# Two versions of the code are provided and yeild identical outputs

### INPUT: T = temperature in degrees C and S = salinity in psu.
### OUTPUT:  bunsen coefficient at given T and S with the units mol/kg/atm

### REFERENCE:  Busenberg and Plummer (2008). Dating groundwater with trifluoromethyl 
# sulfurpentafluoride (SF5CF3), sulfur hexafluoride (SF6), CF3Cl (CFC-13),
# and CF2Cl2 (CFC-12).  WATER RESOURCES RESEARCH, VOL. 44, W02431, 
# doi:10.1029/2007WR006150, 2008

### DISCLAIMER: This code is provided "as is" without warrenty of any kind. 


### VERSION 1 
## Defining function and constants 
sf6_solubility <- function(T,S) {
  T <- T+273.15
  df <- data.frame(T,S)
  a1 <- -82.16390000
  a2 <- 120.15200000
  a3 <- 30.63720000

  b1 <- 0.02932010
  b2 <- -0.03519740
  b3 <- 0.00740056

  lnC <- a1 + a2*(100/df$T) + a3*log(df$T/100) + df$S*(b1 + b2*(df$T/100) + b3*(df$T/100)^2)
  sol = exp(lnC)
  return(sol)  
}


## Plotting data using salinity and temperature data from CLIVAR survey section A20 during Cruise ID 33AT20120419 
# Data from CTD cast 25 used
# Data can be downloaded at: http://cchdo.ucsd.edu

#Sal25<-CTD25v2$CTDSAL
#sf6_sol <- sf6_solubility(CTD25v2$CTDTMP, Sal25)
#sf6_sol 
#plot(sf6_sol~CTD25$CTDTMP, xlab="Temperature (C)", ylab="[SF6] (umol/kg)", main = "SF6 Equilibrium Solubility as a Function of Temperature", cex=1)


### VERSION 2
## Defining function and constants 

sf6_solubility_b <- function(T, S){
  
  a1 <- -82.16390000
  a2 <- 120.15200000
  a3 <- 30.63720000
  b1 <- 0.02932010
  b2 <- -0.03519740
  b3 <- 0.00740056
  
  T.K <- (T+273.15)
  
  lnC_bx <- exp(a1 + a2*(100/T.K) + a3*log(T.K/100) + S*(b1 + b2*(T.K/100) + b3*(T.K/100)^2))
  lnC_b = c(lnC_bx)
  return(lnC_b)  
}

## Plotting data using salinity and temperature data from CLIVAR survey section A20 during Cruise ID 33AT20120419 
# Data from CTD cast 25 used
# Data can be downloaded at: http://cchdo.ucsd.edu

#Sal25<-CTD25v2$CTDSAL
#solubility_sf6_b <- sf6_solubility_b(CTD25v2$CTDTMP, Sal25)
#solubility_sf6_b

#plot(CTD25v2$CTDTMP, solubility_sf6_b, xlab="Temperature (C)", ylab="[SF6] (umol/kg)", main = "SF6 Equilibrium Solubility as a Function of Temperature", cex=1, col="blue")



  