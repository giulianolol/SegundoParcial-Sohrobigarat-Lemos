import pygame, sys, csv, random, json, datetime, time

from clases import *
from consts import *

def eliminar_pregunta(preguntas:list, pregunta):
    
    for i in range(len(preguntas)):
        
        if preguntas[i]["pregunta"] == pregunta:
            
            preguntas.pop(i)
            
            break
                         
def seleccionar_pregunta(preguntas:list): 
    
    pregunta = preguntas[0]["pregunta"]
    
    respuesta_a = preguntas[0]["respuesta_a"]
    
    respuesta_b = preguntas[0]["respuesta_b"]
    
    respuesta_c = preguntas[0]["respuesta_c"]
    
    respuesta_correcta = preguntas[0]["respuesta_correcta"]
    
    return (pregunta, respuesta_a, respuesta_b, respuesta_c, respuesta_correcta )

def obtener_fuente(tamaño):
    
    return pygame.font.Font("Assets/font.ttf", tamaño)

def jugar(screen, preguntas, vidas, puntaje_usuario):
    
    tiempo_inicial = time.time()
    
    preguntas_y_resuestas = seleccionar_pregunta(preguntas)
    
    pregunta = preguntas_y_resuestas[0]
    
    respuesta_a = preguntas_y_resuestas[1]
    
    respuesta_b = preguntas_y_resuestas[2]
    
    respuesta_c = preguntas_y_resuestas[3]
    
    respuesta_correcta = preguntas_y_resuestas[4]
    
    cant_puntaje = puntaje_usuario
    
    tiempo_inicial = time.time()
    
    duracion_temporizador = 10
    
    tiempo_final = tiempo_inicial + duracion_temporizador
    
    while vidas >= 1:
        
        if time.time() > tiempo_final:
            
            vidas -= 1
            
            tiempo_final = tiempo_inicial + duracion_temporizador
            
            eliminar_pregunta(preguntas, pregunta)
            
            jugar(screen, preguntas, vidas, puntaje_usuario)
            
        if vidas >= 1:
        
            mouse_posicion_jugar = pygame.mouse.get_pos()
            
            screen.fill(NEGRO)
            
            screen.blit(fondo_pantalla_preguntas, (0,0))
            
            txt_vidas = obtener_fuente(30).render(f"VIDAS: {vidas}", True, BLANCO)
            
            screen.blit(txt_vidas, (20, 910) )
            
            txt_pregunta = obtener_fuente(20).render(pregunta, True, BLANCO)
        
            txt_width = txt_pregunta.get_size()
            
            txt_x = (SCREEN_RES[0] - txt_width[0]) // 2
            
            if txt_width[0] > SCREEN_RES[0]:
                
                txt_x = 0  

            screen.blit(txt_pregunta, (txt_x, 35))
            
            btn_opcion_a = Boton(imagen = None, pos = (720,270), text_input= respuesta_a, fuente = obtener_fuente(45), color_base = LIGTH_RED, color_hover = LIGTH_GREEN)
            
            btn_opcion_b = Boton(imagen = None, pos = (720,500), text_input= respuesta_b, fuente = obtener_fuente(45), color_base = LIGTH_RED, color_hover = LIGTH_GREEN)
            
            btn_opcion_c = Boton(imagen = None, pos = (720,730), text_input= respuesta_c, fuente = obtener_fuente(45), color_base = LIGTH_RED, color_hover = LIGTH_GREEN)
          
            btn_jugar_back = Boton(imagen = None, pos = (1415,920), text_input= "VOLVER", fuente = obtener_fuente(25), color_base = BLANCO, color_hover = GREEN)
            
            btn_opcion_a.cambiar_color(mouse_posicion_jugar)
            btn_opcion_a.actualizar(screen)
            
            btn_opcion_b.cambiar_color(mouse_posicion_jugar)
            btn_opcion_b.actualizar(screen)
            
            btn_opcion_c.cambiar_color(mouse_posicion_jugar)
            btn_opcion_c.actualizar(screen)
            
            btn_jugar_back.cambiar_color(mouse_posicion_jugar)
            btn_jugar_back.actualizar(screen)
            
            
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    
                    pygame.quit()
                    
                    sys.exit()
                        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if event.type == pygame.MOUSEBUTTONDOWN and (btn_opcion_a.text_rect.collidepoint(mouse_posicion_jugar) or btn_opcion_b.text_rect.collidepoint(mouse_posicion_jugar) or btn_opcion_c.text_rect.collidepoint(mouse_posicion_jugar)):
                        
                            if btn_opcion_a.checkear_input(mouse_posicion_jugar):
                                
                                letra_respuesta = "a"
                                
                                if letra_respuesta == respuesta_correcta:
                                    
                                    cant_puntaje += 10
                                    
                                    modificar_dato_pregunta(pregunta, 'cantidad_veces_preguntada')
                                                                      
                                    modificar_dato_pregunta(pregunta, 'cantidad_aciertos')
                                    
                                    calcular_y_modificar_porcentaje_aciertos(pregunta)
                                              
                                    eliminar_pregunta(preguntas, pregunta)
                                    
                                    if len(preguntas) != 0:
                                    
                                        jugar(screen,preguntas, vidas, cant_puntaje)
                                    
                                    else:
                                        
                                        sonido_juego.stop()
                                        
                                        pedir_nombre(screen, cant_puntaje)
                                
                                else:
                                    
                                    sonido_error.play()
                                    sonido_error.set_volume(0.5)
                                    
                                    vidas -= 1
                                    
                                    modificar_dato_pregunta(pregunta, 'cantidad_veces_preguntada')
                                    
                                    modificar_dato_pregunta(pregunta,'cantidad_fallos')
                                    
                                    calcular_y_modificar_porcentaje_aciertos(pregunta)
                            
                            elif btn_opcion_b.checkear_input(mouse_posicion_jugar):
                                
                                letra_respuesta = "b"
                                
                                if letra_respuesta == respuesta_correcta:
                                    
                                    cant_puntaje += 10
                                    
                                    modificar_dato_pregunta(pregunta, 'cantidad_veces_preguntada')
                                    
                                    modificar_dato_pregunta(pregunta, 'cantidad_aciertos')
                                    
                                    calcular_y_modificar_porcentaje_aciertos(pregunta)
                                    
                                    eliminar_pregunta(preguntas, pregunta)
                                    
                                    if len(preguntas) != 0:
                                    
                                        jugar(screen,preguntas, vidas, cant_puntaje)
                                    
                                    else:
                                        
                                        sonido_juego.stop()
                                        
                                        pedir_nombre(screen, cant_puntaje)
                                       
                                else:
                                    
                                    vidas -= 1
                                    
                                    sonido_error.play()
                                    sonido_error.set_volume(0.5)
                                    
                                    modificar_dato_pregunta(pregunta, 'cantidad_veces_preguntada')
                                    
                                    modificar_dato_pregunta(pregunta,'cantidad_fallos')
                                    
                                    calcular_y_modificar_porcentaje_aciertos(pregunta)
                                    
                            elif btn_opcion_c.checkear_input(mouse_posicion_jugar):
                                
                                letra_respuesta = "c"
                                
                                if letra_respuesta == respuesta_correcta:
                                    
                                    cant_puntaje += 10
                                    
                                    modificar_dato_pregunta(pregunta, 'cantidad_veces_preguntada')
                                    
                                    modificar_dato_pregunta(pregunta, 'cantidad_aciertos')
                                    
                                    calcular_y_modificar_porcentaje_aciertos(pregunta)
                                    
                                    eliminar_pregunta(preguntas, pregunta)
                                    
                                    if len(preguntas) != 0:
                                    
                                        jugar(screen,preguntas, vidas, cant_puntaje)
                                    
                                    else:
                                        
                                        sonido_juego.stop()
                                        
                                        pedir_nombre(screen, cant_puntaje)                      
                            
                                else:
                                
                                    vidas -= 1
                                    
                                    sonido_error.play()
                                    sonido_error.set_volume(0.5)
                                    
                                    modificar_dato_pregunta(pregunta, 'cantidad_veces_preguntada')
                                    
                                    modificar_dato_pregunta(pregunta,'cantidad_fallos')
                                    
                                    calcular_y_modificar_porcentaje_aciertos(pregunta)
                                    
                    if btn_jugar_back.checkear_input(mouse_posicion_jugar):
                        
                        sonido_juego.stop()
                        
                        main_menu(screen)  
        
        else:pedir_nombre(screen,cant_puntaje)
        
        tiempo_restante = int(tiempo_final - time.time())
        
        tiempo_restante = str(tiempo_restante)
        
        txt_temporizador = obtener_fuente(30).render(f'Tiempo restante: {tiempo_restante}', True, BLANCO)
        
        rect_temporizador = txt_temporizador.get_rect(center=(285,850))
        
        screen.blit(txt_temporizador, rect_temporizador)
        
        time.sleep(0.01)
        
        tiempo_restante = int(tiempo_restante)
        
        pygame.display.update()

    pedir_nombre(screen, puntaje_usuario)
    
