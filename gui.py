import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from logic import PenaltyShootoutGame

def start_game():
    app = QApplication(sys.argv)
    window = GameWindow()
    window.show()
    sys.exit(app.exec())

class GameWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Penalty Shootout")
        self.layout = QVBoxLayout()

        self.label = QLabel("Choose your shot direction:")
        self.layout.addWidget(self.label)

        self.left_button = QPushButton("Left")
        self.center_button = QPushButton("Center")
        self.right_button = QPushButton("Right")

        self.left_button.clicked.connect(lambda: self.shoot("left"))
        self.center_button.clicked.connect(lambda: self.shoot("center"))
        self.right_button.clicked.connect(lambda: self.shoot("right"))

        self.layout.addWidget(self.left_button)
        self.layout.addWidget(self.center_button)
        self.layout.addWidget(self.right_button)

        self.setLayout(self.layout)

        self.game = PenaltyShootoutGame()

    def shoot(self, direction: str):
        result = self.game.take_shot(direction)
        self.label.setText(result)
