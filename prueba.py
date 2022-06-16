# ------------------------------------------------------------
# Problema 4:
# Desarrollar una clase que represente un punto en el plano y 
# tenga los siguientes métodos:
# inicializar los valores de x e y que llegan como parámetros, 
# imprimir en que cuadrante se encuentra dicho punto (concepto
# matemático, primer cuadrante si x e y son positivas, si x<0 
# e y>0 segundo cuadrante, etc.)
# ------------------------------------------------------------

class Punto:
    def __init__( self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"El punto está en x={self.x}, y={self.y}"

    def mostrarCuadrante(self):
        if self.x >0 and self.y > 0:
            print("El punto está en el primer cuadrante")
        elif self.x <0 and self.y > 0:
            print("El punto está en el segundo cuadrante")
        elif self.x <0 and self.y < 0:
            print("El punto está en el tercer cuadrante")  
        elif self.x >0 and self.y < 0:
            print("El punto está en el cuarto cuadrante")
        else: 
            print("El punto está sobre los ejes")  

    


#-------------------
print("\033[H\033[J")  


punto1 = Punto(0,3)
punto2 = Punto(4,3)
punto3 = Punto(-4,3)
print(punto2)
punto1.mostrarCuadrante()

del punto1

print("Aca finaliza el programa")



