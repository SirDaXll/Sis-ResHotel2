import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QAction
from reserva_interfaz import ReservaInterfaz
from agencia_turismo_interfaz import AgenciaTurismoInterfaz
from restaurante_interfaz import RestauranteInterfaz

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Reservas de Hotel")
        self.setGeometry(100, 100, 400, 200)
        
        self.menus()
    
    def menus(self):
        # Menú Reserva
        menu_reserva = self.menuBar().addMenu("Reserva")
        
        action_reserva = QAction("Reservar Habitación", self)
        action_reserva.triggered.connect(self.reserva)
        menu_reserva.addAction(action_reserva)
        
        # Menú Agencia de Turismo
        menu_agencia_turismo = self.menuBar().addMenu("Agencia de Turismo")
        
        action_agencia_turismo = QAction("Reservar Excursión", self)
        action_agencia_turismo.triggered.connect(self.agencia_turismo)
        menu_agencia_turismo.addAction(action_agencia_turismo)
        
        # Menú Restaurante
        menu_restaurante = self.menuBar().addMenu("Restaurante")
        
        action_restaurante = QAction("Hacer Pedido", self)
        action_restaurante.triggered.connect(self.restaurante)
        menu_restaurante.addAction(action_restaurante)
    
    def reserva(self):
        self.reserva_interface = ReservaInterfaz()
        # Muestra la interfaz de reserva
        self.reserva_interface.show()
    
    def agencia_turismo(self):
        self.agencia_turismo_interface = AgenciaTurismoInterfaz()
        # Muestra la interfaz de la agencia de turismo
        self.agencia_turismo_interface.show()
    
    def restaurante(self):
        self.restaurante_interface = RestauranteInterfaz()
        # Muestra la interfaz del restaurante
        self.restaurante_interface.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    main_window = MainWindow()
    main_window.show()
    
    sys.exit(app.exec())