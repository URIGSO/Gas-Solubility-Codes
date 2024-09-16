function [conc_Ethylene] = Ethylenesol(S,T)

%  Solubility of Ethylene (C2H4) in sea water
%=========================================================================
% Nitrogen sol Version 1.0 2/6/2018
%          Author: Grace E. Medley (Graduate School of Oceanography)
%
% USAGE:  Finds the concentration of Ethylene (C2H4) in seawater given S
% and T parameters
%
% DESCRIPTION:
%    Solubility (saturation) of Ethylene (C2H4) in sea water
%    at 1-atm pressure of air including saturated water vapor as described
%    in Breitbarth et al. (2004)
%
% INPUT:  (if S and T are not singular they must have same dimensions)
%   S = salinity    [PSS]
%   T = temperature [K]
%
% OUTPUT:
%   conc_Ethylene = mol of Ethylene present in the aqueous phase  
% 
% AUTHOR:  Grace Medley (gmedley@my.uri.edu)
%
% REFERENCE:
%    Breitbarth et al. (2004).
%    "The Bunsen gas solubility coefficient of ethylene as a function of temperature and salinity and its importance for nitrogen fixation assays"
%    Limnology and Oceanography Methods, vol. 2, Issue 8, version of record online.
%
% DISCLAIMER:
%    This software is provided "as is" without warranty of any kind.  
%=========================================================================

% CALLER: general purpose
% CALLEE: none

%----------------------
% Check input parameters
%----------------------
% Plug in Temperature in K, Salinity in ppth
T = [290 291 292 293 294 295 296]%temperature in K. Plug in either an array of temps or one temp
S = [29 30 31 32 33 34 35] % ppth. Plug in either an array of S values or one singlular s value
% % CHECK S,T dimensions and verify consistent
[ms,ns] = size(S);
[mt,nt] = size(T);
% 
% % Check that T&S have the same shape or are singular
if ((ms~=mt) | (ns~=nt)) & (ms+ns>2) & (mt+nt>2)
 
end %if

%------
% BEGIN
%------

% constants from Eqn (6) of Breitbarth et al. (2004).
A1_C2H4 = -189.7530;
A2_C2H4 = 10092.7000;
A3_C2H4 = 26.9729;
k = 0.3212-0.0006063.*T
I = 0.01993*S

% Eqn (10) of Breitbarth et al. (2004).
conc_Ethylene = exp((A1_C2H4 + (A2_C2H4./(T))+ A3_C2H4.*log(T)) - 2.303 .* k .* I)

return