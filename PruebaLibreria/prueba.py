import numpy as np
import matplotlib.pyplot as plt
from numpy.random import uniform as unif

cant_num=10   #Cantidad de numero aleatorios que generamos

##estas dos lineas solo son para graficar 
c=np.linspace(0.0001,3.2) #no empieza desde 0 para enviar un error con el
f=1/(1+np.sinh(2*c)*(np.log(c))**2)

#aqui genera numeros aleatorios especificamente en este intervalo
lim_inf=0.8
lim_sup=3
x=unif(lim_inf,lim_sup,cant_num)

#inicializamos la variable de la sumatoria

suma=0

for j in range(cant_num):
    suma=suma+1/(1+np.sinh(2*x[j])*(np.log(x[j]))**2)
resultado=(lim_sup-lim_inf)*suma/cant_num

plt.xlabel('x')
plt.ylabel('y')
plt.plot(c,f)
plt.hist(x,density=True)

print("El resultado de la integral es:")
print(resultado)
