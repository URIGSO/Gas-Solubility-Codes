function [sol] = f11_solubility(T,S,varargin),
%- Calculate solubility of CFC 11 in sea water.
%- INPUT:
%- 1) T = Temp deg C
%- 2) S = salinity (psu)
%-
%- OUTPUT:  Bunsen solubility coefficient (mol_gas / vol_liquid) or 
%- ( mol_gas/kg_liquid ) at 
%- at one atmosphere and the temperature and salinity given by T,S
%- (inputs).
%
%
%- SOURCE:  Warner, M. J. and Weiss, R.F.
%    Solubilities of Chlorofluorocarbons 11 and 12 in Watter and Seawater,
%    DEEP-SEA RES., 1985, Vol32, 1485-1497.  See Hoyle Lee's cfc_pcfc.m

if nargin>2,
    mass_or_vol = varargin{1};
else
    mass_or_vol = 'mas';
end

T = T + 273.15;

if mass_or_vol == 'mas',
    
    a1 = -232.0411000; 
    a2 = 322.5546000; 
    a3 = 120.4956000; 
    a4 = -1.3916500;
    
    b1 = -0.1465310; 
    b2 = 0.0936210; 
    b3 = -0.0160693;
    
    lnC = a1 + a2*100./T + a3*log(T/100) + a4*T.^2/10000 + S.*[b1 + b2*T/100 + b3*(T/100).^2];

elseif mass_or_vol == 'vol',
    
    a1 = -136.2685;
    a2 = 206.1150;
    a3 = 57.2805;
    
    b1 = -0.148598;
    b2 = 0.095114;
    b3 = -0.0163396;
    
    lnC = a1 + a2*100./T + a3*log(T/100) + S.*[b1 + b2*T/100 + b3*(T/100).^2];
end

%lnC = a1 + a2*100./T + a3*log(T/100) + S.*[b1 + b2*T/100 + b3*(T/100).^2];

sol = exp(lnC);
    