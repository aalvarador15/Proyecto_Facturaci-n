import os
import datetime
import time


# Variables globales: Colores en formato ANSI escape code
reset_color = "\033[0m"
red_color = "\033[91m"
green_color = "\033[92m"
yellow_color = "\033[93m"
blue_color = "\033[94m"
purple_color = "\033[95m"
cyan_color = "\033[96m"

# funciones de usuario

def gotoxy(x,y):
    print("%c[%d;%df"%(0x1B,y,x),end="")
def calcular_tiempo_de_ejecucion(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo de ejecución de '{func.__name__}': {fin - inicio} segundos")
        return resultado
    return wrapper
@calcular_tiempo_de_ejecucion
def borrarPantalla():
    os.system("cls") 

def mensaje(msg,f,c):
    pass

def dibujar_cuadro():
    terminal_size = os.get_terminal_size()
    ancho = terminal_size.columns - 2
    alto = terminal_size.lines - 2
    print(green_color + '*' + '*' * ancho + '*' + reset_color)
    for _ in range(alto):
        print(green_color + '*' + ' ' * ancho + '*' + reset_color)
    print(green_color + '*' + '*' * ancho + '*' + reset_color)