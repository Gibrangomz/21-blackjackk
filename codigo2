"""Codigo 2 14 de marzo"""
import random

def carta_de_la_casa():
    # Esta función elige una carta aleatoriamente de la baraja estándar de blackjack.
    cartas = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  # Baraja de blackjack
    return random.choice(cartas)

def puntaje_mano(mano):
    # Calcula el puntaje de una mano de cartas, teniendo en cuenta la regla del as (11 o 1).
    score = sum(mano)
    ace_count = mano.count(11)  # Cuenta cuántos ases hay en la mano
    while score > 21 and ace_count > 0:  # Convierte los ases de 11 a 1 si el puntaje es mayor a 21
        score -= 10
        ace_count -= 1
    return score

def mostrar_mano(mano, es_dealer=False):
    # Muestra las cartas de la mano del jugador o la primera carta del dealer.
    if es_dealer:
        print(f"Primera carta del dealer: {mano[0]}")  # Muestra solo la primera carta del dealer
    else:
        print(f"Tus Cartas: {mano}, Puntaje actual: {puntaje_mano(mano)}")  # Muestra las cartas y el puntaje del jugador

def tomar_decision():
    # Permite al jugador decidir si desea otra carta o si pasa.
    return input("Pon 'y' para obtener otra carta, escribe 'n' para pasar: ") == 'y'

def jugar_blackjack():
    # Lógica principal del juego de blackjack.
    def jugar_blackjack():
    # Se crean dos manos iniciales, una para el jugador y otra para el dealer, cada una con dos cartas.
    carta_jugador = [carta_de_la_casa(), carta_de_la_casa()]
    dealer_hand = [carta_de_la_casa(), carta_de_la_casa()]
    
    # Muestra las cartas del jugador y la primera carta del dealer (ocultando la segunda).
    mostrar_mano(carta_jugador)
    mostrar_mano(dealer_hand, es_dealer=True)
    
    # Bucle que permite al jugador tomar cartas adicionales mientras decida hacerlo.
    while tomar_decision():
        carta_jugador.append(carta_de_la_casa())  # Añade una nueva carta a la mano del jugador.
        mostrar_mano(carta_jugador)  # Muestra la mano actualizada del jugador.
        if puntaje_mano(carta_jugador) > 21:
            print("Te pasaste. Perdiste :(")  # Si se pasa de 21, el jugador pierde automáticamente.
            return False  # Termina la función indicando que el juego ha terminado.
    
    # Bucle que permite al dealer tomar cartas si su puntaje es menor a 17.
    while puntaje_mano(dealer_hand) < 17:
        dealer_hand.append(carta_de_la_casa())  # Añade una nueva carta a la mano del dealer.
    
    # Muestra la mano final del dealer y su puntaje.
    print(f"Ultimo hand del dealer: {dealer_hand}, Puntaje final: {puntaje_mano(dealer_hand)}")
    
    # Determina el resultado del juego comparando los puntajes del jugador y del dealer.
    if puntaje_mano(dealer_hand) > 21 or puntaje_mano(carta_jugador) > puntaje_mano(dealer_hand):
        resultado = "Ganaste :)"  # El jugador gana si el dealer se pasa de 21 o si tiene un puntaje mayor que el dealer.
    elif puntaje_mano(carta_jugador) == puntaje_mano(dealer_hand):
        resultado = "Es un empate!"  # Es un empate si ambos tienen el mismo puntaje.
    else:
        resultado = "Perdiste :("  # El jugador pierde si su puntaje es menor que el del dealer.
    
    # Imprime el resultado del juego.
    print(resultado)
    return True  # Retorna True para indicar que el jugador puede decidir si quiere jugar otra ronda.


def main():
    # Controla el flujo del juego permitiendo múltiples rondas.
    continuar_jugando = True
    while continuar_jugando:
        game_continues = jugar_blackjack()
        if not game_continues or input("Quieres jugar otra vez? (y/n): ").lower() != 'y':
            continuar_jugando = False

main()
