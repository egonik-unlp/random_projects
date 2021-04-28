###########################Librerías utilizadas################################

import numpy as np
import random 
import matplotlib.pyplot as plt
import matplotlib._color_data as mcd
from itertools import combinations
import seaborn as sns
import pandas as pd
import datetime
import string
#############################Definiciones de clases###########################



class individuos:
    """define cada uno de los individuos. comienza en un lugar aleatorio del espacio esp y
    tiene un numero identificatorio que se pasa cuando se crea, por defecto es 0, Carga viral 
    expresa la cantidad de veces que fue infectado y carga viral 2 expresa la sumatoria de las 
    cargas virales de quienes lo infectaron. Tamanio representa la fraccion del espacio que ocupa
    excluida para otras partículas"""
    def __init__(self,esp,idn=0):
        self.nid = idn
        self.infectado = False
        self.antubicacion = 0
        self.ubicacion = np.array([random.randint(0,esp.ancho),random.randint(0,esp.alto)])
        self.tamanio = 1
        self.carga_viral = 0
        self.carga_viral2 = 0
        self.infectado_paso = np.nan
        self.infecte_a = 0
        self.ultdx = 0
        self.ultdy = 0
        self.color = self.pick_color()
        self.trayectoria = []
    def infectar(self):
       self.infectado = True
    def nueva_ubicacion(self,esp):
        dx,dy = random.random(),random.random()
        a = int(esp.k)*random.choice(np.linspace(self.ubicacion[0]-dx,self.ubicacion[0]+dx,10))
        b = int(esp.k)*random.choice(np.linspace(self.ubicacion[1]-dy,self.ubicacion[1]+dy,10))
        c = np.array([a,b])
        
        return c,dx,dy
    
    def pick_color(self):
      """Elije un color al azar de la colección CSS4"""
      a = mcd.CSS4_COLORS
      b = random.choice(list(a.keys()))
      return b
  
    def mover(self,esp):
        dx,dy = random.random(),random.random() 
        self.antubicacion = self.ubicacion
        self.ubicacion, self.ultdx, self.ultdy = self.nueva_ubicacion(esp)
        while self.ubicacion[0] > esp.ancho or self.ubicacion[1] > esp.alto or self.ubicacion[0] <0 or self.ubicacion[1] < 0:
            self.ubicacion, self.ultdx, self.ultdy = self.nueva_ubicacion(esp)

class espacio:
    
    """Genera un espacio, determina nro de ind, dist de cont y pasos. DIms tambien"""
    def __init__(self,n_ind, dista,k=1, pasos = 100, ancho = 100,alto = 100):
        self.tiempo = 0
        self.ancho = ancho
        self.alto =  alto
        self.tiempo = 0 ##Resolver
        self.pasos = pasos
        self.inds = n_ind
        self.dista = dista
        self.infectados = []
        self.porpaso = []
        self.cont = 0
        self.k = 1
    def df_a(self,step,conteo):
        self.porpaso.append((step,conteo))
    

     
  


#####################Funciones utilizadas en el programa########################

def dist_t(tpl):
    t1,t2 = tpl
    """Mide distancias entre dos individuos en una tupla"""
    return np.sqrt(np.sum(np.power((t1.ubicacion-t2.ubicacion),2)))             

def dios(esp):
    """crea individuos como eslabones de una lista. num indica el numero de individuos a crear.
    """
    a = list(range(esp.inds))
    for i in a:
        a[i] = individuos(esp,i)
    return a 




def primer_infectado(l_individuos):
    """infecta al individuo 0"""
    l_individuos[0].infectar()

        
    
def graficar2(lista, esp):
    """grafica a los individuos como puntos azules los infectados los resalta con x roja"""
    for i in lista:
        plt.plot(i.ubicacion[0],i.ubicacion[1],"bo-")
        if i.infectado == True:
            plt.plot(i.ubicacion[0],i.ubicacion[1],"rx")
    plt.xlim(0,esp.ancho)
    plt.ylim(0,esp.alto)
    plt.show()
    


def hay_afuera(lista,esp):
    """Retorna un booleano si hay individuos afuera del mapa"""
    f = np.zeros(len(lista))
    for i in range(len(lista)):
        mezza = lista[i].ubicacion[0] >esp.ancho  or lista[i].ubicacion[1] > esp.alto or lista[i].ubicacion[0] <0  or lista[i].ubicacion[1] <0
        f[i] = mezza    
        a = np.any(f)
        return a

def comparador(esp,l_ind,paso):
    x = combinations(l_ind,2)
    for i in x:
        i1 , i2 = i
        eix_min = i1.ubicacion[0]-esp.dista
        eix_max = i1.ubicacion[0]+esp.dista
        eiy_min = i1.ubicacion[1]-esp.dista
        eiy_max = i1.ubicacion[1]+esp.dista
        intervalo_x  = pd.Interval(left = eix_min,right = eix_max)
        intervalo_y = pd.Interval(left = eiy_min,right = eiy_max)
        if i2.ubicacion[0] in intervalo_x and i2.ubicacion[1] in intervalo_y:
            if i1.infectado == True and i2.infectado == False:
                i2.infectar()
                i1.infecte_a+=1
                i2.infectado_paso = paso
                i1.carga_viral +=1
                esp.cont +=1
                esp.infectados.append(i2)
            elif i2.infectado == True and i1.infectado == False:
                i1.infectar()
                i2.infecte_a+=1
                i1.infectado_paso = paso
                i1.carga_viral +=1
                esp.cont+=1
                esp.infectados.append(i1)
            elif i2.infectado == True and i1.infectado == True:
                i1.carga_viral +=1
                i2.carga_viral+=1
    cont = esp.cont
    return cont





