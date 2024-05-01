from utilities import borrarPantalla, gotoxy
from utilities import reset_color,red_color,green_color,yellow_color,blue_color,purple_color,cyan_color
import time
import math

class Menu:
    def __init__(self,titulo="",opciones=[],col=6,fil=1):
        self.titulo=titulo
        self.opciones=opciones
        self.col=col
        self.fil=fil
        
    def menu(self):
        gotoxy(self.col,self.fil);print(self.titulo)
        self.col-=5
        for opcion in self.opciones:
            self.fil +=1
            gotoxy(self.col,self.fil);print(opcion)
        gotoxy(self.col+5,self.fil+2)
        opc = input(f"Elija opcion[1...{len(self.opciones)}]: ") 
        return opc   

class Valida:
    def solo_numeros(self,mensajeError,col,fil):
        while True: 
            gotoxy(col,fil)            
            valor = input()
            try:
                if int(valor) > 0:
                    break
            except:
                gotoxy(col,fil);print(mensajeError)
                time.sleep(1)
                gotoxy(col,fil);print(" "*20)
        return valor

    def solo_letras(self,mensaje,mensajeError): 
        while True:
            valor = str(input("          ------>   | {} ".format(mensaje)))
            if valor.isalpha():
                break
            else:
                print("          ------><  | {} ".format(mensajeError))
        return valor

    def solo_decimales(self,mensaje,mensajeError):
        while True:
            valor = str(input("          ------>   | {} ".format(mensaje)))
            try:
                valor = float(valor)
                if valor > float(0):
                    break
            except:
                print("          ------><  | {} ".format(mensajeError))
        return valor
    
    def cedula():
        pass
    
    def validar_letras(Frase,x,y):
        while True:
            gotoxy(x,y),
            nombre = input(f"{Frase}").strip()
            if nombre.isalpha():
                return nombre.capitalize()
            else:
                 gotoxy(50,25);print(yellow_color+"El campo solo puede contener letras.")
                
    
    def validar_numeros(Frase,x,y):
        while True:
            gotoxy(x,y)
            numero = input(f"{Frase}")
            if numero.isdigit():
                return numero
            else:
                 gotoxy(50,25);print(yellow_color+"El campo solo puede contener números enteros.")
    def validar_decimales(Frase,x,y):
        while True:
            gotoxy(x,y)
            numero = input(f"{Frase}")
            if numero.replace('.', '', 1).isdigit():  # Remueve un punto decimal y luego verifica si el resto es un número
                return numero
            else:
                gotoxy(50,25);print(yellow_color+"El campo solo puede contener números decimales.")

    def validar_dni(mensaje,x,y):
        while True:
            gotoxy(x,y)
            # print(blue_color + f"{mensaje}")
            cedula = input(f'{mensaje}')
            
            if len(cedula) == 10 and cedula.isdigit():
                coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2]
                suma = 0
                
                for i in range(9):
                    digito = int(cedula[i]) * coeficientes[i]
                    if digito > 9:
                        digito -= 9
                    suma += digito
                
                total = suma % 10
                if total != 0:
                    total = 10 - total
                
                # Verifica si el dígito de control es igual al último dígito del DNI
                if total == int(cedula[9]):
                    return cedula
            
            gotoxy(50,25);print(purple_color + "El formato del DNI es incorrecto.")
        
  


if __name__ == '__main__':
    # instanciar el menu
    opciones_menu = ["1. Entero", "2. Letra", "3. Decimal"]
    menu = Menu(titulo="-- Mi Menú --", opciones=opciones_menu, col=10, fil=5)
    # llamada al menu
    opcion_elegida = menu.menu()
    print("Opción escogida:", opcion_elegida)
    valida = Valida()
    if(opciones_menu==1):
      numero_validado = valida.solo_numeros("Mensaje de error", 10, 10)
      print("Número validado:", numero_validado)
    
    numero_validado = valida.solo_numeros("Mensaje de error", 10, 10)
    print("Número validado:", numero_validado)
    
    letra_validada = valida.solo_letras("Ingrese una letra:", "Mensaje de error")
    print("Letra validada:", letra_validada)
    
    decimal_validado = valida.solo_decimales("Ingrese un decimal:", "Mensaje de error")
    print("Decimal validado:", decimal_validado)