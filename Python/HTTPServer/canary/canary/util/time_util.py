import datetime


def datetime_toString(dt):
    if dt is not None and isinstance(dt, datetime.datetime):
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    return dt
