from sqlalchemy import Column

from toolkit.core.extensions import db


class OperationRecord(db.Model):
    __tablename__ = 'operation_record'

    recordId = Column('record_id', db.BigInteger, primary_key=True)
    enterpriseId = Column('enterprise_id', db.BigInteger, comment="企业ID")
    accountId = Column('account_id', db.BigInteger, comment="操作人ID")
    userName = Column('user_name', db.String(32), comment="操作人昵称")
    realName = Column('real_name', db.String(32), comment="操作人名称")
    handleStatus = Column('handle_status', db.Integer, comment="处理状态")
    handleStatusDesc = Column('handle_status_desc', db.String(16), comment="处理状态")
    header = Column('header', db.String(1000), comment="操作请求头")
    inBody = Column('in_body', db.TEXT, comment="操作请求内容")
    outBody = Column('out_body', db.TEXT, comment="操作响应内容")
    businessNo = Column('business_no', db.String(32), comment="业务单号")
    businessId = Column('business_id', db.BigInteger, comment="业务ID")
    messageId = Column('message_id', db.String(40), comment="MQ消息ID")
    serviceName = Column('service_name', db.String(32), comment="服务名称")
    moduleName = Column('module_name', db.String(32), comment="模块名称")
    method = Column('method', db.String(128), comment="接口名称")
    remark = Column('remark', db.String(128), comment="功能描述")
    desc = Column('desc', db.String(255), comment="描述信息")
    sourceType = Column('source_type', db.Integer, comment="来源方式类型")
    sourceName = Column('source_name', db.String(32), comment="来源方式名称")
    userAgent = Column('user_agent', db.String(1024), comment="User-Agent")
    domain = Column('domain', db.String(128), comment="域名")
    sourceIp = Column('source_ip', db.String(32), comment="来源IP")
    handleIp = Column('handle_ip', db.String(32), comment="事件处理节点的IP")
    traceId = Column('trace_id', db.String(64), comment="链路")
    createTime = Column('create_time', db.DateTime, comment="创建时间")
    updateTime = Column('update_time', db.DateTime, comment="修改时间")

