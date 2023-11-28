#-----------------------------------------------------
#Project: Knight’s Dance
#
#Date: 29-Aug-2023
#Authors:
#           A01798012 Arturo Montes Gonzalez
#           A01747848 Ares Ortiz Botello
#           A01748086 Rosa Itzel Figueroa Rosas
#-----------------------------------------------------

from dagor import JugadorCaballosBailadores

#Definimos una nueva clase para nuestro jugador (se hereda de la clase JugadorCaballosBailadores)
class JugadorCaballosBailadoresEquipo6(JugadorCaballosBailadores):
    
    def comerOponente(self, posicion, jugador_max) -> bool:
        #Si una posicion lleva al gane, se regresa true si el jugador actual es el maximizing player
        #De lo contrario, regresa False
        if self.triunfo(posicion):
            return jugador_max 
        return False
    
    #Funcion que obtiene todas las posiciones siguientes posibles a partir de la posicion dada
    def evitarPerder(self, posicion) -> int:
        #Se iteran sobre las posiciones
        malas_posiciones = 0
        for p in self.posiciones_siguientes(posicion):
            #Se verifica si mover alguna de estas posiciones, el oponente podria comer al jugador actual
            triunfo = self.triunfo(p)
            if triunfo:
                if triunfo != self.simbolo:
                    malas_posiciones += 1
                    return 11 
        #Si ninguna de las posiciones siguientes lleva a que el oponente coma al jugador actual, se regresa False
        #Indicando que no es necesario evitar perder en la posicion actual    
        return 0 

    def amenaza(self, posicion) -> int:
        #Se calculan las posiciones del jugador contrario
        posiciones_contrario = self.posiciones_contrario(posicion)
        posiciones_amenazadas = 0 
        #Se itera sobre cada posicion del jugador contrario
        for p in posiciones_contrario:
            #Se itera sobre cada posicion siguiente a la posicion actual
            for c in self.posiciones_siguientes(posicion):
                #Cuando el jugador contrario se esta moviendo hacia adelante en terminos de coordenadas,
                #entre menores sean nuestras coordenadas (menos espacio para movernos) estamos en mayor riesgo
                if self.simbolo == 'B' and p[0] > c[0] and p[1] > c[1]:
                    return True
                
                #Cuando nos estamos moviendo hacia adelante en terminos de coordenadas, entre menores sean
                #las coordenadas del jugador contrario, nuestro jugador representara una mayor amenaza 
                elif self.simbolo != 'B' and p[0] < c[0] and p[1] < c[1]:
                    return True
        return False

    def posicionesAmenazadas(self, posicion) -> int:
       #Se calculan las posiciones del jugador contrario
#        posiciones_contrario = self.posiciones_contrario(posicion)
        posiciones_contrario = self.posiciones_siguientes(posicion)
        posiciones_amenazadas = 0 
        #Se itera sobre cada posicion del jugador contrario
        for contrario in posiciones_contrario:
            #Se itera sobre cada posicion siguiente a la posicion actual
            for nosotros in self.posiciones_siguientes(contrario):
                if self.triunfo(nosotros) == self.simbolo:
                    posiciones_amenazadas += 1
        
        return posiciones_amenazadas



    def heuristica(self, posicion, jugador_max) -> int:
        #me parece que esta heuristica todavia se puede mejorar aun mas
        #porque ahorita nomas verifica si 
        if  self.triunfo(posicion) == self.simbolo:
            return 100
        
        if not jugador_max:
            return self.evitarPerder(posicion)
        
        if jugador_max:
            return self.posicionesAmenazadas(posicion)

        return 0
        
    
    """Implementacion de minimax profundidad: 
    profundidad maxima a la que se explorara el arbol de busqueda
    jugador_max: bool que indica si es el turno del maximizing player
    alpha y beta: condiciones base para el algoritmo alpha-beta pruning"""
    
    def minimax(self, posicion, profundidad, jugador_max, alpha, beta) -> int:
        """Si la profundidad especificada se alcanza o se encuentra una posicion ganadora
        #Se devuelve el resultado de la evaluacion heuristica para la posicion actual"""
        if profundidad == 0 or self.triunfo(posicion):
            return self.heuristica(posicion, jugador_max)
        
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
    
    
     #Funcion que toma una posicion como argumento y utiliza minimax para tomar una decision sobre el mejor movimiento
    def tira(self, posicion):
        #Se obtienen las posiciones siguientes posibles a partir de la posicion actual
        posibles = self.posiciones_siguientes(posicion)
        mejorMov = None
        maxEval = float('-inf')

        for p in posibles:
            #Se calcula la evaluacion de la posicion p utilizando un minimax con profundidad maxima de 3
            #Indica que es turno del minimizing player
            eval = self.minimax(p, profundidad=4, jugador_max=False, alpha=float('-inf'), beta=float('inf'))
            if eval > maxEval:
                maxEval = eval
                #Se actualiza el mejor movimiento con la posicion actual
                mejorMov = p
        return mejorMov