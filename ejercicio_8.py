print ("Calcule el precio de su producto mas el iva  ")
nombre_producto = input("ingrese el nombre del producto ")
precio_producto_sin_iva = int(input("ingrese el precio del producto "))
incremento_con_iva = precio_producto_sin_iva * 0.21
precio_producto_con_iva = precio_producto_sin_iva + incremento_con_iva
print ("el precio final del producto con iva es:", precio_producto_con_iva)
