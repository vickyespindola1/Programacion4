#Tenemos la pantalla del celu bloqueada. Partiendo de un PIN_SECRETO, intentaremos
#desbloquear la pantalla. Tenemos hasta 3 intentos. Simula el proceso con Python. En caso de
#acceder, lanza al usuario 'login correcto'. Sino, 'llamando al policía'.

PIN_SECRETO = "1212"  

for intento in range(3):  
    pin_ingresado = input("Introduce el PIN para desbloquear: ")

    if pin_ingresado == PIN_SECRETO: 
        print("Login correcto")  
        break 
else:  
    print("Llamando al policía...")  