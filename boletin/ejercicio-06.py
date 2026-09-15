horas = [530, 682, 258, 662, 310, 405, 118, 684, 473, 829]
libres = [False, True, False, False, True, False, True, True, False, False]

maquina_seleccionada = None

if True in libres:
    for i in range(len(horas)):
        if libres[i]==True and ((maquina_seleccionada is None) or (horas[i] < horas[maquina_seleccionada])): # True es redundante
            maquina_seleccionada = i
    print("maquina_seleccionada: ", maquina_seleccionada+1)
else:
    print("Ninguna libre")