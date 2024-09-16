function [sol] = f12_solubility(T,S,varargin),
% - Calculate solubility of helium in sea water.
%- OUTPUT:  Bunsen solubility coefficient (vol_gas / vol_liquid) at 
%- at one atmosphere and the temperature and salinity given by T,S
%- (inputs).
%
%
%    Bu, X. and Warner, M. J.
%    Solubility of Chlorofluorocarbon 113 in Watter and Seawater,
%    DEEP-SEA RES., 1995, Vol42, 1151-1161

if nargin>2,
    mass_or_vol = varargin{1};
else
    mass_or_vol = 'mas';
end

T = T + 273.15;

a1 = -231.90200000;
a2 = 322.91500000;
a3 = 119.11100000;
a4 = -1.39170000;
b1 = -0.02547000;
b2 = 0.00454000;
b3 = 0.0002708;

lnC = a1 + a2*100./T + a3*log(T/100) + a4*(T/100).^2 + S.*[b1 + b2*T/100 + b3*(T/100).^2];
sol = exp(lnC);
    

