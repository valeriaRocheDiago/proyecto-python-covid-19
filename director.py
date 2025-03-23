from consumir_api.api import obtener_datos
from interfaz_usuario.ui import convertir_a_tabla
from analisis_data.eda import realizar_eda 

#obtener datos
departamento = input("Ingrese el nombre del departamento: ")
departamento = departamento.upper()
limite = int(input("Ingrese el límite de resultados: "))

datos = obtener_datos(departamento, limite)

#Mostrar tabla
tabla = convertir_a_tabla(datos)

print(tabla)

#Mostrar el EDA
realizar_eda ( datos )