def opciones(screen):
    
    while True:
        
        mouse_posicion_opciones = pygame.mouse.get_pos()
        
        screen.blit(fondo_pantalla_opciones,(0,0))
        
        txt_opciones = obtener_fuente(45).render("PANTALLA DE OPCIONES", True, BLANCO)
        
        rect_opciones = txt_opciones.get_rect(center = (800, 120))
        
        screen.blit(txt_opciones, rect_opciones)

        btn_opciones_back = Boton(imagen = None, pos = (1380, 900), text_input = "VOLVER", fuente = obtener_fuente(35), color_base = LIGTH_RED, color_hover = AZUL)
        
        btn_opciones_activar_desactivar_sonido = Boton(imagen = None, pos = (470, 400), text_input= "Activar/Desactivar volumen", fuente = obtener_fuente(35),color_base = LIGTH_RED, color_hover = AZUL)

        btn_opciones_subir_volumen = Boton(imagen = None, pos = (240,600), text_input = "Subir volumen", fuente = obtener_fuente(35), color_base = LIGTH_RED,color_hover = AZUL)

        btn_opciones_bajar_volumen = Boton(imagen = None, pos = (240,800), text_input = "Bajar volumen", fuente = obtener_fuente(35),color_base = LIGTH_RED, color_hover = AZUL)
        
        
        lista_botones = [btn_opciones_activar_desactivar_sonido,btn_opciones_subir_volumen,btn_opciones_bajar_volumen,
                        btn_opciones_back]
        
        for boton in lista_botones:
            
            boton.cambiar_color(mouse_posicion_opciones)
            
            boton.actualizar(screen)
            
        
        for event in pygame.event.get():
            
            if(event.type == pygame.MOUSEBUTTONDOWN):
                if(btn_opciones_activar_desactivar_sonido.checkear_input(mouse_posicion_opciones)):
                    if(evaluar_sonido_json("datos.json") == "0"):
                        sonido_ambiente.play()
                        print("ACTIVE/DESACTIVE VOLUMEN")
                        volumen_actual = leer_json("datos.json")
                        sonido_ambiente.set_volume(volumen_actual["sonido"][1]["nivel_volumen"])
                        escribir_json_sonido(False)

                    else:
                        sonido_ambiente.stop()
                        escribir_json_sonido(True)
                    
                if(btn_opciones_subir_volumen.checkear_input(mouse_posicion_opciones)):
                    
                    if(evaluar_sonido_json("datos.json") == "1"):
                        
                        volumen_actual = leer_json("datos.json")
                        
                        sonido_ambiente.set_volume(volumen_actual["sonido"][1]["nivel_volumen"])

                        if(volumen_actual["sonido"][1]["nivel_volumen"] < 1.0):

                            modificar_sonido(True)
                            
                        else:

                            print("NO SE PUEDE SEGUIR SUBIENDO EL VOLUMEN")

                if(btn_opciones_bajar_volumen.checkear_input(mouse_posicion_opciones)):
                    
                    if(evaluar_sonido_json("datos.json") == "1"):
                        
                        volumen_actual = leer_json("datos.json")
                        
                        sonido_ambiente.set_volume(volumen_actual["sonido"][1]["nivel_volumen"])

                        if(volumen_actual["sonido"][1]["nivel_volumen"] > 0.1):

                            modificar_sonido(False)
                        else:

                            print("NO SE PUEDE SEGUIR BAJANDO EL VOLUMEN")
                            
            
            print(mouse_posicion_opciones)
            
            if event.type == pygame.QUIT:
                
                pygame.quit()
                
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if btn_opciones_back.checkear_input(mouse_posicion_opciones):
                    
                    print(mouse_posicion_opciones)
                    
                    main_menu(screen)
    
        pygame.display.update()
       
