import pygame, sys, csv, random, json, datetime

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

def jugar(screen, preguntas, vidas:object, puntaje_usuario:object):
    
    preguntas_y_resuestas = seleccionar_pregunta(preguntas)
    
    pregunta = preguntas_y_resuestas[0]
    
    respuesta_a = preguntas_y_resuestas[1]
    
    respuesta_b = preguntas_y_resuestas[2]
    
    respuesta_c = preguntas_y_resuestas[3]
    
    respuesta_correcta = preguntas_y_resuestas[4]

    cant_vidas = vidas.get_vidas()
    
    puntaje_usuario.set_puntaje(0)
    
    puntaje_usuario.get_puntaje()
    
    while True:
        
        if cant_vidas >= 1:
        
            mouse_posicion_jugar = pygame.mouse.get_pos()
            
            screen.fill(BLACK)
            
            screen.blit(fondo_pantalla_preguntas, (0,0))
            
            txt_vidas = obtener_fuente(30).render(f"VIDAS: {cant_vidas}", True, WHITE)
            
            screen.blit(txt_vidas, (600, 900) )
            
            txt_pregunta = obtener_fuente(20).render(pregunta, True, WHITE)
        
            txt_width = txt_pregunta.get_size()
            
            txt_x = (SCREEN_RES[0] - txt_width[0]) // 2
            
            if txt_width[0] > SCREEN_RES[0]:
                
                txt_x = 0  

            screen.blit(txt_pregunta, (txt_x, 35))
            
            btn_opcion_a = Boton(imagen = None, pos = (720,270), text_input= respuesta_a, fuente = obtener_fuente(45), color_base = LIGTH_RED, color_hover = LIGTH_GREEN)
            
            btn_opcion_b = Boton(imagen = None, pos = (720,500), text_input= respuesta_b, fuente = obtener_fuente(45), color_base = LIGTH_RED, color_hover = LIGTH_GREEN)
            
            btn_opcion_c = Boton(imagen = None, pos = (720,730), text_input= respuesta_c, fuente = obtener_fuente(45), color_base = LIGTH_RED, color_hover = LIGTH_GREEN)
          
            btn_jugar_back = Boton(imagen = None, pos = (1415,920), text_input= "VOLVER", fuente = obtener_fuente(25), color_base = WHITE, color_hover = GREEN)
            
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
                                    
                                    cant_vidas = vidas.get_vidas()
                                    
                                    cant_puntaje = puntaje_usuario.set_puntaje(10)
                                    
                                    print(pregunta)
                                    
                                    eliminar_pregunta(preguntas, pregunta)
                                    
                                    if len(preguntas) != 0:
                                    
                                        jugar(screen,preguntas, vidas, puntaje_usuario)
                                    
                                    else:
                                        
                                        pedir_nombre(screen, cant_puntaje)
                                
                                else:
                                    
                                    cant_vidas = vidas.set_vidas(False)
                            
                            elif btn_opcion_b.checkear_input(mouse_posicion_jugar):
                                
                                letra_respuesta = "b"
                                
                                if letra_respuesta == respuesta_correcta:
                                    
                                    cant_vidas = vidas.get_vidas()
                                    
                                    cant_puntaje = puntaje_usuario.set_puntaje(10)
                                    
                                    print(pregunta)
                                    
                                    eliminar_pregunta(preguntas, pregunta)
                                    
                                    if len(preguntas) != 0:
                                    
                                        jugar(screen,preguntas, vidas, puntaje_usuario)
                                    
                                    else:
                                        
                                        pedir_nombre(screen, cant_puntaje)
                                                    
                                else:
                                    
                                    cant_vidas = vidas.set_vidas(False)
                            
                            elif btn_opcion_c.checkear_input(mouse_posicion_jugar):
                                
                                letra_respuesta = "c"
                                
                                if letra_respuesta == respuesta_correcta:
                                
                                    cant_vidas = vidas.get_vidas()
                                    
                                    cant_puntaje = puntaje_usuario.set_puntaje(10)
                                    
                                    print(pregunta)
                                    
                                    eliminar_pregunta(preguntas, pregunta)
                                    
                                    if len(preguntas) != 0:
                                    
                                        jugar(screen,preguntas, vidas, puntaje_usuario)
                                    
                                    else:
                                        
                                        pedir_nombre(screen, cant_puntaje)                      
                            
                                else:
                                
                                    cant_vidas = vidas.set_vidas(False)
                        
                    if btn_jugar_back.checkear_input(mouse_posicion_jugar):
                        
                        main_menu(screen)
        
        else: pedir_nombre(screen,cant_puntaje)
        
        pygame.display.update()

