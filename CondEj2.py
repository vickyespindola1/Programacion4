#Haz una calculadora básica que permita realizar el cálculo de la hipotenusa de un triángulo,
#vigilando que ningún cateto debe ser menor o igual a cero. 
# Si se diera el caso, imprimir «Error» por pantalla.
print("esta funcion calucla la hipotenusa de un triangulo rectangulo")
##solicito valor del usuairo 
CatetoA = float(input("dame el valor de A"))
CatetoB = float(input("dame el valor de B"))

if CatetoA > 0:
    if catetoB < 0:
        print("el valor de la hipotenusa es: {(catetoA**2+catetoB**2)}**1/2")
    else:
        print("B es menor o igual a cero,esto es un error")
 else:
    print("A es menor o igual a cero, esto es un error") 