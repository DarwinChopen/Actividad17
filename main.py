class Productos:
    def __init__(self,id_producto,nombre,id_categoria,precio,total_compras,total_ventas,stock):
        self.id_producto=id_producto
        self.nombre=nombre
        self.id_categoria=id_categoria
        self.precio=precio
        self.total_compras=total_compras
        self.total_ventas=total_ventas
        self.stock=stock
    def mostrar_producto(self):
        print(f"Codigo: {self.id_producto}  |  Nombre: {self.nombre}  |  Categoria: {self.id_categoria}  |  Precio: {self.precio}  |  Tootal Compras: {self.total_compras}|  Total Ventas: {self.total_ventas}")


class Categoria:
    def __init__(self,id_categoria,nombre):
        self.id_categoria=id_categoria
        self.nombre=nombre
    def mostrar_categoria(self):
        print(f"Codigo: {self.id_categoria}  |  Nombre: {self.nombre} ")

class Clientes:
    def __init__(self, nit,nombre,telefono,direccion,correo):
        self.nit=nit
        self.nombre=nombre
        self.telefono=telefono
        self.direccion=direccion
        self.correo=correo
    def mostrar_clientes(self):
        print(f"Nit: {self.nit}  |  Nombre: {self.nombre}  |  Telefono: {self.telefono}  |  Direccion: {self.direccion}  |  Correo: {self.correo}")

class Empleados:
    def __init__(self,id_empleado,nombre,telefono,direccion,correo):
        self.id_empleado=id_empleado
        self.nombre=nombre
        self.telefono=telefono
        self.direccion=direccion
        self.correo=correo
    def mostrar_empleados(self):
        print(f"Codigo Empleado: {self.id_empleado}  |  Nombre: {self.nombre}  |  Telefono: {self.telefono}  |  Direccion")

class Proveedores:
    def __init__(self,id_proveedores,nombre,empresa,telefono,direccion,correo,id_categoria):
        self.id_proveedores=id_proveedores
        self.nombre=nombre
        self.empresa=empresa
        self.telefono=telefono
        self.direccion=direccion
        self.correo=correo
        self.id_categoria=id_categoria
    def mostrar_proveedores(self):
        print(f"Codigo Proveedor: {self.id_proveedores}  |  Nombre: {self.nombre}  |  Empresa: {self.empresa}  |  Telefono: {self.telefono}  |  Direccion: {self.direccion}  |  Correo: {self.correo}  |  Categoria: {self.id_categoria} ")


class Ventas:
    def __init__(self,id_venta,fecha,nit,id_empleado,total):
        self.id_venta=id_venta
        self.fecha=fecha
        self.nit=nit
        self.id_empleado=id_empleado
        self.total=total
    def mostrar_ventas(self):
        print(f"Codigo de venta: {self.id_venta}  |  Fecha: {self.fecha}  |  Nit: {self.nit}  |  Codigo Empleado: {self.id_empleado}  |  Total: {self.total}")


class DetalleVenta:
    def __init__(self,id_detallaVenta,id_venta,cantidaad,id_producto,precio,subtotal):
        self.id_detalleVenta=id_detallaVenta
        self.id_venta=id_venta
        self.cantidad=cantidaad
        self.id_producto=id_producto
        self.precio=precio
        self.subtotal=subtotal
    def mostrar_detallaVentas(self):
        print(f"Codigo Detalle de Venta: {self.id_detalleVenta}  |  Codigo Venta: {self.id_venta}  |  Cantidad: {self.cantidad}  |  Codigo Producto: {self.id_producto}  |  Precio: {self.precio}  |  Subtotal: {self.subtotal}")

class Compras:
    def __init__(self,id_comparas,fecha,id_proveedor,id_empleado,total):
        self.id_compras=id_comparas
        self.fecha=fecha
        self.id_proveedor=id_proveedor
        self.id_empleado=id_empleado
        self.total=total
    def mostrar_compras(self):
        print(f"Codigo Compras: {self.id_compras}  | Fecha: {self.fecha}  |  Codigo Proveedor: {self.id_proveedor}  |  Codigo Empleado: {self.id_empleado}  |  Total: {self.total}")