def main_menu(screen):

    pygame.display.set_caption("Menu")
    
    puntaje_usuario = Puntaje(0)
                    
    puntaje_usuario.set_puntaje(0)
    
    while main_menu:
        
        screen.blit(background,(0,0))
        
        posicion_mouse = pygame.mouse.get_pos()
        
        txt_menu = obtener_fuente(70).render("MENU", True, GREEN)
        rect_menu = txt_menu.get_rect(center=(750,100))
        
        btn_jugar = Boton(imagen=pygame.image.load("Assets/rect_difuminado.png"), pos=(750,250), text_input="JUGAR", fuente = obtener_fuente(85), color_base= LIGTH_GREEN, color_hover= BLANCO)
        
        btn_top_10 = Boton(imagen=pygame.image.load("Assets/rect_difuminado.png"), pos=(750,450), text_input="TOP 10", fuente = obtener_fuente(85), color_base= LIGTH_GREEN, color_hover= BLANCO)
        
        btn_opciones = Boton(imagen=pygame.image.load("Assets/rect_difuminado.png"), pos=(750,645), text_input="OPCIONES", fuente = obtener_fuente(65), color_base= LIGTH_GREEN, color_hover= BLANCO)
        
        btn_salir = Boton(imagen=pygame.image.load("Assets/rect_difuminado.png"), pos=(750,820), text_input="SALIR", fuente = obtener_fuente(85), color_base= LIGTH_GREEN, color_hover= BLANCO)
        
        lista_botones = [btn_jugar, btn_opciones, btn_salir, btn_top_10]
        
        screen.blit(txt_menu, rect_menu)
        
        for boton in lista_botones:
            
            boton.cambiar_color(posicion_mouse)
            
            boton.actualizar(screen)
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                
                pygame.quit()
                
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if btn_jugar.checkear_input(posicion_mouse):
                    
                    sonido_ambiente.stop()
                    
                    sonido_juego.play(-1)
                    
                    sonido_juego.set_volume(0.1)
                    
                    csv_leido = leer_csv("preguntas.csv")
                    
                    random.shuffle(csv_leido)
                    
                    jugar(screen,csv_leido, 3, 0)

                if btn_opciones.checkear_input(posicion_mouse):
                     
                    opciones(screen)
                
                if btn_top_10.checkear_input(posicion_mouse):
                    
                    top_10(screen)
                    
                if btn_salir.checkear_input(posicion_mouse):
                    
                    pygame.quit()
                    
                    sys.exit()
        
        pygame.display.update()
    
    main_menu(screen)   

