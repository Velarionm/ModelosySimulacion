import json
import random
import numpy as np
from scipy.stats import ksone 
from scipy.stats import chi2
def problema3() -> dict:
    result = {}
    a = [21, 23]
    x = 1
    while x == 1 or (a[x - 1] != a[0] or a[x] != a[1]):
        a.append((a[x] + a[x - 1]) % 64)
        x += 1
    result["a"] = a
    result["NA(a)"] = [i / 64 for i in a]
    result["Periodo a"] = len(a)

    b = [19]
    x = 0
    while (x == 0 or (b[x] != b[0])) and x != 10 ** 8:
        b.append(211 * b[x] % (10 ** 8))
        x += 1
    result["b"] = b
    result["NA(b)"] = [i / (10 ** 8) for i in b]
    result["Periodo b"] = len(b)

    c = [3]
    x = 0
    while x == 0 or c[x] != c[0]:
        c.append(221 * c[x] % 10 ** 3)
        x += 1
    result["c"] = c
    result["NA(c)"] = [i / (10 ** 3) for i in c]
    result["Periodo c"] = len(c)

    d = [7]
    x = 0
    while x == 0 or d[x] != d[0]:
        d.append(5 * c[x] % 64)
        x += 1
    result["d"] = d

    return result

def problema4():
    results = []
    for a in range(1, 100):
        for c in range(1, 100):
            for m in range(2, 100):
                semilla = random.randint(1, m)
                array = [semilla]
                for i in range(m):
                    array.append((a * array[i] + c) % m)
                if array[m - 1] == array[0]:
                    result = {
                        "a": a,
                        "c": c,
                        "m": m,
                        "semilla": semilla
                    }
                    results.append(result)
                if len(results) == 10:
                    return results
def problema8()->dict:
    result={}
    array=[23]
    x=0
    while x==0 or array[x]!=array[0]:
        array.append((553+121*array[x])%177)
        x+=1
    result["x"]=array
    #Kolgomorrow 5
    if len(array)<20:
        array.sort()
        Dmax=0
        Dmin=0
        for i in range(len(array)):
            Dmax=max(Dmax,(i/len(array))-array[i])
            Dmin=max(Dmin,array[i]-(i-1)/len(array))
        D=max(Dmax,Dmin)
        result["D"]=D
        result["Critical Value"]=ksone.ppf(1-0.05/2,len(array))
        if result["D"]>result["Critical Value"]:
            result["Result"]="La muestra no viene de una Distribucion Uniforme"
        else:
            result["Result"]="La muestra viene de una Distribucion Uniforme"
    #Chi cuadrado
    else:
        K=len(array)*0.15
        Ei=K
        X=0
        intervalo=np.min(array)
        diferencia=(np.max(array)-np.min(array))/int(K)
        for i in range(len(array)):
            Oi=len([x for x in array if x > intervalo and x<(intervalo+diferencia)])
            X+=((Oi-Ei)**2)/Ei
            intervalo+=diferencia
        result["Chi cuadrado Teorico"]=chi2.isf(0.05,K-1)
        result["Chi cuadrado calculado"]=X
        if result["Chi cuadrado Teorico"]>result["Chi cuadrado calculado"]:
            result["Result"]="La muestra viene de una distribucion uniforme"
        else:
            result["Result"]="La muestra no viene de una distribucion uniforme"
    return result

def main():
    with open("problema3.json", "w") as p3:
        json.dump(problema3(), p3)
    
    with open("problema4.json", "w") as p4:
        json.dump(problema4(), p4)
    with open("problema8.json", "w") as p8:
        json.dump(problema8(), p8)

if __name__ == "__main__":
    main()
