import os

from PyQt6.QtWidgets import QApplication
from GUI import InfromationWindows
from work_with_exel import ExelReader
from dotenv import load_dotenv


def main():
    load_dotenv()

    # Инициализация Qt
    app = QApplication([])

    # Создание экземпляра
    reports = ExelReader(os.getenv('CONST'), filter_row=os.getenv('FILTER'))

    window = InfromationWindows(reports)
    window.show()

    app.exec()


if __name__ == "__main__":
    main()
