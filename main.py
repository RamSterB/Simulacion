import threading
from interfaz import select_n_and_solve

if __name__ == "__main__":
    
    # Crear dos threads para ejecutar en paralelo los algoritmos determinista y de las vegas
    thread_determinist = threading.Thread(target=select_n_and_solve, args=("determinist",))
    thread_vegas = threading.Thread(target=select_n_and_solve, args=("vegas",))

    # Iniciar los threads
    thread_determinist.start()
    thread_vegas.start()

    # Esperar a que ambos threads terminen
    thread_determinist.join()
    thread_vegas.join()

# Se espera que se muestren dos ventanas, una para el algoritmo determinista y otra para el algoritmo de las vegas.
# Ambas ventanas permiten seleccionar el valor de n y mostrar la solución al problema de las n reinas.
    
