"""Codigo final 26 de abril."""
import random

def carta_de_la_casa():
    """Esta función selecciona una carta al azar de la baraja de blackjack que incluye los valores típicos:
    números del 2 al 10, figuras (J, Q, K) que valen 10, y el As que puede valer 11 o 1, dependiendo de la situación."""
    # Test Case 1: Verificar que la carta devuelta está dentro del rango permitido de valores.
    # Test Case 2: Ejecutar la función múltiples veces para asegurar que la distribución de valores parece aleatoria y no sesgada.
    cartas = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(cartas)

def puntaje_mano(mano):
    """Calcula el puntaje de una mano de cartas ajustando el valor del As de 11 a 1 si el puntaje total supera 21."""
    # Test Case 1: Dar a la función una mano con un As y un valor alto (ej. As y 10), y verificar que el puntaje sea 21.
    # Test Case 2: Dar a la función una mano con varios Ases y valores que inicialmente sumen más de 21, y verificar que ajuste correctamente los Ases de 11 a 1.
    score = sum(mano)
    ace_count = mano.count(11)
    while score > 21 and ace_count > 0:
        score -= 10
        ace_count -= 1
    return score

def mostrar_mano(mano, es_dealer=False):
    """Muestra las cartas de la mano del jugador o la primera carta del dealer si es_dealer es True.
    Esto ayuda a visualizar el estado actual del juego."""
    # Test Case 1: Verificar que al mostrar la mano de un jugador, la función imprime correctamente las cartas y el puntaje.
    # Test Case 2: Verificar que al mostrar la mano del dealer solo muestra la primera carta si 'es_dealer' es True.
    if es_dealer:
        print(f"Primera carta del dealer: {mano[0]}")
    else:
        print(f"Tus Cartas: {mano}, Puntaje actual: {puntaje_mano(mano)}")

def tomar_decision():
    """Pide al jugador decidir si quiere otra carta o parar, validando que la entrada sea 'y' o 'n'."""
    # Test Case 1: Simular la entrada del usuario para 'y' y verificar que la función retorna True.
    # Test Case 2: Simular la entrada del usuario para 'n' y verificar que la función retorna False.
    while True:
        decision = input("Pon 'y' para obtener otra carta, escribe 'n' para pasar: ")
        if decision.lower() in ['y', 'n']:
            return decision == 'y'
        else:
            print("Entrada no válida. Por favor, escribe 'y' para otra carta o 'n' para pasar.")

def jugar_blackjack(historial, resultados, apuesta):
    """Inicia una partida de blackjack, maneja las acciones del jugador y del dealer, y registra los resultados."""
    # Test Case 1: Jugador gana una mano con 21 exacto y apuesta de $100, verificar que los resultados muestren una ganancia de $100.
    # Test Case 2: Jugador pierde inmediatamente después de que el dealer obtiene un blackjack natural, verificar que los resultados reflejen una pérdida de la apuesta completa.
    carta_jugador = [carta_de_la_casa(), carta_de_la_casa()]
    dealer_hand = [carta_de_la_casa(), carta_de_la_casa()]
    mostrar_mano(carta_jugador)
    mostrar_mano(dealer_hand, es_dealer=True)

    while tomar_decision():
        carta_jugador.append(carta_de_la_casa())
        mostrar_mano(carta_jugador)
        if puntaje_mano(carta_jugador) > 21:
            print("Te pasaste. Perdiste :(")
            resultados['perdidas'] += apuesta
            historial.append([carta_jugador, dealer_hand, -apuesta])
            return

    while puntaje_mano(dealer_hand) < 17:
        dealer_hand.append(carta_de_la_casa())

    print(f"Mano final del dealer: {dealer_hand}, Puntaje final: {puntaje_mano(dealer_hand)}")
    jugador_score = puntaje_mano(carta_jugador)
    dealer_score = puntaje_mano(dealer_hand)

    if dealer_score > 21 or jugador_score > dealer_score:
        print("Ganaste :)")
        resultados['victorias'] += apuesta
    elif jugador_score == dealer_score:
        print("Es un empate!")
        resultados['empates'] += 0  # No se añade ni se resta nada en empates.
    else:
        print("Perdiste :(")
        resultados['perdidas'] += apuesta
    historial.append([carta_jugador, dealer_hand, apuesta if jugador_score > dealer_score else -apuesta])

def mostrar_balance(resultados):
    """Muestra el balance actual de ganancias y pérdidas."""
    # Test Case 1: Después de perder una apuesta de $100, verificar que al seleccionar la opción de balance en el menú, el balance muestre -$100.
    # Test Case 2: Después de ganar una apuesta de $100 y luego perder $50, verificar que el balance muestre $50 positivos al elegir la opción de balance.
    total_ganado = resultados['victorias'] - resultados['perdidas']
    print(f"Balance actual de ganancias y pérdidas: ${total_ganado}")

