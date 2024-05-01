from components import Menu,Valida
from utilities import borrarPantalla,gotoxy,dibujar_cuadro
from utilities import reset_color,red_color,green_color,yellow_color,blue_color,purple_color,cyan_color
from clsJson import JsonFile
from company  import Company
from customer import RegularClient,VipClient
from sales import Sale
from product  import Product
from iCrud import ICrud
import datetime
import time,os
from functools import reduce

path, _ = os.path.split(os.path.abspath(__file__))
# Procesos de las Opciones del Menu Facturacion
class CrudClients(ICrud):
    def create(self):
        borrarPantalla()
        dibujar_cuadro()
        gotoxy(60,2);print(purple_color+"Registro de Cliente")
        gotoxy(47,3);print(blue_color+Company.get_business_name())
        gotoxy(5,6);print(purple_color+"Seleccione el tipo de cliente:")
        gotoxy(5,7);print(red_color+"1) Cliente Regular")
        gotoxy(5,8);print(red_color+"2) Cliente VIP")
        gotoxy(5,9);tipo_cliente = input("Seleccione una opción: ")
        
        def obtener_datos_cliente(tipo):
            if tipo == "1":
                gotoxy(10,10);print(cyan_color+"Cliente Regular")
                gotoxy(10,14);nombre = Valida.validar_letras("Ingresa el nombre: ", 10, 14)
                gotoxy(10,16);apellido = Valida.validar_letras("Ingresa el apellido: ", 10, 16)
                gotoxy(10,18);dni = Valida.validar_dni("Ingrese su Dni ", 10, 18)
                gotoxy(10,20);card = input("¿El cliente tiene tarjeta de descuento? (s/n): ").lower() == "s"
                return RegularClient(nombre, apellido, dni, card)
            elif tipo == "2":
                gotoxy(10,10);print(cyan_color+"Cliente VIP")
                gotoxy(10,14);nombre = Valida.validar_letras("Ingrese su nombre: ", 10, 14)
                gotoxy(10,16);apellido = Valida.validar_letras("Ingrese su apellido: ", 10, 16)
                gotoxy(10,18);dni = Valida.validar_dni("Ingrese su Dni ", 10, 18)
                return VipClient(nombre, apellido, dni)
            else:
                gotoxy(6,7);print("Opción inválida")
                tipo_cliente = input("Seleccione una opción válida (1 o 2): ")
                return obtener_datos_cliente(tipo_cliente)
            
        new_client = obtener_datos_cliente(tipo_cliente)
        
        json_file = JsonFile(path+'/archivos/clients.json')
        clients = json_file.read()
        clients.append(new_client.getJson())
        json_file.save(clients)
        gotoxy(50,25);print(red_color+"Cliente registrado exitosamente! 😎")
        time.sleep(2)

        
    def update(self):
        borrarPantalla()
        dibujar_cuadro()
        # print('\033c', end='')
        # gotoxy(2,1);print(green_color + "*" * 90 + reset_color)
        gotoxy(60,2);print(purple_color + "Actualización de Cliente")
        gotoxy(47,3);print(blue_color + Company.get_business_name())
        gotoxy(10,6);dni = Valida.validar_dni(green_color+"Ingrese el DNI del cliente que desea actualizar: ",10,6)
        json_file = JsonFile(path + '/archivos/clients.json')
        
        # Cargar todos los clientes del archivo JSON
        clients = json_file.read()
        
        # Buscar el cliente por su DNI
        client_found = False
        for client in clients:
            if client["dni"] == dni:
                client_found = True
                gotoxy(10,8);print("Cliente encontrado:")
                gotoxy(10,9);print(f"Nombre: {client['nombre']}")
                gotoxy(10,10);print(f"Apellido: {client['apellido']}")
                gotoxy(10,11);print(f"DNI: {client['dni']}")
                print()
                # Solicitar nueva información para el cliente
                gotoxy(10,14);new_nombre =Valida.validar_letras(cyan_color+"Ingrese el nuevo nombre : ",10,14)
                gotoxy(10,16);new_apellido =Valida.validar_letras(cyan_color+"Ingrese el nuevo apellido : ",10,16)
                
                # Actualizar la información  proporcionada
                if new_nombre:
                    client['nombre'] = new_nombre
                if new_apellido:
                    client['apellido'] = new_apellido
                break  # Salir del bucle después de encontrar el cliente
                
        if client_found:
            # Guardar todos los clientes nuevamente en el archivo JSON
            json_file.save(clients)
            gotoxy(50,25);print(red_color+"Cliente actualizado exitosamente! 😎")
        else:
            gotoxy(50,25);print(red_color+"Cliente no encontrado. 😢")
        time.sleep(2)
  
    def delete(self):
        borrarPantalla()
        dibujar_cuadro()
        # print('\033c', end='')
        # gotoxy(2,1);print(green_color+"*"*90+reset_color)
        gotoxy(60,2);print(purple_color+"Eliminación de Cliente")
        gotoxy(47,3);print(blue_color+Company.get_business_name())
        gotoxy(5,6);dni =Valida.validar_dni("Ingrese el DNI del cliente que desea eliminar: ",5,6)
        json_file = JsonFile(path+'/archivos/clients.json')
        clients = json_file.read()
        
        filtered_clients = [client for client in clients if client['dni'] != dni]
        
        if len(filtered_clients) < len(clients):
            json_file.save(filtered_clients)
            gotoxy(50,25);print(red_color+"Cliente eliminado exitosamente! 😎")
        else:
            gotoxy(50,25);print(red_color+"Cliente no encontrado.😢")
        time.sleep(4)
    
    def consult(self):
        # print('\033c', end='')
        dibujar_cuadro()
        gotoxy(2,1);print(green_color+"█"*90)
        gotoxy(60,2);print(purple_color+"Consulta de Cliente")
        # gotoxy(2,2);print("██"+" "*34+"Consulta de Cliente"+" "*35+"██")
        gotoxy(2,4);dni =Valida.validar_dni("Ingrese DNI del cliente: ",2,4)
        json_file = JsonFile(path+'/archivos/clients.json')
        clients = json_file.find("dni", dni)
        
        if clients:
            client = clients[0]
            print(f"Nombre: {client['nombre']}")
            print(f"Apellido: {client['apellido']}")
            print(f"DNI: {client['dni']}")
        else:
            gotoxy(50,25);print(red_color+"Cliente no encontrado.😢")
        input("Presione una tecla para continuar...")    

        
