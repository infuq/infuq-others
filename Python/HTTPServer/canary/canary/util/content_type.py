
def judge_file_type(content_type):
    if content_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        return "excel"
    elif content_type == "application/zip":
        return "zip"
    else:
        return None