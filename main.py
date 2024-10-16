from classe_animal import Animal


def app_animal():
    perro = Animal("chimuelo", 7,"perro")
    gato = Animal("suertudo", 2 ,"gato" )
    
    print (perro.describir())
    print (perro.edad_en_anios_humanos)
    print (gato.describir())
    print (gato.edad_en_anios_humanos)
    print (Animal.cuidados_generales())

if __name__ == "__main__":
    app_animal()
    
    
