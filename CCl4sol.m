function [sol] = CCl4sol(S,T)
%DESCRIPTION: Calculate the solubility of carbon tetrachloride (CCl4) 
%based on the (bunsen solubility coefficient) in Seawater

%OUTPUT:sol = solubility of CCl4 (mol/(L atm))
%INPUT: S = Salinity in (o/00) aka PSU; T = Temperature in degrees Celsius

%Author: Melanie Feen, University of Rhode Island GSO

%Sources: Bullister, J. L., & Wisegarver, D. P. (1998). The solubility of
%carbon tetrachloride in water and seawater. Deep Sea Research Part I:
%Oceanographic Research Papers, 45(8), 1285-1302.
%Wanninkhof, R. (2014). Relationship between wind speed and gas exchange 
%over the ocean revisited. Limnology and Oceanography: Methods, 12(6), 
%351-362.




% constants from table 2 Bullister &
% Wisegarver (1998) and table 2 of Wanninkhof 2014 & 
A1_ccl4 = -166.321;
A2_ccl4 = 252.542;
A3_ccl4 = 71.5211;
B1_ccl4 = -0.41216;
B2_ccl4 = 0.273093;
B3_ccl4 = -0.0460112;

%convert temperature from celsius to Kelvin
temp = T + 273.15;

%rename salinity
salt = S;

%eqn from Bullister & Wisegarver (1998) and Wanninkhof (2014)
lnbeta = A1_ccl4 + (A2_ccl4*(100./temp)) + (A3_ccl4.*log(temp./100)) + salt.*(B1_ccl4 + (B2_ccl4.*(temp./100)) + (B3_ccl4.*(temp/100).^2));

sol = exp(lnbeta); %UNITS: mol/(L atm)
end

