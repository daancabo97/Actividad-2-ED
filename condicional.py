genero =  str(input('Usted es hombre o mujer? : '))
alimentacion = str(input('Usted es carnivor@ o vegetarian@? :'))


print("-------------------------------------------------------")

if genero == "hombre":
    print(f'Usted es mucho {alimentacion}',"mano!") 
    if alimentacion != "carnivoro":
        print('Aviso : Eres una flor que se mese con el viento 🤣, fracasaste como hombre, come mas carne!')    
    else:
        print(f'Recomendacion : Oiga {genero} le recomiendo cuidar el planeta! 👍 ')   
               
if genero == "mujer":
    print(f'Eres una {alimentacion}', "muy linda!") 
    if alimentacion != "vegetariana":
        print('Aviso : Excelente!! Asi es que me gustan! ❤ ')    
    else:
        print(f'Halagos : Oye {genero} lo estas haciendo muy bien ternurita ❤  ')   
                         
elif genero != "hombre" and genero != "mujer":
    print(f'Genero indefinido ingrese sus datos de manera correcta') 
    





     
     

