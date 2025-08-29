import datetime
class Productos:
    def __init__(self,id_producto,nombre,id_categoria,precio,stock=0):
        self.id_producto=id_producto
        self.nombre=nombre
        self.id_categoria=id_categoria
        self.precio=float(precio)
        #self.total_compras=total_compras
        #self.total_ventas=total_ventas
        self.stock=int(stock)
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
    def __init__(self,id_detallaVenta,id_venta,cantidaad,id_producto,precio):
        self.id_detalleVenta=id_detallaVenta
        self.id_venta=id_venta
        self.cantidad=cantidaad
        self.id_producto=id_producto
        self.precio=precio
        self.subtotal=cantidaad*precio
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
    def __init__(self,id_detalleCompra,id_compras,cantidad,id_producto,precioCompra,fechaCaducidad):
        self.id_detalleCompra=id_detalleCompra
        self.id_compras=id_compras
        self.cantidad=cantidad
        self.id_producto=id_producto
        self.pecioCompra=precioCompra
        self.subtotal=cantidad*precioCompra
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

        self.cargar_categorias()
        self.cargar_clientes()
        self.cargar_empleados()
        self.cargar_productos()
        self.cargar_proveedores()


    def cargar_categorias(self):
        try:
            with open("categorias.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        id_categoria, nombre = linea.split(":")
                        self.categorias[id_categoria] = Categoria(id_categoria, nombre)
            print("Categorias importados desde categorias.txt")
        except FileNotFoundError:
            print("No existe el archivo categorias.txt, se creará uno nuevo al guardar.")

    def guardar_categorias(self):
        with open("categorias.txt", "w", encoding="utf-8") as archivo:
            for c in self.categorias.values():
                archivo.write(f"{c.id_categoria}:{c.nombre}\n")

    def cargar_clientes(self):
        try:
            with open("clientes.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        nit, nombre, telefono, direccion, correo = linea.split(":")
                        self.clientes[nit] = Clientes(nit, nombre, telefono, direccion, correo)
            print("Clientes importados desde clientes.txt")
        except FileNotFoundError:
            print("No existe el archivo clientes.txt, se creará uno nuevo al guardar.")

    def guardar_clientes(self):
        with open("clientes.txt", "w", encoding="utf-8") as archivo:
            for cliente in self.clientes.values():
                archivo.write(f"{cliente.nit}:{cliente.nombre}:{cliente.telefono}:{cliente.direccion}:{cliente.correo}\n")

    def cargar_empleados(self):
        try:
            with open("empleados.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        id_empleado, nombre, telefono, direccion, correo = linea.split(":")
                        self.empleadoss[id_empleado] = Empleados(id_empleado, nombre, telefono, direccion, correo)
            print("Empleados importados desde empleados.txt")
        except FileNotFoundError:
            print("No existe el archivo empleados.txt, se creará uno nuevo al guardar.")

    def guardar_empleados(self):
        with open("empleados.txt", "w", encoding="utf-8") as archivo:
            for empleado in self.empleadoss.values():
                archivo.write(f"{empleado.id_empleado}:{empleado.nombre}:{empleado.telefono}:{empleado.direccion}:{empleado.correo}\n")

    def cargar_productos(self):
        try:
            with open("productos.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        id_producto, nombre, id_categoria, precio, stock = linea.split(":")
                        self.productos[id_producto] = Productos(id_producto, nombre, id_categoria, precio, stock)
            print("Empleados importados desde productos.txt")
        except FileNotFoundError:
            print("No existe el archivo productos.txt, se creará uno nuevo al guardar.")

    def guardar_productos(self):
        with open("productos.txt", "w", encoding="utf-8") as archivo:
            for producto in self.productos.values():
                archivo.write(f"{producto.id_producto}:{producto.nombre}:{producto.id_categoria}:{producto.precio}:{producto.stock}\n")

    def cargar_proveedores(self):
        try:
            with open("proveedores.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        id_proveedores, nombre, empresa, telefono, direccion, correo, id_categoria = linea.split(":")
                        self.proveedores[id_proveedores] = Proveedores(id_proveedores, nombre,empresa,telefono,direccion,correo, id_categoria)
            print("Proveedores importados desde proveedores.txt")
        except FileNotFoundError:
            print("No existe el archivo proveedores.txt, se creará uno nuevo al guardar.")

    def guardar_proveedores(self):
        with open("proveedores.txt", "w", encoding="utf-8") as archivo:
            for proveedor in self.proveedores.values():
                archivo.write(f"{proveedor.id_proveedores}:{proveedor.nombre}:{proveedor.empresa}:{proveedor.telefono}:{proveedor.direccion}:{proveedor.correo}:{proveedor.id_categoria}\n")


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
                    """
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
                        """
                    while True:
                        try:
                            stock = int(input("Ingrese la cantidad en Stock:               "))
                            if stock < 0:
                                print("Error, la cantidad en stock, no puede ser negativa")
                            else:
                                break
                        except ValueError:
                            print("Solo se permiten enteros")
                    self.productos[codigo]=Productos(codigo, nombre, id_categoria,precio, stock)
                    self.guardar_productos()
                    print(f'El producto con codigo {codigo} se Agrego y Guardo Correctamente')
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
                    self.guardar_categorias()
                    print(f'La categoria con codigo {id_categoria} se agrego y guaro')
                    print('\n')
                break
            except Exception as e:
                print(f'Por favor ingrese datos validos, ocurrio {e}')

    def ingreso_clientes(self):
        cantidad_clientes = int(input('¿Cuantos clientes desea ingresar al inventario?:     '))
        for i in range(cantidad_clientes):
            print(f'\t\t\t\tIngreso datos de {i + 1} clientes: ')
            while True:
                nit = input("Ingrese el nit del cliente:                        ")
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
                    telefono_cliente = int(input("Ingrese el numero del cliente:  "))
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
                direccion_cliente=input("Ingrese la direccion del cliente:          ")
                if direccion_cliente in self.clientes:
                    print("Esta direccion ya esta en uso")
                elif direccion_cliente=="":
                    print("Este campo no puede quedar vacio,ingrese el dato")
                else:
                    break
            while True:
                correo_cliente=input("Ingrese el correo del cliente:                 ")
                if correo_cliente in self.clientes:
                    print("Este correo ya esta en uso")
                elif correo_cliente=="":
                    print("Este campo no puede quedar vacio,ingrese el dato")
                else:
                    break
            self.clientes[nit]=Clientes(nit,nombre_cliente,telefono_cliente,direccion_cliente,correo_cliente)
            self.guardar_clientes()
            print("El cliente se agrego y guardo Correctamente...")

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
            self.guardar_empleados()
            print("El Empleado se agrego y guardo Correctamente...")
    def ingreso_proverdores(self):#falta validaciones
        cantidad_proveedores = int(input('¿Cuantos proveedores desea ingresar?:     '))
        for i in range(cantidad_proveedores):
            print(f'\t\t\t\tIngreso datos de {i + 1} preveedor: ')
            while True:
                id_proveedor = input("Ingrese el codigo de proveedor:           ")
                if id_proveedor in self.proveedores:
                    print("Este id Ya existe, Intentelo de nuevo...")
                elif id_proveedor == "":
                    print("El codigo no puede estar vacio, Intentelo de nuevo... ")
                else:
                    break
            while True:
                nombre_proveedor = input("Ingrese el Nombre del proveedor:           ")
                if nombre_proveedor in self.proveedores:
                    print("Este Nombre en especifico ya existe, ingrese otro:")
                elif nombre_proveedor == "":
                    print("Este Campo no puede quedar vacio, Ingrese el nombre del proveedor")
                else:
                    break
            while True:
                empresa_proveedor = input("Ingrese la empresa del proveedor:           ")
                if empresa_proveedor in self.proveedores:
                    print("Esta empresa ya existe, verifique:")
                elif empresa_proveedor == "":
                    print("Este Campo no puede quedar vacio, ingrese el nombre de la empresa")
                else:
                    break
            while True:
                try:
                    telefono_provedor = int(input("Ingrese el telefono del proveedor:   "))
                    if telefono_provedor in self.proveedores:
                        print("Este Telefono ya esta en uso, Intente con otro")
                    elif telefono_provedor=="":
                        print("Este campo no Puede quedar vacio, Ingrese el Dato")

                    elif telefono_provedor<0:
                        print("El telefono no tiene sentido")
                    else:
                        break
                except ValueError:
                    print("Solo se permiten numeros")
            while True:
                direccion_provedor=input("Ingrese la direccion del proveedor:         ")
                if direccion_provedor in self.proveedores:
                    print("Esta direccion ya esta en uso")
                elif direccion_provedor=="":
                    print("Este campo no puede quedar vacio,ingrese el dato")
                else:
                    break
            while True:
                correo_provedor=input("Ingrese el correo del proveedor:         ")
                if correo_provedor in self.proveedores:
                    print("Este correo ya esta en uso")
                elif correo_provedor=="":
                    print("Este campo no puede quedar vacio,ingrese el dato")
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
            self.proveedores[id_proveedor]=Proveedores(id_proveedor,nombre_proveedor,empresa_proveedor,telefono_provedor,direccion_provedor,correo_provedor,id_categoria)
            self.guardar_proveedores()
            print("El Proveedor se agrego y guardo Correctamente...")

    def regitrar_venta(self):
        while True:
            id_venta=input("Ingrese el codigo de la venta: ")
            if id_venta in self.ventas:
                print("Este codigo ya existe,registre otro: ")
            elif id_venta=="":
                print("Este campo no puede quedar vacio, ingrese dato")
            else:
                break

        fecha_venta= datetime.datetime.now()

        while True:
            id_cliente=input("Ingrese el codigo del cliente: ")
            if id_cliente=="":
                print("Este campo no puede quedar vacio, ingrese dato")
            else:
                break
        while True:
            id_empleado=input("Ingrese el codigo del empleado: ")
            if id_empleado=="":
                print("Este campo no puede quedar vacio, ingrese dato")
            else:
                break
        total=0#aun no se calcula
        self.ventas[id_venta]=Ventas(id_venta,fecha_venta,id_cliente,id_empleado,total)
        print("Venta Registrada")

        while True:
            id_detalleventa = input("ID Detalle Venta: ")
            id_producto = input("Ingrese el Codigo del Producto: ")
            if id_producto not in self.productos:
                print("Producto no existe.")
                continue
            cantidad = int(input("Cantidad: "))

            precio=float(self.productos[id_producto].precio)
            detalle=DetalleVenta(id_detalleventa,id_venta,cantidad,id_producto,precio)
            self.detalleVentas[id_detalleventa]=detalle
            total+=detalle.subtotal
            self.productos[id_producto].stock-=cantidad
            opcioningreso=input("Desea ingresar otro producto (s/n): ")
            if opcioningreso.lower()!="s":
                break
        self.ventas[id_venta].total=total
        print("Venta realizada")

    def registrar_compras(self):#aun no funciona, decesita el detalle de compra
        while True:
            id_compra=input("Ingrese el codigo de la compra: ")
            if id_compra in self.compras:
                print("Este codigo ya existe,registre otro: ")
            elif id_compra=="":
                print("Este campo no puede quedar vacio, ingrese dato")
            else:
                break

        fecha_compra= datetime.datetime.now()

        while True:
            id_proveedor=input("Ingrese el codigo del proveedor: ")
            if id_proveedor=="":
                print("Este campo no puede quedar vacio, ingrese dato")
            else:
                break
        while True:
            id_empleado=input("Ingrese el codigo del empleado: ")
            if id_empleado=="":
                print("Este campo no puede quedar vacio, ingrese dato")
            else:
                break
        total=0
        self.compras[id_compra]=Compras(id_compra,fecha_compra,id_proveedor,id_empleado,total)
        while True:
            id_detallecompra = input("ID Detalle Compra: ")
            id_producto = input("ID Producto: ")
            if id_producto not in self.productos:
                print("Producto no existe.")
                continue
            cantidad = int(input("Cantidad: "))
            precio_compra = float(input("Precio compra: "))
            fecha_caducidad = input("Fecha de caducidad (YYYY-MM-DD): ")


            detalle=DetalleCompras(id_detallecompra,id_compra,cantidad,id_producto,precio_compra,fecha_caducidad)
            self.detallecompras[id_detallecompra]=detalle
            total+=detalle.subtotal
            self.productos[id_producto].stock+=cantidad
            opcioningreso=input("Desea ingresar otro producto (s/n): ")
            if opcioningreso.lower()!="s":
                break
        self.compras[id_compra].total=total
        print("Compra realizada")

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

    def listar_proveedor(self):
        if not self.proveedores:
            print("No hay proveedores")
        for pr in self.proveedores.values():
            cat = self.categorias[pr.id_categoria]
            print(f"[{pr.id_proveedores}] {pr.nombre}  | Empresa: {pr.empresa}| Telefono : {pr.telefono} | Direccion: {pr.direccion} | correo: {pr.correo}| Categoria: {cat.nombre}")

    def listar_ventas(self):
            if not self.ventas:
                print("No hay ventas.")
                return
            else:
                for venta in self.ventas.values():
                    cliente = self.clientes[venta.nit]
                    empleado= self.empleadoss[venta.id_empleado]
                    print(f"[{venta.id_venta}] Fecha: {venta.fecha} | Cliente: {cliente.nombre} | Empleado: {empleado.nombre} | Total: {venta.total}")
                    for detalle in self.detalleVentas.values():
                        if detalle.id_venta==venta.id_venta:
                            producto=self.productos[detalle.id_producto]
                        print(f"[{detalle.id_detalleVenta}]  {producto.nombre}| Cantidad: {detalle.cantidad}* {detalle.precio}| = Subtotal: {detalle.subtotal}")

    def listar_compras(self):
            if not self.compras:
                print("No hay compras.")
            else:
                for comp in self.compras.values():
                    provedor = self.proveedores[comp.id_proveedores]
                    empleado= self.empleadoss[comp.id_empleado]
                    print(f"[{comp.id_venta}] Fecha: {comp.fecha} | Proveedor: {provedor.nombre} | Empleaod: {empleado.nombre} | Total: {comp.total}")
                    for det in self.detallecompras.values():
                        if det.id_compras==comp.id_compras:
                            producto=self.productos[det.id_producto]
                            print(f"Detalle {det.id_detalleCompra}: {producto.nombre} x{det.cantidad} = {det.subtotal} (Vence: {det.fechaCaducidad})")



registro = GestionTienda()
while True:
    print("Menu")
    print("1. Ingresar Categorias")
    print("2. Ingresar Productos")
    print("3. Ingresar Clientes")
    print("4. Ingresar Empleados")
    print("5. Ingresar Proveedores")
    print("6. Reaizarr una venta")
    print("7. Realizar una compra")
    print("8. Listar Categorias")
    print("9. Listar Productos")
    print("10, Listar Clientes")
    print("11. Listar Empleados")
    print("12. Listar Proveedores")
    print("13. Listar Ventas")
    print("14. Listar Compras")
    print("15. Salir")
    try:
        opcion=int(input("Ingrese una opcion"))
    except ValueError:
        print("Ingrese un entero")
    match opcion:
        case 1:
            registro.ingreso_categotia()
        case 2:
            registro.ingreso_producto()
        case 3:
            registro.ingreso_clientes()
        case 4:
            registro.ingreso_empleados()
        case 5:
            registro.ingreso_proverdores()
        case 6:
            registro.regitrar_venta()
        case 7:
            registro.registrar_compras()
        case 8:
            registro.listar_categorias()
        case 9:
            registro.listar_productos()
        case 10:
            registro.listar_clientes()
        case 11:
            registro.listar_empleados()
        case 12:
            registro.listar_proveedor()
        case 13:
            registro.listar_ventas()
        case 14:
            registro.listar_compras()
        case 15:
            print("Saliendo")
            break
        case _:
            print("Error, Intentelo sse nuevo")