def top_10(screen):
    
    x, y = 50 , 50
    
    alutra_linea = 20 + 30
    
    contador = 0
    
    json_ordenado = ordenar_json('datos.json', 'jugador', 'puntaje')
    
    top_10_json_ordenado = json_ordenado[:10]
    
    print(top_10_json_ordenado)
    
    while True:
        
        screen.blit(background_top_10, (0,0))
        
        btn_volver = Boton(imagen=None, pos=(1380,900), text_input="Volver", fuente = obtener_fuente(35), color_base = BLANCO, color_hover= LIGTH_RED)
        
        posicion_mouse = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                
                pygame.quit()
                
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if btn_volver.checkear_input(posicion_mouse):
                    
                    print("ACAAASDASDA")
                    
                    main_menu(screen)
        
        txt_title = obtener_fuente(70).render("TOP 10", True, BLANCO)
        rect_txt = txt_title.get_rect(center=(750,y))
        
        y_actual = y
        
        for i in top_10_json_ordenado:
            
            txt_jugador = obtener_fuente(20).render(f" Top:{(top_10_json_ordenado.index(i) + 1)} Nombre: {i['nombre']} - Puntaje: {i['puntaje']} - Fecha: {i['fecha']}", True, NEGRO)
            
            screen.blit(txt_jugador, (x,y_actual))
            
            y_actual += alutra_linea

        btn_volver.cambiar_color(posicion_mouse)
        btn_volver.actualizar(screen)
        pygame.display.update()