def mover_graficar_dist(l_ind,esp):
    """Mueve a todos los individuos y grafica vectores por trayectoria, con cada color distinto por individuo, llama a contagios"""
    for ind in l_ind:
        plt.plot(ind.ubicacion[0],ind.ubicacion[1],"bo-")
    U = 0    
    for i in range(esp.pasos):
        for ind in l_ind:
            ind.mover(esp1)
            if i % 30 == 0:
                ind.trayectoria.append((ind.ubicacion[0],ind.ubicacion[1]))
            X = comparador(esp, l_ind,i)
            U=+X
        esp.df_a(i,U)
    for ind in l_ind:
        plt.plot(ind.ubicacion[0],ind.ubicacion[1],"ro-")
    plt.xlim(0,esp.ancho)
    plt.ylim(0,esp.alto)
    plt.savefig(str(random.randint(0,15000))+".png")
    plt.show()

def contagio(esp,l_ind,paso):
    """Si dos individuos se acercan a mas de cierta distancia, y uno no está infectado, se infecta"""
    x = combinations(l_ind,2)
    #d = []
    
    for i in x:
        d = dist_t(i)
        cont = 0
        if d < esp.dista:
            i1, i2 = i
            if i1.infectado == True and i2.infectado == False:
                i2.infectar()
                i1.infecte_a+=1
                i2.infectado_paso = paso
                i1.carga_viral +=1
                esp.cont +=1
            elif i2.infectado == True and i1.infectado == False:
                i1.infectar()
                i2.infecte_a+=1
                i1.infectado_paso = paso
                i1.carga_viral +=1
                esp.cont+=1
            elif i2.infectado == True and i1.infectado == True:
                i1.carga_viral +=1
                i2.carga_viral+=1
    cont = esp.cont
    return cont
        

def distr(l_ind,esp):
    l = []
    for i in l_ind:
        if i.infectado == True:
            l.append(i.infectado_paso)
            
    df = pd.DataFrame()
    df["inf_paso"] = l
    df.to_csv("pas" + str(esp.pasos) + "inds" + str(esp.inds) + "dis" + str(esp.dista)+ ".csv")
    return l ,df


def dataframe (l_ind, esp):
    """Genera un dataframe de pandas. Resume las características de todos los individuos en el espacio"""
    l = [x for x in vars(l_ind[0]).keys()]
    x2 = pd.DataFrame()
    for ind in l_ind:
        
        l2 = [x for x in vars(ind).values()]
        sl2 = pd.Series(l2)
        dfsl2 = pd.DataFrame([sl2])
        x2 = pd.concat([x2,dfsl2],ignore_index = True)    
    x2.columns = l 
    a = str(datetime.datetime.now())
    J = "Pas"+ str(esp.pasos)+"Inds"+ str(esp.inds)+str(random.choice(range(20)))
    x2.to_csv(J+ ".csv")
    return x2
            
def dataframe2(esp):
    """Genera un dataframe de pandas. Primera columna es el número de paso y la segunda es el numero de infectados en ese paso"""
    X = esp.porpaso
    x = []
    y = []
    for i in X:
        i, j = i
        x.append(i)
        y.append(j)
    df = pd.DataFrame()
    df["Paso"] = x
    df["Infectados"] = y
    J = "Pas"+ str(esp.pasos)+"Inds"+ str(esp.inds)+str(random.choice(range(20)))
    df.to_csv("por_pa" + J + ".csv")
    return df
    
def post_plot(l_ind,esp):
    for ind in l_ind:
        plt.plot(*zip(*ind.trayectoria), color = ind.color)
    plt.xlim(0,esp.ancho)
    plt.ylim(0,esp.alto)
    plt.ylabel("Longitud del espacio")
    plt.xlabel("Ancho del espacio")
    plt.savefig(C_especiales(datetime.datetime.now()) + ".pdf")
    plt.show()
    
    
def C_especiales(datet):
    estr = str(datet)
    conj = string.ascii_letters + string.digits
    a = [i for i in estr if i in conj]
    e = "".join(a)
    return e 

##############-------Inicio del Programa-------##############        

start = datetime.datetime.now()    
nind = int(input(prompt = "Ingrese Numero de Individuos = "))
dist = float(input(prompt = "Ingrese distancia critica = "))
pasos = int(input(prompt = "Cuantos pasos se realizaran? = ")) 
ka = int(input(prompt = "ingrese la constante = "))
ancho = float(input(prompt = "Cual es el ancho del espacio = "))
alto = float(input(prompt = "Cual es el alto del espacio = "))     
esp1 = espacio(nind,dist,ka,pasos,ancho,alto)
l1 = dios(esp1)
primer_infectado(l1)
if hay_afuera(l1,esp1):
    print("Hay gente fuera del mapa")
else:
    print("no hay gente afuera del mapa")
graficar2(l1,esp1)
mover_graficar_dist(l1,esp1)
graficar2(l1,esp1)
dataframe(l1,esp1)
dataframe2(esp1)
distr(l1,esp1)
end = datetime.datetime.now()
dur = end - start
print(dur)
if hay_afuera(l1,esp1):
    print("Hay gente fuera del mapa")
else:
    print("no hay gente afuera del mapa")
################-------Fin del Programa-------################
