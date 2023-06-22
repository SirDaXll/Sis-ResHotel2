from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QPushButton, QLineEdit, QMessageBox

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
            if i in '0123456789' or i in '!"#$%&/()=?¡¿@,;.:-_{[]^}<>¨´*+~':
                None
            return QMessageBox.warning(self, "Error", "Por favor, ingrese un dato valido.")
            
        
        for i in nombre:
            if i not in '0123456789' or nombre == '':
                None
            mensaje = f"Plan de Comida Reservado:\n\nNombre: {nombre}\nPlan: {plan}"
            QMessageBox.information(self, "Reserva Exitosa", mensaje)
            
        self.input_nombre.clear()
    
    def actualizar_reserva(self):
        QMessageBox.information(self, "Reserva Actualizada", "Reserva actualizada exitosamente.")
        self.input_nombre.clear()

    def eliminar_reserva(self):
        QMessageBox.information(self, "Reserva Eliminada", "Reserva eliminada exitosamente.")
        self.input_nombre.clear()