class CrudProducts(ICrud):
    def create(self):
        borrarPantalla()
        dibujar_cuadro()
        # gotoxy(2, 1);print(green_color + "=" * 90 + reset_color)
        gotoxy(60,2);print(purple_color + "Registro de Producto")
        gotoxy(5,6);description = Valida.validar_letras("Ingrese la descripción del producto: ",5,6)
        gotoxy(5,8);price =Valida.validar_decimales("Ingrese el precio del producto: ",5,8)
        gotoxy(5,10);stock =Valida.validar_numeros("Ingrese el stock inicial del producto: ",5,10)
        
        json_file = JsonFile(path + '/archivos/products.json')
        products = json_file.read()
        
        # Obtener el último ID utilizado
        last_id = max([product['id'] for product in products]) if products else 0
        
        # Verificar si el producto ya existe
        existing_product = next((product for product in products if product['descripcion'] == description), None)
        
        if existing_product:
            print(red_color+"El producto ya existe 😉")
            print(f"ID: {existing_product['id']}, Descripción: {existing_product['descripcion']}, Precio: {existing_product['precio']}, Stock: {existing_product['stock']}")
            actualizar = input("¿Desea actualizar este producto? (s/n): ").lower()
            if actualizar == 's':
                # Actualizar el producto existente
                id_producto = existing_product['id']
                gotoxy(5,6);description = Valida.validar_letras(f"Ingrese la nueva descripción del producto (actual: {existing_product['descripcion']}): ",5,6).strip()
                gotoxy(5,8);price =float(Valida.validar_decimales(f"Ingrese el nuevo precio del producto (actual: {existing_product['precio']}): ",5,8))
                gotoxy(5,10);stock =int(Valida.validar_numeros(f"Ingrese el nuevo stock del producto (actual: {existing_product['stock']}): ",5,10))
                
                existing_product['descripcion'] = description if description else existing_product['descripcion']
                existing_product['precio'] = price if price else existing_product['precio']
                existing_product['stock'] = stock if stock else existing_product['stock']
                
                # Guardar los cambios en el archivo JSON
                json_file.save(products)
                gotoxy(50,25);print(red_color+"Producto actualizado exitosamente! 😎")
            else:
                gotoxy(50,25);print(red_color+"Registro cancelado.")
        else:
            # Crear un nuevo producto con un nuevo ID único
            new_id = last_id + 1
            new_product = Product(id=new_id, descrip=description, preci=price, stock=stock)
            products.append(new_product.getJson())
            json_file.save(products)
            gotoxy(50,25);print(red_color+"Producto registrado exitosamente! 😎")
        time.sleep(4)


    def update(self):
        borrarPantalla()
        dibujar_cuadro()
        # gotoxy(2,1);print(green_color+"*"*90+reset_color)
        gotoxy(60,2 );print(purple_color+"Actualizar producto")
        gotoxy(47,3);print(blue_color+Company.get_business_name())
        gotoxy(5,4);id_producto =int(Valida.validar_numeros("Ingrese el ID del producto que desea actualizar: ",5,4))
        json_file = JsonFile(path + '/archivos/products.json')
        products = json_file.read()

        # Buscar el producto por su ID
        found = False
        updated_products = []
        for product in products:
            if product['id'] == id_producto:
                found = True
                # Si se encuentra el producto, solicitar nueva información
                gotoxy(5,6);description = Valida.validar_letras(f"Ingrese la nueva descripción del producto (actual: {product['descripcion']}): ",5,6)
                gotoxy(5,8);price = float(Valida.validar_decimales(f"Ingrese el nuevo precio del producto (actual: {product['precio']}): ",5, 8))
                gotoxy(5,10);stock =int(Valida.validar_numeros(f"Ingrese el nuevo stock del producto (actual: {product['stock']}): ",5, 10))
                # Actualizar la información si se proporcionó
                product['descripcion'] = description if description else product['descripcion']
                product['precio'] = price if price else product['precio']
                product['stock'] = stock if stock else product['stock']
            updated_products.append(product)

        if found:
            # Guardar los cambios en el archivo JSON
            json_file.save(updated_products)
            gotoxy(50,25);print(red_color+"Producto actualizado exitosamente 😎!")
        else:
            gotoxy(50,25);print(red_color+"Producto no encontrado.😥")
        time.sleep(4)

    def delete(self):
        borrarPantalla()
        dibujar_cuadro()
        # gotoxy(2,1);print(green_color+"*"*90+reset_color)
        gotoxy(60,2 );print(purple_color+"Eliminación del producto")
        gotoxy(47,3);print(blue_color+Company.get_business_name())
        gotoxy(5,6);id_producto = int(Valida.validar_numeros("Ingrese el ID del producto que desea eliminar: ", 5, 6))

        json_file = JsonFile(path + '/archivos/products.json')
        products = json_file.read()

        # Buscar el producto por su ID
        product_a_eliminar = None
        for product in products:
            if product['id'] == id_producto:
                product_a_eliminar = product
                break

        # Si se encontró el producto, se muestra su información y se confirma la eliminación
        if product_a_eliminar:
            gotoxy(5, 10);print("El producto a eliminar es el siguiente:")
            gotoxy(5, 12);print(f"ID: {product_a_eliminar['id']}")
            gotoxy(5, 14);print(f"Nombre: {product_a_eliminar['descripcion']}")
            gotoxy(5, 16);print(f"Precio: {product_a_eliminar['precio']}")
            gotoxy(5, 18);print(f"Stock: {product_a_eliminar['stock']}")

            confirmacion = input("¿Está seguro que desea eliminar este producto? (s/n): ").lower()
            if confirmacion == "s":
                # Filtrar los productos para eliminar el seleccionado
                filtered_products = [product for product in products if product['id'] != id_producto]
                json_file.save(filtered_products)
                gotoxy(50, 25);print(red_color + "Producto eliminado exitosamente! 😎")
            else:
                gotoxy(50, 25);print(yellow_color + "Eliminación cancelada.")
        else:
            gotoxy(50, 25);print(red_color + "Producto no encontrado. 😥")

        time.sleep(4)

    def consult(self):
        borrarPantalla()
        dibujar_cuadro()
        # gotoxy(2,1);print(green_color+"*"*90+reset_color)
        gotoxy(60,2);print(purple_color+"Consulta del producto")
        gotoxy(47,3);print(blue_color+Company.get_business_name())
        json_file = JsonFile(path + '/archivos/products.json')
        products = json_file.read()

        if products:
            print("""ID   Descripción   Precio   Stock""")
            for product in products:
                print(f"""{product['id']} {product['descripcion']} {product['precio']} {product['stock']}""")

            # Opción de búsqueda por descripción
            gotoxy(15,15);search_term = Valida.validar_letras("Ingrese la descripción del producto a buscar (o dejar en blanco para omitir ):",15,15)
            if search_term:
                found = False
                for product in products:
                    if search_term.lower() in product['descripcion'].lower():
                        found = True
                        print(f"ID: {product['id']}, Descripción: {product['descripcion']}, Precio: {product['precio']}, Stock: {product['stock']}")
                if not found:
                    gotoxy(30,2);print(red_color+"No se encontraron productos con esa descripción.")
        else:
            gotoxy(50,25);print(red_color+"No hay productos registrados. 😢")

        input("Presione una tecla para continuar...")

