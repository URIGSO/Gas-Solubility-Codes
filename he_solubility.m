function [sol] = he_solubility(T,S,varargin),
% - Calculate solubility (Bunsen Coefficient) of helium in sea water.
%- OUTPUT:  Bunsen solubility coefficient (vol/vol) and temperature and salinity given by T,S
%- (inputs).
%
%
%- SOURCE:  Weiss, R. (1971) Solubility of Helium and Neon in Water and
%- Seawater, Journal of Chemical Engineering Data, Vol. 16(2).
T = T+273.16;

    
    a1 = -34.6261;
    a2 = 43.0285;
    a3 = 14.1391;
    a4 = 0;
    
    b1 = -0.042340;
    b2 = 0.022624;
    b3 = -0.0033120;

lnC = a1 + a2*100./T + a3*log(T/100) + a4*T/100+ S.*[b1 + b2*T/100 + b3*(T/100).^2];

sol = exp(lnC);
    