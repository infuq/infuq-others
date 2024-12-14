from sqlalchemy import Column

from canary.core.extensions import db


class Area(db.Model):
    __tablename__ = 'area'

    id = Column('id', db.BigInteger, primary_key=True)
    shortCode = Column('short_code', db.String(12), comment="短编码")
    code = Column('code', db.String(12), comment="编码")
    shortName = Column('short_name', db.String(128), comment="行政区划名称")
    name = Column('name', db.String(256), comment="行政区划全称")
    level = Column('level', db.Integer, comment="1:省 2:地级市 3:区/县级市 4:乡/镇/街道/政企合一单位 5:村/社区")
    year = Column('year', db.String(16), comment="行政区划年份")
    parentId = Column('parent_id', db.BigInteger, comment="父节点")
    description = Column('description', db.String(128), comment="说明")


