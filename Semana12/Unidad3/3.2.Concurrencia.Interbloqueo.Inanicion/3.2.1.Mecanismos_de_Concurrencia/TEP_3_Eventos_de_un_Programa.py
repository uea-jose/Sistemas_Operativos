# Importamos el módulo threading para trabajar con hilos
import threading
# Importamos el módulo time para utilizar la función sleep
import time

# Creamos un objeto evento
evento = threading.Event()

# Función que espera a que se active el evento
def esperar_evento():
    # Imprimimos un mensaje indicando que estamos esperando
    print("Esperando al evento...")
    evento.wait()  # Esperamos a que el evento se active
    # Imprimimos un mensaje cuando el evento se activa
    print("El evento ha sido activado!")

# Función que activa el evento después de un cierto tiempo
def activar_evento():
    # Indicamos que vamos a esperar 5 segundos
    print("Esperando 5 segundos antes de activar el evento...")
    time.sleep(5)  # Pausamos la ejecución durante 5 segundos
    evento.set()  # Activamos el evento
    # Mensaje indicando que el evento ha sido activado
    print("El evento ha sido activado después de 5 segundos\n")

# Creamos dos hilos que ejecutarán las funciones
# Primer hilo ejecutará la función 'esperar_evento'
hilo1 = threading.Thread(target=esperar_evento)
# Segundo hilo ejecutará la función 'activar_evento'
hilo2 = threading.Thread(target=activar_evento)

# Iniciamos los hilos
hilo1.start()  # Iniciamos el primer hilo
hilo2.start()  # Iniciamos el segundo hilo

# Esperamos a que ambos hilos terminen
hilo1.join()  # Espera a que el primer hilo termine
hilo2.join()  # Espera a que el segundo hilo termine

# Mensaje indicando que el programa ha finalizado
print("Programa terminado")
