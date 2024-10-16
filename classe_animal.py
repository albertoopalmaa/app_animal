
class Animal:
        especie_peligro=True
        
        def __init__(self, nombre:str, edad:int, tipo:str):
            self.nombre: str= nombre
            self.edad: int= edad
            self.tipo: str= tipo
            
        @property
        def edad_en_anios_humanos(self):
                """"Calcula la edad del animal en años humanos."""
                if self.tipo.lower() == "perro":
                        return f"En años humanos tiene {self.edad * 7}"
                elif self.tipo.lower() == "gato":
                        return f"En años humanos tiene {self.edad * 6}"
                else:
                        return f"En años humanos tiene {self.eda}"

        def describir(self):
                """Metodo que despcribe al animal"""
                return f"{self.nombre} es un {self.tipo} de {self.edad} años"

        @classmethod 
        def especie_en_peligro(cls):
                """Metodo de clase que si la especie esta en peligro"""
                return cls.especie_peligro 

        @staticmethod
        def cuidados_generales():
                """"Metodo estatico proporciona informacion basica sobre cuidados"""
                return "Proporcionar agua, comida y atencion veterinaria"

