import threading  # Importamos el módulo threading para trabajar con hilos
import time  # Importamos el módulo time para utilizar la función sleep

# Creamos un objeto evento
evento = threading.Event()

# Función que espera a que se active el evento
def esperar_evento():
    print("Esperando al evento...")  # Imprimimos un mensaje indicando que estamos esperando
    evento.wait()  # Esperamos a que el evento se active
    print("El evento ha sido activado!")  # Imprimimos un mensaje cuando el evento se activa

# Función que activa el evento después de un cierto tiempo
def activar_evento():
    print("Esperando 5 segundos antes de activar el evento...")  # Indicamos que vamos a esperar 5 segundos
    time.sleep(5)  # Pausamos la ejecución durante 5 segundos
    evento.set()  # Activamos el evento
    print("El evento ha sido activado después de 5 segundos\n")  # Mensaje indicando que el evento ha sido activado

# Creamos dos hilos que ejecutarán las funciones
hilo1 = threading.Thread(target=esperar_evento)  # Primer hilo ejecutará la función 'esperar_evento'
hilo2 = threading.Thread(target=activar_evento)  # Segundo hilo ejecutará la función 'activar_evento'

# Iniciamos los hilos
hilo1.start()  # Iniciamos el primer hilo
hilo2.start()  # Iniciamos el segundo hilo

# Esperamos a que ambos hilos terminen
hilo1.join()  # Espera a que el primer hilo termine
hilo2.join()  # Espera a que el segundo hilo termine

print("Programa terminado")  # Mensaje indicando que el programa ha finalizado
