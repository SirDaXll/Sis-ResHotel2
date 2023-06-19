from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, QMessageBox

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
        
        if nombre and habitacion:
            mensaje = f"Reserva Realizada:\n\nNombre: {nombre}\nHabitación: {habitacion}"
            QMessageBox.information(self, "Reserva Exitosa", mensaje)
            
            self.input_nombre.clear()
        else:
            QMessageBox.warning(self, "Error", "Por favor, complete el nombre y seleccione una habitación.")
    
    def actualizar_reserva(self):
        QMessageBox.information(self, "Reserva Actualizada", "Reserva actualizada exitosamente.")
        self.input_nombre.clear()
    
    def eliminar_reserva(self):
        QMessageBox.information(self, "Reserva Eliminada", "Reserva eliminada exitosamente.")
        self.input_nombre.clear()
