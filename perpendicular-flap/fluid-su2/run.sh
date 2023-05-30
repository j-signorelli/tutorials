#!/bin/sh
set -e -u

SU2_preCICE_FSI.py -f euler_config_unsteady.cfg -d 2 --parallel