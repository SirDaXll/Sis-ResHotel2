from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, QMessageBox
import csv

class ReservaInterfaz(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Reserva")
        
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout()
        
        label_nombre = QLabel("Nombre de la Persona:")
        self.input_nombre = QLineEdit()
        layout.addWidget(label_nombre)
        layout.addWidget(self.input_nombre)
        
        label_habitacion = QLabel("Seleccione una Habitación:")
        self.combo_habitacion = QComboBox()
        self.combo_habitacion.addItem("Ejecutiva Individual")
        self.combo_habitacion.addItem("Ejecutiva Doble")
        self.combo_habitacion.addItem("Familiar")
        self.combo_habitacion.addItem("PentHouse Volcanes")
        self.combo_habitacion.addItem("PentHouse Pacífico")
        layout.addWidget(label_habitacion)
        layout.addWidget(self.combo_habitacion)
        
        button_reservar = QPushButton("Realizar Reserva")
        button_reservar.clicked.connect(self.realizar_reserva)
        layout.addWidget(button_reservar)

        button_actualizar = QPushButton("Actualizar Reserva")
        button_actualizar.clicked.connect(self.actualizar_reserva)
        layout.addWidget(button_actualizar)

        button_eliminar = QPushButton("Eliminar Reserva")
        button_eliminar.clicked.connect(self.eliminar_reserva)
        layout.addWidget(button_eliminar)
        
        self.setLayout(layout)
    
    def realizar_reserva(self):
        nombre = self.input_nombre.text()
        habitacion = self.combo_habitacion.currentText()

        for i in nombre:
            if i in '0123456789':
                return QMessageBox.warning(self, "Error", "Por favor, ingrese un dato valido.") and self.input_nombre.clear()
        
        for i in nombre:
            if i in '!"#$%&/()=?¡¿@,;.:-{[]^}<>¨´*+~':
                return QMessageBox.warning(self, "Error", "Por favor, ingrese un dato valido.") and self.input_nombre.clear()
        
        lista_nombres= []
        texto_csv = open('personas_reservas.csv', 'r')
        lineas = texto_csv.readlines()
        for linea in lineas:
            dato = linea.split(",")
            nombre_C = dato[0]
            lista_nombres.append(nombre_C)
        print (lista_nombres)

        if nombre in lista_nombres:
            return QMessageBox.warning(self, "Error", "Nombre repetido, ingrese un nombre valido.") and self.input_nombre.clear()
            
        else:
            csv_lista = [nombre,habitacion]
            print(csv_lista)

            with open('personas_reservas.csv', 'a', newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(csv_lista)

            mensaje = f"Reserva Realizada:\n\nNombre: {nombre}\nHabitación: {habitacion}"
            QMessageBox.information(self, "Reserva Exitosa", mensaje)

        self.input_nombre.clear()
        
    
    def actualizar_reserva(self):
        nombre = self.input_nombre.text()
        habitacion = self.combo_habitacion.currentText()

        for i in nombre:
            if i in '0123456789':
                return QMessageBox.warning(self, "Error", "Por favor, ingrese un dato valido.") and self.input_nombre.clear()
        
        for i in nombre:
            if i in '!"#$%&/()=?¡¿@,;.:-{[]^}<>¨´*+~':
                return QMessageBox.warning(self, "Error", "Por favor, ingrese un dato valido.") and self.input_nombre.clear()

        lista_nombres= []
        texto_csv = open('personas_reservas.csv', 'r')
        lineas = texto_csv.readlines()
        for linea in lineas:
            dato = linea.split(",")
            nombre_C = dato[0]
            lista_nombres.append(nombre_C)
        print (lista_nombres)

        if nombre not in lista_nombres:
            return QMessageBox.warning(self, "Error", "Nombre no encontrado.") and self.input_nombre.clear()
            
        if nombre in lista_nombres:
            texto_csv = open('personas_reservas.csv', 'r')
            lineas = texto_csv.readlines()
            with open('personas_reservas.csv', 'w', newline="") as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow("Nombre;Habitacion")
            for linea in lineas:
                separar = linea.split(",")
                separar1 = separar[1].split("\n")
                nombre1 = str(separar[0])
                habitacion1 = str(separar1[0])
                csv_personas = [nombre1,habitacion1]
                if separar[0] != nombre:
                    with open('personas_reservas.csv', 'a', newline="") as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow(csv_personas)

            csv_lista = [nombre,habitacion]

            with open('personas_reservas.csv', 'a', newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(csv_lista)
                mensaje = f"Nombre: {nombre}\nHabitación: {habitacion}\n\nReserva actualizada exitosamente."
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
        texto_csv = open('personas_reservas.csv', 'r')
        lineas = texto_csv.readlines()
        for linea in lineas:
            dato = linea.split(",")
            nombre_C = dato[0]
            lista_nombres.append(nombre_C)
        print (lista_nombres)

        if nombre not in lista_nombres:
            return QMessageBox.warning(self, "Error", "Nombre no encontrado.") and self.input_nombre.clear()
            
        if nombre in lista_nombres:
            texto_csv = open('personas_reservas.csv', 'r')
            lineas = texto_csv.readlines()
            with open('personas_reservas.csv', 'w', newline="") as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow("Nombre;Habitacion")
            for linea in lineas:
                separar = linea.split(",")
                if len(separar)<2:
                    None
                else:
                    separar1 = separar[1].split("\n")
                    nombre1 = str(separar[0])
                    habitacion1 = str(separar1[0])
                    csv_personas = [nombre1,habitacion1]
                    if separar[0] != nombre:
                        with open('personas_reservas.csv', 'a', newline="") as csvfile:
                            writer = csv.writer(csvfile)
                            writer.writerow(csv_personas)

            QMessageBox.information(self, "Reserva Eliminada", "Reserva eliminada exitosamente.")
            self.input_nombre.clear()
