import h5py
import numpy as np

# Main program begins

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Set test name
testName = 'Beam'

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Read initial condition
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Read data from plascom2 file

filename1 = 'PlasCom2_000000000.h5'

hf = h5py.File(filename1, 'r')

print('Parse the grid and ovkstate (grid M1) ... ')
XM1   = (hf[''.join(['//PlasCom2/Geometry/cmgeom/geom2dM1/X'])][:]).T
YM1   = (hf[''.join(['//PlasCom2/Geometry/cmgeom/geom2dM1/Y'])][:]).T
#ZM1   = (hf[''.join(['//PlasCom2/Geometry/cmgeom/geom2dM1/Z'])][:]).T

print('  ')
print('=================== ')
print('  ')

hf.close()

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Compute initial condition of interest
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
u_infty = 0.1/np.sqrt(103500/1.0)

# Set the value of gamma 
gamma = 5000.0/(5000-345)

print('Updating state data to grid M1 ... ')
v1M1   = 0*XM1 + u_infty
v2M1   = 0*XM1 + 0
#v3M1   = 0*XM1 + 0*np.sqrt(gamma)
pM1    = 1.0 + 0*XM1
TM1    = 1.0 + 0*XM1
rhoM1  = 1.0 + 0*XM1
rhoUM1 = rhoM1*v1M1
rhoVM1 = rhoM1*v2M1
#rhoWM1 = rhoM1*v3M1
rhoEM1 = 0*XM1 + pM1/(gamma-1.0) + 0.5*rhoM1*( v1M1**2 +v2M1**2 )

print('  ')
print('=================== ')
print('  ')

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Write initial condition of interest
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

filename1 = 'PlasCom2_000000000.h5'
hf = h5py.File(filename1, 'a')

print('Write the state variables and pressure (grid M1) ... ')
(hf[''.join(['//PlasCom2/Simulation/',testName,'/grid1/rho'])][:])      = rhoM1.T
(hf[''.join(['//PlasCom2/Simulation/',testName,'/grid1/rhoV-1'])][:])   = rhoUM1.T
(hf[''.join(['//PlasCom2/Simulation/',testName,'/grid1/rhoV-2'])][:])   = rhoVM1.T
#(hf[''.join(['//PlasCom2/Simulation/',testName,'/grid1/rhoV-3'])][:])   = rhoWM1.T
(hf[''.join(['//PlasCom2/Simulation/',testName,'/grid1/rhoE'])][:])     = rhoEM1.T
(hf[''.join(['//PlasCom2/Simulation/',testName,'/grid1/pressure'])][:])   = pM1.T
(hf[''.join(['//PlasCom2/Simulation/',testName,'/grid1/velocity-1'])][:]) = v1M1.T
(hf[''.join(['//PlasCom2/Simulation/',testName,'/grid1/velocity-2'])][:]) = v2M1.T
#(hf[''.join(['//PlasCom2/Simulation/',testName,'/grid1/velocity-3'])][:]) = v3M1.T
(hf[''.join(['//PlasCom2/Simulation/',testName,'/grid1/temperature'])][:]) = TM1.T

hf.close()

