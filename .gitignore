"""codigo 3 20 de abril."""
import random

def carta_de_la_casa():
    # explicado en código 2#
    cartas = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(cartas)

def puntaje_mano(mano):
    # explicado en código 2#
    score = sum(mano)
    ace_count = mano.count(11)
    while score > 21 and ace_count > 0:
        score -= 10
        ace_count -= 1
    return score

def mostrar_mano(mano, es_dealer=False):
    # explicado en código 2#
    if es_dealer:
        print(f"Primera carta del dealer: {mano[0]}")
    else:
        print(f"Tus Cartas: {mano}, Puntaje actual: {puntaje_mano(mano)}")

def tomar_decision():
    # Pide al jugador decidir si quiere otra carta o parar, validando que la entrada sea 'y' o 'n'.
    while True:
        decision = input("Pon 'y' para obtener otra carta, escribe 'n' para pasar: ")
        if decision.lower() in ['y', 'n']:
            return decision == 'y'
        else:
            print("Entrada no válida. Por favor, escribe 'y' para otra carta o 'n' para pasar.")

def jugar_blackjack(historial, resultados):
    # Inicia una partida de blackjack, maneja las acciones del jugador y del dealer, y registra los resultados.
    carta_jugador = [carta_de_la_casa(), carta_de_la_casa()]  # Inicializa la mano del jugador con dos cartas.
    dealer_hand = [carta_de_la_casa(), carta_de_la_casa()]  # Inicializa la mano del dealer con dos cartas.
    mostrar_mano(carta_jugador)
    mostrar_mano(dealer_hand, es_dealer=True)

    while tomar_decision():
        carta_jugador.append(carta_de_la_casa())  # Añade una nueva carta a la mano del jugador.
        mostrar_mano(carta_jugador)  # Muestra la mano actualizada del jugador.
        if puntaje_mano(carta_jugador) > 21:
            print("Te pasaste. Perdiste :(")
            resultados['perdidas'] += 1
            historial.append([carta_jugador, dealer_hand])  # Registra la ronda actual en el historial.
            return False  

    while puntaje_mano(dealer_hand) < 17:
        dealer_hand.append(carta_de_la_casa())  # El dealer toma cartas hasta que su puntaje sea al menos 17.

    print(f"Ultimo hand del dealer: {dealer_hand}, Puntaje final: {puntaje_mano(dealer_hand)}")
    jugador_score = puntaje_mano(carta_jugador)  # Calcula el puntaje final del jugador.
    dealer_score = puntaje_mano(dealer_hand)  # Calcula el puntaje final del dealer.

    if dealer_score > 21 or jugador_score > dealer_score:
        resultado = "Ganaste :)"
        resultados['victorias'] += 1
    elif jugador_score == dealer_score:
        resultado = "Es un empate!"
        resultados['empates'] += 1
    else:
        resultado = "Perdiste :("
        resultados['perdidas'] += 1
    historial.append([carta_jugador, dealer_hand])  # Añade el resultado de esta ronda al historial.
    print(resultado)
    return True

def main():
    # Controla el flujo del juego, permitiendo múltiples rondas y mostrando un resumen al final.
    resultados = {'victorias': 0, 'perdidas': 0, 'empates': 0}
    historial = []
    continuar_jugando = True

    while continuar_jugando:
        game_continues = jugar_blackjack(historial, resultados)
        if game_continues:
            respuesta = input("Quieres jugar otra vez? (y/n): ").lower().strip()
            continuar_jugando = (respuesta == 'y')
        else:
            continuar_jugando = False

    print("Resumen de la sesión:")
    print(f"Victorias: {resultados['victorias']}, Perdidas: {resultados['perdidas']}, Empates: {resultados['empates']}")
    print("Historial de manos:")
    for juego in historial:
        print(f"Jugador: {juego[0]}, Dealer: {juego[1]}")

main()
