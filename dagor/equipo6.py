from dagor import JuegoCaballosBailadores, \
JugadorCaballosBailadoresAleatorio, JugadorCaballosBailadoresInteractivo, JugadorCaballosBailadores



class JugadorCaballosBailadoresEquipo6(JugadorCaballosBailadores):
    def heuristica(self, posicion):
        return self.triunfo(posicion) == self.simbolo
    
    '''Función que iba a utilizar para predecir la posición del jugador contrario
    pero no la acabe, una disculpa'''
    def amenaza(self, posicion):
        posibles = self.posiciones_siguientes(posicion)
        if self.simbolo == 'B':
            p

        for p in posibles:
            for c in posibles_contrario:
                if p == c:
                    return True
                else:
                    return False

    def tira(self, posicion):
        posibles = self.posiciones_siguientes(posicion)

        for p in posibles:
            if self.heuristica(p):
                return p
        
        for p in posibles:
            futuro = self.posiciones_siguientes(p)
            for pp in futuro:
                if self.heuristica(pp):
                    return p
        
        # for p in posibles:
        #     for c in posibles:
        #         if self.amenaza(c, self._contrario):
        #             return p
        
        return posibles[0]

# heuristica(self, posicion): Función heurística que puede utilizar un jugador para ranquear la posición enviada como argumento.
# tira(self, posicion): Invocada automáticamente por el objeto controlador del juego para determinar el tiro de este jugador. 
# Debe devolver un tiro válido a partir de la posición enviada como argumento.


if __name__ == '__main__':
    juego = JuegoCaballosBailadores(
        JugadorCaballosBailadoresEquipo6('Equipo 6'),
        JugadorCaballosBailadoresAleatorio('RandomBoy'),
        5, 8)
    # juego.inicia()
    juego.inicia(veces=100, delta_max=2)

