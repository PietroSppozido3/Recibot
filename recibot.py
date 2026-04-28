OBJETOS = {
    "bolsa de plastico": {
        "reciclable": True,
        "tiempo_descomposicion": "10-20 años"
    },
    
    "vidrio": {
        "reciclable": True,
        "tiempo_descomposicion": "1 millón de años"
    },
    "ropa vieja": { 
        "reciclable": False,
        "tiempo_descomposicion": "1-5 años",
        "manualidad": "puedes convertirla en trapos de limpieza o bolsas reutilizables"
    },
    "electrónicos": {
        "reciclable": False,
        "tiempo_descomposicion": "1000 años",
        "manualidad": "utilizarlos de repuestos o donarlos"
    }  
   
}

def evaluar_objeto(nombre_objeto):  
    # Convierte el nombre del objeto a minúsculas para evitar errores con mayúsculas/minúsculas
    nombre_objeto = nombre_objeto.lower()  

    # Verifica si el objeto existe dentro del diccionario OBJETOS
    if nombre_objeto not in OBJETOS:
        # Si no existe, devuelve un mensaje indicando los objetos disponibles
        return f"No conozco ese objeto. Intenta con estos {list(OBJETOS.keys())}"

    # Obtiene los datos del objeto desde el diccionario OBJETOS
    datos = OBJETOS[nombre_objeto]

    # Verifica si el objeto es reciclable
    if datos["reciclable"] == True:
        accion = "RECICLAR"  # Si es reciclable, la acción será reciclar
    else:
        accion = "DALE UN NUEVO USO"  # Si no lo es, sugiere una manualidad

    # Construye el mensaje con la información básica del objeto
    resultado = f"🔍 OBJETO: {nombre_objeto}\n"
    resultado += f"♻️ ACCIÓN: {accion}\n"
    resultado += f"⏳ TIEMPO DE DESCOMPOSICIÓN: {datos['tiempo_descomposicion']}\n"

    # Si el objeto no es reciclable y además tiene una sugerencia de manualidad, la agrega al resultado
    if not datos["reciclable"] and "manualidad" in datos:
        resultado += f"🎨 SUGERENCIA: {datos['manualidad']}\n"

    # Retorna el mensaje final con toda la información procesada
    return resultado

# Ejemplo de uso: imprime la evaluación de "botella de plástico"
print(evaluar_objeto("ropa vieja"))
