from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTreeWidget, QTreeWidgetItem, QMessageBox, QLineEdit, QComboBox

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
        # Obtener el nombre y la excursión seleccionada
        nombre = self.input_nombre.text()
        excursion = self.combo_excursion.currentText()
        
        # Verificar si se ingresaron datos válidos
        if nombre and excursion:
            mensaje = f"Excursión Reservada:\n\nNombre: {nombre}\nExcursión: {excursion}"
            QMessageBox.information(self, "Reserva Exitosa", mensaje)
            
            # Limpiar el campo de nombre después de la reserva exitosa
            self.input_nombre.clear()
        else:
            QMessageBox.warning(self, "Error", "Por favor, complete el nombre y seleccione una excursión.")
    
    def actualizar_reserva(self):
        QMessageBox.information(self, "Reserva Actualizada", "Reserva actualizada exitosamente.")
        self.input_nombre.clear()
    
    def eliminar_reserva(self):
        QMessageBox.information(self, "Reserva Eliminada", "Reserva eliminada exitosamente.")
        self.input_nombre.clear()