import threading

# Definimos una variable global compartida
contador_global = 0

# Creamos un objeto mutex para controlar el acceso al recurso compartido
mutex = threading.Lock()

# Función que incrementa el contador global de forma segura utilizando un mutex
def incrementar():
    global contador_global
    # Adquirimos el mutex para asegurar que solo un hilo puede ejecutar esta sección a la vez
    mutex.acquire()
    try:
        # Sección crítica: Incrementamos el contador
        contador_global += 1
    finally:
        # Liberamos el mutex para permitir que otros hilos puedan adquirirlo
        mutex.release()

# Función que ejecuta la tarea de incrementar el contador un número determinado de veces
def tarea():
    # Imprimimos un mensaje indicando que el hilo ha comenzado su tarea
    print(f"Hilo {threading.current_thread().name} ha comenzado")
    for _ in range(100000):
        incrementar()  # Llamamos a la función para incrementar el contador de forma segura
    # Imprimimos un mensaje indicando que el hilo ha terminado su tarea
    print(f"Hilo {threading.current_thread().name} ha terminado")

# Imprimimos el valor inicial del contador global
print("Valor inicial del contador global:", contador_global)

# Creamos dos hilos que ejecutarán la misma tarea
hilo1 = threading.Thread(target=tarea, name='Hilo-1')
hilo2 = threading.Thread(target=tarea, name='Hilo-2')

# Iniciamos la ejecución de los hilos
hilo1.start()
hilo2.start()

# Esperamos a que ambos hilos terminen su ejecución
hilo1.join()
hilo2.join()

# Imprimimos el valor final del contador global después de que ambos hilos hayan terminado
print("Valor final del contador global:", contador_global)
