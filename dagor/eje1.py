from dagor import JuegoD10, JugadorCaballosBailadoresInteractivo, JugadorD10Estrategico 

jugador1 = JugadorD10Interactivo('Humano') 
jugador2 = JugadorD10Estrategico('Máquina') 
juego = JuegoD10(jugador1, jugador2) 
juego.inicia() 