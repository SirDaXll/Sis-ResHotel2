import os



if __name__ == '__main__':

    #Leer archivo plano

    #excepciones
    try:#intentar una sección de código
        texto_recuperado = open('sprint1 pyqt6\\texto1.txt', 'r')
        print(texto_recuperado.read())
        texto_recuperado.close
    except Exception as e:#acción de capturar la excepción capturada
        print(f'El archivo "texto1.txt" no se encuentra... {e}')

    #escribir un archivo
    try: 
        texto_escrito = open('sprint1 pyqt6\\texto2.txt', 'a') #si no encuentra archivo
        #entonces lo crea
        texto_escrito.write('Se agregan nuevas lineas\n')
        texto_escrito.write('sin problemas de sobreescritura\n')
        texto_escrito.close()
    except Exception as e:
        print(f'El archivo no se encuentra... {e}')
    
    #crear solamente archivo
    try:
        # texto_creado = open('sprint1 pyqt6\\textocreado.txt', 'x')
        # texto_creado.close('sprint1 pyqt6\\textocreado.txt')

        #para eliminar archivos
        os.remove('sprint1 pyqt6\\textocreado.txt')
    except Exception as e:
        print(f'El archivo no se encuentra... {e}')
    


