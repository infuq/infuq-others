from sqlalchemy import Column

from toolkit.core.extensions import db


class StoreBatch(db.Model):
    __tablename__ = 'store_batch'

    batchId = Column('batch_id', db.BigInteger, primary_key=True)

    batchNo = Column('batch_no', db.String(32), comment="批次号")
    warehouseOwnerGoodsId = Column('warehouse_owner_goods_id', db.BigInteger, comment="仓库货主商品ID")
    goodsOwnerId = Column('goods_owner_id', db.BigInteger, comment="货主ID")
    supplierId = Column('supplier_id', db.BigInteger, comment="供应商ID")
    unitPrice = Column('unit_price', db.Numeric(10,2), comment="价格")
    productionDate = Column('production_date', db.Date, comment="生产日期")
    createTime = Column('create_time', db.DateTime, comment="创建时间")
    updateTime = Column('update_time', db.DateTime, comment="修改时间")

