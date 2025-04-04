import pandas as pd


class ExelReader:
    def __init__(self, path, check_cells=3, filter_row=None):
        self.path = path
        self.check_cells = check_cells
        self.filter_row = filter_row

    def read(self):
        """ Чтение данных из Exel """
        exel_data = pd.read_excel(self.path,
                                  header=None,
                                  dtype=str,
                                  keep_default_na=False)


        empty_row_index = self._empty_row(exel_data)
        if empty_row_index is not None:
            exel_data = exel_data.iloc[:empty_row_index]

        # Вывод информации в виде списка
        exel_data = exel_data.values.tolist()


        if self.filter_row == None:
            return exel_data
        else:
            return self._filter_row(exel_data)

    def _empty_row(self, data):
        """ Ищем первую пустую строку """
        for index, row in data.iterrows():
            if all(cell == '' for cell in row[:self.check_cells]):
                return index
        return None

    def _filter_row(self, data):
        """ Фильтрация данных по параметру """
        new_data = []
        data = data[1:]
        for index, value in enumerate(data):
            if value[2] == self.filter_row:
                new_data.append(data[index])
        return new_data
