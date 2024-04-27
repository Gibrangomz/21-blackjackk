Proyecto Final Blackjack en Python

El código está diseñado para ser modular, con cada parte del juego encapsulada en funciones reutilizables que demuestran distintas subcompetencias 
dentro del desarrollo de software. Este enfoque no solo ayuda a mantener el código organizado, sino que también facilita la comprensión de la lógica
del juego y la estrategia detrás del desarrollo de un programa estructurado y eficiente.

Contexto
"El Blackjack, también conocido como 21, es un juego de cartas donde el objetivo principal es obtener cartas cuyo valor sumado sea lo más cercano posible a 21, sin pasarse.
A través de este proyecto, se pueden aplicarconceptos de probabilidad, toma de decisiones y estructuras de control vistas en el curso, dentro de un contexto de juego interactivo
y divertido."

Este programa corre en terminal con Python 3 y facilita la práctica de estrategias básicas de Blackjack, manejo de entradas/salidas de archivos y control de flujo de un programa.


**Problema**: El juego de Blackjack (21) requiere un sistema que pueda manejar las interacciones y reglas del juego entre un jugador y el dealer (casa),
tomando decisiones basadas en el estado actual del juego y la entrada del usuario, todo dentro de un entorno controlado por la terminal.

Algoritmo del Juego de Blackjack

El algoritmo del juego se estructura en tres fases principales: Inputs, Procedimiento y Outputs.

#### 1. Inputs
   - **Lectura de Paquetes de Apuestas**: El juego comienza leyendo los diferentes paquetes de apuestas desde un archivo de texto, permitiendo al jugador elegir
     cuánto desea apostar.
   - **Selección de Apuesta**: El jugador selecciona uno de los paquetes de apuestas disponibles que determinará el monto de la apuesta para esa ronda.

#### 2. Procedimiento
   - **Reparto de Cartas**: Se reparten dos cartas al jugador y al dealer. 
   - **Mostrar Mano**: Inicialmente se muestra solo la primera carta del dealer y todas las cartas del jugador.
   - **Turno del Jugador**: El jugador decide si desea recibir más cartas ("hit") o plantarse ("stand"). Si el total del jugador supera 21, pierde automáticamente.
   - **Turno del Dealer**: Si el jugador no se pasa, el dealer juega según las reglas fijas, tomando cartas hasta alcanzar un mínimo de 17.
   - **Evaluación del Ganador**: Se compara el total de cartas del jugador con el del dealer para determinar el ganador.

#### 3. Outputs
   - **Resultados del Juego**: Se informa al jugador si ha ganado, perdido o si es un empate.
   - **Actualización del Balance**: Dependiendo del resultado del juego, se actualiza el balance de ganancias y pérdidas del jugador.
   - **Historial de Juego**: Opcionalmente, al final de la sesión de juego, el jugador puede revisar el historial completo de las manos jugadas.

### Estrategias de Implementación

- **Modularidad**: El código está organizado en funciones claramente definidas que manejan aspectos específicos del juego, facilitando su mantenimiento y expansión futura.
- **Control de Errores**: Implementación de validaciones para asegurar que las entradas del usuario son correctas y manejo de errores para la lectura de archivos.
- **Interacción con el Usuario**: A través de la terminal, el programa proporciona una interfaz interactiva que guía al usuario durante el juego.

Este enfoque garantiza que el juego de Blackjack sea justo, transparente y proporciona una experiencia de usuario divertida y aprendiendo del codigo tambien.

Instrucciones de Uso
1. Descargar el archivo `blackjack.py` y tambien Paquetes_de_apuestas.txt, y agregalos a una misma carpeta.
2. Abrir una terminal o CMD o abrir en Thonny y dar boton de play
5. Seguir las instrucciones en pantalla para jugar al Blackjack. El juego ofrece opciones para realizar apuestas basadas en un archivo de paquetes, consultar el balance
   de ganancias/pérdidas y ver el historial de manos jugadas.

Características del Proyecto
- Lectura de Archivos: El programa lee los valores de las apuestas desde un archivo externo, permitiendo una fácil modificación de las apuestas sin necesidad de alterar el código.
- Control de Flujo: El juego utiliza loops y condicionales para manejar el flujo del juego, decisiones del jugador y del dealer.
- Funciones Reutilizables: Cada acción dentro del juego está encapsulada en funciones, lo que permite reutilizar y modificar fácilmente partes del código sin afectar el resto
  del programa.

Buenas Prácticas de Programación
El proyecto sigue los estándares PEP 8 para el estilo de código en Python, lo cual incluye:
- Nombres de funciones y variables descriptivos.
- Uso de comentarios para explicar bloques de código y decisiones de diseño.
- Estructura de código que facilita la lectura y mantenimiento.

