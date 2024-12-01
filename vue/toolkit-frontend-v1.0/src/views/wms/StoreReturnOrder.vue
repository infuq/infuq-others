<template>
  <div>
    <section class="content clearfix" style="width: 97%;">
      <div class="el-backtop" style="right: 40px; top: 130px;">
        <el-link type="primary" :href="'/'" :underline="false" target="_blank"><i class="el-icon-s-home"></i></el-link>
      </div>
      <el-divider content-position="right">{{ env }}环境</el-divider>

      <el-form :inline="true" class="demo-form-inline">

        <div v-if="isShowQuery">
          <div style="height: 50px;">
            <el-form-item label="">
              <el-input v-model="returnOrderCode" placeholder="SC4RP6MZ20240302203624825" clearable @clear="clearReturnOrderCode" style="width: 300px;"></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="onSubmit(2)">查询</el-button>
            </el-form-item>
            <span style="display: inline-block; padding-top: 10px;" v-if="sizeOfReturnOrderNo > 0">{{ sizeOfReturnOrderNo }}个TH单</span>
          </div>
          <div style="height: 50px;">
            <el-form-item label="">
              <el-input v-model="returnOrderNo" placeholder="TH-230828-002610" clearable @clear="clearReturnOrderNo" style="width: 300px;"></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="onSubmit(3)">查询</el-button>
            </el-form-item>
          </div>
        </div>


        <div>
          <template>
            <el-tabs v-model="activeName" type="card" @tab-click="handleTabClick">
              <el-tab-pane v-for="(item,index) in this.tabsData" :key="index" :label="item.labelName" :name="item.tabName">
              </el-tab-pane>
            </el-tabs>
          </template>
        </div>


        <!-- 结果 -->
        <div style="margin-top: 15px;">

          <!-- 退货单 -->
          <div style="margin-top: 10px;" v-loading="loading">
            <el-divider content-position="left">退货单</el-divider>

            <div style="margin-left: 40px; font-weight: 500; font-size: 14px;">

              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">退货单号:</label><label>&nbsp;&nbsp;&nbsp;{{ returnOrder.returnOrderNo }}</label>
                <label>
                  <span v-if="showCopyNo">
                    &nbsp;&nbsp;<i @click="copy(returnOrder.returnOrderNo)" class="el-icon-document-copy"></i>
                  </span>
                </label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">退货自定义单号:</label><label>&nbsp;&nbsp;&nbsp;{{ returnOrder.returnOrderCode }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">订货单号:</label><label>&nbsp;&nbsp;&nbsp;{{ returnOrder.customerOrderNo }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">订货自定义单号:</label><label>&nbsp;&nbsp;&nbsp;{{ returnOrder.customerOrderCode }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">OMS门店订单号:</label><label>&nbsp;&nbsp;&nbsp;{{ returnOrder.storeOrderCode }}</label>
              </div>

              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">企业:</label><label>&nbsp;&nbsp;&nbsp;{{ returnOrder.enterpriseName }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">仓库:</label><label>&nbsp;&nbsp;&nbsp;{{ returnOrder.warehouseName }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">货主:</label><label>&nbsp;&nbsp;&nbsp;{{ returnOrder.goodsOwnerName }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">收获人:</label><label>&nbsp;&nbsp;&nbsp;{{ returnOrder.customerName }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">状态:</label>
                <span v-if="returnOrder.returnOrderStatus === '已完成'">
                  <span style="color: green;">&nbsp;&nbsp;已完成</span>
                </span>
                <span v-else>
                  &nbsp;&nbsp;{{ returnOrder.returnOrderStatus }}
                </span>
              </div>


              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">完结类型:</label><label>&nbsp;&nbsp;&nbsp;{{ returnOrder.returnOrderFinishType }}</label>
              </div>

              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">创建时间:</label><label>&nbsp;&nbsp;&nbsp;{{ returnOrder.createTimeDesc }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">更新时间:</label><label>&nbsp;&nbsp;&nbsp;{{ returnOrder.updateTimeDesc }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">SQL:</label>
                <label>
                  <span v-if="showCopyNo">
                    &nbsp;&nbsp;SQL&nbsp;&nbsp;<i @click="copy(returnOrder.sql)" class="el-icon-document-copy"></i>
                  </span>
                </label>
              </div>
            </div>
          </div>


          <!-- 退货明细 -->
          <div style="margin-top: 10px;">
            <el-divider content-position="left">退货明细</el-divider>

            <div style="margin-left: 40px; font-weight: 500; font-size: 14px;">
              <template>
                <el-table :data="srodList" border style="width: 100%" :row-style="{ height: 10+'px'}" :cell-style="{padding:0+'px'}"> <!-- height="250" -->
                  <el-table-column fixed label="序号" type="index" width="50"></el-table-column>
                  <el-table-column prop="goodsNo" label="商品编码"></el-table-column>
                  <el-table-column prop="goodsName" label="商品名称" max-width="180" :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="externalGoodsNo" label="OMS商品编码" max-width="180" :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="warehouseOwnerGoodsNo" label="仓库货主商品编码" width="170"></el-table-column>
                  <el-table-column prop="warehouseOwnerGoodsCode" label="自定义编码" min-width="150" :show-overflow-tooltip="true"></el-table-column>

                  <el-table-column align="center" prop="goodsUnitPrice" label="销售单价(元)" width="120"></el-table-column>
                  <el-table-column align="center" prop="goodsValue" label="货值(元)" width="120"></el-table-column>

                  <el-table-column prop="returnQuantity" label="退货数量" width="100"></el-table-column>
                  <el-table-column prop="processingQuantity" label="退货中数" width="100"></el-table-column>

                  <el-table-column label="已退数量" align="center">
                    <el-table-column prop="waitOutReturnQuantity" width="110">
                      <template slot-scope="scope" slot="header">
                        <span>待出库退货数</span>
                      </template>
                    </el-table-column>
                    <el-table-column prop="alreadyOutReturnQuantity" width="110">
                      <template slot-scope="scope" slot="header">
                        <span>已出库退货数</span>
                      </template>
                    </el-table-column>
                  </el-table-column>
                  <el-table-column align="center" prop="extension" label="扩展信息" max-width="120" :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="createTimeStr" label="创建时间" width="200"></el-table-column>
                  <el-table-column prop="updateTimeStr" label="更新时间" width="200"></el-table-column>
                </el-table>
              </template>
            </div>
          </div>

          <!-- 入库单 -->
          <div style="margin-top: 10px;">
            <el-divider content-position="left">入库单</el-divider>

            <div style="margin-left: 40px; font-weight: 500; font-size: 14px;">
              <template>
                <el-table :data="ssList" border style="width: 100%" :row-style="{ height: 10+'px'}" :cell-style="{padding:0+'px'}"> <!-- height="250" -->
                  <el-table-column fixed label="单号" width="180">
                    <template slot-scope="scope">
                      <i @click="copy(scope.row.storageNo)" class="el-icon-document-copy"></i>&nbsp;&nbsp;{{ scope.row.storageNo }}
                    </template>
                  </el-table-column>
                  <el-table-column prop="storageType" label="入库类型" width="80"></el-table-column>
                  <el-table-column label="入库状态" width="80">
                    <template slot-scope="scope">
                      <span v-if="scope.row.storageStatus === '已入库'">
                        <span style="color: green;">{{ scope.row.storageStatus }}</span>
                      </span>
                      <span v-else>
                        <span>{{ scope.row.storageStatus }}</span>
                      </span>
                    </template>
                  </el-table-column>
                  <el-table-column align="center" label="仓库" width="220">
                    <template slot-scope="scope">
                      <span v-if="scope.row.changeWarehouseId == null">
                        <span>原仓: {{ scope.row.warehouseName }}</span>
                      </span>
                      <span v-else>
                        <span style="color: red;">换仓: {{ scope.row.changeWarehouseName }}</span>
                      </span>
                    </template>
                  </el-table-column>

                  <el-table-column prop="sourceOrderNo" label="关联单号"></el-table-column>
                  <el-table-column prop="createTime" label="创建时间" width="200"></el-table-column>
                  <el-table-column prop="updateTime" label="更新时间" width="200"></el-table-column>
                  <el-table-column fixed="right" label="操作" width="210">
                    <template slot-scope="scope">
                      <router-link :to="{path: '/store_storage', query:{storeStorageNo: scope.row.storageNo}}" target="_blank" style="margin-left: 5px;">
                        <span class="icon-link">查看明细</span>
                      </router-link>
                    </template>
                  </el-table-column>
                </el-table>
              </template>
            </div>
          </div>


          <!-- 自动作业记录 -->
          <div style="margin-top: 10px;">
            <el-divider content-position="left">自动作业记录</el-divider>

            <div style="margin-left: 40px; font-weight: 500; font-size: 14px;">
              <template>
                <el-table :data="autoRecordList" border style="width: 100%" :row-style="{ height: 10+'px'}" :cell-style="{padding:0+'px'}"> <!-- height="250" -->
                  <el-table-column fixed label="序号" type="index" width="50"></el-table-column>
                  <el-table-column prop="applicationType" label="类型" width="120" :show-overflow-tooltip="true"></el-table-column>

                  <el-table-column label="状态" width="200">
                    <template slot-scope="scope">
                      <span v-if="scope.row.status === '执行失败'">
                        <span style="color: red;">{{ scope.row.status }}</span>
                      </span>
                      <span v-else>
                          <span>{{ scope.row.status }}</span>
                      </span>
                    </template>
                  </el-table-column>
                  <el-table-column prop="exception" label="异常信息"></el-table-column>
                  <el-table-column prop="createTime" label="创建时间" width="200"></el-table-column>
                  <el-table-column prop="updateTime" label="更新时间" width="200"></el-table-column>
                </el-table>
              </template>
            </div>
          </div>


          <div style="margin-top: 10px;">
            <el-divider content-position="left">MQ消息记录</el-divider>

            <div style="margin-left: 40px; font-weight: 500; font-size: 14px;">
              <template>
                <el-table :data="mqRecordList" border style="width: 100%" :row-style="{ height: 10+'px'}" :cell-style="{padding:0+'px'}"> <!-- height="250" -->
                  <el-table-column fixed label="序号" type="index" width="50"></el-table-column>
                  <el-table-column label="业务单号" width="220" :show-overflow-tooltip="true">
                    <template slot-scope="scope">
                      <el-button @click="handleMqOperationRecordClick(scope.$index, scope.row)" type="text">
                        {{ scope.row.businessNo }}
                      </el-button>
                    </template>
                  </el-table-column>
                  <el-table-column prop="method" label="方法名" min-width="120" :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="messageId" label="MQ消息ID" width="305" :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="remark" label="动作" width="200" :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="desc" label="说明信息" min-width="100" :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="createTimeStr" label="创建时间" width="200"></el-table-column>
                </el-table>

                <el-dialog :title="'[ ' + DETAIL_INDEX + ' ][ ' + Operation_Record_Body_Title + ' ] 内容体'" :visible.sync="Operation_Record_DETAIL_dialogVisible" :show-close="false" width="50%">
                  <div style="display: block; margin: 5px 0;">
                    <label style="display: inline-block; text-align: right;">[ 阿里云ID ]</label><label>&nbsp;&nbsp;&nbsp;{{ operationRecord.messageId }}</label>
                  </div>
                  <div style="display: block; margin: 5px 0;">
                    <label style="display: inline-block; text-align: right;">[ 观测云ID ]</label><label>&nbsp;&nbsp;&nbsp;{{ operationRecord.traceId }}</label>
                  </div>
                  <div style="display: block; margin: 5px 0;">
                    <label style="display: inline-block; text-align: right;">[ 服务名称 ]</label><label>&nbsp;&nbsp;&nbsp;{{ operationRecord.serviceName }}</label>
                  </div>
                  <div style="display: block; margin: 5px 0;">
                    <label style="display: inline-block; text-align: right;">[ 方法名称 ]</label><label>&nbsp;&nbsp;&nbsp;{{ operationRecord.method }}</label>
                  </div>
                  <div style="display: block; margin: 5px 0;">
                    <label style="display: inline-block; text-align: right;">[ 动作名称 ]</label><label>&nbsp;&nbsp;&nbsp;{{ operationRecord.remark }}</label>
                  </div>
                  <div style="display: block; margin: 5px 0;">
                    <label style="display: inline-block; text-align: right;">[ 说明信息 ]</label><label>&nbsp;&nbsp;&nbsp;{{ operationRecord.desc }}</label>
                  </div>
                  <div style="display: block; margin: 5px 0;">
                    <label style="display: inline-block; text-align: right;">[ 请求地址 ]</label><label>&nbsp;&nbsp;&nbsp;{{ operationRecord.sourceIp }}</label>
                  </div>
                  <div style="display: block; margin: 5px 0;">
                    <label style="display: inline-block; text-align: right;">[ 事件地址 ]</label><label>&nbsp;&nbsp;&nbsp;{{ operationRecord.handleIp }}</label>
                  </div>
                </el-dialog>

              </template>
            </div>
          </div>

          <!-- 推送记录 -->
          <div style="margin-top: 10px;">
            <el-divider content-position="left">推送记录</el-divider>

            <div style="margin-left: 40px; font-weight: 500; font-size: 14px;">
              <template>
                <el-table :data="pushRecordList" border style="width: 90%" :row-style="{ height: 10+'px'}"
                          :cell-style="{padding:0+'px'}"> <!-- height="250" -->
                  <el-table-column fixed label="序号" type="index" width="50"></el-table-column>
                  <el-table-column align="center" prop="apiRecordCode" label="记录编码" width="270"></el-table-column>
                  <el-table-column align="center" prop="pushApplicationName" label="平台名称"
                                   width="120"></el-table-column>

                  <el-table-column align="center" label="状态" width="160">
                    <template slot-scope="scope">
                      <span v-if="scope.row.pushStatusName === '处理失败' || scope.row.pushStatusName === '推送失败'">
                        <span style="color: red;">{{ scope.row.pushStatusName }}</span>
                      </span>
                      <span v-else>
                          <span style="color: green;">{{ scope.row.pushStatusName }}</span>
                      </span>
                    </template>
                  </el-table-column>


                  <el-table-column align="center" label="仓库" width="220">
                    <template slot-scope="scope">
                                  <span v-if="scope.row.changeWarehouseName == null">
                                      <span>原仓: {{ scope.row.warehouseName }}</span>
                                  </span>
                      <span v-else>
                                      <span style="color: red;">换仓: {{ scope.row.changeWarehouseName }}</span>
                                  </span>
                    </template>
                  </el-table-column>
                  <el-table-column align="center" prop="pushTypeName" label="类型" min-width="200"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column align="center" prop="pushTimeStr" label="推送时间" min-width="200"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column label="链路ID" width="270">
                    <template slot-scope="scope">
                      <router-link :to="{path: '/select_trace', query:{traceId: scope.row.traceId}}" target="_blank" style="margin-left: 5px;">
                        <span class="icon-link">{{ scope.row.traceId }}</span>
                      </router-link>
                    </template>
                  </el-table-column>
                </el-table>
              </template>
            </div>
          </div>


        </div>

      </el-form>


    </section>
  </div>

</template>

<script>

import Config from '@/assets/js/route.js'
import axios from 'axios';

export default {
  name: "StoreReturnOrder",
  data() {

    return {
      env: Config.env,
      host: Config.host,

      returnOrderCode: '',
      returnOrderNo: '',
      returnOrder: {},
      srodList: [],
      pushRecordList: [],
      autoRecordList: [],
      ssList: [],
      mqRecordList: [],

      select_return_order_no: '',

      sizeOfReturnOrderNo: 0,
      loading: false,
      showCopyNo: false,
      isShowQuery: true,

      tabsData: [],
      activeName: '',

      operationRecord: {},
      DETAIL_INDEX: '',
      Operation_Record_Body_Title: '',
      Operation_Record_DETAIL_dialogVisible: false,

    }
  },
  created: function () {
    let returnOrderNo = this.$route.query.returnOrderNo;
    if (returnOrderNo) {
      this.returnOrderNo = returnOrderNo
      this.select_return_order_no = returnOrderNo
      this.onSubmit(3)
      //this.isShowQuery = false
    }

  },
  methods: {

    handleTabClick(tab, event) {
      this.select_return_order_no = tab.name
      this.onSubmit(1);
    },

    // 列表行有问题的情况下, 标记颜色
    tableRowClassName(row) {
      let r = row.row
      if (r.processedQuantity > r.orderQuantity || r.deliveredQuantity > r.processedQuantity) {
        return "warning-row";
      }
    },


    // 查询
    onSubmit(type) {

      let returnOrderNo = this.select_return_order_no
      if (type === 2) {
        let returnOrderCode = this.returnOrderCode
        if (!returnOrderCode) {
          this.$message({
            message: '单号不能为空',
            type: 'warning'
          });
          return;
        }

        this.loading = true
        this.tabsData = []
        this.select_return_order_no = ''
        let activeName = ''
        this.sizeOfReturnOrderNo = 0
        axios({
          url: this.host + '/toolkit/sro/queryReturnOrderByReturnOrderCode',
          method: 'GET',
          params: {
            returnOrderCode: returnOrderCode
          },
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
          }
        })
        .then(response => {
          if (response.data['code'] && response.data['code'] === 1126) {
            this.$router.push("/login")
            return
          }

          if (response.data) {
            if (response.data.length === 0) {
              this.$message({
                message: '未查询到数据',
                type: 'warning'
              });

              this.loading = false
              return;
            }

            for (let i = 0; i < response.data.length; i++) {
              let label = response.data[i]['returnOrderNo']
              let value = response.data[i]['returnOrderNo']
              this.tabsData.push({'labelName': label, 'tabName': value})
            }

            this.activeName = this.tabsData[0]['tabName']
            this.select_return_order_no = this.tabsData[0]['tabName']
            this.onSubmit(1);

            this.sizeOfReturnOrderNo = response.data.length

          }
        }, error => {
          console.log(error)
          this.$message({
            message: '查询失败',
            type: 'warning'
          });

          this.loading = false
        })
        return;

      } else if (type === 3) {
        let returnOrderNo = this.returnOrderNo
        if (!returnOrderNo) {
          this.$message({
            message: '单号不能为空',
            type: 'warning'
          });
          return;
        }

        this.tabsData = []

        let label = returnOrderNo
        let value = returnOrderNo
        this.tabsData.push({'labelName': label, 'tabName': value})

        this.activeName = returnOrderNo
        this.select_return_order_no = returnOrderNo
        this.onSubmit(1);
        return;
      }


      if (!returnOrderNo) {
        this.$message({
          message: '单号不能为空',
          type: 'warning'
        });
        return;
      }

      this.showCopyNo = false

      this.loading = true
      this.returnOrder = {}
      this.srodList = []
      this.pushRecordList = []
      this.autoRecordList = []
      this.ssList = []
      this.mqRecordList = []

      axios({
        url: this.host + '/toolkit/sro/getReturnOrder',
        method: 'GET',
        params: {
          businessNo: returnOrderNo
        },
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        }
      })
          .then(response => {
            if (response.data['code'] && response.data['code'] === 1126) {
              this.$router.push("/login")
              return
            }

            if (response.data.storeReturnOrder) {
              this.returnOrder = response.data.storeReturnOrder
              this.srodList = response.data.srodList
              this.pushRecordList = response.data.pushRecordList
              this.autoRecordList = response.data.autoRecordList
              this.ssList = response.data.ssList
              this.mqRecordList = response.data.mqRecordList
              this.loading = false


              this.showCopyNo = true

            } else {
              this.loading = false
              this.$message({
                message: '没有数据',
                type: 'warning'
              });
            }
          }, error => {
            console.log(error)
            this.$message({
              message: '查询失败',
              type: 'warning'
            });
            this.loading = false
          })

    },

    handleMqOperationRecordClick(index, row) {
      this.DETAIL_INDEX = index + 1
      this.Operation_Record_Body_Title = row.businessNo

      this.operationRecord = {}

      axios({
        url: this.host + '/toolkit/or/detail',
        method: 'GET',
        params: {
          recordId: row.recordIdStr
        },
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        }
      })
      .then(response => {
        if (response.data['code'] && response.data['code'] === 1126) {
          this.$router.push("/login")
          return
        }

        this.operationRecord = response.data
        this.operationRecord['businessNo'] = row.businessNo
        this.Operation_Record_DETAIL_dialogVisible = true
      }, error => {
        console.log(error)
        this.$message({
          message: '查询失败',
          type: 'warning'
        });
      })
    },


    clearReturnOrderCode() {
      this.returnOrderCode = ''
    },
    clearReturnOrderNo() {
      this.returnOrderNo = ''
    },
    copy(data) {
      let url = data;
      let oInput = document.createElement('textarea');
      oInput.value = url;
      document.body.appendChild(oInput);
      oInput.select(); // 选择对象

      document.execCommand("Copy"); // 执行浏览器复制命令
      this.$message({
        message: '复制成功',
        type: 'success'
      });
      oInput.remove()
    },

  }
}
</script>


<style>
@import '@/assets/css/common.css';

.el-link.el-link--primary {
  color: #0000FF;
}

.icon-link {
  display: inline-block;
  display: inline-table;
  position: relative;
  bottom: 1.5px;
  font-size: 15px;
  margin-left: 7px;
  margin-right: 7px;
}

.el-link.el-link--default {
  color: #0000FF;
}

.el-step__title.is-process {
  font-size: 15px;
}

.el-divider__text.is-left {
  color: #FA8919;
  font-weight: bold;
}

.el-table .warning-row {
  background: #FFFFBB;
}

pre {
  font-family: Microsoft YaHei;
  white-space: pre-wrap;
  word-wrap: break-word;
}
</style>