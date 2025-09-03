import datetime
from math import trunc


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
    def __init__(self,id_compra,fecha,id_proveedor,id_empleado,total):
        self.id_compra=id_compra
        self.fecha=fecha
        self.id_proveedor=id_proveedor
        self.id_empleado=id_empleado
        self.total=total
    def mostrar_compras(self):
        print(f"Codigo Compras: {self.id_compra}  | Fecha: {self.fecha}  |  Codigo Proveedor: {self.id_proveedor}  |  Codigo Empleado: {self.id_empleado}  |  Total: {self.total}")

class DetalleCompras:
    def __init__(self,id_detalleCompra,id_compra,cantidad,id_producto,precioCompra,fechaCaducidad):
        self.id_detalleCompra=id_detalleCompra
        self.id_compra=id_compra
        self.cantidad=cantidad
        self.id_producto=id_producto
        self.precioCompra=precioCompra
        self.fechaCaducidad=fechaCaducidad
        self.subtotal=cantidad*precioCompra
    def mostrar_detalleCompras(self):
        print(f"Codigo Detalle Compra: {self.id_detalleCompra}  |  Codigo Compras: {self.id_compra}  |  Cantidad: {self.cantidad}  |  Codigo Producto: {self.id_producto}  |  Precio Compra: {self.pecioCompra}  |  Subtotal: {self.subtotal}  |  Fecha Caducidad: {self.fechaCaducidad} ")


class Ordenador:
    def quick_sort(self, lista, clave):
        if len(lista) <= 1:
            return lista
        pivote = lista[0]
        valor_pivote = pivote[clave]
        inicial = [x for x in lista[1:] if x[clave] < valor_pivote]
        medio = [x for x in lista if x[clave] == valor_pivote]
        final = [x for x in lista[1:] if x[clave] >= valor_pivote]
        return self.quick_sort(inicial, clave) + medio + self.quick_sort(final, clave)


class Administrador:
    def __init__(self, user, password):
        self.nombre = user
        self.contra = password
def validacion_admin(administradores):
    intentos = 0
    while intentos < 3:
        try:
            print(f'Esta accion requiere perfil de administrador...\nTienes {3 - intentos} intentos')
            nombre_tmp = input('Ingrese nombre de usuario: ')
            contra_tmp = input('Ingrese la contraseña: ')
            for ob in administradores:
                if ob.nombre == nombre_tmp:
                    if ob.contra == contra_tmp:
                        print('Bienvenido! permiso concedido')
                        return True
            print('Usuario o contraseña incorrecta por favor intente de nuevo')
            print('\n')
            intentos += 1

        except Exception as e:
            print('Error por favor ingrese un dato valido')
    print('Intentos fallidos no tiene acceso a estas funciones')
    return False
