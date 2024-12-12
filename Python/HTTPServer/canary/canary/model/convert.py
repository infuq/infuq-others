
"""
样例数据说明:
row = {
    "customer_order_id": 556526218158313472,
    "customer_order_no": "DH-241114-000002"
}

返回值 = {
    "customerOrderId": 556526218158313472,
    "customerOrderNo": "DH-241114-000002"
}
"""
def convert(clazz, row):
    obj = { }
    # 所有属性和对应的值
    attributes = clazz.__dict__
    for attribute, value in attributes.items():
        # 包含下划线的属性直接跳过
        if "_" in attribute:
            continue

        # 数据库字段名称
        field_name = value.__dict__['key']

        field_value = row[field_name]
        obj[attribute] = field_value

    return obj