import numpy as np
import pandas as pd
def main(archivo):
    try:
        A = pd.read_csv(archivo, header= None).to_numpy()

        X, Y, Z = [], [], []

        for i, y in enumerate(A[0][1:], 1):
            for z in A[1:]:
                X.append(z[0])
                Y.append(y)
                Z.append(z[i])

        XYZ = np.vstack((X,Y,Z))
        XYZ_t = np.transpose(XYZ)
        np.savetxt(f'../xyz/{archivo}_xyz.csv', XYZ_t, delimiter=",")
    except TypeError:
        print(f'{archivo}no se pudo procesar')
        with open('problemas_con_xyz.txt', 'w') as f:
            f.write(archivo) 
        pass