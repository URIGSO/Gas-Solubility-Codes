
%%%%%% Carbon monoxide (CO) solubility code

function [conc_CO] = COsol(S,T)

% COsol   Solubility of carbon monoxide in sea water
%=========================================================================
% COsol Version 05/18/1979

% AUTHORS:  Denis Wiesenburg & Norman Gulnasso (Texas A&M University,
%                                           Department of Oceanography)
%
% USAGE:  conc_CO = COsol(S,T)
%
% DESCRIPTION:
%    Solubility (saturation) of carbon monoxide (CO) in sea water
%    at 1 atm total pressure 
%
% INPUT:  (if S and T are not singular they must have same dimensions)
%   S = salinity    [PSS]
%   T = temperature [degree C]
%
% OUTPUT:
%   conc_CO = solubility of carbon monoxide [nmol/kg] 
%
% CONSTANTS:
%   fG is the Molecular Fraction of carbon monoxide in the atmosphere
%   For this equation fG is assumed to equal 0.11*10^-6 atm
%      -> as defined by Table 5 and the last paragraph before conclusions
%   Ai & Bi are constant coefficients for calculations
%      -> as defined by Table 6 for the given units
%
% REFERENCE:
%    Denis A. Wiesenburg & Norman L. Gulnasso Jr., 1979.
%    "Equilibrium Solubilities of Methane, Carbon Monoxide, and Hydrogen in Water and Sea Water."
%    J. Chem. Eng. Data, Vol. 24, No. 4, p. 356-360.
% 
%=========================================================================

% CALLER: general purpose
% CALLEE: none

%----------------------
% Check input parameters
%----------------------

if nargin ~=2
   error('COsol.m: Must pass 2 parameters')
end %if

% Check S,T dimensions and verify consistent
[ms,ns] = size(S);
[mt,nt] = size(T);

% Check that S & T have the same shape or are singular
if ((ms~=mt) || (ns~=nt)) && (ms+ns>2) && (mt+nt>2)
   error('COsol: S & T must have same dimensions or be singular')
end %if

%------
% BEGIN
%------

% Convert T(deg. C) to Kelvin
T = T + 273.16;

% Constants from Table 6 of W.&G. (1979) for units nmol/kg
fG = 0.11*(10^-6);         % fG = molecular fraction of CO in atmosphere
A1 = -175.6092;            % -> fG assumed to be 0.11*10^-6 from Table 5
A2 = 267.6796;
A3 = 161.0862;
A4 = -25.6218;
B1 = 0.046103;
B2 = -0.041767;
B3 = 0.0081890;

% Equation (7) of W.&G.(1979):
% log(conc_CO) = log(fG) + A1 + A2*100./T + A3*log(T./100) + A4*T./100 + S.*(B1 + B2*T./100 + B3*(T./100).^2);
% then take exponent of both sides so outputs final concentration of CO:
conc_CO = exp(log(fG) + A1 + (A2*100./T) + (A3*log(T./100)) + (A4*T./100) + S.*(B1 + (B2*T./100) + (B3*((T./100).^2))));

% conc_CO = concentrataion of CO in nmol/kg

return

