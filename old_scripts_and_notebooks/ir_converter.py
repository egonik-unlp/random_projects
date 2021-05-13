##Librerias
from os import listdir
from os.path import isfile, join

##Funciones

def plotter_ir(filename):
    d_crudos=list()
    for line in open(filename):
        line=line.replace("\n", "")
        line = line.replace(",",".")
        d_crudos.append(line)
    trans=d_crudos[6:]    
    fin=float(d_crudos[2])
    
    ini=float(d_crudos[1])
    
    long=float(d_crudos[0])
    
    nus=list()
    paso=(ini - fin)/long
    ini_fal=ini
    
    for i in trans:
        nus.append(ini_fal)
        ini_fal-=paso
    trans_flo=list()
    
    for i in trans:
        trans_flo.append(float(i))
    esto=(nus,trans_flo)
    import matplotlib.pyplot as plt
    plt.plot(nus,trans_flo)
    plt.axis([4000,620,30,105])
    d2=filename+"_espectro.txt"
    f=open(d2,"w")
    pu=list(range(len(trans)))
    for i in pu:
        u=int(i)
        f.write(str(nus[u])+"   "+str(trans_flo[u]) +"\n")
 
def cargar_folder():
    a = listdir()
    x = [i for i in a if ".asp" in i]
    return x    
#--------------------------------Programa-----------------------------------
X = cargar_folder()
for i in X:
    plotter_ir(i)
print("todo exportado")
    
    
