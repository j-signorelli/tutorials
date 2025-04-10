#!/usr/bin/env python3
#!/usr/bin/env python3
import vtk
from matplotlib import pyplot as plt
import matplotlib
matplotlib.use("Qt5Agg")
import numpy as np
import os

def vtk_to_dict(vtkFileName):
    if not os.path.exists(vtkFileName):
        print("No file found for " + vtkFileName)
        return {} # return empty dict if file not found
    
    # read the vtk file as an unstructured grid
    reader = vtk.vtkUnstructuredGridReader()
    reader.SetFileName(vtkFileName)
    reader.ReadAllVectorsOn()
    reader.ReadAllScalarsOn()
    reader.Update()

    # obtain the data
    data = reader.GetOutput()
    n_data = data.GetPointData().GetNumberOfTuples()

    data_dict = {}

    for i in range(n_data):
        data_dict[data.GetPoint(i)] = data.GetPointData().GetArray("Temperature").GetValue(i)
    return data_dict

def main():
    case_labels = {
        "../flow-over-heated-plate/reference-results/fluid-openfoam_solid-nutils/Fluid-Mesh-Solid.dt100.vtk": "OpenFOAM-nutils",
        "../flow-over-heated-plate/reference-results/fluid-su2_solid-ccx/Fluid-Mesh-Solid.dt100.vtk": "SU2-CCX",
        "../flow-over-heated-plate/reference-results/fluid-su2_solid-jots/Fluid-Mesh-Solid.dt100.vtk": "SU2-JOTS",
        "solid-jots/precice-exports/Solid-Mesh-Solid.dt100000.vtk": "PC2-JOTS"}
    styles = [':', '-', '--']
    colors = ['r', 'b', 'g', 'k']

    for i, case in enumerate(case_labels.keys()):
        case_data = vtk_to_dict(case)
        if not case_data:
            continue
        x, t = [p[0] for p in case_data.keys()], np.array(list(case_data.values()))

        # sort by x
        combined = list(zip(x,t))
        combined.sort()
        x, t = zip(*combined)
        x = np.array(x)
        t = np.array(t)

        theta = (t - 300) / (310 - 300)
        plt.plot(x, theta, colors[i % 4] + styles[i % 3], label=case_labels[case])

    plt.ylabel("Theta")
    plt.xlabel("x-coordinate along coupling interface")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()