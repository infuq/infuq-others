from sqlalchemy import Column

from toolkit.core.extensions import db


class StoreBatchDetailLog(db.Model):
    __tablename__ = 'store_batch_details_log'

    batchDetailsLogId = Column('batch_details_log_id', db.BigInteger, primary_key=True)
    batchDetailsId = Column('batch_details_id', db.BigInteger, comment="批次详情ID")
    storageDetailsId = Column('storage_details_id', db.BigInteger, comment="出入库详情ID")
    storageCategory = Column('storage_category', db.Integer, comment="操作类型")
    storageType = Column('storage_type', db.Integer, comment="出入库类型")
    beforeQuantity = Column('before_quantity', db.Numeric(16,6), comment="操作前数量")
    quantity = Column('quantity', db.Numeric(16,6), comment="操作数量")
    afterQuantity = Column('after_quantity', db.Numeric(16,6), comment="操作后数量")
    batchDetailsLogDesc = Column('batch_details_log_desc', db.String(255), comment="操作描述")
    createTime = Column('create_time', db.DateTime, comment="创建时间")
    updateTime = Column('update_time', db.DateTime, comment="修改时间")

