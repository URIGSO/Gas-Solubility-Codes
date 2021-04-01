function [Ct] = headspace(Ci,Cw,vw,va,F,varargin);
%- function [cout] = headspace(Ci,Cw,vw,va,F);
%-
%- Compute {Cw, or Ci} from the given variable {Cw or Ci}, and F, the
%- Henry's Law Solubility.
%-
%- INPUT:
%- 1) Input either Cw or Ci, and make the other variable, nan.  
%-  Example: headspace(1e-5,nan,.005) computes Ci, knowing Ca).
%- 2) vw, va are volume of air and water in syringe (equilibrated volume)
%-    can be any units, but be consistent.

%- CONSTANTS:

mw_h2o = 55.5 %- mol/kg
mw_air = 1./(14.007*2*.7808+15.999*2*.2095+39.948*.0093)*1e3; %- mol/kg

%- molar density of air (rho = 1.027)
rhom_air = 1.027*mw_air;
%- assume seawater;
rhom_h2o = sw_dens(35,-2,0)*mw_h2o;

if nargin<5,
    error('Input at least 4 variables, unknown == nan');
end

%-- Look for T & S
if nargin == 6,
    T = varargin{1};
    %- molar density of air
    rhom_air = air_dens(T,100)*mw_air;
    %- assume freshwater;
    rhom_h2o = sw_dens(0,T,0)*mw_h2o;
elseif nargin > 6,
    T = varargin{1};
    S = varargin{2};
    %- molar density of air
    rhom_air = air_dens(T,100)*mw_air;
    %- assume seawater;
    rhom_h2o = sw_dens(S,T,0)*mw_h2o;
else
    %- If no T and S, assume STP
    %- molar density of air
    rhom_air = air_dens(0,100)*mw_air;
    %- assume seawater;
    rhom_h2o = sw_dens(0,0,0)*mw_h2o; 
end


numdenom = (F.*sw_dens(35,-2,0)*vw + va.*rhom_air);

if isnan(Cw), %- compute 
        
    Ca = Ci.*vw.*rhom_h2o./numdenom;

    Cw = Ca.*F./mw_h2o;
    
elseif isnan(Ci),
    
    Ci = Cw.*numdenom./(vw.*rhom_h2o);
    
    Ca = Cw./F.*mw_h2o;

end

Ct = [Cw,Ca,Ci];