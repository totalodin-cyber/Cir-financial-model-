import pandas as pd
import numpy as np
import yfinance as yf

#-----------
#MODELO CIR
#----------


#descargamos los datos

ticker_bono= "^TNX"

datos=yf.Ticker(ticker_bono).history(period="1y")

tasas=datos["Close"].dropna()

tasas_limpias=tasas.to_numpy()/100

r_ant = tasas_limpias[:-1]
r_act = tasas_limpias[1:] 

datosx = r_ant
datosy = r_act - r_ant

Rt = tasas_limpias[-1] 


#tiene que ser lista aqui para operar, ya que si importa  el orden de la operacion y si importan los repetidos 

promedio_Y=np.mean(datosy)
promedio_X=np.mean(datosx)


#FACTORES:

#calculo de k

matriz_covarianza=np.cov(datosx, datosy, ddof=1)
dato_de_covarianza=matriz_covarianza[0,1] #esto para que el resultado sea un numero, no una matriz
varianza=np.var(datosx, ddof=1) #solo puede haber una lista
b1=(dato_de_covarianza/varianza)
k= -(b1)



#calculo de theta
intercepto=promedio_Y-b1*promedio_X
theta= -(intercepto/b1)
print(f"Theta es {theta}")

#Calculo de  volatividad 


residuo=datosy-(intercepto+b1*r_ant)
residuos_normalizados=residuo/ np.sqrt(r_ant)
sigma=np.std(residuos_normalizados, ddof=1)


#proceso de wiener

dt=1/252

wiener=np.random.normal(0,1)*np.sqrt(dt) #usando distribucion normal
print(f"El proceso de wiener es {wiener}")


#Calculo 

cir=k*(theta-Rt)*dt+ sigma * np.sqrt(Rt) * wiener

#Anualizacion de los datos, ya que teniamos datos con escala diaria. Solo se anualiza velocidad de reversion y volatividad
k_anual=k*252
sigma_anual=sigma*(np.sqrt(252))
print(f"La velocidad de reversion anual es de {k_anual} y la volatividad de {sigma_anual}")
print(F"La variacion de tasas de interes por CIR es {cir}")

diferencia=2*k*theta - sigma**2
if (2*k*theta >= sigma**2):
    
    print(f"El modelo es valido para operar por una diferencia de {diferencia}")
else:
    print(f"El modelo no es valido para operar por una diferencia de {diferencia}")
    