class CrudSales(ICrud):
    def create(self):
        # cabecera de la venta
        validar = Valida()
        borrarPantalla()
        dibujar_cuadro()
        # print('\033c', end='')
        # gotoxy(2,1);print(green_color+"*"*90+reset_color)
        gotoxy(60,2);print(purple_color+"Registro de Venta")
        gotoxy(47,3);print(blue_color+Company.get_business_name())
        gotoxy(5,4);print(f"Factura#:F0999999 {' '*3} Fecha:{datetime.datetime.now()}")
        gotoxy(66,4);print("Subtotal:")
        gotoxy(66,5);print("Decuento:")
        gotoxy(66,6);print("Iva     :")
        gotoxy(66,7);print("Total   :")
        gotoxy(15,6);print("Cedula:")
        dni=validar.solo_numeros("Error: Solo numeros",23,6)
        json_file = JsonFile(path+'/archivos/clients.json')
        client = json_file.find("dni",dni)
        if not client:
            gotoxy(35,6);print(red_color+"Cliente no existe")
            return
        client = client[0]
        cli = RegularClient(client["nombre"],client["apellido"], client["dni"], card=True) 
        sale = Sale(cli)
        gotoxy(35,6);print(cli.fullName())
        gotoxy(2,8);print(green_color+"*"*90+reset_color) 
        gotoxy(5,9);print(purple_color+"Linea") 
        gotoxy(12,9);print("Id_Articulo") 
        gotoxy(24,9);print("Descripcion") 
        gotoxy(38,9);print("Precio") 
        gotoxy(48,9);print("Cantidad") 
        gotoxy(58,9);print("Subtotal") 
        gotoxy(70,9);print("n->Terminar Venta)"+reset_color)
        # detalle de la venta
        follow ="s"
        line=1
        while follow.lower()=="s":
            gotoxy(7,9+line);print(line)
            gotoxy(15,9+line);
            id=int(validar.solo_numeros("Error: Solo numeros",15,9+line))
            json_file = JsonFile(path+'/archivos/products.json')
            prods = json_file.find("id",id)
            if not prods:
                gotoxy(24,9+line);print(red_color+"Producto no existe")
                time.sleep(1)
                gotoxy(24,9+line);print(" "*20)
            else:    
                prods = prods[0]
                product = Product(prods["id"],prods["descripcion"],prods["precio"],prods["stock"])
                gotoxy(24,9+line);print(product.descrip)
                gotoxy(38,9+line);print(product.preci)
                gotoxy(49,9+line);qyt=int(validar.solo_numeros("Error:Solo numeros",49,9+line))
                gotoxy(59,9+line);print(product.preci*qyt)
                sale.add_detail(product,qyt)
                gotoxy(76,4);print(round(sale.subtotal,2))
                gotoxy(76,5);print(round(sale.discount,2))
                gotoxy(76,6);print(round(sale.iva,2))
                gotoxy(76,7);print(round(sale.total,2))
                gotoxy(74,9+line);follow=input() or "s"  
                gotoxy(76,9+line);print(green_color+"✔"+reset_color)  
                line += 1
        gotoxy(15,9+line);print(red_color+"Esta seguro de grabar la venta(s/n):")
        gotoxy(54,9+line);procesar = input().lower()
        if procesar == "s":
            gotoxy(15,10+line);print("😊 Venta Grabada satisfactoriamente 😊"+reset_color)
            # print(sale.getJson())  
            json_file = JsonFile(path+'/archivos/invoices.json')
            invoices = json_file.read()
            ult_invoices = invoices[-1]["factura"]+1
            data = sale.getJson()
            data["factura"]=ult_invoices
            invoices.append(data)
            json_file = JsonFile(path+'/archivos/invoices.json')
            json_file.save(invoices)
        else:
            gotoxy(20,10+line);print(red_color+"🤣 Venta Cancelada 🤣"+reset_color)    
        time.sleep(4)    
    
    def update(self):
        borrarPantalla()
        dibujar_cuadro()
        # gotoxy(2,1);print(green_color+"*"*90+reset_color)
        gotoxy(60,2);print(purple_color+"Actualizacion de Venta")
        gotoxy(47,3);print(blue_color+Company.get_business_name())
        gotoxy(5,7);invoice_number = Valida.validar_numeros("Ingrese el número de factura que desea actualizar: ",5,7)
        json_file = JsonFile(path + '/archivos/invoices.json')
        invoices = json_file.read()

        if invoices:
            # Buscar la factura específica
            for invoice in invoices:
                if invoice["factura"] == int(invoice_number):
                    cliente = invoice["cliente"]
                    gotoxy(2,5);print(f"Número de Factura: {invoice['factura']}")
                    gotoxy(2,6);print(f"Fecha: {invoice['Fecha']}")
                    gotoxy(2,7);print(f"Cliente: {cliente}")
                    gotoxy(2,8);print(f"Total: {invoice['total']}")
                    gotoxy(2,10);print("\nDetalle de la Venta:")
                    gotoxy(2,14);detalles = invoice['detalle']
                    for i, detalle in enumerate(detalles, start=1):
                        print(f"{detalle['poducto']}: {detalle['cantidad']} x {detalle['precio']}")
                    print(green_color + "=" * 90 + reset_color)

                    # Opciones para modificar la factura
                    while True:
                        print(purple_color+"\nOpciones:")
                        print(red_color+"1. Modificar cantidad de un producto")
                        print(purple_color+"2. Eliminar un producto")
                        print(red_color+"3. Agregar un nuevo producto")
                        print(purple_color+"4. Terminar actualización")
                        gotoxy(50,25);option = input(cyan_color+"Seleccione una opción 📝: ")

                        if option == "1":
                            # Modificar cantidad de un producto en la factura
                            gotoxy(5,12);detalle_index = int(Valida.validar_numeros(green_color+"Ingrese el número de línea del detalle que desea modificar o actualizar: ",5,12)) - 1
                            if 0 <= detalle_index < len(detalles):
                                gotoxy(5,14);new_quantity = Valida.validar_numeros(green_color+"Ingrese la nueva cantidad: ",5,6)
                                detalles[detalle_index]['cantidad'] = new_quantity
                                gotoxy(50,25);print("Cantidad modificada correctamente.😊")
                            else:
                                print("Número de línea inválido.")
                        elif option == "2":
                            # Eliminar un producto de la factura
                            gotoxy(5,14);detalle_index = int(Valida.validar_numeros(green_color+"Ingrese el número de línea del detalle que desea eliminar: ",5,12)) - 1
                            if 0 <= detalle_index < len(detalles):
                                del detalles[detalle_index]
                                gotoxy(50,25);print(red_color+"Producto eliminado correctamente 😎.")
                            else:
                                print("Número de línea inválido.")
                        elif option == "3":
                            # Agregar un nuevo producto a la factura
                            gotoxy(5,12);product_id = Valida.validar_numeros(green_color+"Ingrese el ID del nuevo producto: ",5,12)
                            gotoxy(5,14);product_quantity = Valida.validar_numeros(green_color+"Ingrese la cantidad del nuevo producto: ",5,14)
                            json_file_products = JsonFile(path + '/archivos/products.json')
                            products = json_file_products.find("id", product_id)
                            if products:
                                product = products[0]
                                new_product = {
                                    'poducto': product['descripcion'],
                                    'precio': product['precio'],
                                    'cantidad': product_quantity
                                }
                                detalles.append(new_product)
                                gotoxy(50,25);print(red_color+"Producto agregado correctamente 😎.")
                            else:
                                gotoxy(50,25);print(red_color+"Producto no encontrado 😥.")
                        elif option == "4":
                            print(red_color+"Actualización de factura terminada.😉")
                            # Guardar los cambios en el archivo JSON
                            invoice['detalle'] = detalles
                            json_file.save(invoices)
                            break
                        else:
                            gotoxy(50,25);print("Opción inválida. Intente nuevamente.")
                    break
            else:
                gotoxy(50,25);print(red_color+"Factura no encontrada.😥")
        else:
            gotoxy(50,25);print(red_color+"No hay facturas disponibles.")
        input("Presione una tecla para continuar...")
    
    def delete(self):
        borrarPantalla()
        dibujar_cuadro()
        # gotoxy(2,1);print(green_color+"*"*90+reset_color)
        gotoxy(60,2);print(purple_color+"Eliminacion de Venta")
        gotoxy(47,3);print(blue_color+Company.get_business_name())
        gotoxy(5,6);invoice_number =Valida.validar_numeros("Ingrese el número de factura que desea eliminar: ",5,6)
        json_file = JsonFile(path + '/archivos/invoices.json')
        invoices = json_file.read()

        # Buscar la factura específica
        found = False
        updated_invoices = []
        for invoice in invoices:
            if invoice["factura"] == int(invoice_number):
                found = True
                # Mostrar la factura antes de eliminarla
                print(f"Factura encontrada:")
                print(f"Número de Factura: {invoice['factura']}")
                print(f"Fecha: {invoice['Fecha']}")
                print(f"Cliente: {invoice['cliente']}")
                print(f"Total: {invoice['total']}")
                print("\nDetalle de la Venta:")
                for detalle in invoice['detalle']:
                    print(f"{detalle['poducto']}: {detalle['cantidad']} x {detalle['precio']}")
                print(green_color + "=" * 90 + reset_color)

                # Confirmar la eliminación
                confirmacion = input("¿Está seguro que desea eliminar esta factura? (s/n): ").lower()
                if confirmacion == "s":
                    print(red_color+"Factura eliminada exitosamente.😎")
                else:
                    print(red_color+"Eliminación cancelada.😥")
            else:
                updated_invoices.append(invoice)

        if not found:
            print(red_color+"Factura no encontrada. 😥")

        # Guardar los cambios en el archivo JSON
        json_file.save(updated_invoices)
        time.sleep(4)
    
    def consult(self):
        borrarPantalla()
        # print('\033c', end='')
        # gotoxy(2,1);print(green_color+"█"*90)
        dibujar_cuadro()
        gotoxy(2,2);print(purple_color+"Consulta de Venta")
        gotoxy(17,3);print(blue_color+Company.get_business_name())
        gotoxy(2,4);invoice_number = Valida.validar_numeros("Ingrese el número de factura: ", 2,4)
        invoice_number = int(invoice_number)

        json_file = JsonFile(path + '/archivos/invoices.json')
        invoices = json_file.read()

        found = False
        for invoice in invoices:
            if invoice["factura"] == invoice_number:
                found = True

                gotoxy(5,8);print("Factura encontrada:")
                gotoxy(5,9);print(blue_color + "Número de Factura: " + purple_color + f"{invoice['factura']}")
                gotoxy(5,10);print(blue_color + "Fecha: " + purple_color + f"{invoice['Fecha']}")
                gotoxy(5,11);print(blue_color + "Cliente: " + purple_color + f"{invoice['cliente']}")
                gotoxy(5,12);print(blue_color + "Total: " + purple_color + f"{invoice['total']}")
                gotoxy(5,14);print(blue_color + "Detalle de la Venta:")
                gotoxy(5,16);print(f"{'Producto'.center(20)}  {'Cantidad'.center(20)} {'Precio'.center(20)}")
                for detalle in invoice['detalle']:
                    gotoxy(5,17);print(purple_color + f"{detalle['poducto'].center(20)} {str(detalle['cantidad']).center(20)}  {str(detalle['precio']).center(20)}")
                # print(green_color + "=" * 90 + reset_color)
                break

        if not found:
            gotoxy(50,25);print("Factura no encontrada.")
        gotoxy(50,25);input("Presione una tecla para continuar...")
   

