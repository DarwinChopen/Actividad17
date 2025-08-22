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

productos={}
categoria={}
clientes={}
empleados={}
proveedores={}
ventas={}
detalleVentas={}
compras={}
detallecompras={}

while True:
    print("Menu")
    print("1. Ingresar Producto")
    print("2. Ingresar Categoria")
    print("3. Ingresar Clientes")
    print("4. Ingresar Empleados")
    print("5. Ingresar Proveedores")

    print("6. Salir")
    try:
        opcion=int(input("Ingrese una opcion"))
    except ValueError:
        print("Ingrese un entero")
    match opcion:
        case 1:
            print("Inpreso Productos")
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            print("Saliendo")
            break
        case _:
            print("Error, Intentelo sse nuevo")