def opciones(screen):
    
    while True:
        
        mouse_posicion_opciones = pygame.mouse.get_pos()
        
        screen.blit(fondo_pantalla_opciones,(0,0))
        
        txt_opciones = obtener_fuente(45).render("PANTALLA DE OPCIONES", True, BLACK)
        
        rect_opciones = txt_opciones.get_rect(center = (600, 260))
        
        screen.blit(txt_opciones, rect_opciones)

        btn_opciones_back = Boton(imagen = None, pos = (600, 460), text_input = "VOLVER", fuente = obtener_fuente(75), color_base = BLACK, color_hover = GREEN)
        
        btn_opciones_back.cambiar_color(mouse_posicion_opciones)
        btn_opciones_back.actualizar(screen)
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                
                pygame.quit()
                
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if btn_opciones_back.checkear_input(mouse_posicion_opciones):
                    
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
        
        btn_jugar = Boton(imagen=pygame.image.load("Assets/rect_difuminado.png"), pos=(750,250), text_input="JUGAR", fuente = obtener_fuente(85), color_base= LIGTH_GREEN, color_hover= WHITE)
        
        btn_top_10 = Boton(imagen=pygame.image.load("Assets/rect_difuminado.png"), pos=(750,450), text_input="TOP 10", fuente = obtener_fuente(85), color_base= LIGTH_GREEN, color_hover= WHITE)
        
        btn_opciones = Boton(imagen=pygame.image.load("Assets/rect_difuminado.png"), pos=(750,645), text_input="OPCIONES", fuente = obtener_fuente(65), color_base= LIGTH_GREEN, color_hover= WHITE)
        
        btn_salir = Boton(imagen=pygame.image.load("Assets/rect_difuminado.png"), pos=(750,820), text_input="SALIR", fuente = obtener_fuente(85), color_base= LIGTH_GREEN, color_hover= WHITE)
        
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
                    
                    vidas = Vidas(3)
                    
                    csv_leido = leer_csv("preguntas.csv")
                    
                    random.shuffle(csv_leido)
                    
                    jugar(screen,csv_leido, vidas, puntaje_usuario)

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
        
        btn_volver = Boton(imagen=None, pos=(1380,900), text_input="Volver", fuente = obtener_fuente(35), color_base = WHITE, color_hover= LIGTH_RED)
        
        posicion_mouse = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                
                pygame.quit()
                
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if btn_volver.checkear_input(posicion_mouse):
                    
                    print("ACAAASDASDA")
                    
                    main_menu(screen)
        
        txt_title = obtener_fuente(70).render("TOP 10", True, WHITE)
        rect_txt = txt_title.get_rect(center=(750,y))
        
        y_actual = y
        
        for i in top_10_json_ordenado:
            
            txt_jugador = obtener_fuente(20).render(f" Top:{(top_10_json_ordenado.index(i) + 1)} Nombre: {i['nombre']} - Puntaje: {i['puntaje']} - Fecha: {i['fecha']}", True, BLACK)
            
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

def pedir_nombre(screen, puntaje):
     
    fecha_actual = datetime.datetime.today()
    fecha_actual = fecha_actual.strftime("%d/%m/%Y") 
    letra = ""
    txt_letra = obtener_fuente(75).render(letra, True, WHITE)
    x = 140
    rect_letra = txt_letra.get_rect(center=(x,250))
    while True:
        
        posicion_mouse = pygame.mouse.get_pos()
        screen.blit(difuminado,(0,0))
        
        txt_input = obtener_fuente(70).render("INGRESE SU NOMBRE", True, BLACK)
        rect_txt = txt_input.get_rect(center=(750,100))
        
        txt_aviso = obtener_fuente(20).render("HASTA 12 CARACTERES", True, BLACK)
        rect_aviso = txt_aviso.get_rect(center=(750,150))

        screen.blit(txt_aviso, rect_aviso)
        screen.blit(txt_input, rect_txt)
        
        btn_guardar = Boton(imagen=pygame.image.load("Assets/rect_difuminado.png"), pos=(750,800), text_input="GUARDAR", fuente = obtener_fuente(55), color_base = WHITE, color_hover= LIGTH_RED)
        
        btn_guardar.cambiar_color(posicion_mouse)
        btn_guardar.actualizar(screen)
        
        for event in pygame.event.get():
            
            if event.type == pygame.KEYDOWN:
                
                print(event.key)
                         
            if event.type == pygame.MOUSEBUTTONDOWN:
                    
                if btn_guardar.checkear_input(posicion_mouse):
                    
                    print("ACA")
                    
                    escribir_json(letra, puntaje, fecha_actual)
                    
                    main_menu(screen)
                
            if event.type == pygame.KEYDOWN:
                
                if len(letra) <12:
                    
                    letra += event.unicode
                        
                    txt_letra = obtener_fuente(75).render(letra, True, WHITE)
                        
                    rect_letra = txt_letra.get_rect(center=(750,250))
            
            if event.type == pygame.KEYDOWN and event.key == 8:
                
                letra = letra[:-1]

                txt_letra = obtener_fuente(75).render(letra, True, WHITE)
                        
                rect_letra = txt_letra.get_rect(center=(750,250))
            
            if event.type == pygame.KEYDOWN and event.key == 32:
                
                letra += " "
                
                txt_letra = obtener_fuente(75).render(letra, True, WHITE)
                        
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
    
    datos.append(ultimos_datos)
                    
    with open("datos.json", "w") as file:
                        
        json.dump(datos, file, indent=4)
    
    file.close()

def ordenar_json(ruta_json, clave_json, clave_orden):
    
    archivo_json = leer_json(ruta_json)
    
    jugadores_ordenados = sorted(archivo_json[clave_json], key=lambda x: x[clave_orden], reverse=True)
                
    return jugadores_ordenados