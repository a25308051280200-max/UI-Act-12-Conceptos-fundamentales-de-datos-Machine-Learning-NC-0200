# Alejandra Rivera Valenzuela NC 0200
# =============================================================================
# PARTE 1: EJERCICIOS DEL 1 AL 30 (Referencia: El Pythonista)
# =============================================================================
# --- Ejercicio 1: Definición y llamada a una función básica ---
def saludar_programadora():
    """Imprime un saludo para la desarrolladora."""
    print("¡Hola! Bienvenida al curso de Python.")

saludar_programadora()
# --- Ejercicio 2: Parámetros posicionales ---
def calcular_area_rectangulo(ancho, alto):
    """Calcula y retorna el área de un rectángulo."""
    return ancho * alto

area = calcular_area_rectangulo(5, 10)
print(f"Área del rectángulo: {area}")
# --- Ejercicio 3: Parámetros con nombre (keyword arguments) ---
def crear_perfil_usuario(nombre, edad, ciudad):
    """Retorna los datos de la usuaria formateados."""
    return f"Usuaria: {nombre}, {edad} años, residente en {ciudad}"

perfil = crear_perfil_usuario(ciudad="Madrid", nombre="Laura", edad=28)
print(perfil)
# --- Ejercicio 4: Parámetros con valores por defecto ---
def bienvenida_usuario(nombre, saludo="Bienvenida"):
    """Saluda a la usuaria usando un saludo personalizable."""
    return f"¡{saludo}, {nombre}!"

print(bienvenida_usuario("Ana"))
print(bienvenida_usuario("María", "Hola de nuevo"))
# --- Ejercicio 5: Sentencia return simple y múltiple ---
def calcular_estadisticas(numeros):
    """Calcula suma, promedio y valor máximo de una lista."""
    total = sum(numeros)
    promedio = total / len(numeros)
    maximo = max(numeros)
    return total, promedio, maximo

suma_tot, prom_val, max_val = calcular_estadisticas([10, 20, 30, 40, 50])
print(f"Suma: {suma_tot}, Promedio: {prom_val}, Máximo: {max_val}")
# --- Ejercicio 6: Argumentos variables (*args y **kwargs) ---
def registrar_actividades_programadora(desarrolladora, *tareas, **detalles):
    """Registra las tareas y detalles técnicos de una desarrolladora."""
    print(f"\n--- Registro de actividades para la programadora {desarrolladora} ---")
    print("Tareas completadas:")
    for tarea in tareas:
        print(f" - {tarea}")
    print("Detalles del entorno:")
    for clave, valor in detalles.items():
        print(f" - {clave.capitalize()}: {valor}")
registrar_actividades_programadora(
    "Carla",
    "Diseño de BD", "Refactorización de módulos", "Pruebas unitarias",
    lenguaje="Python",
    ide="VS Code",
    estado="Activa"
)
# =============================================================================
# PARTE 2: EJERCICIOS DEL 31 AL 60 (Referencia: Pythones.net)
# =============================================================================
# --- Ejercicio 31: Uso de funciones incorporadas (Built-in) ---
def analizar_datos_entrada(datos):
    """Muestra información básica de los datos usando funciones incorporadas."""
    print("\n--- Análisis de datos ---")
    print(f"Tipo de datos recibidos: {type(datos)}")
    print(f"Cantidad de elementos: {len(datos)}")
    print(f"Suma total de los elementos: {sum(datos)}")

analizar_datos_entrada([15, 25, 35, 45])
# --- Ejercicio 32: Función con cuerpo, lógica interna y return ---
def calcular_descuento_compra(monto, porcentaje_descuento):
    """Calcula el precio final tras aplicar un descuento."""
    descuento = monto * (porcentaje_descuento / 100)
    precio_final = monto - descuento
    return precio_final

precio_original = 120.0
descuento_aplicado = 15
precio_a_pagar = calcular_descuento_compra(precio_original, descuento_aplicado)
print(f"\nPrecio original: ${precio_original} | Descuento: {descuento_aplicado}% | Total: ${precio_a_pagar}")
# --- Ejercicio 33: Función con validación de datos ---
def validar_correo_electronico(correo):
    """Verifica si una cadena tiene el formato básico de un correo."""
    if "@" in correo and "." in correo.split("@")[-1]:
        return True
    return False
correo_prueba = "desarrolladora@ejemplo.com"
es_valido = validar_correo_electronico(correo_prueba)
print(f"¿El correo '{correo_prueba}' es válido?: {es_valido}")
# --- Ejercicio 34: Exploración con dir() y help() ---
def explorar_objeto(objeto):
    """Utiliza dir() para mostrar los métodos disponibles de un objeto."""
    atributos_y_metodos = dir(objeto)
    print(f"\nTotal de atributos/métodos para {type(objeto)}: {len(atributos_y_metodos)}")
    print("Primeros 5 elementos:", atributos_y_metodos[:5])

explorar_objeto("Python")


# --- Ejercicio 35: Calculadora básica con funciones integradas ---
def sumar_nums(a, b):
    return a + b

def restar_nums(a, b):
    return a - b

def multiplicar_nums(a, b):
    return a * b

def dividir_nums(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero."
    return a / b

def ejecutar_calculadora(num1, num2, operacion):
    """Ejecuta la operación matemática seleccionada por la usuaria."""
    if operacion == "suma":
        return sumar_nums(num1, num2)
    elif operacion == "resta":
        return restar_nums(num1, num2)
    elif operacion == "multiplicacion":
        return multiplicar_nums(num1, num2)
    elif operacion == "division":
        return dividir_nums(num1, num2)
    else:
        return "Operación no reconocida."

print("\n--- Prueba de Calculadora ---")
n1, n2 = 20, 5
print(f"Suma ({n1} + {n2}): {ejecutar_calculadora(n1, n2, 'suma')}")
print(f"División ({n1} / {n2}): {ejecutar_calculadora(n1, n2, 'division')}")
print("Alejandra Rivera Valenzuela NC 0200")
