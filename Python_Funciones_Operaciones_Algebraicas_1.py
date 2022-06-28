#%%
import matplotlib.pyplot as plt
import numpy as np

# Definir la función g
def g(x):
    if x != 0:
        return (12/(2*x))**2
    else:
        return np.inf

# Plotea salida de la función g
def plotear(x,y):
    fig, axes = plt.subplots(1,1,figsize=(10,5))
    axes.plot(x,y,'r--',label="$(12/(2*x))**2$")
    return fig,axes

def plotear_punto(x,y,fig,axes):
     axes.plot(x,y,'ro')

# Crear un intervalo de valores 'x' de -100 a 100
x = np.linspace(-100,100,201)


# Obtener los valores 'y' correspondientes de la función
y = [g(i) for i in x]

# Configurar el gráfico
def configurar(fig,axes):

    axes.set_title('FUNCION ALGEBRAICA Y GRAFICA')
    axes.set_xlabel('X')
    axes.set_ylabel('Y')
    axes.legend()

# Graficar 'x' contra g(x)
fig,axes = plotear(x,y)
configurar(fig,axes)
# Plotea un círculo vacío para mostrar el punto indefinido
plotear_punto(0,40,fig,axes)

