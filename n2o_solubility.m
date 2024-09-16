
function [sol] = n2o_solubility(T,S,varargin),
% - Calculate solubility of N2O in sea water.
%- OUTPUT:  Equilibrium solubility (F) for moist air at 1atm pressure. 
%- at one atmosphere and the temperature and salinity given by T,S
%- (inputs).
%
%
%- SOURCE:  Weiss and Price (1980) Nitrous oxide solubility in water and 
%- seawater, Marine Chemistry, Vol. 8 pp. 347-359.

if nargin>2,
    mass_or_vol = varargin{1};
else
    mass_or_vol = 'vol';
end

if mass_or_vol(1:3) == 'vol', %- mol/liter
    
    a1 = -165.8806;
    a2 = 222.8743;
    a3 = 92.0792;
    a4 = -1.48425;
    
    b1 = -0.056235;
    b2 = 0.031619;
    b3 = -0.0048472;
    
elseif mass_or_vol(1:3) == 'mas', %- mol/kg
    
    a1 = -168.2549;
    a2 = 226.0894;
    a3 = 93.2817;
    a4 = -1.48693;
    
    b1 = -0.060361;
    b2 = 0.033765;
    b3 = -0.0051862;
end

lnC = a1 + a2*100./T + a3*log(T/100) + a4*(T/100).^2+ S.*[b1 + b2*T/100 + b3*(T/100).^2];

sol = exp(lnC);
    