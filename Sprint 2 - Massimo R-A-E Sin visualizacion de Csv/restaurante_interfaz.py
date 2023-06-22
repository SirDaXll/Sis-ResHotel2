from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, QMessageBox
import csv

class RestauranteInterfaz(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Restaurante")
        
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout()
        
        label_nombre = QLabel("Nombre de la Persona:")
        self.input_nombre = QLineEdit()
        layout.addWidget(label_nombre)
        layout.addWidget(self.input_nombre)
        
        label_plan = QLabel("Seleccione un Plan de Comida:")
        self.combo_plan = QComboBox()
        self.combo_plan.addItem("Inicial")
        self.combo_plan.addItem("Intermedio")
        self.combo_plan.addItem("Completo")
        self.combo_plan.addItem("Avanzado")
        self.combo_plan.addItem("Premium")
        layout.addWidget(label_plan)
        layout.addWidget(self.combo_plan)
        
        button_reservar = QPushButton("Reservar Plan")
        button_reservar.clicked.connect(self.reservar_plan)
        layout.addWidget(button_reservar)

        button_actualizar = QPushButton("Actualizar Reserva")
        button_actualizar.clicked.connect(self.actualizar_reserva)
        layout.addWidget(button_actualizar)

        button_eliminar = QPushButton("Eliminar Reserva")
        button_eliminar.clicked.connect(self.eliminar_reserva)
        layout.addWidget(button_eliminar)
        
        self.setLayout(layout)
    
    def reservar_plan(self):
        nombre = self.input_nombre.text()
        plan = self.combo_plan.currentText()

        for i in nombre:
            if i in '0123456789':
                return QMessageBox.warning(self, "Error", "Por favor, ingrese un dato valido.") and self.input_nombre.clear()
        
        for i in nombre:
            if i in '!"#$%&/()=?¡¿@,;.:-{[]^}<>¨´*+~':
                return QMessageBox.warning(self, "Error", "Por favor, ingrese un dato valido.") and self.input_nombre.clear()
        
        lista_nombres= []
        texto_csv = open('restaurante_reservas.csv', 'r')
        lineas = texto_csv.readlines()
        for linea in lineas:
            dato = linea.split(",")
            nombre_C = dato[0]
            lista_nombres.append(nombre_C)
        print (lista_nombres)

        if nombre in lista_nombres:
            return QMessageBox.warning(self, "Error", "Nombre repetido, ingrese un nombre valido.") and self.input_nombre.clear()
            
        else:
            csv_lista = [nombre,plan]
            print(csv_lista)

            with open('restaurante_reservas.csv', 'a', newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(csv_lista)

            mensaje = f"Reserva Realizada:\n\nNombre: {nombre}\nPlan: {plan}"
            QMessageBox.information(self, "Reserva Exitosa", mensaje)

        self.input_nombre.clear()
    
    def actualizar_reserva(self):
        nombre = self.input_nombre.text()
        plan = self.combo_plan.currentText()
        
        for i in nombre:
            if i in '0123456789':
                return QMessageBox.warning(self, "Error", "Por favor, ingrese un dato valido.") and self.input_nombre.clear()
        
        for i in nombre:
            if i in '!"#$%&/()=?¡¿@,;.:-{[]^}<>¨´*+~':
                return QMessageBox.warning(self, "Error", "Por favor, ingrese un dato valido.") and self.input_nombre.clear()

        lista_nombres= []
        texto_csv = open('restaurante_reservas.csv', 'r')
        lineas = texto_csv.readlines()
        for linea in lineas:
            dato = linea.split(",")
            nombre_C = dato[0]
            lista_nombres.append(nombre_C)
        print (lista_nombres)

        if nombre not in lista_nombres:
            return QMessageBox.warning(self, "Error", "Nombre no encontrado.") and self.input_nombre.clear()
            
        if nombre in lista_nombres:
            texto_csv = open('restaurante_reservas.csv', 'r')
            lineas = texto_csv.readlines()
            with open('restaurante_reservas.csv', 'w', newline="") as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow("Nombre;Plan")
            for linea in lineas:
                separar = linea.split(",")
                separar1 = separar[1].split("\n")
                nombre1 = str(separar[0])
                plan1 = str(separar1[0])
                csv_personas = [nombre1,plan1]
                if separar[0] != nombre:
                    with open('restaurante_reservas.csv', 'a', newline="") as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow(csv_personas)

            csv_lista = [nombre,plan]

            with open('restaurante_reservas.csv', 'a', newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(csv_lista)
                mensaje = f"Nombre: {nombre}\nPlan: {plan}\n\nReserva actualizada exitosamente."
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
        texto_csv = open('restaurante_reservas.csv', 'r')
        lineas = texto_csv.readlines()
        for linea in lineas:
            dato = linea.split(",")
            nombre_C = dato[0]
            lista_nombres.append(nombre_C)
        print (lista_nombres)

        if nombre not in lista_nombres:
            return QMessageBox.warning(self, "Error", "Nombre no encontrado.") and self.input_nombre.clear()
            
        if nombre in lista_nombres:
            texto_csv = open('restaurante_reservas.csv', 'r')
            lineas = texto_csv.readlines()
            with open('restaurante_reservas.csv', 'w', newline="") as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow("Nombre;Plan")
            for linea in lineas:
                separar = linea.split(",")
                if len(separar)<2:
                    None
                else:
                    separar1 = separar[1].split("\n")
                    nombre1 = str(separar[0])
                    plan1 = str(separar1[0])
                    csv_personas = [nombre1,plan1]
                    if separar[0] != nombre:
                        with open('restaurante_reservas.csv', 'a', newline="") as csvfile:
                            writer = csv.writer(csvfile)
                            writer.writerow(csv_personas)

            QMessageBox.information(self, "Reserva Eliminada", "Reserva eliminada exitosamente.")
            self.input_nombre.clear()
