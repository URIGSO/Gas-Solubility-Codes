function [lnK1 lnK2] = K1K2_CO2(T,S,varargin);
%- function [K1 K2] = K1K2_CO2(T,S,varargin);
%- Calculate the Dissociation Constants for H2CO3 (K1) and HCO3- (K2)
%-
%- INPUTS: 
%-    1) T (temp deg. C)
%-    2) S (salinity in psue)
%- Reference:
%- DOE (1994) - from R. Zeebe and D.W. Gladrow.  CO2 In Seawater:
%- Equilibrium, Kinetics, Isotopes.  (2001).  Elsevier Oceanography Series.


T = T+273.15;

a1 = 2.83655;
a2 = -2307.1266;
a3 = -1.5529413;
a4 = -0.207608410;
a5 = -4.0484;
a6 = 0.0846834;
a7 = -0.00654208;
a8 = -0.001005;

lnK1 =  a1 + a2./T + a3.*log(T) + (a4 + a5./T).*S.^0.5 + a6.*S + a7.*S.^1.5 + log(1 + a8.*S);


a1 = -9.226508;
a2 = -3351.6106;
a3 = -0.2005743;
a4 = -0.106901773;
a5 = -23.9722;
a6 = 0.1130822;
a7 = -0.00846934;
a8 = -0.001005;

lnK2 =  a1 + a2./T + a3.*log(T) + (a4 + a5./T).*S.^0.5 + a6.*S + a7.*S.^1.5 + log(1 + a8.*S);
