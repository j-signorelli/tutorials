#!/usr/bin/env python3
import vtk
from matplotlib import pyplot as plt
import numpy as np


def vtk_to_dict(case):
    vtkFileName = str(case + "Fluid-Mesh-Solid.dt100.vtk").format(case)
    # read the vtk file as an unstructured grid
    reader = vtk.vtkUnstructuredGridReader()
    reader.SetFileName(vtkFileName)
    reader.ReadAllVectorsOn()
    reader.ReadAllScalarsOn()
    reader.Update()

    # obtain the data
    data = reader.GetOutput()
    n_data = data.GetPointData().GetNumberOfTuples()

    data_names = []
    num_arrays = data.GetPointData().GetNumberOfArrays()

    # get all data names
    for i in range(num_arrays):
        this_data_name = data.GetPointData().GetArray(i).GetName()
        data_names.append(this_data_name)

    # check + get temperature if available
    data_dict = {}
    temperature = "Temperature"
    if not temperature in data_names:
        print(
            "For file {} name {} not found.".format(vtkFileName, temperature))

    for i in range(n_data):
        data_dict[data.GetPoint(i)] = data.GetPointData().GetArray(temperature).GetValue(i)

    return data_dict

def main():
    case_labels = {
        #'reference-results/fluid-openfoam_solid-fenics/': 'OpenFOAM-FEniCS',
        #'reference-results/fluid-openfoam_solid-openfoam/': 'OpenFOAM-OpenFOAM',
        #'reference-results/fluid-openfoam_solid-nutils/': 'OpenFOAM-Nutils',
        'solid-nutils/precice-exports/': 'SU2-Nutils',
        'reference-results/fluid-su2_solid-nutils/': "SU2-Nutils OLD"}
        #'reference-results/fluid-su2_solid-ccx/': "SU2-CCX",
        #'solid-jots/precice-exports/': "SU2-JOTS"}
    styles = [':', '-', '--']
    colors = ['r', 'k', 'g', 'b']

    for i, case in enumerate(case_labels.keys()):
        case_data = vtk_to_dict(case)
        x, t = [p[0] for p in case_data.keys()], np.array(list(case_data.values()))
        combined = list(zip(x,t))
        combined.sort()
        x, t = zip(*combined)
        x = np.array(x)
        t = np.array(t)
        theta = (t - 300) / (310 - 300)
        plt.plot(x, theta, colors[i % 4] + styles[i % 3], label=case_labels[case], linewidth=3)

    plt.ylabel("Theta")
    plt.xlabel("x-coordinate along coupling interface")
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()