def leer_csv(ruta_archivo):
    
    datos = []
    
    with open(ruta_archivo, mode='r', newline='', encoding ='UTF-8') as archivo_csv:
        
        lector_csv = csv.DictReader(archivo_csv)
        
        for fila in lector_csv:
            
            datos.append(dict(fila))
    
    return datos

    
def agregar_pregunta(screen):
    
    letra = "Hola :)"
    txt_letra = obtener_fuente(75).render(letra, True, BLANCO)
    while True:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                
                pygame.quit()
                
                sys.exit()
        
        superficie_texto = obtener_fuente(35).render(letra,True,(255,255,255))
                
            
        screen.blit(superficie_texto,screen(0,0))
        pygame.display.update()

def pedir_nombre(screen, puntaje):
     
    sonido_juego.stop()
    
    datos = leer_json('datos.json')
    
    if (datos['sonido'][0]['estado_reproduccion'] == "1"):
        
        sonido_ambiente.play()
    
      
    fecha_actual = datetime.datetime.today()
    fecha_actual = fecha_actual.strftime("%d/%m/%Y") 
    letra = ""
    txt_letra = obtener_fuente(75).render(letra, True, BLANCO)
    x = 140
    rect_letra = txt_letra.get_rect(center=(x,250))
    while True:
        
        posicion_mouse = pygame.mouse.get_pos()
        screen.blit(difuminado,(0,0))
        
        txt_input = obtener_fuente(70).render("INGRESE SU NOMBRE", True, NEGRO)
        rect_txt = txt_input.get_rect(center=(750,100))
        
        txt_aviso = obtener_fuente(20).render("HASTA 12 CARACTERES", True, NEGRO)
        rect_aviso = txt_aviso.get_rect(center=(750,150))

        screen.blit(txt_aviso, rect_aviso)
        screen.blit(txt_input, rect_txt)
        
        btn_guardar = Boton(imagen=pygame.image.load("Assets/rect_difuminado.png"), pos=(750,800), text_input="GUARDAR", fuente = obtener_fuente(55), color_base = BLANCO, color_hover= LIGTH_RED)
        
        btn_guardar.cambiar_color(posicion_mouse)
        btn_guardar.actualizar(screen)
        
        for event in pygame.event.get():
            
            if event.type == pygame.KEYDOWN:
                
                print(event.key)
                         
            if event.type == pygame.MOUSEBUTTONDOWN:
                    
                if btn_guardar.checkear_input(posicion_mouse):
                    
                    escribir_json(letra, puntaje, fecha_actual)
                    
                    main_menu(screen)
                
            if event.type == pygame.KEYDOWN:
                
                if len(letra) <12:
                    
                    letra += event.unicode
                        
                    txt_letra = obtener_fuente(75).render(letra, True, BLANCO)
                        
                    rect_letra = txt_letra.get_rect(center=(750,250))
                    
                if event.key ==pygame.K_BACKSPACE:
                    
                    letra = letra[:-1]
            
            if event.type == pygame.KEYDOWN and event.key == 8:
                
                letra = letra[:-1]

                txt_letra = obtener_fuente(75).render(letra, True, BLANCO)
                        
                rect_letra = txt_letra.get_rect(center=(750,250))
            
            if event.type == pygame.KEYDOWN and event.key == 32:
                
                letra += " "
                
                txt_letra = obtener_fuente(75).render(letra, True, BLANCO)
                        
                rect_letra = txt_letra.get_rect(center=(750,250))
                
            
        screen.blit(txt_letra, rect_letra)
        pygame.display.update()

def leer_json(ruta_json):
    
    archivo_json = open(ruta_json, 'r')
    
    datos = json.load(archivo_json)
    
    archivo_json.close()
    
    return datos

