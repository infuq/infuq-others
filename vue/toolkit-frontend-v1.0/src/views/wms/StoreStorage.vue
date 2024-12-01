<template>
  <div>
    <section class="content clearfix" style="width: 97%;">
      <div class="el-backtop" style="right: 40px; top: 130px;">
        <el-link type="primary" :href="'/'" :underline="false" target="_blank"><i class="el-icon-s-home"></i></el-link>
      </div>
      <el-divider content-position="right">{{ env }}环境</el-divider>

      <el-form :inline="true" class="demo-form-inline">

        <div v-if="isShowQuery">
          <el-form-item label="">
            <el-input v-model="storeStorageNo" placeholder="CK-230715-000003 或 RK-230609-000021" clearable
                      @clear="clearStoreStorageNo" style="width: 330px;"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="onSubmit">查询</el-button>
          </el-form-item>
        </div>


        <!-- 结果 -->
        <div style="margin-top: 15px;">

          <!-- 出入库单 -->
          <div style="margin-top: 10px;" v-loading="loading">
            <el-divider content-position="left">{{ title1 }}</el-divider>

            <div style="margin-left: 40px; font-weight: 500; font-size: 14px;">

              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">单号:</label><label>&nbsp;&nbsp;&nbsp;{{ storeStorage.storageNo }}</label>
                <span v-if="showCopyStorageNo">
                              &nbsp;&nbsp;<i @click="copy(storeStorage.storageNo)" class="el-icon-document-copy"></i>
                          </span>
                </label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">关联单号:</label><label>&nbsp;&nbsp;&nbsp;{{ storeStorage.sourceOrderNo }}</label>
                <span
                    v-if="showCopyStorageNo && storeStorage.sourceOrderNo != null && storeStorage.sourceOrderNo != ''">
                          &nbsp;&nbsp;<i @click="copy(storeStorage.sourceOrderNo)" class="el-icon-document-copy"></i>
                      </span>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">类型:</label><label>&nbsp;&nbsp;&nbsp;{{ storeStorage.storageType }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">状态:</label>
                <span v-if="storeStorage.storageStatus == '已出库' || storeStorage.storageStatus == '已入库'">
                          <span style="color: green;">&nbsp;&nbsp;{{ storeStorage.storageStatus }}</span>
                      </span>
                <span v-else>
                          &nbsp;&nbsp;{{ storeStorage.storageStatus }}
                      </span>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">企业:</label><label>&nbsp;&nbsp;&nbsp;{{ storeStorage.enterpriseName }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">仓库:</label><label>&nbsp;&nbsp;&nbsp;{{ storeStorage.warehouseName }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">货主:</label><label>&nbsp;&nbsp;&nbsp;{{ storeStorage.goodsOwnerName }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">收货人:</label><label>&nbsp;&nbsp;&nbsp;{{ storeStorage.customerName }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">创建人:</label><label>&nbsp;&nbsp;&nbsp;{{ storeStorage.creater }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">供应商:</label><label>&nbsp;&nbsp;&nbsp;{{ storeStorage.supplierName }}</label>
              </div>

              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">创建时间:</label><label>&nbsp;&nbsp;&nbsp;{{ storeStorage.createTime }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">更新时间:</label><label>&nbsp;&nbsp;&nbsp;{{ storeStorage.updateTime }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">SQL:</label><label>
                          <span v-if="showCopySQL">
                              &nbsp;&nbsp;SQL&nbsp;&nbsp;<i @click="copy(storeStorage.sql)"
                                                            class="el-icon-document-copy"></i>
                          </span>
              </label>
              </div>

            </div>
          </div>


          <!-- 出入库明细 -->
          <div style="margin-top: 10px;">
            <el-divider content-position="left">{{ title2 }}</el-divider>

            <div style="margin-left: 40px; font-weight: 500; font-size: 14px;">
              <template>
                <el-table :data="ssdList" border style="width: 90%" :row-style="{ height: 10+'px'}"
                          :cell-style="{padding:0+'px'}"> <!-- height="250" -->
                  <el-table-column fixed label="序号" type="index" width="50"></el-table-column>
                  <el-table-column prop="goodsNo" label="商品编码"></el-table-column>
                  <el-table-column prop="goodsName" label="商品名称" max-width="180"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="externalGoodsNo" label="OMS商品编码" max-width="180"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="warehouseOwnerGoodsNo" label="仓库货主商品编码"></el-table-column>
                  <el-table-column prop="warehouseOwnerGoodsCode" label="自定义编码" min-width="150"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="expectQuantity" label="预期数量"></el-table-column>
                  <el-table-column label="实际数量">
                    <template slot-scope="scope">
                                  <span v-if="scope.row.realQuantity > scope.row.expectQuantity">
                                      <span style="color: red;">{{ scope.row.realQuantity }}</span>
                                  </span>
                      <span v-else>
                                      {{ scope.row.realQuantity }}
                                  </span>
                    </template>
                  </el-table-column>


                  <el-table-column prop="createTimeDesc" label="创建时间" width="200"></el-table-column>
                </el-table>
              </template>
            </div>
          </div>


          <div style="margin-top: 10px;">
            <el-divider content-position="left">自动作业记录</el-divider>

            <div style="margin-left: 40px; font-weight: 500; font-size: 14px;">
              <template>
                <el-table :data="autoRecordList" border style="width: 100%" :row-style="{ height: 10+'px'}"
                          :cell-style="{padding:0+'px'}"> <!-- height="250" -->
                  <el-table-column fixed label="序号" type="index" width="50"></el-table-column>
                  <el-table-column prop="applicationType" label="类型" width="120"
                                   :show-overflow-tooltip="true"></el-table-column>

                  <el-table-column label="状态" width="200">
                    <template slot-scope="scope">
                                  <span v-if="scope.row.status == '执行失败'">
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
                <el-table :data="mqRecordList" border style="width: 100%" :row-style="{ height: 10+'px'}"
                          :cell-style="{padding:0+'px'}"> <!-- height="250" -->
                  <el-table-column fixed label="序号" type="index" width="50"></el-table-column>
                  <el-table-column label="业务单号" width="220" :show-overflow-tooltip="true">
                    <template slot-scope="scope">
                      <el-button @click="handleMqOperationRecordClick(scope.$index, scope.row)" type="text">
                        {{ scope.row.businessNo }}
                      </el-button>
                    </template>
                  </el-table-column>

                  <el-table-column prop="method" label="方法名" min-width="120"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="messageId" label="MQ消息ID" width="305"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="remark" label="动作" width="200"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="desc" label="说明信息" min-width="100"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="createTimeStr" label="创建时间" width="200"></el-table-column>
                </el-table>
              </template>

              <el-dialog :title="'[ ' + DETAIL_INDEX + ' ][ ' + Operation_Record_Body_Title + ' ] 内容体'"
                         :visible.sync="Operation_Record_DETAIL_dialogVisible" :show-close="false" width="50%">

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
                  <el-table-column align="center" prop="recordCode" label="记录编码" width="270"></el-table-column>
                  <el-table-column align="center" prop="pushApplicationName" label="平台名称"
                                   width="120"></el-table-column>

                  <el-table-column align="center" label="状态" width="160">
                    <template slot-scope="scope">
                                  <span
                                      v-if="scope.row.pushStatusName == '处理失败' || scope.row.pushStatusName == '推送失败'">
                                      <span style="color: red;">{{ scope.row.pushStatusName }}</span>
                                  </span>
                      <span v-else>
                                      <span style="color: green;">{{ scope.row.pushStatusName }}</span>
                                  </span>
                    </template>
                  </el-table-column>
                  <el-table-column align="center" prop="pushTypeName" label="类型" min-width="200"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column align="center" prop="pushTime" label="推送时间" min-width="150"
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
  name: "StoreStorage",
  data() {

    return {
      env: Config.env,
      host: Config.host,

      storeStorageNo: '',
      title1: '出库单/入库单',
      title2: '出库明细/入库明细',

      storeStorage: {
        storageId: '',
        enterpriseId: '',
        enterpriseName: '',
        warehouseId: '',
        warehouseName: '',
        changeWarehouseId: '',
        changeWarehouseName: '',
        storageNo: '',
        creater: '',
        goodsOwnerId: '',
        supplierId: '',
        customerId: '',
        storageCategory: '',
        fixedTime: '',
        sourceOrderId: '',
        sourceOrderNo: '',
        storageType: '',
        storageTypeStr: '',
        storageStatus: '',
        storageStatusStr: '',
        storageCode: '',
        operator: '',
        storageDesc: '',
        shelveEnable: '',
        shelveTime: '',
        version: '',
        createTime: '',
        updateTime: '',
      },

      ssdList: [],
      autoRecordList: [],
      mqRecordList: [],
      pushRecordList: [],
      showCopySQL: false,

      loading: false,
      showCopyStorageNo: false,
      showCopySourceNo: false,
      isShowQuery: true,

      operationRecord: {},
      DETAIL_INDEX: '',
      Operation_Record_Body_Title: '',
      Operation_Record_DETAIL_dialogVisible: false,

    }
  },

  created: function () {

    let storeStorageNo = this.$route.query.storeStorageNo;

    if (storeStorageNo) {
      this.storeStorageNo = storeStorageNo
      this.onSubmit()
      //this.isShowQuery = false
    }

  },
  methods: {
    // 查询
    onSubmit() {

      if (!this.storeStorageNo) {
        this.$message({
          message: '单号不能为空',
          type: 'warning'
        });
        return;
      }

      this.showCopyStorageNo = false
      this.showCopySourceNo = false


      this.loading = true
      this.storeStorage = {}
      this.ssdList = []
      this.autoRecordList = []
      this.mqRecordList = []
      this.pushRecordList = []
      this.showCopySQL = false

      this.title1 = '出库单/入库单'
      this.title2 = '出库明细/入库明细'

      axios({
        url: this.host + '/toolkit/ss/getStoreStorage',
        method: 'GET',
        params: {
          storeStorageNo: this.storeStorageNo
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

        if (response.data.ss) {
          this.storeStorage = response.data.ss
          this.ssdList = response.data.ssdList
          this.autoRecordList = response.data.autoRecordList
          this.mqRecordList = response.data.mqRecordList
          this.pushRecordList = response.data.pushRecordList
          this.loading = false

          if (this.storeStorage.isRK === 1) {
            this.title1 = '入库单'
            this.title2 = '入库明细'
          } else {
            this.title1 = '出库单'
            this.title2 = '出库明细'
          }
          this.showCopyStorageNo = true
          if (response.data.ss.sourceOrderNo) {
            this.showCopySourceNo = true
          }

          this.showCopySQL = true


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


    clearStoreStorageNo() {
      this.storeStorageNo = ''
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