#Menu Proceso Principal
opc=''
while opc !='4':  
    borrarPantalla()      
    menu_main = Menu(blue_color+"Menu Facturacion",[green_color+"1) Clientes","2) Productos","3) Ventas","4) Salir"],20,10)
    opc = menu_main.menu()
    if opc == "1":
        opc1 = ''
        while opc1 !='5':
            borrarPantalla()    
            menu_clients = Menu(blue_color+"Menu Cientes",[green_color+"1) Ingresar","2) Actualizar","3) Eliminar","4) Consultar","5) Salir"],20,10)
            opc1 = menu_clients.menu()
            if opc1 == "1":
                crud_clients = CrudClients()
                crud_clients.create()
            elif opc1 == "2":
                crud_clients = CrudClients()
                crud_clients.update()
            elif opc1 == "3":
                crud_clients = CrudClients()
                crud_clients.delete()
            elif opc1 == "4":
                crud_clients = CrudClients()
                crud_clients.consult()
            print("Regresando al menu Clientes...")
            # time.sleep(2)            
    elif opc == "2":
        opc2 = ''
        while opc2 !='5':
            borrarPantalla()    
            menu_products = Menu(blue_color+"Menu Productos",[green_color+"1) Ingresar","2) Actualizar","3) Eliminar","4) Consultar","5) Salir"],20,10)
            opc2 = menu_products.menu()
            if opc2 == "1":
                crudProducts = CrudProducts()
                crudProducts.create()
            elif opc2 == "2":
                crudProducts = CrudProducts()
                crudProducts.update()
            elif opc2 == "3":
                crudProducts = CrudProducts()
                crudProducts.delete()
            elif opc2 == "4":
                crudProducts = CrudProducts()
                crudProducts.consult()
    elif opc == "3":
        opc3 =''
        while opc3 !='5':
            borrarPantalla()
            sales = CrudSales()
            menu_sales = Menu(blue_color+"Menu Ventas",[green_color+"1) Registro Venta","2) Consultar","3) Modificar","4) Eliminar","5) Salir"],20,10)
            opc3 = menu_sales.menu()
            if opc3 == "1":
                sales.create()   
            elif opc3 == "2":
                sales.consult()
            elif opc3 == "3":
                sales.update()
            elif opc3 == "4":
                sales.delete()
                time.sleep(2)
     
    print("Regresando al menu Principal...")
    # time.sleep(2)            

borrarPantalla()
input("Presione una tecla para salir...")
borrarPantalla()