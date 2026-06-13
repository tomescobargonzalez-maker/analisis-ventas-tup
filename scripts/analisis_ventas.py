
# KAN-2: Script de análisis de ventas

ventas = []

with open("datos/ventas.csv", "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()

    for linea in lineas[1:]:
        partes = linea.strip().split(",")

        ventas.append({
            "fecha": partes[0],
            "producto": partes[1],
            "cantidad": int(partes[2]),
            "precio": int(partes[3]),
            "monto": int(partes[2]) * int(partes[3])
        })

# Ventas totales
total = 0

for venta in ventas:
    total += venta["monto"]

# Producto más vendido
por_producto = {}

for venta in ventas:
    producto = venta["producto"]

    if producto not in por_producto:
        por_producto[producto] = 0

    por_producto[producto] += venta["monto"]

mas_vendido = max(por_producto, key=por_producto.get)

# Ventas por mes
por_mes = {}

for venta in ventas:
    mes = venta["fecha"][:7]

    if mes not in por_mes:
        por_mes[mes] = 0

    por_mes[mes] += venta["monto"]

with open("resultados/resumen_ventas.txt", "w", encoding="utf-8") as salida:
    salida.write("RESUMEN DE ANÁLISIS DE VENTAS\n")
    salida.write("==============================\n\n")
    salida.write(f"Ventas totales: ${total}\n")
    salida.write(f"Producto más vendido: {mas_vendido}\n\n")
    salida.write("Ventas por mes:\n")

    for mes, monto in sorted(por_mes.items()):
        salida.write(f"{mes}: ${monto}\n")

print(f"Ventas totales: ${total}")
print(f"Producto más vendido: {mas_vendido}")
print("Archivo generado en resultados/resumen_ventas.txt")
