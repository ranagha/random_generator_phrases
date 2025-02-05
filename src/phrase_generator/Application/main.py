import random

frases_esdla = [
    'No es sino la sombra de una ilusión lo que amas. No puedo darte lo que anhelas.',
    '¡Cuenta con mi espada! ¡Y con mi hacha! ¡Y con mi arco!',
    'Vuelve al infierno, llama de Idhun. ¡No puedes pasar!',
    'Si con mi vida o con mi muerte puedo salvaros, así lo haré.'
]

frases_hp = [
    'Tú no eres una mala persona. Eres una persona muy buena a la que le han pasado cosas malas.',
    'La grandeza inspira envidia, la envidia engendra rencor y el rencor genera mentiras.',
    'No importa lo que alguien nace, sino lo que llega a ser cuando crece.',
    '¡Podrías afirmar que cualquier cosa es real si la única base para creer en ella es que nadie ha demostrado que no existe!'
]

frases_juego_tronos = [
    'Los dioses no tienen piedad, por eso son dioses.',
    'No es fácil estar borracho todo el tiempo. Si fuera fácil, todos lo harían.',
    '¿Qué le decimos al Dios de la muerte? Hoy no.',
    'La mente necesita libros como la espada necesita una piedra de afilar si quiere mantener su agudeza.'
]

def generar_contenido(tipo):
    if tipo == "1":
        return random.choice(frases_esdla)
    elif tipo == "2":
        return random.choice(frases_hp)
    elif tipo == "3":
        return random.choice(frases_juego_tronos)
    elif tipo != "0":
        return "Opción no válida, prueba de nuevo."

def menu():
    print("📢 Bienvenido al Generador de Contenido Aleatorio 📢")
    print("Elige una opción:")
    print("1 - ¿Eres de El señor de los anillos?")
    print("2 - ¿Eres de Harry Potter?")
    print("3 - ¿Eres de Juego de tronos?")
    print("0 - Salir")



def start():
    opcion = '1'
    while opcion != '0':
        menu()
        opcion = input("Introduce el número de tu elección: ")
        if opcion != '0':
            print(generar_contenido(opcion))