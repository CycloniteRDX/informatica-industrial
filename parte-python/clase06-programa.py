#import resistencias as re
#print(re.limite)

#from resistencias import limite,calc_resis as calcular
#print(limite, calcular(100,2))

import resistencias # importando de esta manera siempre debemos poner resistencias."metodo"
from resistencias import * # * de esta manera podemos llamar a los métodos directament

print(resistencias.medidas, resistencias.limite, medidas, limite)

resistencias.limite = 345
print(resistencias.limite, limite)

#medidas[0]=12341346457
medidas = [1,2]
print(medidas,resistencias.medidas)

try:
    resistencias.calc_resis(100,-2)
except ValueError as ve:
    print("ERROR: ",str(ve))