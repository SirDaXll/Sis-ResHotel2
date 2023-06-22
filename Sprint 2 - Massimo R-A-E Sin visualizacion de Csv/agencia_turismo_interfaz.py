from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, QMessageBox
import csv

class AgenciaTurismoInterfaz(QWidget):
    def __init__(self):
        super().__init__()
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
        button_reservar.clicked.connect(self.reservar_excursion)
        layout.addWidget(button_reservar)

        button_actualizar = QPushButton("Actualizar Reserva")
        button_actualizar.clicked.connect(self.actualizar_reserva)
        layout.addWidget(button_actualizar)

        button_eliminar = QPushButton("Eliminar Reserva")
        button_eliminar.clicked.connect(self.eliminar_reserva)
        layout.addWidget(button_eliminar)
        
        self.setLayout(layout)
    
    def reservar_excursion(self):
        nombre = self.input_nombre.text()
        excursion = self.combo_excursion.currentText()

        for i in nombre:
            if i in '0123456789':
                return QMessageBox.warning(self, "Error", "Por favor, ingrese un dato valido.") and self.input_nombre.clear()
        
        for i in nombre:
            if i in '!"#$%&/()=?¡¿@,;.:-{[]^}<>¨´*+~':
                return QMessageBox.warning(self, "Error", "Por favor, ingrese un dato valido.") and self.input_nombre.clear()
        
        lista_nombres= []
        texto_csv = open('agencia_reservas.csv', 'r')
        lineas = texto_csv.readlines()
        for linea in lineas:
            dato = linea.split(",")
            nombre_C = dato[0]
            lista_nombres.append(nombre_C)
        print (lista_nombres)

        if nombre in lista_nombres:
            return QMessageBox.warning(self, "Error", "Nombre repetido, ingrese un nombre valido.") and self.input_nombre.clear()
            
        else:
            csv_lista = [nombre,excursion]
            print(csv_lista)

            with open('agencia_reservas.csv', 'a', newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(csv_lista)

            mensaje = f"Reserva Realizada:\n\nNombre: {nombre}\nExcursión: {excursion}"
            QMessageBox.information(self, "Reserva Exitosa", mensaje)

        self.input_nombre.clear()
    
    def actualizar_reserva(self):
        nombre = self.input_nombre.text()
        excursion = self.combo_excursion.currentText()

        for i in nombre:
            if i in '0123456789':
                return QMessageBox.warning(self, "Error", "Por favor, ingrese un dato valido.") and self.input_nombre.clear()
        
        for i in nombre:
            if i in '!"#$%&/()=?¡¿@,;.:-{[]^}<>¨´*+~':
                return QMessageBox.warning(self, "Error", "Por favor, ingrese un dato valido.") and self.input_nombre.clear()

        lista_nombres= []
        texto_csv = open('agencia_reservas.csv', 'r')
        lineas = texto_csv.readlines()
        for linea in lineas:
            dato = linea.split(",")
            nombre_C = dato[0]
            lista_nombres.append(nombre_C)
        print (lista_nombres)

        if nombre not in lista_nombres:
            return QMessageBox.warning(self, "Error", "Nombre no encontrado.") and self.input_nombre.clear()
            
        if nombre in lista_nombres:
            texto_csv = open('agencia_reservas.csv', 'r')
            lineas = texto_csv.readlines()
            with open('agencia_reservas.csv', 'w', newline="") as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow("Nombre;Excursion")
            for linea in lineas:
                separar = linea.split(",")
                separar1 = separar[1].split("\n")
                nombre1 = str(separar[0])
                excursion1 = str(separar1[0])
                csv_personas = [nombre1,excursion1]
                if separar[0] != nombre:
                    with open('agencia_reservas.csv', 'a', newline="") as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow(csv_personas)

            csv_lista = [nombre,excursion]

            with open('agencia_reservas.csv', 'a', newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(csv_lista)
                mensaje = f"Nombre: {nombre}\nExcursión: {excursion}\n\nReserva actualizada exitosamente."
                QMessageBox.information(self, "Reserva Actualizada:", mensaje )

        self.input_nombre.clear()
    
    def eliminar_reserva(self):
        nombre = self.input_nombre.text()
        
        for i in nombre:
            if i in '0123456789':
                return QMessageBox.warning(self, "Error", "Por favor, ingrese un dato valido.") and self.input_nombre.clear()
        
        for i in nombre:
            if i in '!"#$%&/()=?¡¿@,;.:-{[]^}<>¨´*+~':
                return QMessageBox.warning(self, "Error", "Por favor, ingrese un dato valido.") and self.input_nombre.clear()

        lista_nombres= []
        texto_csv = open('agencia_reservas.csv', 'r')
        lineas = texto_csv.readlines()
        for linea in lineas:
            dato = linea.split(",")
            nombre_C = dato[0]
            lista_nombres.append(nombre_C)
        print (lista_nombres)

        if nombre not in lista_nombres:
            return QMessageBox.warning(self, "Error", "Nombre no encontrado.") and self.input_nombre.clear()
            
        if nombre in lista_nombres:
            texto_csv = open('agencia_reservas.csv', 'r')
            lineas = texto_csv.readlines()
            with open('agencia_reservas.csv', 'w', newline="") as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow("Nombre;Excursion")
            for linea in lineas:
                separar = linea.split(",")
                if len(separar)<2:
                    None
                else:
                    separar1 = separar[1].split("\n")
                    nombre1 = str(separar[0])
                    excursion1 = str(separar1[0])
                    csv_personas = [nombre1,excursion1]
                    if separar[0] != nombre:
                        with open('agencia_reservas.csv', 'a', newline="") as csvfile:
                            writer = csv.writer(csvfile)
                            writer.writerow(csv_personas)

            QMessageBox.information(self, "Reserva Eliminada", "Reserva eliminada exitosamente.")
            self.input_nombre.clear()