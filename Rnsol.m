function [conc_Rn] = Rnsol(S,T)

% Rnsol   Solubility of Rn in sea water
%=========================================================================
% Rnsol Version 1 2/9/2018
%          Author: Nyla Husain (University of Rhode Island)
%
% USAGE:  concRn = Rnsol(S,T)
%
% DESCRIPTION:
%    Solubility of radon (Rn) in sea water for temperature range 
%    273 < T[K] < 323 and salinity range 0 < S < 360.
%
% INPUT:  (if S and T are not singular they must have same dimensions)
%   S = salinity    [PSS]
%   T = temperature [K]
%
% OUTPUT:
%   concRn = solubility of Rn  [umol/kg] 
% 
% AUTHOR:  Nyla Husain (nylahusain@uri.edu)
%
% REFERENCE:
%    Michael Schubert, Albrecht Paschke, Eric Lieberman, William C. Burnett
%    (2012).
%    "Air-Water Partitioning of 222Rn and its Dependence on Water 
%    Temperature and Salinity."
%    Environmental Science & Technology, 46(7): 3905-3911.
%
% DISCLAIMER:
%    This software is provided "as is" without warranty of any kind.  
%=========================================================================

% CALLER: general purpose
% CALLEE: none

%----------------------
% Check input parameters
%----------------------
if nargin ~=2
   error('Rnsol.m: Must pass 2 parameters')
end %if

% CHECK S,T dimensions and verify consistent
[ms,ns] = size(S);
[mt,nt] = size(T);

% Check that T&S have the same shape or are singular
if ((ms~=mt) | (ns~=nt)) & (ms+ns>2) & (mt+nt>2)
   error('Rnsol: S & T must have same dimensions or be singular')
end %if

%------
% BEGIN
%------

% constants from Table 1 of Schubert et al. 2012
A1_rn = -76.14;
A2_rn = 120.36;
A3_rn = 31.26;
B1_rn = -0.2631;
B2_rn = 0.1673;
B3_rn = -0.0270;

% Eqn (3) of Schubert et al. 2012
Bunsen = exp(A1_rn*ones(size(T)) + A2_rn*(100./T) + A3_rn*log(T/100) + S.*(B1_rn*ones(size(S)) + B2_rn*(T/100) + B3_rn*(T/100).^2));
conc_Rn = Bunsen.*(T/273.15);

return