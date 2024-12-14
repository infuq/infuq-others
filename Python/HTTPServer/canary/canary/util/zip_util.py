import zipfile

def unzip(file_object):
    with zipfile.ZipFile(file_object, 'r') as zip_ref:
        # 列出ZIP文件中的所有文件
        for file_name in zip_ref.namelist():
            # 打开Excel文件
            with zip_ref.open(file_name) as excel_file:
                yield excel_file