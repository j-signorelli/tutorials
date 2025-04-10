#!/bin/sh
set -e -u
export OMP_NUM_THREADS=1
mpirun -np 5 plascom2x -v 4 -c run.config IC/PlasCom2_000000000.h5 IC/PlasCom2_000000000.h5 