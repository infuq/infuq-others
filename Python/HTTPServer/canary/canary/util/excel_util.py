
# 读取Sheet数据
def read_sheet(sheet, start_row=1):
    max_row = sheet.max_row
    max_column = sheet.max_column
    row = start_row # 从第几行开始读取数据

    while row < max_row:

        row += 1

        # 读取行内容
        row_data = []
        for i in range(1, max_column + 1):
            cell_value = sheet.cell(row=row, column=i).value
            row_data.append(cell_value)
        # (行号, 行内容)
        yield (row, row_data)