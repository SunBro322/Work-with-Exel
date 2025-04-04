from PyQt6.QtWidgets import (QWidget,
                             QVBoxLayout,
                             QPushButton,
                             QLineEdit,
                             QListWidget)
from PyQt6.QtCore import Qt

class InfromationWindows(QWidget):
    def __init__(self, excel_worker):
        super().__init__()
        self.exel = excel_worker
        self.initUI()
        self.load_initial_data()

    def initUI(self):
        layout = QVBoxLayout()

        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText('Введите информацию ...')

        self.add_button = QPushButton('Добавить')
        self.add_button.clicked.connect(self.add_to_list)

        self.output_list = QListWidget()
        # self.output_list.setHorizontalScrollBar(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        # self.output_list.setVerticalScrollBar(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        # layout.addWidget(self.input_field)
        # layout.addWidget(self.add_button)
        layout.addWidget(self.output_list)

        self.setLayout(layout)
        self.setWindowTitle('Управление данными')
        self.adjustSize()

    def load_initial_data(self):
        temp_list = []
        data = self.exel.read()
        for d in data:
            temp = '||'.join(d)
            temp_list.append(temp)
            self.output_list.addItems(temp_list)

    def add_to_list(self):
        text = self.input_field.text()
        if text:
            self.output_list.addItem(text)
            self.input_field.clear()
