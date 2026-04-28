Recibot

Un programa en Python que evalúa objetos y sugiere si deben ser reciclados o reutilizados, además de mostrar su tiempo de descomposición.

Cómo usar

1. Abre el proyecto en Visual Studio Code
2. Abre Discord
3. Ejecuta el archivo Python (por ejemplo: main.py)
4. Ejecuta el programa
5. Escriba en el servidor:pepeserver !reciclar *comando en la lista*


Objetos soportados

bolsa de plastico
vidrio
ropa vieja
electrónicos
botella de plastico
papel
pilas

Cómo modificar

Puedes añadir nuevos objetos editando el diccionario `OBJETOS` dentro del código.

Ejemplo:
"nuevo objeto": {
    "reciclable": True,
    "tiempo_descomposicion": "X años",
    "manualidad": "opcional"
}

Objetivo

Ayudar en la concienciación ambiental de forma simple.