def escribir_json(letra, puntaje, fecha_actual):
    
    datos = leer_json('datos.json')
    
    ultimos_datos = {'nombre': letra, 'puntaje': puntaje, 'fecha':fecha_actual}
    
    datos["jugador"].append(ultimos_datos)
                    
    with open("datos.json", "w") as file:
                        
        json.dump(datos, file, indent=4)
    
    file.close()

def ordenar_json(ruta_json, clave_json, clave_orden):
    
    archivo_json = leer_json(ruta_json)
    
    jugadores_ordenados = sorted(archivo_json[clave_json], key=lambda x: x[clave_orden], reverse=True)
                
    return jugadores_ordenados

def contador(valor_inicial):
    
    tiempo_inicial = valor_inicial
    
    duracion_temporizador = 10
    
    tiempo_final = tiempo_inicial + duracion_temporizador
    
    while valor_inicial <= tiempo_final:
        
        tiempo_restante = int(tiempo_final - valor_inicial)
        
        print(tiempo_restante)
    
        time.sleep(1)
        
def cargar_csv_lista(ruta):
    
    with open(ruta, mode='r', newline='', encoding='utf8') as archivo:
        
        lector = csv.DictReader(archivo)
        
        return list(lector)

def modificar_dato_pregunta(pregunta, clave):
    
    lista_archivo = cargar_csv_lista('preguntas.csv')
    
    for i in lista_archivo:
        
        if i['pregunta'] == pregunta:
            
            i[clave] = int(i[clave])
                
            i[clave] += 1
                
            i[clave] = str(i[clave])

    with open('preguntas.csv', mode='w', newline='', encoding='utf-8') as archivo:
        
        escritor = csv.DictWriter(archivo, fieldnames=lista_archivo[0].keys())
        escritor.writeheader()
        escritor.writerows(lista_archivo)


def calcular_y_modificar_porcentaje_aciertos(pregunta):
    
    lista_archivo = cargar_csv_lista('preguntas.csv')

    for i in lista_archivo:
        
        if i ['pregunta'] == pregunta:
            
            cantidad_aciertos = int(i['cantidad_aciertos'])
        
            cantidad_veces_preguntadas = int(i['cantidad_veces_preguntada'])
                 
            cantidad_fallos = int(i['cantidad_fallos'])
            
            porcentaje_fallos = int((cantidad_fallos/ cantidad_veces_preguntadas) * 100)
            
            if cantidad_veces_preguntadas >= 2:
                
                i['porcentaje_aciertos'] = int((cantidad_aciertos / cantidad_veces_preguntadas) * 100)
            
            elif  int((cantidad_aciertos / cantidad_veces_preguntadas) * 100) != 0:
            
                i['porcentaje_aciertos'] =  int((cantidad_aciertos / cantidad_veces_preguntadas) * 100)  - porcentaje_fallos
                              
    with open('preguntas.csv', mode='w', newline='', encoding='utf-8') as archivo:
        
        escritor = csv.DictWriter(archivo, fieldnames=lista_archivo[0].keys())
        escritor.writeheader()
        escritor.writerows(lista_archivo)

def reproducir_musica_ambiente():

    escribir_json_sonido(False)
    sonido_ambiente.play()

    volumen_actual = leer_json("datos.json")
    sonido_ambiente.set_volume(volumen_actual["sonido"][1]["nivel_volumen"])
    
def evaluar_sonido_json(ruta_json):

    datos = leer_json(ruta_json)

    estado_sonido = datos["sonido"][0]["estado_reproduccion"]

    return estado_sonido


def escribir_json_sonido(valor_antiguo):

    datos = leer_json('datos.json')

    if(valor_antiguo == True):

        datos["sonido"][0]["estado_reproduccion"] = "0"
    else:

        datos["sonido"][0]["estado_reproduccion"] = "1"

    with open("datos.json", "w") as file:

        json.dump(datos, file, indent=4)

    file.close()

def modificar_sonido(valor):
    datos = leer_json("datos.json")

    if(valor == True):
        datos["sonido"][1]["nivel_volumen"] += 0.1

    elif(valor == False and datos["sonido"][1]["nivel_volumen"] != 0.10000000000000003):

        datos["sonido"][1]["nivel_volumen"] -= 0.1

    with open("datos.json","w+") as archivo:

        json.dump(datos,archivo,indent=4)