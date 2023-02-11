import xlrd


class GetExcelData():

    def get_data(self,file_path, sheet_name):
        # 打开文件
        self.book = xlrd.open_workbook(file_path)
        # 选择sheet页
        self.sheet = self.book.sheet_by_name(sheet_name)

        data_list = []
        for row in range(1, self.sheet.nrows):
            dicta = {}
            data_list.append(dicta)  # 将行字典添加到for循环外面的列表内
            for col in range(0, self.sheet.ncols):
                key = self.sheet.cell_value(0, col)  # 取excel表中的标题
                value = self.sheet.cell_value(row, col)  # 取单元格数据
                dicta[key] = value  # 将每一列的数据添加到行字典内
        return data_list  # 返回最终取到的数据

if __name__ == '__main__':
    file_path = r"C:\Users\11314\Desktop\web自动化2023-2-1\ecshop\cases\test-data.xls"
    sheet_name = "login"
    getexceldata = GetExcelData()
    data_list = getexceldata.get_data(file_path, sheet_name)
    print(data_list)