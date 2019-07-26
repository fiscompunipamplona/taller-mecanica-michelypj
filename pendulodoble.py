from numpy import array, linspace
from math import sin, cos, pi
from pylab import plot, xlabel, ylabel, show
from scipy.integrate import odeint

from vpython import sphere, scene, vector, color, arrow, text, sleep

arrow_size = 0.1

arrow_x = arrow(pos=vector(0,0,0), axis=vector(arrow_size,0,0), color=color.red)
arrow_y = arrow(pos=vector(0,0,0), axis=vector(0,arrow_size,0), color=color.green)
arrow_z = arrow(pos=vector(0,0,0), axis=vector(0,0,arrow_size))

R = 0.02 #Radio de la esfera

def func (conds, t, g, l): #Función que devuelve valores de theta y omega(arreglo)
    dda=conds[4]
    ddb=conds[5]
    dphi1=conds[1]
    da=(1/2)*(-(conds[5])*cos(conds[0]-conds[2])-((conds[2])**2)*sin(conds[0]-conds[2]))-(g/l)*sin(conds[0])
    dphi2=conds[3]
    db=-(conds[4])*cos(conds[0]-conds[2])+((conds[1])**2)*sin(conds[0]-conds[2])-(g/l)*sin(conds[2])
    return array([dphi1,da,dphi2,db,dda,ddb], float)

g = 9.81
l = 0.1

phi1=60*pi/180.
a=0.
phi2=45*pi/180.
b=0.
da=0.
db=0.

initcond = array([phi1,a,phi2,b,da,db])

n_steps = 1000 #Número de pasos
t_start = 0.   #Tiempo inicial
t_final = 15.  #Tiempo final
t_delta = (t_final - t_start) / n_steps #Diferencial de tiempo (Paso temporal)
t = linspace(t_start, t_final, n_steps) #Arreglo de diferencial de tiempo

solu, outodeint = odeint( func, initcond, t, args = (g, l), full_output=True) #Solución de la ecuación diferencial(Parámetros acordes a los definidos en la función) 
#solu (Matriz de n filas y 2 columnas) es la solución diferencial para cada paso(columnas) de theta y omega


phi_1,aa,phi_2,bb,aaa,bbb = solu.T #Devuelve la matriz transpuesta (a cada una de las variables de la izquierda, theta y omega, le define el respectivo vector)

# =====================

scene.range = 0.2 #Tamaño de la ventana de fondo

xp = l*sin(phi1) #Pasa de coordenadas polares a cartesianas
yp = -l*cos(phi1)
zp = 0.

xs=l*(sin(phi1)+sin(phi2))
ys=-l*(cos(phi1)+cos(phi2))
zs=0.

sleeptime = 0.0001 #Tiempo con que se actualiza la posición de la partícula

prtcl = sphere(pos=vector(xp,yp,zp), radius=R, color=color.yellow) #Define objeto con que se va a trabajar
prtcls= sphere(pos=vector(xs,ys,zs), radius=R, color=color.white)

time_i = 0 #Contador que se mueve en el espacio temporal en el que se resolvió la ecuación diferencial
t_run = 0  #Tiempo en el que se ejecuta la animación

#for i in omega:
#    print(i)


while t_run < t_final: #ANIMACIÓN
    prtcl.pos = vector( l*sin(phi_1[time_i]), -l*cos(phi_1[time_i]), zp )
    prtcls.pos= vector( l*(sin(phi_1[time_i])+sin(phi_2[time_i])), -l*(cos(phi_1[time_i])+cos(phi_2[time_i])), zs )
    t_run += t_delta
    sleep(sleeptime)
    time_i += 1

