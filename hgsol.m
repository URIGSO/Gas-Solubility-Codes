function sol = hgsol(T,S)
%hgsol  solubility of elemental mercury vapor in water
%Version 1 2/2018 
%Author Emma Thomas

% USAGE:  sol = hgsol(T,S)
%
% DESCRIPTION:
%    Solubility (saturation) of elemental Mercury vapor (Ar) in sea water
% 
% INPUT:  (if S and T are not singular they must have same dimensions)
%   S = salinity    [PSS]
%   T = temperature [degree C]
%
% OUTPUT:
%   sol = solubility of Hg  [umol/kg] 
% 
% AUTHOR:  Emma Thomas (emma_thomas@uri.edu)
%
% REFERENCE:
%    Sanesama et al. 1981
%    Sanesama 1975
%
% The following are the measurements from Sanesama 1975 giving the
% solubility of Hg in fresh water as a function of temperature. A quadratic
% fit to these points is substituted into the expression in Sanesame et al. 1981 
% for solubility as a function of molarity of a dissolved salt (which also
% depends on the original solubility in fresh water):
% to = [5:5:20 30:10:80 100];
% so = [19.2 27.4 45 81.3 137 218 368 560 850 1200 1800];

% DISCLAIMER:
%    This software is provided "as is" without warranty of any kind.  
%=========================================================================

sol = (0.2167*T.^2 - 3.81*T +44.89).*exp(0.788.*S./58.43);

