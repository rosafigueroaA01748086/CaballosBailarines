#Puse esto aqui porque si lo dejaba en el otro acrhivo no me dejaba correrlo ahhh
#Pero si esta mal, diganme y lo cambio

from dagor import JuegoCaballosBailadores, \
    JugadorCaballosBailadoresAleatorio
from equipo6 import JugadorCaballosBailadoresEquipo6

if __name__ == '__main__':
    juego = JuegoCaballosBailadores(
        JugadorCaballosBailadoresAleatorio('Dora la Iteradora'),
        JugadorCaballosBailadoresEquipo6('Bichites'),
        6, 9)
    juego.inicia(veces=1000, delta_max=2)