def mostrar_resumen_partida(historial):
    """Muestra el historial de todas las manos jugadas durante la sesión de juego."""
    # Test Case 1: Después de una partida donde el jugador gana y otra donde pierde, verificar que el historial muestre ambos resultados correctamente al elegir ver el resumen de la partida.
    # Test Case 2: Verificar que el resumen de partida muestre correctamente el historial en una sesión sin partidas jugadas al comenzar.
    print("Historial de manos:")
    for juego in historial:
        print(f"Jugador: {juego[0]}, Dealer: {juego[1]}, Apuesta: {juego[2]}")

def mostrar_menu(paquetes):
    """Muestra el menú de opciones al usuario y permite la selección de diferentes funciones como jugar, ver balance o resumen."""
    # Test Case 1: El jugador elige ver el balance después de una serie de partidas donde ha perdido más de lo que ha ganado, verificar que el menú muestra un balance negativo.
    # Test Case 2: El jugador elige ver el resumen de la partida después de jugar varias partidas, verificar que el menú muestra todas las partidas jugadas con los resultados y apuestas correspondientes.
    print("\nMENÚ DE APUESTAS")
    print("1. Selecciona un paquete de apuestas para jugar blackjack")
    print("2. Ver balance de ganancias y pérdidas")
    print("3. Ver resumen de partida")
    print("4. Salir")
    opcion = int(input("Escribe tu opción: "))
    return opcion

def leer_paquetes(nombre_archivo):
    """Lee los paquetes de apuestas desde un archivo y los carga en un diccionario."""
    # Test Case 1: Verificar que la función pueda leer correctamente un archivo bien formateado y cargar los paquetes de apuestas.
    # Test Case 2: Verificar cómo la función maneja un archivo mal formateado o inaccesible, asegurando que no cause una falla irrecuperable.
    paquetes = {}
    with open(nombre_archivo, 'r') as archivo:
        next(archivo)  # Opcional: saltar la primera línea si tiene un encabezado
        for linea in archivo:
            nombre_paquete, precio = linea.strip().split('$')
            paquetes[nombre_paquete.strip()] = float(precio)
    return paquetes

def seleccionar_apuesta(paquetes):
    """Permite al usuario seleccionar un paquete de apuestas y devuelve el valor de la apuesta."""
    # Test Case 1: Seleccionar una apuesta estándar como "Bet1" y comenzar una partida, verificar que se deduzca correctamente del balance del jugador.
    # Test Case 2: Intentar seleccionar una apuesta que supera el saldo disponible del jugador, verificar que se le notifique y se le pida que elija una apuesta menor.
    listar_apuestas_con_precio(paquetes)
    apuesta_seleccionada = input("Escribe qué apuesta quieres hacer: ")
    if apuesta_seleccionada in paquetes:
        print(f"Has seleccionado la apuesta {apuesta_seleccionada} con un valor de ${paquetes[apuesta_seleccionada]} para jugar al blackjack.")
        return paquetes[apuesta_seleccionada]
    else:
        print("La apuesta seleccionada no existe, por favor elige una de la lista.")
        return seleccionar_apuesta(paquetes)

def listar_apuestas_con_precio(paquetes):
    """Lista todos los paquetes de apuestas disponibles con sus respectivos precios."""
    # Test Case 1: Probar con un diccionario de apuestas y precios típicos y verificar que la lista de salida sea correcta y completa.
    # Test Case 2: Probar con un diccionario vacío para ver cómo maneja la ausencia de datos sin arrojar errores.
    for paquete, precio in paquetes.items():
        print(f"{paquete}: ${precio}")

def main():
    """Punto de entrada principal del programa. Gestiona la secuencia del juego."""
    nombre_archivo = "Paquetes_de_apuestas.txt"
    paquetes = leer_paquetes(nombre_archivo)
    resultados = {'victorias': 0, 'perdidas': 0, 'empates': 0}
    historial = []

    while True:
        opcion = mostrar_menu(paquetes)
        if opcion == 1:
            apuesta = seleccionar_apuesta(paquetes)
            jugar_blackjack(historial, resultados, apuesta)
        elif opcion == 2:
            mostrar_balance(resultados)
        elif opcion == 3:
            mostrar_resumen_partida(historial)
        elif opcion == 4:
            break
        else:
            print("Opción no válida. Intente de nuevo.")

    print("Resumen de la sesión:")
    print(f"Victorias: {resultados['victorias']}, Perdidas: {resultados['perdidas']}, Empates: {resultados['empates']}")

main()
