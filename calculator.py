import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        button_style = "QPushButton { background-color: lightgray; border-radius: 10px; }"
        equal_button_style = "QPushButton { background-color: black; color: white; border-radius: 10px; font-size: 20px; font-weight: bold; }"
        del_ac_button_style = "QPushButton { color: red; background-color: lightgray; border-radius: 10px; border: 1px solid black; }"
        ac_button_style = "QPushButton { color: blue; background-color: lightgray; border-radius: 10px; border: 1px solid black; }"
        text_font = QFont()
        text_font.setPointSize(10)  
        text_font.setBold(True)

        names = ['AC', 'Del', '', '',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(1, 6) for j in range(4)]

        button_size = 40
        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            button.setFont(text_font)
            if name == 'Del':  
                button.setStyleSheet(del_ac_button_style)
            elif name == 'AC':  
                button.setStyleSheet(ac_button_style)
            elif name == '=':  
                button.setStyleSheet(equal_button_style)
                button.setFixedSize(button_size * 2, button_size)
            else:  
                button.setStyleSheet(button_style)
                button.setFixedSize(button_size, button_size)
            grid.addWidget(button, *position)
            button.clicked.connect(self.on_click)

        
        self.display = QLineEdit()
        self.display.setFixedSize(button_size * 4, int(button_size * 1.5))
        grid.addWidget(self.display, 0, 0, 1, 4)
        grid.setContentsMargins(10, 10, 10, 10)  

        self.setWindowTitle('Calculator')
        self.show()

    def on_click(self):
        sender = self.sender()
    
        text = sender.text()

        if text == 'AC':
            self.display.setText('')
        elif text == 'Del':
            self.display.setText(self.display.text()[:-1])
        elif text == '=':
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except Exception as e:
                self.display.setText('Error')
        else:
            self.display.setText(self.display.text() + text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    sys.exit(app.exec_())
