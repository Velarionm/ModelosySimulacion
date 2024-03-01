import numpy as np
import pandas as pd
import pandas_datareader.data as pdr
import seaborn as sns 
import matplotlib.pyplot as plt
from matplotlib import style
from scipy.stats import norm
import os

# Establece tu API key de Tiingo (reemplaza 'TU_API_KEY' con tu propia clave)
TIINGO_API_KEY = 'TU_API_KEY'

style.use('seaborn-v0_8-bright')

ticker = 'eze.mc'

# Obtén los datos utilizando la API de Tiingo
df = pdr.get_data_tiingo(ticker, api_key=TIINGO_API_KEY)

# Crea un DataFrame para almacenar los datos de cierre ajustados
data = pd.DataFrame(df['adjClose'])

log_returns = np.log(1 + data.pct_change())
u = log_returns.mean()
var = log_returns.var()
drift = u - (0.5 * var)
stdev = log_returns.std()

# VARIABLES CONFIGURABLES POR EL USUARIO
days = 100
trials = 1000   # Numero de pruebas

# Componente de azar
Z = norm.ppf(np.random.rand(days, trials))
retornos_diarios = np.exp(drift.values + stdev.values * Z)
camino_de_precios = np.zeros_like(retornos_diarios)
camino_de_precios[0] = data.iloc[-1]

for t in range(1, days):
    camino_de_precios[t] = camino_de_precios[t-1] * retornos_diarios[t]

# APARTADO PARA EL GRAFICO
plt.figure(figsize=(15,6))
plt.plot(pd.DataFrame(camino_de_precios))
plt.xlabel("Numero De dias")
plt.ylabel("Precio de " + ticker)
sns.displot(pd.DataFrame(camino_de_precios).iloc[-1])
plt.xlabel("Precio a " + str(days) + " días")
plt.ylabel("Frecuencia")
plt.show()
