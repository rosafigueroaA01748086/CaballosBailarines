# from dagor import JuegoCaballosBailadores, \
# JugadorCaballosBailadoresAleatorio, JugadorCaballosBailadoresInteractivo, JugadorCaballosBailadores

from dagor import JugadorCaballosBailarines

#Definimos una nueva clase para nuestro jugador (se hereda de la clase JugadorCaballosBailadores)
class JugadorCaballosBailadoresEquipo6(JugadorCaballosBailadores):
    def heuristica(self, posicion):
        
        #Definir heuristica/implementacion alternativa basada en triunfo
        # if self.triunfo(posicion):
        #     return 1 if self.simbolo == 'B' else -1
        # else:
        #     return 0
        
        return self.triunfo(posicion) == self.simbolo
    
    """Implementacion de minimax profundidad: 
    profundidad maxima a la que se ecplorara el arbol de busqueda
    jugador_max: bool que indica si es el turno del maximizing player
    alpha y beta: condiciones base para el algoritmo alpha-beta pruning"""
    def minimax(self, posicion, profundidad, jugador_max, alpha, beta):
        """Si la profundidad especificada se alcanza o se encuentra una posicion ganadora
        #Se devuelve el resultado de la evaluacion heuristica para la posicion actual"""
        if profundidad == 0 or self.triunfo(posicion):
            return self.heuristica(posicion)
        
        #Se obtienen todas las posibles posiciones siguientes a partir de la posicion actual
        posiblesMovs = self.posiciones_siguientes(posicion)
        
        #Se verifica si es el turno del maximizing player
        if jugador_max:
            #Se inicializa maxEval con un valor negativo infinito que se utilizara para realizar
            maxEval = float('-inf')
            for p in posiblesMovs:
                #Llamada recursiva a minimax con el maximizing player cambiado a Falso (turno del otro jugador)
                evaluacion = self.minimax(p, profundidad -1, False, alpha, beta)
                #Se actualiza la variable con el valor máximo entre el actual y la evaluacion obtenida
                maxEval = max(maxEval, evaluacion)
                #Se actualiza alpha con el valor maximo obtenido
                alpha = max(alpha, evaluacion)
                #Si beta es menor o igual que alpha, dejamos de recorrer la rama
                if beta <= alpha:
                    break
            #Mejor evaluacion encontrada para el maximizing player
            return maxEval
        else:
            #Si no es el turno del maximizing player, es turno del minimizing player
            minEval = float('inf')
            #La estructura es la misma al de jugador_max, pero aqui se busca el minimo (para minimizar lo maximizado por el otro jugador)
            for p in posiblesMovs:
                evaluacion = self.minimax(p, profundidad -1, True, alpha, beta)
                minEval = min(minEval, evaluacion)
                beta = min(beta, evaluacion)
                if beta <= alpha:
                    break
            return minEval
    
    
    # '''Función que iba a utilizar para predecir la posición del jugador contrario
    # pero no la acabe, una disculpa'''
    # def amenaza(self, posicion):
    #     posibles = self.posiciones_siguientes(posicion)
    #     if self.simbolo == 'B':
    #         p

    #     for p in posibles:
    #         for c in posibles_contrario:
    #             if p == c:
    #                 return True
    #             else:
    #                 return False

    #Funcion que toma una posicion como argumento y utiliza minimax para tomar una decision sobre el mejor movimiento
    def tira(self, posicion):
        #Se obtienen las posiciones siguientes posibles a partir de la posicion actual
        posibles = self.posiciones_siguientes(posicion)
        mejorMov = None
        maxEval = float('-inf')

        for p in posibles:
            #Se calcula la evaluacion de la posicion p utilizando un minimax con profundidad maxima de 3
            #Indica que es turno del minimizing player
            eval = self.minimax(p, profundidad=3, jugador_max=False, alpha=float('-inf'), beta=float('inf'))
            if eval > maxEval:
                maxEval = eval
                #Se actualiza el mejor movimiento con la posicion actual
                mejorMov = p
        return mejorMov
    
        # for p in posibles:
        #     if self.heuristica(p):
        #         return p
        
        # for p in posibles:
        #     futuro = self.posiciones_siguientes(p)
        #     for pp in futuro:
        #         if self.heuristica(pp):
        #             return p
        
        # for p in posibles:
        #     for c in posibles:
        #         if self.amenaza(c, self._contrario):
        #             return p
        
        # return posibles[0]

# heuristica(self, posicion): Función heurística que puede utilizar un jugador para ranquear la posición enviada como argumento.
# tira(self, posicion): Invocada automáticamente por el objeto controlador del juego para determinar el tiro de este jugador. 
# Debe devolver un tiro válido a partir de la posición enviada como argumento.