import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes

import webbrowser
import datetime
import wikipedia

# Escuchar nuestro microfono y devolver audio como texto
def transformar_audio_en_texto():
    # Almacenar el reconocedor
    r = sr.Recognizer()

    # Configurar el micrófono
    with sr.Microphone() as origen:
        # Tiempo de espera
        r.pause_threshold = 0.8

        # Informar que comenzó la grabación
        print('Ya puedes hablar')

        # Guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            # Buscar en google lo que haya escuchado
            pedido = r.recognize_google(audio,language="es-ar")

            # Prueba de que pudo ingresar
            print("Dijiste: " + pedido)

            # Devolver pedido
            return pedido
        
        except sr.UnknownValueError:

            print('No entendí lo que dijiste')

            return "Sigo esperando el audio"
        
        except sr.RequestError:

            print('No hay servicio')

            return "Sigo esperando el servicio"
        
        except:
            print('Algo ha salido mal')


# Función para que el asistente pueda ser escuchado
def hablar(mensaje):
    # Opciones de voz/idioma
    id1 = 'roa/es'
    id2 = 'zle/ru'
    # Encender el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice',id1)

    # Pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


# Informar el día de la semana
def pedir_dia():

    # Crear variable con datos de hoy
    dia = datetime.date.today()
    print(dia)

    # Crear una variable para el día de la semana
    dia_semana = dia.weekday()
    print(dia_semana)

    # Diccionario con nombres de días
    calendario = {0: 'Lunes',
                  1: 'Martes',
                  2: 'Miércoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sábado',
                  6: 'Domingo'}

    # Decir el día de la semana
    hablar(f'Hoy es {calendario[dia_semana]}')


# Informar que hora es
def pedir_hora():
    
    # Crear una variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'

    # Decir la hora
    hablar(hora)


# Función saludo inicial
def saludo_inicial():

    # Crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif 6 <= hora.hour < 13:
        momento = 'Buen día'
    else:
        momento = 'Buenas tardes'

    # Decir el saludo
    hablar(f'{momento}, soy Francisco, tu asistente personal. Por favor, dime en qué te puedo ayudar')


# Función central del asistente
def pedir_cosas():

    # Activar saludo inicial
    saludo_inicial()

    # Variable de corte
    comenzar = True

    # Loop central 
    while comenzar:

        # Activar el microfono y guardar pedido en un string
        pedido = transformar_audio_en_texto().lower()


        if 'abrir youtube' in pedido:
            hablar('Con gusto, estoy abriendo youtube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            hablar('Claro, estoy en eso')
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('Buscando eso en wikipedia')
            pedido = pedido.replace('busca en wikipedia','')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1) # Primer párrafo que encuentre en Wikipedia
            hablar('Wikipedia dice lo siguiente:')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('Buscando eso en internet')
            pedido = pedido.replace('busca en internet','')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado')
            continue 
        elif 'reproducir' in pedido:
            hablar('Buena elección, ya voy a reproducirlo:')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {
                'apple':'APPL',
                'amazon':'AMZN',
                'google':'GOOGL'
            }
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'La encontré, el precio es {precio_actual}')
                continue
            except:
                print('Disculpa no he encontrado la información')
                continue

        elif 'adiós' in pedido:
            hablar('De acuerdo, nos vemos cuando vuelvas a activarme')
            break

pedir_cosas()

