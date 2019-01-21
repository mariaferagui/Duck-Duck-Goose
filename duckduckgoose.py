def duckduckgoose (gente, posicion):
    lista = list (gente)
    posicion = int (posicion)
    oca = lista[posicion]
    return oca, posicion

oca = duckduckgoose (['María', 'Alicia', 'Blanca', 'Celia','Espe'], 4)[0]
posicion = duckduckgoose (['María', 'Alicia', 'Blanca', 'Celia','Ainhoa','Lucía'], 4)[1]

print ('La oca es: ', oca, 'y su posición es: ', posicion)
