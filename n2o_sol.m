function [sol] = n2o_sol(T,S,varargin),
% - Calculate solubility of N2O in sea water.
%- OUTPUT:  Equilibrium solubility (K_o or C*) for moist air at 1atm pressure. 
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

if mass_or_vol(1:3) == 'vol', %- mol/liter/atm
    
    a1 = -62.7062;
    a2 = 97.3066;
    a3 = 24.1406;
    a4 = 0;
    
    b1 = -0.05842;
    b2 = 0.033193;
    b3 = -0.0051313;
    
elseif mass_or_vol(1:3) == 'mas', %- mol/kg/atm
    
    a1 = -64.8539;
    a2 = 100.2520;
    a3 = 25.2049;
    a4 = -1.48693;
    
    b1 = -0.062544;
    b2 = 0.035337;
    b3 = -0.0054699;
end

lnC = a1 + a2*100./T + a3*log(T/100) +  S.*[b1 + b2*T/100 + b3*(T/100).^2];

sol = exp(lnC);
    