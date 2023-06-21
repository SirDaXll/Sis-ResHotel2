from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTreeWidget, QTreeWidgetItem, QMessageBox, QLineEdit, QComboBox
from PyQt6.QtCore import pyqtSignal


class AgenciaTurismoInterfaz(QWidget):

    mi_signal = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.nombre = None
        self.seccion = 'Agencia de Turismo'
        self.excursion = None


        self.setWindowTitle("Agencia de Turismo")
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout()
        
        label_nombre = QLabel("Nombre de la Persona:")
        self.input_nombre = QLineEdit()
        layout.addWidget(label_nombre)
        layout.addWidget(self.input_nombre)
        
        label_excursion = QLabel("Seleccione una Excursión:")
        self.combo_excursion = QComboBox()
        self.combo_excursion.addItem("Tour por la Ciudad")
        self.combo_excursion.addItem("Senderismo en el Bosque")
        self.combo_excursion.addItem("Visita a las Playas")
        self.combo_excursion.addItem("Tour de Aventura")
        layout.addWidget(label_excursion)
        layout.addWidget(self.combo_excursion)
        
        button_reservar = QPushButton("Reservar Excursión")
        button_reservar.clicked.connect(self.agregar_reserva_excursion)
        layout.addWidget(button_reservar)

        button_actualizar = QPushButton("Actualizar Reserva")
        button_actualizar.clicked.connect(self.actualizar_reserva)
        layout.addWidget(button_actualizar)

        button_eliminar = QPushButton("Eliminar Reserva")
        button_eliminar.clicked.connect(self.eliminar_reserva)
        layout.addWidget(button_eliminar)
        
        self.setLayout(layout)
    
    def agregar_reserva_excursion(self):
        # Obtener el nombre y la excursión seleccionada
        self.nombre = self.input_nombre.text()
        self.excursion = self.combo_excursion.currentText()

                
        # Verificar si se ingresaron datos válidos
        if self.nombre and self.excursion:
            mensaje = f"Excursión Reservada:\n\nNombre: {self.nombre}\nExcursión: {self.excursion}"
            QMessageBox.information(self, "Reserva Exitosa", mensaje)
            
            # Limpiar el campo de nombre después de la reserva exitosa
            self.input_nombre.clear()

            #agregar los datos de la reserva al archivo csv
            try:
                texto_csv = open('sprint2-andres\\archivo_reservas.csv', 'a')
                texto_csv.write(f"'{self.nombre}','Agencia de Turismo', '{self.excursion}'\n")
                texto_csv.close()
            except Exception as e:
                print(f'El archivo no se encuentra ... {e}')

            self.mi_signal.emit()

        else:
            QMessageBox.warning(self, "Error", "Por favor, complete el nombre y seleccione una excursión.")

        

    def actualizar_reserva(self):
        QMessageBox.information(self, "Reserva Actualizada", "Reserva actualizada exitosamente.")
        
        archivo = 'sprint2-andres\\archivo_reservas.csv'
        nombre_reserva = self.input_nombre.text()
        excursion = self.combo_excursion.currentText()
        num_linea_reserva = self.encontrar_elemento_archivo(archivo, nombre_reserva, excursion)
        nueva_linea = f"'{nombre_reserva}', 'Agencia de Turismo'"
        self.modificar_linea(num_linea_reserva, nueva_linea)

        self.input_nombre.clear()
    
    def eliminar_reserva(self):
        QMessageBox.information(self, "Reserva Eliminada", "Reserva eliminada exitosamente.")
        
        archivo = 'sprint2-andres\\archivo_reservas.csv'
        nombre_reserva = self.input_nombre.text()
        excursion = self.combo_excursion.currentText()

        linea_reserva = self.encontrar_elemento_archivo(archivo, nombre_reserva, excursion)
        self.eliminar_linea_archivo(archivo, linea_reserva)

        self.mi_signal.emit()


    def eliminar_linea_archivo(self, archivo, numero_linea):
        with open(archivo, 'r') as archivo_origen:
            lineas = archivo_origen.readlines()

        # Verifica que el número de línea sea válido
        if numero_linea < 1 or numero_linea > len(lineas):
            print("Número de línea inválido")
            return

        # Elimina la línea deseada de la lista de líneas
        del lineas[numero_linea - 1]

        with open(archivo, 'w') as archivo_destino:
            archivo_destino.writelines(lineas)
    
    def encontrar_elemento_archivo(self, archivo, elemento1, elemento2):
        with open(archivo, 'r') as archivo_origen:
            linea_actual = 0

            for linea in archivo_origen:
                linea_actual += 1
                if elemento1 in linea and elemento2 in linea:
                    return linea_actual

        return None
    
    def modificar_linea(self, archivo, linea_index, nueva_linea):
        with open(archivo, 'r') as file:
            lineas = file.readlines()

        if linea_index < 0 or linea_index >= len(lineas):
            print("Índice de línea inválido")
            return

        lineas[linea_index] = nueva_linea + '\n'

        with open(archivo, 'w') as file:
            file.writelines(lineas)
    

    
    


