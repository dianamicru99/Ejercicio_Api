import json
from pathlib import Path
import requests
import os
try:
    def menu():
        os.system('cls')
        print("Selecciona una opción:")
        print("\t1 - Listar los episodios de cada temporada de Naruto")
        print("\t2 - Todas las fechas finales de temporada de Naruto")
        print("\t3 - Salir")
        opciones=int(input("Selecciona una opcion : "))
        return (opciones)
    
    def opciones1():
        if Vinculo.status_code==200:#todo correcto
            json_data=Vinculo.json()
            Devuelve=json_data.get('results',[])
            if Devuelve:
                for x in Devuelve:
                    naruto=x ['episodes']
                    print(naruto)
    def opciones2():
        if Vinculo.status_code==200:
            json_data=Vinculo.json()
            Fecha=json_data.get('results',[])
            if Fecha:
                for j in Fecha:
                    fecha_naruto=j['end_date']
                    print(fecha_naruto)
            
        
    while True:
        url='https://api.jikan.moe/v3/search/anime?q=Naruto&limit=16'
        Vinculo=requests.get(url)
        opcion=menu()
        if opcion==1:
            opciones1()
        elif opcion==2:
           opciones2() 
        elif opcion==3:
            break
 
        input("Pulse una tecla para terminar...")

except:
    print("Ha ocurrido algun error")