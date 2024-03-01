#!/usr/bin/python
#HACKERS_FIGHT_CLUB

simpsons = ['homero','lisa','bart']
pokemon = ['ash','brock','misty']
rickymorty = ['rick','morty','jerry','squanchy']
malcom = ['dewey','reese','hal','lois','francis','malcom']


#expresion funcional:
# 1) funcion lambda que sume las cuatro listas
suma = lambda x,y,z,s : x+y+z+s
lista = suma(simpsons,pokemon,rickymorty,malcom)
print(lista)

# 2) filtre la lista resultante para obtener todos los nombres que tienen una "i"
filtrar = list(filter(lambda x:'i' in x, lista))
print(filtrar)

# 3) convierta a mayusculas el resultado anterior
#UNA SOLA EXPRESION
mayusculas = list(map(lambda x:x.upper(),filtrar))
print(mayusculas)

### todo junto visto en clase
resultado = list(map(lambda x: x.upper(), filter( lambda y: 'i' in y, (lambda w, x, y, z: x + y + w + z)(simpsons, malcom, pokemon, rickymorty))))

'''
resultado = list(  # Convierte el resultado en una lista    
    map(  # Aplica una función a cada elemento de la lista resultante
        lambda x: x.upper(),  # Convierte cada elemento a mayúsculas        
        filter(  # Filtra los elementos de la lista resultante
            lambda y: 'i' in y,  # Solo incluye los elementos que contienen la letra 'i'            
            (lambda w, x, y, z: x + y + w + z)(simpsons, malcom, pokemon, rickymorty)  # Combina todas las listas
        )    )
)
'''