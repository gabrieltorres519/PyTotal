import pygame, math
import random # Para generar números aleatorios, para la posición del enemigo
from pygame import mixer

# Inicializar Pygame
pygame.init()

# Crear la pantalla
pantalla = pygame.display.set_mode((800, 600))

# Titulo e icono
pygame.display.set_caption("Invasión Espacial")
icono = pygame.image.load('ovni.png')
pygame.display.set_icon(icono)
fondo = pygame.image.load('Fondo.jpg')

# Agregar musica
mixer.music.load('MusicaFondo.mp3')
mixer.music.set_volume(0.6) # Para bajar el volumen de la música
mixer.music.play(-1) # Para que la música se repita ()

# Jugador
jugadorImg = pygame.image.load('cohete.png')
jugador_x = 368
jugador_y = 500 
jugador_x_cambio = 0


# Enemigos
enemigoImg = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos): # Para generar varios enemigos, se crean listas para cada una de sus características y se llenan con un ciclo for
    enemigoImg.append(pygame.image.load('ovni.png'))
    enemigo_x.append(random.randint(0,736))
    enemigo_y.append(random.randint(50,200))
    enemigo_x_cambio.append(1)
    enemigo_y_cambio.append(50)


# Bala
balaImg = pygame.image.load('bala.png')
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 3
bala_visible = False


#  Puntaje
puntaje = 0
# fuente = pygame.font.Font('freesansbold.ttf', 32)  # Cambiando por la fuente descargada
fuente = pygame.font.Font('freesansbold.ttf',32)
texto_x = 10
texto_y = 10


# Texto final de juego
fuente_final = pygame.font.Font('freesansbold.ttf',40)

def texto_final():
    mi_fuente_final = fuente_final.render("JUEGO TERMINADO", True, (255,255,255))
    pantalla.blit(mi_fuente_final, (60,200)) # Aparecer al centro de la pantalla


# Función mostrar puntaje
def mostrar_puntaje(x,y):
    texto = fuente.render("Puntaje: " + str(puntaje), True, (255,255,255))
    pantalla.blit(texto,(x,y))


# Función jugador
def jugador(x, y):
    pantalla.blit(jugadorImg,(x,y))


# Función enemigo
def enemigo(x, y, ene):
    pantalla.blit(enemigoImg[ene],(x,y))


# Función disparar bala
def disparar_bala(x,y):
    global bala_visible
    bala_visible = True
    pantalla.blit(balaImg,(x + 16,y  + 10))  # Que la bala aparezca en el centro de la nave


# Función detectar colisión
def hay_colision(enemigo_x, enemigo_y, bala_x, bala_y):
    distancia = math.sqrt(math.pow(enemigo_x-bala_x,2)+math.pow(enemigo_y-bala_y,2))
    if distancia < 37: #Basados en el tamaño en pixeles de los enemigos, colisión a esa distancia de su centro
        return True
    else:
        return False 

# Loop del juego
se_ejecuta = True

while True:

    #  RGB
    # pantalla.fill((205,144,228))

    # Ejemplo de movimiento automático aprovechando el ciclo
    # jugador_x+=1
    # jugador_y+=1
    
    # Imagen de fondo
    pantalla.blit(fondo,(0,0))

    # Iterar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        
        # Evento presionar flechas
        if evento.type == pygame.KEYDOWN:
            print('Una tecla fue presionada')
            if evento.key == pygame.K_LEFT:
                print('flecha izquierda presionada')
                jugador_x_cambio = -1
            if evento.key == pygame.K_RIGHT:
                print('flecha derecha presionada')
                jugador_x_cambio = 1
            if evento.key == pygame.K_SPACE:
                print('flecha derecha presionada')
                # Música disparo
                sonido_bala = mixer.Sound('disparo.mp3')
                sonido_bala.set_volume(0.5) # Para bajar el volumen del sonido
                sonido_bala.play()
                # Evitar que se reinicie la posición de la bala cada que se presione el espacio
                if not bala_visible:
                    bala_x = jugador_x # Para que la bala salga de la nave, se le asigna la posición del jugador y ya no lo sigue, sino que se mantiene en esa posición
                disparar_bala(bala_x, bala_y)
        
        # Evento soltar flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or pygame.K_RIGHT:
                print('la flecha fue soltada')
                jugador_x_cambio = 0

    # Modificar ubicación del jugador
    jugador_x+=jugador_x_cambio

    # Modificar ubicación del enemigo
    for e in range(cantidad_enemigos):

        # Finalizar el juego
        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break

        enemigo_x[e] +=enemigo_x_cambio[e]




    # Mantener dentro de bordes al jugador
    if jugador_x <= 0:
        jugador_x = 0 # Detener movimiento del jugador 
    elif jugador_x >= 736:
        jugador_x = 736

    # Mantener dentro de bordes al enemigo
    for e in range(cantidad_enemigos):
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 1
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -1
            enemigo_y[e] += enemigo_y_cambio[e]
            # Colisión
        colision = hay_colision(enemigo_x[e],enemigo_y[e],bala_x,bala_y)
        if colision:
            # Sonido colisión
            sonido_colision = mixer.Sound('Golpe.mp3')
            sonido_colision.set_volume(0.5) # Para bajar el volumen del sonido
            sonido_colision.play()
            bala_y = 500
            bala_visible = False
            puntaje += 1
            # Después de la colisión el enemigo desaparece y generamos uno nuevo en  posición aleatoria de nuevo
            enemigo_x[e] = random.randint(0,736)
            enemigo_y[e] = random.randint(50,200)
        enemigo(enemigo_x[e], enemigo_y[e],e)


    # Movimiento bala
    if bala_y <= -64: # Si la bala sale de la pantalla (tomando su tamaño en pixels), volver a su posición inicial
        bala_y = 500
        bala_visible = False

    if bala_visible:
        disparar_bala(bala_x,bala_y) # La posición en x se arregló para que no siga al jugador
        bala_y -= bala_y_cambio




    jugador(jugador_x, jugador_y)


    # Mostrar puntaje
    mostrar_puntaje(texto_x, texto_y)

    # Actualizar
    pygame.display.update()