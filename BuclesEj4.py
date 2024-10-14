#Calcula la Hipotenusa. Para ello, pide al usuario que te de el valor de los catetos. Por seacaso,
#comprueba que los catetos son mayores a 0. Hasta que estos datos sean validados no calcular

CatetoA = float(input("dame el valor de A"))
CatetoB = float(input("dame el valor de B"))

while CatetoA <= 0 or CatetoB <=0
    print("error, Catetos deben ser mayor a cero")
    CatetoA = float(input("dame el valor de A:"))
    CatetoB = float(input("dame el valor de cateto B"))
    
if CatetoA > 0:
    if catetoB < 0:
        print("el valor de la hipotenusa es: {(catetoA**2+catetoB**2)}**1/2")
    else:
        print("B es menor o igual a cero,esto es un error")
 else:
    print("A es menor o igual a cero, esto es un error") 
    