class DetalleCompras:
    def __init__(self,id_detalleCompra,id_compras,cantidad,id_producto,precioCompra,subtotal,fechaCaducidad):
        self.id_detalleCompra=id_detalleCompra
        self.id_compras=id_compras
        self.cantidad=cantidad
        self.id_producto=id_producto
        self.pecioCompra=precioCompra
        self.subtotal=subtotal
        self.fechaCaducidad=fechaCaducidad
    def mostrar_detalleCompras(self):
        print(f"Codigo Detalle Compra: {self.id_detalleCompra}  |  Codigo Compras: {self.id_compras}  |  Cantidad: {self.cantidad}  |  Codigo Producto: {self.id_producto}  |  Precio Compra: {self.pecioCompra}  |  Subtotal: {self.subtotal}  |  Fecha Caducidad: {self.fechaCaducidad} ")
class GestionTienda:
    def __init__(self):
        self.productos={}
        self.categorias={}
        self.clientes={}
        self.empleadoss={}
        self.proveedores={}
        self.ventas={}
        self.detalleVentas={}
        self.compras={}
        self.detallecompras={}


    def ingreso_producto(self):
        while True:
            try:
                cantidad_productos = int(input('¿Cuantos productos desea ingresar al inventario?:     '))
                for i in range(cantidad_productos):
                    print(f'\t\t\t\tIngreso datos de {i + 1} producto: ')
                    while True:
                        codigo = input("Ingrese el codigo del Producto:           ")
                        if codigo in self.productos:
                            print("Este Codigo Ya existe, Intentelo de nuevo...")
                        elif codigo == "":
                            print("El codigo no puede estar vacio, Intentelo de nuevo... ")
                        else:
                            break
                    while True:
                        nombre = input("Ingrese el Nombre del Producto:           ")
                        if nombre in self.productos:
                            print("Este Nombre en especifico ya existe, ingrese otro:")
                        elif nombre == "":
                            print("Este Campo no puede quedar vacio, Ingrese el nombre")
                        else:
                            break
                    while True:
                        id_categoria = input("Ingrese el código de la categoría: ")
                        if id_categoria not in self.categorias:
                            print("La categoría no existe, primero regístrela.")
                        elif id_categoria == "":
                            print("El campo no puede estar vacío.")
                        else:
                            break
                    while True:
                        try:
                            precio = float(input("Ingrese el Precio en Quetzales del Producto:     Q."))
                            if precio == "":
                                print("Este campo no Puede quedar vacio, Ingrese el precio")

                            elif precio < 0:
                                print("El precio debe ser mayor a Q0 este no puede ser negativo ni igual a 0")
                            else:
                                break
                        except ValueError:
                            print("Solo se permiten cantidades")
                    while True:
                        try:
                            total_compras = float(input("Ingrese el total compras:     Q."))
                            if total_compras == "":
                                print("Este campo no Puede quedar vacio, Ingrese dato")

                            elif total_compras < 0:
                                print("debe ser mayor a Q0 este no puede ser negativo ni igual a 0")
                            else:
                                break
                        except ValueError:
                            print("Solo se permiten cantidades")
                    while True:
                        try:
                            total_ventas = float(input("Ingrese total ventas:     Q."))
                            if total_ventas == "":
                                print("Este campo no Puede quedar vacio, Ingrese el dato")

                            elif total_ventas < 0:
                                print("debe ser mayor a Q0 este no puede ser negativo ni igual a 0")
                            else:
                                break
                        except ValueError:
                            print("Solo se permiten cantidades")
                    while True:
                        try:
                            stock = int(input("Ingrese la cantidad en Stock:               "))
                            if stock < 0:
                                print("Error, la cantidad en stock, no puede ser negativa")
                            else:
                                break
                        except ValueError:
                            print("Solo se permiten enteros")
                    self.productos[codigo]=Productos(codigo, nombre, id_categoria, precio,total_compras,total_ventas, stock)

                    print(f'El producto con codigo {codigo} se Agrego Correctamente')
                    print('\n')
                break  # Termina el break principal porque este bloque se ejecuto bien
            except Exception as e:
                print(f'Por favor ingrese datos validos, ocurrio {e}')

    def ingreso_categotia(self):
        while True:
            try:
                cantidad_categorias = int(input('¿Cuantas categorias desea ingresar?:     '))
                for i in range(cantidad_categorias):
                    print(f'\t\t\t\tIngreso datos de {i + 1} Categorias: ')
                    while True:
                        id_categoria = input("Ingrese el codigo de la categoria:           ")
                        if id_categoria in self.categorias:
                            print("Este Codigo de la categoria Ya existe, Intentelo de nuevo...")
                        elif id_categoria == "":
                            print("El codigo no puede estar vacio, Intentelo de nuevo... ")
                        else:
                            break
                    while True:
                        nombre = input("Ingrese el Nombre de la categoria:           ")
                        if nombre in self.categorias:  # Validacion por nombre check
                            print("Este Nombre en especifico ya existe, ingrese otro:")
                        elif nombre == "":
                            print("Este Campo no puede quedar vacio, Ingrese el nombre")
                        else:
                            break
                    self.categorias[id_categoria]=Categoria(id_categoria, nombre)

                    print(f'La categoria con codigo {id_categoria} se Agrego Correctamente')
                    print('\n')
                break
            except Exception as e:
                print(f'Por favor ingrese datos validos, ocurrio {e}')

    def ingreso_clientes(self):
        cantidad_clientes = int(input('¿Cuantos clientes desea ingresar al inventario?:     '))
        for i in range(cantidad_clientes):
            print(f'\t\t\t\tIngreso datos de {i + 1} clientes: ')
            while True:
                nit = input("Ingrese el nit del cliente:           ")
                if nit in self.clientes:
                    print("Este nit Ya existe, Intentelo de nuevo...")
                elif nit == "":
                    print("El codigo no puede estar vacio, Intentelo de nuevo... ")
                else:
                    break
            while True:
                nombre_cliente = input("Ingrese el Nombre del cliente:           ")
                if nombre_cliente in self.clientes:
                    print("Este Nombre en especifico ya existe, ingrese otro:")
                elif nombre_cliente == "":
                    print("Este Campo no puede quedar vacio, Ingrese el nombre del cliente")
                else:
                    break
            while True:
                try:
                    telefono_cliente = int(input("Ingrese el numero del cliente:   "))
                    if telefono_cliente in self.clientes:
                        print("Este Telefono ya esta en uso, Intente con otro")
                    elif telefono_cliente=="":
                        print("Este campo no Puede quedar vacio, Ingrese el Dato")

                    elif telefono_cliente<0:
                        print("El telefono no tiene sentido jaja")
                    else:
                        break
                except ValueError:
                    print("Solo se permiten numeros")
            while True:
                direccion_cliente=input("Ingrese la direccion del cliente:         ")
                if direccion_cliente in self.clientes:
                    print("Esta direccion ya esta en uso")
                elif direccion_cliente=="":
                    print("Este campo no puede quedar vacio,ingrese el dato")
                else:
                    break
            while True:
                correo_cliente=input("Ingrese el correo del cliente:         ")
                if correo_cliente in self.clientes:
                    print("Este correo ya esta en uso")
                elif correo_cliente=="":
                    print("Este campo no puede quedar vacio,ingrese el dato")
                else:
                    break
            self.clientes[nit]=Clientes(nit,nombre_cliente,telefono_cliente,direccion_cliente,correo_cliente)
            print("El cliente se agrego Correctamente...")

    def ingreso_empleados(self):
        cantidad_empleados = int(input('¿Cuantos empleados desea ingresar?:     '))
        for i in range(cantidad_empleados):
            print(f'\t\t\t\tIngreso datos de {i + 1} empleado: ')
            while True:
                id_empleado = input("Ingrese el codigo de Empledo:           ")
                if id_empleado in self.empleadoss:
                    print("Este id Ya existe, Intentelo de nuevo...")
                elif id_empleado == "":
                    print("El codigo no puede estar vacio, Intentelo de nuevo... ")
                else:
                    break
            while True:
                nombre_empleado = input("Ingrese el Nombre del empleado:           ")
                if nombre_empleado in self.empleadoss:
                    print("Este Nombre en especifico ya existe, ingrese otro:")
                elif nombre_empleado == "":
                    print("Este Campo no puede quedar vacio, Ingrese el nombre del empleado")
                else:
                    break
            while True:
                try:
                    telefono_empleado = int(input("Ingrese el telefono del empleado:   "))
                    if telefono_empleado in self.empleadoss:
                        print("Este Telefono ya esta en uso, Intente con otro")
                    elif telefono_empleado=="":
                        print("Este campo no Puede quedar vacio, Ingrese el Dato")

                    elif telefono_empleado<0:
                        print("El telefono no tiene sentido jaja")
                    else:
                        break
                except ValueError:
                    print("Solo se permiten numeros")
            while True:
                direccion_empleado=input("Ingrese la direccion del empleado:         ")
                if direccion_empleado in self.empleadoss:
                    print("Esta direccion ya esta en uso")
                elif direccion_empleado=="":
                    print("Este campo no puede quedar vacio,ingrese el dato")
                else:
                    break
            while True:
                correo_empleado=input("Ingrese el correo del empleado:         ")
                if correo_empleado in self.empleadoss:
                    print("Este correo ya esta en uso")
                elif correo_empleado=="":
                    print("Este campo no puede quedar vacio,ingrese el dato")
                else:
                    break
            self.empleadoss[id_empleado]=Empleados(id_empleado,nombre_empleado,telefono_empleado,direccion_empleado,correo_empleado)
            print("El Empleado se agrego Correctamente...")

    def listar_categorias(self):
        if not self.categorias:
            print("No hay categorías.")
        for c in self.categorias.values():
            print(f"[{c.id_categoria}] {c.nombre}")

    def listar_productos(self):
        if not self.productos:
            print("No hay productos.")
        for p in self.productos.values():
            cat = self.categorias[p.id_categoria]
            print(f"[{p.id_producto}] {p.nombre} | Precio: {p.precio} | Categoría: {cat.nombre} | Stock: {p.stock}")

    def listar_clientes(self):
        if not self.clientes:
            print("No hay Clientes")
        for cl in self.clientes.values():
            print(f"[{cl.nit}] {cl.nombre}  | Telefono : {cl.telefono} | Direccion: {cl.direccion} | correo: {cl.correo}")

    def listar_empleados(self):
        if not self.empleadoss:
            print("No hay emleados")
        for em in self.empleadoss.values():
            print(f"[{em.id_empleado}] {em.nombre}  | Telefono : {em.telefono} | Direccion: {em.direccion} | correo: {em.correo}")


registro = GestionTienda()
while True:
    print("Menu")
    print("1. Ingresar Producto")
    print("2. Ingresar Categoria")
    print("3. Ingresar Clientes")
    print("4. Ingresar Empleados")
    print("5. Ingresar Proveedores")
    print("6. Listar Productos")
    print("7. Listar Categorias")
    print("8, Listar Clientes")
    print("9. Listar Empleados")
    print("10. Salir")
    try:
        opcion=int(input("Ingrese una opcion"))
    except ValueError:
        print("Ingrese un entero")
    match opcion:
        case 1:
            print("Inpreso Productos")
            registro.ingreso_producto()
        case 2:
            registro.ingreso_categotia()
        case 3:
            registro.ingreso_clientes()
        case 4:
            registro.ingreso_empleados()
        case 5:
            pass
        case 6:
            registro.listar_productos()
        case 7:
            registro.listar_categorias()
        case 8:
            registro.listar_clientes()
        case 9:
            registro.listar_empleados()
        case 10:
            print("Saliendo")
            break
        case _:
            print("Error, Intentelo sse nuevo")







