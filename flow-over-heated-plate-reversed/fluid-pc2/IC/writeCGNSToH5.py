import h5py
import numpy as np

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Specify grid details
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Name of CGNS file
cgnsName = 'mesh.cgns'

# Name of domain or block from Pointwise

domainName = 'dom-1'
#domainName = 'blk-1'

#Dimension
dim = 2

# Set names used in PC2 file
testName = 'Beam'
gridName = 'grid1'
geometryName = 'cmgeom/geom2dM1'

# Dummy PC2 restart file name
pc2Name = 'PlasCom2_000000000.h5'

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Read in CGNS grid
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#filename1 = '../../PC2_Testing/PC2_DiamondAirfoil_v6/PlasCom2_001300000.h5'

hf = h5py.File(cgnsName, 'r')

print('Read CGNS grid ')

X   = (hf[''.join(['/Base/',domainName,'/GridCoordinates/CoordinateX/ data'])][:]).T
Y   = (hf[''.join(['/Base/',domainName,'/GridCoordinates/CoordinateY/ data'])][:]).T

if dim == 3:
	Z   = (hf[''.join(['/Base/',domainName,'/GridCoordinates/CoordinateZ/ data'])][:]).T

hf.close()



# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Write PC2 grid
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#filename1 = '../init_grid1/PlasCom2_000000000.h5'
hf = h5py.File(pc2Name, 'a')

print('Write grid to PC2 h5 file ')
(hf[''.join(['//PlasCom2/Geometry/',geometryName,'/X'])][:])      = X.T
(hf[''.join(['//PlasCom2/Geometry/',geometryName,'/Y'])][:])      = Y.T

if dim == 3:
	(hf[''.join(['//PlasCom2/Geometry/',geometryName,'/Z'])][:])      = Z.T

hf.close()

