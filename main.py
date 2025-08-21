class Productos:
    def __init__(self,id_producto,nombre,id_categoria,precio,total_compras,total_ventas,stock):
        self.id_producto=id_producto
        self.nombre=nombre
        self.id_categoria=id_categoria
        self.precio=precio
        self.total_compras=total_compras
        self.total_ventas=total_ventas
        self.stock=stock

class Categoria:
    def __init__(self,id_categoria,nombre):
        self.id_categoria=id_categoria
        self.nombre=nombre

class Clientes:
    def __init__(self, nit,nombre,telefono,direccion,correo):
        self.nit=nit
        self.nombre=nombre
        self.telefono=telefono
        self.direccion=direccion
        self.correo=correo

class Empleados:
    def __init__(self,id_empleado,nombre,telefono,direccion,correo):
        self.id_empleado=id_empleado
        self.nombre=nombre
        self.telefono=telefono
        self.direccion=direccion
        self.correo=correo

class Proveedores:
    def __init__(self,id_proveedores,nombre,empresa,telefono,direccion,correo,id_categoria):
        self.id_proveedores=id_proveedores
        self.nombre=nombre
        self.empresa=empresa
        self.telefono=telefono
        self.direccion=direccion
        self.correo=correo
        self.id_categoria=id_categoria

class Ventas:
    def __init__(self,id_venta,fecha,nit,id_empleado,total):
        self.id_venta=id_venta
        self.fecha=fecha
        self.nit=nit
        self.id_empleado=id_empleado
        self.total=total

class DetalleVenta:
    def __init__(self,id_detallaVenta,id_venta,cantidaad,id_producto,precio,subtotal):
        self.id_detalleVenta=id_detallaVenta
        self.id_venta=id_venta
        self.cantidad=cantidaad
        self.id_producto=id_producto
        self.precio=precio
        self.subtotal=subtotal

class Compras:
    def __init__(self,id_comparas,fecha,id_proveedor,id_empleado,total):
        self.id_compras=id_comparas
        self.fecha=fecha
        self.id_proveedor=id_proveedor
        self.id_empleado=id_empleado
        self.total=total

class DetalleCompras:
    def __init__(self,id_detalleCompra,id_compras,cantidad,id_producto,precioCompra,subtotal,fechaCaducidad):
        self.id_detalleCompra=id_detalleCompra
        self.id_compras=id_compras
        self.cantidad=cantidad
        self.id_producto=id_producto
        self.pecioComra=precioCompra
        self.subtotal=subtotal
        self.fechaCaducidad=fechaCaducidad


