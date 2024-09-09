import threading  # Importamos el módulo threading para trabajar con hilos
#
# Creamos una barrera que permitirá que hasta 2 hilos esperen antes de continuar
barrera = threading.Barrier(2)

# Definimos una función que representa la tarea que ejecutará cada hilo
def tarea():
    print("Hilo iniciado")  # Imprimimos un mensaje indicando que el hilo ha comenzado
    barrera.wait()  # El hilo se detiene aquí hasta que ambos hilos hayan llegado a este punto
    print("Hilo continuando")  # Una vez que ambos hilos han llegado, continúan ejecutándose

# Creamos dos hilos que ejecutarán la misma tarea
hilo1 = threading.Thread(target=tarea)  # Primer hilo que ejecutará la función 'tarea'
hilo2 = threading.Thread(target=tarea)  # Segundo hilo que ejecutará la función 'tarea'

# Iniciamos los hilos para que comiencen a ejecutar la función 'tarea'
hilo1.start()  # Inicia el primer hilo
hilo2.start()  # Inicia el segundo hilo

# Esperamos a que ambos hilos terminen su ejecución antes de continuar
hilo1.join()  # Espera a que el primer hilo termine
hilo2.join()  # Espera a que el segundo hilo termine

print("Programa terminado")  # Imprimimos un mensaje indicando que el programa ha finalizado
