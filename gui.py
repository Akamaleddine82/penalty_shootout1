from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QMessageBox
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QUrl
from PyQt6.QtMultimedia import QSoundEffect
from logic import PenaltyShootoutGame, save_result
import sys

class PenaltyShootoutGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.game = PenaltyShootoutGame()
        self.init_ui()
        self.sound = QSoundEffect()
        self.sound.setSource(QUrl.fromLocalFile('assets/crowd_cheer.wav'))

    def init_ui(self):
        self.setWindowTitle('Penalty Shootout')

        self.layout = QVBoxLayout()
        self.result_label = QLabel('Take your shot!')

        self.keeper_label = QLabel()
        self.update_keeper_image('center')

        self.left_button = QPushButton('Left')
        self.center_button = QPushButton('Center')
        self.right_button = QPushButton('Right')
        self.restart_button = QPushButton('Restart')

        self.left_button.clicked.connect(lambda: self.shoot('left'))
        self.center_button.clicked.connect(lambda: self.shoot('center'))
        self.right_button.clicked.connect(lambda: self.shoot('right'))
        self.restart_button.clicked.connect(self.restart_game)

        self.layout.addWidget(self.result_label)
        self.layout.addWidget(self.keeper_label)
        self.layout.addWidget(self.left_button)
        self.layout.addWidget(self.center_button)
        self.layout.addWidget(self.right_button)
        self.layout.addWidget(self.restart_button)

        self.setLayout(self.layout)

    def update_keeper_image(self, direction):
        pixmap = QPixmap(f'assets/keeper_{direction}.jpeg').scaled(300, 300)
        self.keeper_label.setPixmap(pixmap)

    def shoot(self, direction):
        result = self.game.take_shot(direction)
        self.update_keeper_image(direction)
        self.result_label.setText(result)

        if self.game.shots_taken == self.game.total_shots:
            save_result(self.game.goals_scored, self.game.total_shots)
            if self.game.goals_scored > self.game.total_shots // 2:
                self.sound.play()
                QMessageBox.information(self, "You Win!", "Congratulations, you beat the keeper!")
            else:
                QMessageBox.information(self, "Game Over", "Better luck next time!")

    def restart_game(self):
        self.game = PenaltyShootoutGame()
        self.result_label.setText('Game restarted! Take your shot!')
        self.update_keeper_image('center')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PenaltyShootoutGUI()
    window.show()
    sys.exit(app.exec())

  