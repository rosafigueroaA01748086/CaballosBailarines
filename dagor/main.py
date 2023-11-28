#Puse esto aqui porque si lo dejaba en el otro acrhivo no me dejaba correrlo ahhh
#Pero si esta mal, diganme y lo cambio

from dagor import JuegoCaballosBailadores, JugadorCaballosBailadoresAleatorio
from equipo6 import JugadorCaballosBailadoresEquipo6

if __name__ == '__main__':
    juego = JuegoCaballosBailadores(
        JugadorCaballosBailadoresEquipo6('Equipo 6'),
        JugadorCaballosBailadoresAleatorio('Malos'),
        7, 9)
    juego.inicia(veces=100, delta_max=2)