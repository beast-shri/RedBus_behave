import xlrd
from library.config import Configuration


class ReadExcel:
    def read_testdata(self, sheetname):

        wb = xlrd.open_workbook(Configuration.TEST_DATA)
        ws = wb.sheet_by_name(sheetname)
        rows = ws.get_rows()
        columns = ws.ncols
        header = next(rows)
        data = []

        for row in rows:
            values = ()
            for j in range(columns):
                values += (row[j].value,)
            data.append(values)
        return data

    def read_locators(self, sheetname):
        wb = xlrd.open_workbook(Configuration.TEST_DATA)
        ws = wb.sheet_by_name(sheetname)
        rows = ws.get_rows()
        header = next(rows)
        data_loc = {}

        for row in rows:
            data_loc[row[0].value] = (row[1].value, row[2].value)

        return data_loc