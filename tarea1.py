notas = [4.8, 6.2, 5.5, 3.9, 7.0, 4.1, 5.8, 6.0, 3.5, 5.2, 6.8, 2.9, 4.0, 5.0,
        6.5, 4.3, 5.7, 3.2, 6.1, 4.6]
grados_c = [0,15,25,30,100]

ciudades = [
{"ciudad": "Santiago", "temperaturas": [30.2, 28.5, 25.1, 18.3, 12.7, 9.5, 8.8, 10.1, 14.6, 19.3, 24.8, 28.9]},
{"ciudad": "Valparaíso", "temperaturas": [22.1, 21.8, 20.5, 17.2, 14.3, 12.1, 11.5, 12.0, 13.8, 16.5, 19.2, 21.0]},
{"ciudad": "Concepción", "temperaturas": [20.5, 19.8, 17.2, 13.5, 10.8, 8.5, 7.9, 9.2, 11.5, 14.8, 17.5, 19.8]},
{"ciudad": "Temuco", "temperaturas": [22.3, 21.5, 18.0, 13.2, 9.5, 7.0, 6.5, 8.0, 10.5, 14.0, 17.8, 20.5]},
{"ciudad": "Punta Arenas", "temperaturas": [14.2, 13.5, 11.0, 7.5, 4.2, 2.0, 1.5, 3.0, 6.5, 9.8, 12.0, 13.8]},
]

#Esta funcion se encarga de sumar los datos
def calcular_suma(datos):

    suma = 0 
    iterador = 0
    for iterador in datos:
        suma = suma + iterador
    
    return suma

#.................
def calcular_largo(datos):
    iterador = 0
    contador_largo = 0
    for iterador in datos:
        contador_largo = 1 + contador_largo
    
    return contador_largo

#.....................
def calcular_promedio(datos):

    promedio = calcular_suma(datos) / calcular_largo(datos)

    return promedio

#................
def calcular_minimo(datos):
    iterador = 0 
    minimo = datos[0]
    for iterador in datos:
        if iterador < minimo:
            minimo = iterador
    
    return minimo


def calcular_maximo(datos):
    iterador = 0 
    maximo = datos[0]
    for iterador in datos:
        if iterador > maximo:
            maximo = iterador
    
    return maximo

def burbuja(datos):
    largo = calcular_largo(datos)
    for i in range(largo):
        for j in range(0, largo - i - 1):
            if datos[j] > datos[j + 1]:
                datos[j], datos[j + 1] = datos[j + 1], datos[j]
    return datos


def calcular_mediana(datos):
    datos_ord = burbuja(datos)

    cantidad_datos = calcular_largo(datos)

    if cantidad_datos % 2 == 0:
        dato_mitad = cantidad_datos // 2
        mediana = (datos_ord[dato_mitad-1] + datos_ord[dato_mitad]) / 2
    else:
        mitad = cantidad_datos // 2
        mediana = datos_ord[mitad]
    return mediana 

def calcular_desviacion_estandar(datos):
    
    promedio = calcular_promedio(datos)
    iterador = 0
    suma = []

    for iterador in datos:
        suma.append((iterador - promedio)**2)
    
    promedio_para_desviacion = calcular_promedio(suma)

    desviacion_estandar = promedio_para_desviacion **0.5
    return desviacion_estandar

def celsius_a_fahrenheit(grados_c):

    nueva_lista_farenheit = []
    iterador = 0
    for iterador in grados_c:
        dato_farenheit = ((9/5) * iterador) + 32
        nueva_lista_farenheit.append(dato_farenheit)
    
    return nueva_lista_farenheit

def imprimir_reporte(ciudades):

    for ciudad in ciudades:
        nombre = ciudad["ciudad"]
        temperaturas = ciudad["temperaturas"]

        promedio = calcular_promedio(temperaturas)
        minimo = calcular_minimo(temperaturas)
        maximo = calcular_maximo(temperaturas)

        print("Ciudad:", nombre)
        print("Promedio anual:", round(promedio, 2))
        print("Temperatura mínima:", minimo)
        print("Temperatura máxima:", maximo)
        print("-----------------------------------")

resultado_suma = calcular_suma(notas)
print("La suma de las notas es: ", resultado_suma)


resultado_largo = calcular_largo(notas)
print("La cantidad de notas es: " , resultado_largo)


resultado_promedio = calcular_promedio(notas)
print("El resultado del promedio es: " , resultado_promedio)


resultado_minimo = calcular_minimo(notas)
print("La nota minima es: ",resultado_minimo)


resultado_maximo = calcular_maximo(notas)
print("La nota maxima es: ",resultado_maximo)


datos_ordenados = burbuja(notas)
print("Los datos ordenados: ",datos_ordenados)


resultado_mediana = calcular_mediana(notas)
print("El resultado de la mediana es: ",resultado_mediana)


resultado_desviacion_estandar = calcular_desviacion_estandar(notas)
print("El resultado de la desviacion estandar es: ",resultado_desviacion_estandar)


convertura = celsius_a_fahrenheit(grados_c)
print("La nueva lista de grados fahrenheit: ",convertura)

imprimir_reporte(ciudades)