admin1 = Administrador("Darwin", "Darwin123")  # Administrador creado
administradores = [admin1]
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

        self.contadores = {"Categoria": 0,
                           "Producto":0,
                           "Proveedores":0,
                           "Empleados":0,
                           "Venta":0,
                           "Compra":0
                           }
        self.cargar_contadores()
        self.cargar_categorias()
        self.cargar_clientes()
        self.cargar_empleados()
        self.cargar_productos()
        self.cargar_proveedores()
        self.cargar_ventass()
        self.cargar_detalleventas()
        self.cargar_compras()
        self.cargar_detallecompras()

    def cargar_contadores(self):
        try:
            with open("contadores.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if not linea:
                        continue
                    tipo, valor = linea.split(":")
                    self.contadores[tipo] = int(valor)
            print("Contadores importados desde contadores.txt")
        except FileNotFoundError:
            print("No existe contadores.txt, se creará uno nuevo al guardar.")

    def guardar_contadores(self):
        with open("contadores.txt", "w", encoding="utf-8") as archivo:
            for tipo, valor in self.contadores.items():
                archivo.write(f"{tipo}:{valor}\n")

    def siguiente_id(self, tipo: str) -> str:
        self.contadores[tipo] = int(self.contadores.get(tipo, 0)) + 1
        self.guardar_contadores()
        return f"{tipo}-{self.contadores[tipo]}"



    def listar_CategoriasOrdenados(self):
        if not self.categorias:
            print("No hay Categorias aún")
            return
        #base erick
        ordenado = Ordenador()
        categorias_lista = [
            {
                "id_categoria":cate.id_categoria.lower(),
                "nombre": cate.nombre.lower(),
                "copia": cate,  # el objeto original
            }
            for codigo, cate in self.categorias.items()
        ]
        while True:
            print("Como desea ordenar las categorias")
            print("1. Codigo")
            print("2. Nombre")
            print("3. Salir")
            try:
                opcionOrdenar = int(input('Digite la opción: '))
                match opcionOrdenar:
                    case 1:
                        ordenados_u = ordenado.quick_sort(categorias_lista, "id_categoria")
                    case 2:
                        ordenados_u = ordenado.quick_sort(categorias_lista, "nombre")
                    case 3:
                        print("Saliendoo")
                        break
                    case _:
                        print('La opción no existe, por favor vuelve a intentarlo')
                        continue
                print("Productos ordenados")
                for tmp in ordenados_u:
                    cate = tmp["copia"]
                    print(f"id_ categoria: {cate.id_categoria}| nombre: {cate.nombre}")
                break
            except ValueError:
                print("Debes ingresar un número. Intenta de nuevo.")
            except Exception as e:
                print(f'Por favor volver a intentar, ocurrió {e}')
    def listar_productosOrdenados(self):
        if not self.productos:
            print("No hay productos aún")
            return
        ordenado = Ordenador()
        productos_lista = [
            {
                "codigo": codigo,
                "nombre": prod.nombre.lower(),
                "id_categoria":prod.id_categoria,
                "precio": prod.precio,
                "stock": prod.stock,
                "copia": prod,
            }
            for codigo, prod in self.productos.items()
        ]
        while True:
            print("Como desea ordenar los productos")
            print("1. Nombe")
            print("2. Precio")
            print("3. Cantidad en stock")
            print("4. Salir")
            try:
                opcionOrdenar = int(input('Digite la opción: '))
                match opcionOrdenar:
                    case 1:
                        ordenados_u = ordenado.quick_sort(productos_lista, "nombre")
                    case 2:
                        ordenados_u = ordenado.quick_sort(productos_lista, "precio")
                    case 3:
                        ordenados_u = ordenado.quick_sort(productos_lista, "stock")
                    case 4:
                        print("Saliendoo")
                        break
                    case _:
                        print('La opción no existe, por favor vuelve a intentarlo')
                        continue
                print("Productos ordenados")
                for tmp in ordenados_u:
                    prod = tmp["copia"]
                    print(f"[{prod.id_producto}] {prod.nombre} | id_ categoria: {prod.id_categoria}| Precio: {prod.precio} | Stock: {prod.stock}")
                break
            except ValueError:
                print("Debes ingresar un número. Intenta de nuevo.")
            except Exception as e:
                print(f'Por favor volver a intentar, ocurrió {e}')

    def listar_clientesOrdenados(self):
        if not self.clientes:
            print("No hay Clientes aún")
            return
        ordenado = Ordenador()
        clientes_lista = [
            {
                "nit": clie.nit,
                "nombre": clie.nombre.lower(),
                "telefono": clie.telefono,
                "direccion": clie.direccion,
                "correo": clie.correo,
                "copia": clie,
            }
            for codigo, clie in self.clientes.items()
        ]
        while True:
            print("Como desea ordenar a los clientes")
            print("1. Nit")
            print("2. Nombre")
            print("3. Telefono")
            print("4. Salir")
            try:
                opcionOrdenar = int(input('Digite la opción: '))
                match opcionOrdenar:
                    case 1:
                        ordenados_u = ordenado.quick_sort(clientes_lista, "nit")
                    case 2:
                        ordenados_u = ordenado.quick_sort(clientes_lista, "nombre")
                    case 3:
                        ordenados_u = ordenado.quick_sort(clientes_lista, "telefono")
                    case 4:
                        print("Saliendoo")
                        break
                    case _:
                        print('La opción no existe, por favor vuelve a intentarlo')
                        continue
                print("Productos ordenados")
                for tmp in ordenados_u:
                    clie = tmp["copia"]
                    print(
                        f"[Nit {clie.nit} | Nombre: {clie.nombre} | Telefono: {clie.telefono}| Direccion: {clie.direccion} | Correo: {clie.correo}")
                break
            except ValueError:
                print("Debes ingresar un número. Intenta de nuevo.")
            except Exception as e:
                print(f'Por favor volver a intentar, ocurrió {e}')

    def listar_empleadosOrdenados(self):
        if not self.empleadoss:
            print("No hay Empleados aún")
            return
        ordenado = Ordenador()
        empleados_lista = [
            {
                "id_empleado": emp.id_empleado,
                "nombre": emp.nombre.lower(),
                "telefono": emp.telefono,
                "direccion": emp.direccion,
                "correo": emp.correo,
                "copia": emp,
            }
            for codigo, emp in self.empleadoss.items()
        ]
        while True:
            print("Como desea ordenar a los Empleados")
            print("1. Id Empleado")
            print("2. Nombre")
            print("3. Telefono")
            print("4. Salir")
            try:
                opcionOrdenar = int(input('Digite la opción: '))
                match opcionOrdenar:
                    case 1:
                        ordenados_u = ordenado.quick_sort(empleados_lista, "id_empleado")
                    case 2:
                        ordenados_u = ordenado.quick_sort(empleados_lista, "nombre")
                    case 3:
                        ordenados_u = ordenado.quick_sort(empleados_lista, "telefono")
                    case 4:
                        print("Saliendoo")
                        break
                    case _:
                        print('La opción no existe, por favor vuelve a intentarlo')
                        continue
                print("Empleados ordenados")
                for tmp in ordenados_u:
                    emp = tmp["copia"]
                    print(
                        f"[ID Empleado: {emp.id_empleado} | Nombre: {emp.nombre} | Telefono: {emp.telefono}| Direccion: {emp.direccion} | Correo: {emp.correo}")
                break
            except ValueError:
                print("Debes ingresar un número. Intenta de nuevo.")
            except Exception as e:
                print(f'Por favor volver a intentar, ocurrió {e}')

    def listar_proveedoresOrdenados(self):
        if not self.proveedores:
            print("No hay Proveedores aún")
            return
        ordenado = Ordenador()
        proveedores_lista = [
            {
                "id_proveedores": prov.id_proveedores,
                "nombre": prov.nombre.lower(),
                "empresa":prov.empresa,
                "telefono": prov.telefono,
                "direccion": prov.direccion,
                "correo": prov.correo,
                "id_categoria":prov.id_categoria,
                "copia": prov,
            }
            for codigo, prov in self.proveedores.items()
        ]
        while True:
            print("Como desea ordenar a los Proveedores")
            print("1. ID Proveedores")
            print("2. Nombre")
            print("3. Telefono")
            print("4. Salir")
            try:
                opcionOrdenar = int(input('Digite la opción: '))
                match opcionOrdenar:
                    case 1:
                        ordenados_u = ordenado.quick_sort(proveedores_lista, "id_proveedores")
                    case 2:
                        ordenados_u = ordenado.quick_sort(proveedores_lista, "nombre")
                    case 3:
                        ordenados_u = ordenado.quick_sort(proveedores_lista, "telefono")
                    case 4:
                        print("Saliendoo")
                        break
                    case _:
                        print('La opción no existe, por favor vuelve a intentarlo')
                        continue
                print("Proveedores ordenados")
                for tmp in ordenados_u:
                    prov = tmp["copia"]
                    print(f"[Codigo Proveedor: {prov.id_proveedores} | Nombre: {prov.nombre} | Empresa: {prov.empresa} | Telefono: {prov.telefono}| Direccion: {prov.direccion} | Correo: {prov.correo}")
                break
            except ValueError:
                print("Debes ingresar un número. Intenta de nuevo.")
            except Exception as e:
                print(f'Por favor volver a intentar, ocurrió {e}')

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

    def cargar_ventass(self):
        try:
            with open("ventas.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        id_venta, fecha, nit, id_empleado, total,= linea.split("/")
                        self.ventas[id_venta] = Ventas(id_venta,fecha, nit,id_empleado, float(total))
            print("Ventas importados desde ventas.txt")
        except FileNotFoundError:
            print("No existe el archivo ventas.txt, se creará uno nuevo al guardar.")

    def guardar_ventass(self):
        with open("ventas.txt", "w", encoding="utf-8") as archivo:
            for venta in self.ventas.values():
                archivo.write(f"{venta.id_venta}/{venta.fecha}/{venta.nit}/{venta.id_empleado}/{venta.total}\n")

    def cargar_detalleventas(self):
        try:
            with open("detalleventas.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        id_detalleVenta, id_venta, cantidad, id_producto, precio,subtotal,= linea.split(":")
                        self.detalleVentas[id_detalleVenta] = DetalleVenta(id_detalleVenta, id_venta,int(cantidad),id_producto, float(precio))
                        self.detalleVentas[id_detalleVenta].subtototal=float(subtotal)
            print("Detalles de Ventas importados desde detalleventas.txt")
        except FileNotFoundError:
            print("No existe el archivo detalleventas.txt, se creará uno nuevo al guardar.")

    def guardar_detalleventas(self):
        with open("detalleventas.txt", "w", encoding="utf-8") as archivo:
            for detalle in self.detalleVentas.values():
                archivo.write(f"{detalle.id_detalleVenta}:{detalle.id_venta}:{detalle.cantidad}:{detalle.id_producto}:{detalle.precio}:{detalle.subtotal}\n")

    def cargar_compras(self):
        try:
            with open("Compras.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        id_compra, fecha, id_proveedor, id_empleado, total = linea.split("/")
                        self.compras[id_compra] = Compras(id_compra, fecha, id_proveedor, id_empleado, float(total))
            print("Compras importadas desde Compras.txt")
        except FileNotFoundError:
            print("No existe el archivo Compras.txt, se creará uno nuevo al guardar.")

    def guardar_compras(self):
        with open("Compras.txt", "w", encoding="utf-8") as archivo:
            for compra in self.compras.values():
                archivo.write(
                    f"{compra.id_compra}/{compra.fecha}/{compra.id_proveedor}/{compra.id_empleado}/{compra.total}\n")

    def cargar_detallecompras(self):
        try:
            with open("detallecompras.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if not linea:
                        continue
                    # Formato esperado: id_detalleCompra:id_compra:cantidad:id_producto:precioCompra:fechaCaducidad:subtotal
                    id_detalleCompra, id_compra, cantidad, id_producto, precioCompra, fechaCaducidad, subtotal = linea.split(":")
                    det = DetalleCompras(id_detalleCompra, id_compra, int(cantidad), id_producto, float(precioCompra),fechaCaducidad)
                    # Sobrescribir el subtotal con lo leído (opcional, puedes recalcularlo)
                    det.subtotal = float(subtotal)
                    self.detallecompras[id_detalleCompra] = det

            print("Detalles de Compras importados desde detallecompras.txt")
        except FileNotFoundError:
            print("No existe el archivo detallecompras.txt, se creará uno nuevo al guardar.")

    def guardar_detallecompras(self):
        with open("detallecompras.txt", "w", encoding="utf-8") as archivo:
            for detalle in self.detallecompras.values():
                archivo.write(
                    f"{detalle.id_detalleCompra}:{detalle.id_compra}:{detalle.cantidad}:"
                    f"{detalle.id_producto}:{detalle.precioCompra}:{detalle.fechaCaducidad}:{detalle.subtotal}\n"
                )
    def ingreso_producto(self):
        if not self.categorias:
            print("No hay categorias, Ingrese una primero")
            return
        while True:
            try:
                cantidad_productos = int(input('¿Cuantos productos desea ingresar al inventario?:     '))
                for i in range(cantidad_productos):
                    print(f'\t\t\t\tIngreso datos de Producto ')
                    codigo = self.siguiente_id("Producto-")

                    while True:
                        nombre = input("Ingrese el Nombre del Producto: ")
                        if nombre == "":
                            print("Este Campo no puede quedar vacio, Ingrese el nombre")
                            continue
                        if any(p.nombre.lower() == nombre.lower() for p in self.productos.values()):
                            print("Este nombre ya existe, ingrese otro.")
                            continue
                        break
                    while True:
                        print("\nCategorías disponibles:")
                        for categorias in self.categorias.values():
                            print(f"  - {categorias.id_categoria}: {categorias.nombre}")
                        id_categoria = input("ID Categoría: ")
                        if id_categoria == "":
                            print("El campo no puede estar vacío.")
                            continue
                        if id_categoria not in self.categorias:
                            print("La categoría no existe Ingrese una de la lista.")
                            continue
                        break
                    while True:
                        try:
                            precio = float(input("Ingrese el Precio en Quetzales del Producto: Q."))
                            if precio == "":
                                print("Este campo no Puede quedar vacio, Ingrese el precio")

                            elif precio <=0:
                                print("El precio no puede ser negativo ni igual a 0")
                            else:
                                break
                        except ValueError:
                            print("Solo se permiten cantidades")
                    while True:
                        try:
                            stock = int(input("Ingrese la cantidad Inicial en Stock(no puede ser negativo ni igual a 0): "))
                            if stock <=0:
                                print("Error, la cantidad en stock, no puede ser negativa y no puede ser 0")
                            else:
                                break
                        except ValueError:
                            print("Solo se permiten enteros")
                    self.productos[codigo]=Productos(codigo, nombre, id_categoria,precio, stock)
                    self.guardar_productos()
                    print(f'El producto con codigo {codigo} se Agrego y Guardo Correctamente')
                    print('\n')
                break
            except Exception as e:
                print(f'Por favor ingrese datos validos, ocurrio {e}')
    def ingreso_categotia(self):
        while True:
            try:
                cantidad_categorias = int(input('¿Cuantas categorias desea ingresar?: '))
                for i in range(cantidad_categorias):
                    print(f'\t\t\t\tIngreso datos de la Categoria')
                    id_categoria=self.siguiente_id("Categoria-")
                    if self.categorias:
                        print("Estas son las categorias ya registradas:")
                        for categorias in self.categorias.values():
                            print(f"Codigo: {categorias.id_categoria}: Nombre: {categorias.nombre}")
                    else:
                        print("No hay Categorias registradas...")
                    while True:
                        nombre = input("Ingrese el Nombre de la categoria: ")
                        if nombre in self.categorias:
                            print("Este Nombre en especifico ya existe, ingrese otro:")
                        elif nombre == "":
                            print("Este Campo no puede quedar vacio, Ingrese el nombre")
                        elif any(c.nombre.lower() == nombre.lower() for c in self.categorias.values()):
                            print("Ya existe una categoría con ese nombre, ingrese otro.")
                            continue
                        else:
                            break
                    self.categorias[id_categoria]=Categoria(id_categoria, nombre)
                    self.guardar_categorias()
                    print(f'La categoria con codigo {id_categoria} se agrego y guardo correctamente')
                    print('\n')
                break
            except Exception as e:
                print(f'Por favor ingrese datos validos, ocurrio {e}')

    def ingreso_clientes(self):
        cantidad_clientes = int(input('¿Cuantos clientes desea ingresar al inventario?: '))
        for i in range(cantidad_clientes):
            print(f'\t\t\t\tIngreso datos de Cliente: ')
            while True:
                nit = input("Ingrese el nit del cliente: ")
                if nit in self.clientes:
                    print("Este nit Ya existe, Intentelo de nuevo...")
                elif nit == "":
                    print("El codigo no puede estar vacio, Intentelo de nuevo...")
                else:
                    break
            while True:
                nombre_cliente = input("Ingrese el Nombre del cliente: ")
                if any(c.nombre_cliente.lower() == nombre_cliente.lower() for c in self.clientes.values()):
                    print("Este Nombre en especifico ya existe, ingrese otro:")
                    continue
                elif nombre_cliente == "":
                    print("Este Campo no puede quedar vacio, Ingrese el nombre del cliente")
                    continue
                break
            while True:
                try:
                    telefono_cliente = int(input("Ingrese el numero del cliente: "))
                    if any(c.telefono_cliente.lower() == telefono_cliente.lower() for c in self.clientes.values()):
                        print("Este Numero en especifico ya existe, ingrese otro:")
                        continue
                    if telefono_cliente=="":
                        print("Este campo no Puede quedar vacio, Ingrese el Dato")
                        continue
                    if telefono_cliente<0:
                        print("El telefono no es Valido")
                        continue
                    else:
                        break
                except ValueError:
                    print("Solo se permiten numeros")
            while True:
                direccion_cliente=input("Ingrese la direccion del cliente: ")
                if direccion_cliente in self.clientes:
                    print("Esta direccion ya esta en uso")
                elif direccion_cliente=="":
                    print("Este campo no puede quedar vacio,ingrese el dato")
                else:
                    break
            while True:
                correo_cliente=input("Ingrese el correo del cliente: ")
                if correo_cliente in self.clientes:
                    print("Este correo ya esta en uso")
                elif correo_cliente=="":
                    print("Este campo no puede quedar vacio,ingrese el dato")
                else:
                    break
            self.clientes[nit]=Clientes(nit,nombre_cliente,telefono_cliente,direccion_cliente,correo_cliente)
            self.guardar_clientes()
            print(f'El cliente con nit {nit} se agrego y guardo correctamente')
            print('\n')

    def ingreso_empleados(self):
        cantidad_empleados = int(input('¿Cuantos empleados desea ingresar?: '))
        for i in range(cantidad_empleados):
            print(f'\t\t\t\tIngreso datos de {i + 1} empleado: ')
            while True:
                id_empleado = self.siguiente_id("Empleado-")
                if id_empleado in self.empleadoss:
                    print("Este id Ya existe, Intentelo de nuevo...")
                elif id_empleado == "":
                    print("El codigo no puede estar vacio, Intentelo de nuevo... ")
                else:
                    break
            while True:
                nombre_empleado = input("Ingrese el Nombre del empleado: ")
                if any(c.nombre.lower() == nombre_empleado.lower() for c in self.empleadoss.values()):
                    print("Este Nombre en especifico ya existe, ingrese otro:")
                    continue
                if nombre_empleado == "":
                    print("Este Campo no puede quedar vacio, Ingrese el nombre del empleado")
                    continue
                else:
                    break
            while True:
                try:
                    telefono_empleado = int(input("Ingrese el numero del empleado: "))
                    if any(c.telefono == telefono_empleado for c in self.empleadoss.values()):
                        print("Este Numero en especifico ya existe, ingrese otro:")
                        continue
                    elif telefono_empleado=="":
                        print("Este campo no Puede quedar vacio, Ingrese el Dato")
                    elif telefono_empleado<0:
                        print("El telefono no es valido")
                    else:
                        break
                except ValueError:
                    print("Solo se permiten numeros")
            while True:
                direccion_empleado=input("Ingrese la direccion del empleado:")
                if direccion_empleado in self.empleadoss:
                    print("Esta direccion ya esta en uso")
                elif direccion_empleado=="":
                    print("Este campo no puede quedar vacio,ingrese el dato")
                else:
                    break
            while True:
                correo_empleado=input("Ingrese el correo del empleado: ")
                if correo_empleado in self.empleadoss:
                    print("Este correo ya esta en uso")
                elif correo_empleado=="":
                    print("Este campo no puede quedar vacio,ingrese el dato")
                else:
                    break
            self.empleadoss[id_empleado]=Empleados(id_empleado,nombre_empleado,telefono_empleado,direccion_empleado,correo_empleado)
            self.guardar_empleados()
            print(f'El Empleado con codigo {id_empleado} se agrego y guardo correctamente')
            print('\n')
    def ingreso_proverdores(self):
        print("Categorias disponibles: ")
        for categoria in self.categorias.values():
            print(f"  - {categoria.id_categoria}: {categoria.nombre}")
        cantidad_proveedores = int(input('¿Cuantos proveedores desea ingresar?: '))
        for i in range(cantidad_proveedores):
            print(f'\t\t\t\tIngreso datos del Proveedor')
            id_proveedor = self.siguiente_id("Proveedor-")
            while True:
                nombre_proveedor = input("Ingrese el Nombre del proveedor: ")
                if nombre_proveedor == "":
                    print("Este Campo no puede quedar vacio, Ingrese el nombre del proveedor")
                    continue
                if any(p.nombre.lower() == nombre_proveedor.lower() for p in self.proveedores.values()):
                    print("Este nombre ya esta en uso, ingrese otro")
                    continue
                break
            while True:
                empresa_proveedor = input("Ingrese la empresa del proveedor: ")
                if empresa_proveedor == "":
                    print("Este Campo no puede quedar vacio, Ingrese el nombre del proveedor")
                    continue
                if any(p.empresa.lower() == empresa_proveedor.lower() for p in self.proveedores.values()):
                    print("Esta empresa ya esta registrada, ingrese otro")
                    continue
                break
            while True:
                try:
                    telefono_provedor = int(input("Ingrese el telefono del proveedor: "))
                    if telefono_provedor == "":
                        print("Este Campo no puede quedar vacio, Ingrese el telefono del proveedor")
                        continue
                    if any(p.telefono == telefono_provedor for p in self.proveedores.values()):
                        print("Esta Telefono ya esta registrada, ingrese otro")
                        continue
                    break
                except ValueError:
                    print("Solo se permiten numeros")
            while True:
                direccion_provedor=input("Ingrese la direccion del proveedor: ")
                if direccion_provedor in self.proveedores:
                    print("Esta direccion ya esta en uso")
                elif direccion_provedor=="":
                    print("Este campo no puede quedar vacio,ingrese el dato")
                else:
                    break
            while True:
                correo_provedor=input("Ingrese el correo del proveedor: ")
                if correo_provedor == "":
                    print("Este Campo no puede quedar vacio, Ingrese el nombre del proveedor")
                    continue
                if any(p.correo.lower() == correo_provedor.lower() for p in self.proveedores.values()):
                    print("Esta empresa ya esta registrada, ingrese otro")
                    continue
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

            print(f'El Proveedor con codigo {id_proveedor} se agrego y guardo correctamente')
            print('\n')

    def regitrar_venta(self):

        id_venta = self.siguiente_id("venta-")
        fecha_venta= datetime.datetime.now()
        while True:
            print("Estos son los clientes registrados")
            for cliente in self.clientes.values():
                print(f"  - {cliente.nit}: {cliente.nombre}")
            id_cliente=input("Ingrese el codigo del cliente: ")
            if id_cliente=="":
                print("Este campo no puede quedar vacio, ingrese dato")
            elif id_cliente not in self.clientes:
                print("Este codigo No existe, intentelo de nuevo")
            else:
                break
        while True:
            print("Estos son los Empleados registrados")
            for empleado in self.empleadoss.values():
                print(f"  - {empleado.id_empleado}: {empleado.nombre}")
            id_empleado=input("Ingrese el codigo del empleado: ")
            if id_empleado=="":
                print("Este campo no puede quedar vacio, ingrese dato")
            elif id_empleado not in self.empleadoss:
                print("Este codigo No existe, intentelo de nuevo")
            else:
                break
        total=0#aun no se calcula
        self.ventas[id_venta]=Ventas(id_venta,fecha_venta,id_cliente,id_empleado,total)
        self.guardar_ventass()
        print(f"Venta registrada con ID: {id_venta}")
        while True:
            id_detalleventa = input("ID Detalle Venta: ")
            print("Estos son los Productos Registraso")
            for producto in self.productos.values():
                print(f"  - {producto.id_producto}: {producto.nombre}")
            id_producto = input("Ingrese el Codigo del Producto: ")
            if id_producto not in self.productos:
                print("Producto no existe.")
                continue

            producto = self.productos[id_producto]
            print(f"El producto '{producto.nombre}' tiene {producto.stock} en stock.")
            cantidad = int(input("Cantidad: "))

            if cantidad > producto.stock:
                print("Stock insuficiente.")
                continue

            precio=float(self.productos[id_producto].precio)
            detalle=DetalleVenta(id_detalleventa,id_venta,cantidad,id_producto,precio)
            self.detalleVentas[id_detalleventa]=detalle
            total+=detalle.subtotal
            self.productos[id_producto].stock-=cantidad
            opcioningreso=input("Desea ingresar otro producto s/n: ")
            if opcioningreso.lower()!="s":
                break
        self.ventas[id_venta].total=total
        self.guardar_ventass()
        self.guardar_detalleventas()
        self.guardar_productos()
        self.ticket_venta(id_venta)
        print("Venta realizada")

    def registrar_compras(self):#aun no funciona, decesita el detalle de compra
        id_compra = self.siguiente_id("compra")

        fecha_compra= datetime.datetime.now()

        while True:
            print("Estos son los Proveedores registrados")
            for proveedor in self.proveedores.values():
                print(f"  - {proveedor.id_proveedores}: {proveedor.nombre}")
            id_proveedor=input("Ingrese el codigo del proveedor: ")
            if id_proveedor=="":
                print("Este campo no puede quedar vacio, ingrese dato")
            elif id_proveedor not in self.proveedores:
                print("Este Proveedor No existe, intentelo de nuevo")
            else:
                break

        while True:
            print("Estos son los Empleados registrados")
            for empleado in self.empleadoss.values():
                print(f"  - {empleado.id_empleado}: {empleado.nombre}")
            id_empleado=input("Ingrese el codigo del empleado: ")
            if id_empleado=="":
                print("Este campo no puede quedar vacio, ingrese dato")
            elif id_empleado not in self.empleadoss:
                print("Este Empleado No existe, intentelo de nuevo")
            else:
                break
        total=0
        self.compras[id_compra]=Compras(id_compra,fecha_compra,id_proveedor,id_empleado,total)
        print(f"Compra registrada con ID: {id_compra}")
        while True:
            id_detallecompra = input("ID Detalle Compra: ")
            print("Estos son los Productos Registrados")
            for producto in self.productos.values():
                print(f"  - {producto.id_producto}: {producto.nombre}")
            id_producto = input("ID Producto: ")
            if id_producto not in self.productos:
                print("Producto no existe.")
                continue
            cantidad = int(input("Cantidad: "))
            precio_compra = float(input("Precio compra: "))
            fecha_caducidad = input("Fecha de caducidad (AAAA/MM/DD): ")

            detalle=DetalleCompras(id_detallecompra,id_compra,cantidad,id_producto,precio_compra,fecha_caducidad)
            self.detallecompras[id_detallecompra]=detalle
            total+=detalle.subtotal
            self.productos[id_producto].stock+=cantidad
            opcioningreso=input("Desea ingresar otro producto (s/n): ")
            if opcioningreso.lower()!="s":
                break
        self.compras[id_compra].total=total
        self.guardar_compras()
        self.guardar_detallecompras()
        self.guardar_productos()
        self.ticket_compra(id_compra)
        print("Venta realizada")

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
                for compra in self.compras.values():
                    provedor = self.proveedores[compra.id_proveedor]
                    empleado= self.empleadoss[compra.id_empleado]
                    print(f"[{compra.id_compra}] Fecha: {compra.fecha} | Proveedor: {provedor.nombre} | Empleaod: {empleado.nombre} | Total: {compra.total}")
                    for detalle in self.detallecompras.values():
                        if detalle.id_compra==compra.id_compra:
                            producto=self.productos[detalle.id_producto]
                            print(f"[{detalle.id_detalleCompra}]  {producto.nombre}| Cantidad: {detalle.cantidad}* {detalle.precioCompra}| = Subtotal: {detalle.subtotal}: fecha vencimiento{detalle.fechaCaducidad}")
    def ticket_venta(self, id_venta):
        if id_venta not in self.ventas:
            print("Esa venta no existe.")
            return

        v = self.ventas[id_venta]
        cliente  = self.clientes.get(v.nit)
        empleado = self.empleadoss.get(v.id_empleado)
        nom_cli  = cliente.nombre
        nom_emp  = empleado.nombre

        print(f"\n[Venta {v.id_venta}] Fecha: {v.fecha} | Cliente: {nom_cli} | Empleado: {nom_emp} | Total: {v.total}")
        print("Detalles:")
        for d in self.detalleVentas.values():
            if d.id_venta == v.id_venta:
                prod = self.productos.get(d.id_producto)
                nom_prod = prod.nombre if prod else d.id_producto
                print(f"  [{d.id_detalleVenta}] {nom_prod} | Cant: {d.cantidad} x {d.precio} = {d.subtotal}")

    def ticket_compra(self, id_compra):
        if id_compra not in self.compras:
            print("Esa compra no existe.")
            return

        c = self.compras[id_compra]
        proveedor = self.proveedores.get(c.id_proveedor)
        empleado = self.empleadoss.get(c.id_empleado)

        nom_prov = proveedor.nombre
        nom_emp = empleado.nombre
        print(
            f"\n[Compra {c.id_compra}] Fecha: {c.fecha} | Proveedor: {nom_prov} | Empleado: {nom_emp} | Total: {c.total}")
        print("Detalles:")
        for d in self.detallecompras.values():
            if d.id_compra == c.id_compra:
                prod = self.productos.get(d.id_producto)
                nom_prod = prod.nombre if prod else d.id_producto
                print(
                    f"  [{d.id_detalleCompra}] {nom_prod} | Cant: {d.cantidad} x {d.precioCompra} = {d.subtotal} | Vence: {d.fechaCaducidad}")
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
    print("8. Listar")
    print("9. Ordenar")
    print("10. Salir")
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
            if validacion_admin(administradores):
                registro.registrar_compras()
        case 8:
            while True:
                print("1. Listar Categorias")
                print("2. Listar Productos")
                print("3, Listar Clientes")
                print("4. Listar Empleados")
                print("5. Listar Proveedores")
                print("6. Listar Ventas")
                print("7. Listar Compras")
                print("8. Salir")
                try:
                    subop = int(input("Elige una opción: "))
                except ValueError:
                    print("Ingresa un número válido.")
                    continue
                match subop:
                    case 1:
                        registro.listar_categorias()
                    case 2:
                        registro.listar_productos()
                    case 3:
                        registro.listar_clientes()
                    case 4:
                        registro.listar_empleados()
                    case 5:
                        registro.listar_proveedor()
                    case 6:
                        registro.listar_ventas()
                    case 7:
                        registro.listar_compras()
                    case 8:
                        break
                    case _:
                        print("Opción inválida.")
        case 9:
            while True:
                print("1. Listar Categorias Ordenados")
                print("2. Listar Productos Ordenados")
                print("3, Listar Clientes Ordenados")
                print("4. Listar Empleados Ordenados")
                print("5. Listar Proveedores Ordenados")
                print("6. Salir")
                try:
                    subop = int(input("Elige una opción: "))
                except ValueError:
                    print("Ingresa un número válido.")
                    continue
                match subop:
                    case 1:
                        registro.listar_CategoriasOrdenados()
                    case 2:
                        registro.listar_productosOrdenados()
                    case 3:
                        registro.listar_clientesOrdenados()
                    case 4:
                        registro.listar_empleadosOrdenados()
                    case 5:
                        registro.listar_proveedoresOrdenados()
                    case 6:
                        break
                    case _:
                        print("Opción inválida.")
        case 10:
            print("Saliendo")
            break
        case _:
            print("Error, Intentelo sse nuevo")