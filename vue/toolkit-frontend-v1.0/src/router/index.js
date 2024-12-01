import Vue from "vue";
import Router from "vue-router";


import Index from '../components/Index.vue';
import Login from '../components/Login.vue';
import Account from '../views/wms/Account.vue';
import AllocateOrder from '../views/wms/AllocateOrder.vue';
import EnterpriseWarehouse from '../views/wms/EnterpriseWarehouse.vue';
import ExportRecord from '../views/wms/ExportRecord.vue';
import OperationRecord from '../views/wms/OperationRecord.vue';
import OwnerStockHistory from '../views/wms/OwnerStockHistory.vue';
import PushRecord from '../views/wms/PushRecord.vue';
import PushRecordOld from '../views/wms/PushRecordOld.vue';
import ReceiveRecord from '../views/wms/ReceiveRecord.vue';
import ReceiveRecordOld from '../views/wms/ReceiveRecordOld.vue';
import StockSyncOms from '../views/wms/StockSyncOms.vue';
import StoreBatchDetailLogHistory from '../views/wms/StoreBatchDetailLogHistory.vue';
import StoreCustomerOrder from '../views/wms/StoreCustomerOrder.vue';
import StoreCustomerOrderDetailQuantity from '../views/wms/StoreCustomerOrderDetailQuantity.vue';
import GoodsStockHistory from '../views/wms/GoodsStockHistory.vue';
import StoreReturnOrder from '../views/wms/StoreReturnOrder.vue';
import StoreSendOrder from '../views/wms/StoreSendOrder.vue';
import StoreStorage from '../views/wms/StoreStorage.vue';
import StoreTran from '../views/wms/StoreTran.vue';
import Warehouse from '../views/wms/Warehouse.vue';
import WarehouseEnterprise from '../views/wms/WarehouseEnterprise.vue';
import WarehouseStoreCustomerOrder from '../views/wms/WarehouseStoreCustomerOrder.vue';
import ApiRequestRecord from '../views/platform/ApiRequestRecord.vue';
import AppBusiness from '../views/platform/AppBusiness.vue';
import AppRelation from '../views/platform/AppRelation.vue';
import ChanjetToken from '../views/platform/ChanjetToken.vue';
import PlatformBusiness from '../views/platform/PlatformBusiness.vue';
import PlatformPushRecord from '../views/platform/PlatformPushRecord.vue';
import PlatformReceiveRecord from '../views/platform/PlatformReceiveRecord.vue';
import Repush from '../views/platform/Repush.vue';
import SelectTrace from '../views/platform/SelectTrace.vue';
import Enum from '../views/other/Enum.vue';
import FileUpload from '../views/other/FileUpload.vue';
import JsonFormat from '../views/other/JsonFormat.vue';
import SqlStatement from '../views/other/SqlStatement.vue';
import StoreCustomerOrderSplit from '../views/wms/StoreCustomerOrderSplit.vue';


Vue.use(Router);


const routes = [
  { path: "/", meta:{title:"首页"}, component: Index },
  { path: "/login", meta:{title:"登录页"}, component: Login },
  { path: "/account", meta:{title:"仓配账号"}, component: Account },
  { path: "/allocate_order", meta:{title:"调拨单"}, component: AllocateOrder },
  { path: "/enterprise_warehouse", meta:{title:"企业-仓库"}, component: EnterpriseWarehouse },
  { path: "/operation_record", meta:{title:"访问记录"}, component: OperationRecord },
  { path: "/owner_stock_history", meta:{title:"货主库存"}, component: OwnerStockHistory },
  { path: "/warehouse_enterprise", meta:{title:"仓库-企业"}, component: WarehouseEnterprise },
  { path: "/warehouse_store_customer_order", meta:{title:"仓库-订货单"}, component: WarehouseStoreCustomerOrder },
  { path: "/store_return_order", meta:{title:"退货单"}, component: StoreReturnOrder },
  { path: "/store_send_order", meta:{title:"发货单"}, component: StoreSendOrder },
  { path: "/store_storage", meta:{title:"出入库单"}, component: StoreStorage },
  { path: "/store_tran", meta:{title:"车次"}, component: StoreTran },
  { path: "/warehouse", meta:{title:"仓库查询"}, component: Warehouse },
  { path: "/push_record", meta:{title:"WMS推送记录"}, component: PushRecord },
  { path: "/push_record_old", meta:{title:"WMS推送记录(旧)"}, component: PushRecordOld },
  { path: "/receive_record", meta:{title:"WMS接收记录"}, component: ReceiveRecord },
  { path: "/receive_record_old", meta:{title:"WMS接收记录(旧)"}, component: ReceiveRecordOld },
  { path: "/stock_sync_oms", meta:{title:"库存同步到OMS记录"}, component: StockSyncOms },
  { path: "/store_batch_detail_log_history", meta:{title:"批次日志记录"}, component: StoreBatchDetailLogHistory },
  { path: "/store_customer_order", meta:{title:"订货单"}, component: StoreCustomerOrder },
  { path: "/store_customer_order_detail_quantity", meta:{title:"订货退货明细数量"}, component: StoreCustomerOrderDetailQuantity },
  { path: "/goods_stock_history", meta:{title:"商品库存"}, component: GoodsStockHistory },
  { path: "/export_record", meta:{title:"单据导出记录"}, component: ExportRecord },
  { path: "/store_customer_order_split", meta:{title:"订货单拆单查询"}, component: StoreCustomerOrderSplit },
  { path: "/api_request_record", meta:{title:"接口平台API接口请求记录"}, component: ApiRequestRecord },
  { path: "/app_business", meta:{title:"应用和应用业务"}, component: AppBusiness },
  { path: "/app_relation", meta:{title:"映射数据"}, component: AppRelation },
  { path: "/chanjet_token", meta:{title:"获取畅捷通TOKEN"}, component: ChanjetToken },
  { path: "/platform_business", meta:{title:"平台和平台业务"}, component: PlatformBusiness },
  { path: "/platform_push_record", meta:{title:"对接平台推送记录"}, component: PlatformPushRecord },
  { path: "/platform_receive_record", meta:{title:"对接平台接收记录"}, component: PlatformReceiveRecord },
  { path: "/re_push", meta:{title:"补推"}, component: Repush },
  { path: "/select_trace", meta:{title:"全局链路速查"}, component: SelectTrace },
  { path: "/enum", meta:{title:"字典值"}, component: Enum },
  { path: "/file_upload", meta:{title:"文件上传"}, component: FileUpload },
  { path: "/json_format", meta:{title:"JSON格式化"}, component: JsonFormat },
  { path: "/sql_statement", meta:{title:"常用SQL"}, component: SqlStatement }

]

const routerConfig = {
  mode: 'hash',
  routes
}

const router = new Router(routerConfig)
router.beforeEach((to,from,next) => {
  if (to.meta['title']) {
    document.title = "杂货柜-" + to.meta['title']
  }
  next()
})

export default router