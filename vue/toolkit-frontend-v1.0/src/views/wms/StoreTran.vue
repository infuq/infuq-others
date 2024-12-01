<template>
  <div>
    <section class="content clearfix" style="width: 97%;">
      <div class="el-backtop" style="right: 40px; top: 130px;">
        <el-link type="primary" :href="'/'" :underline="false" target="_blank"><i class="el-icon-s-home"></i></el-link>
      </div>
      <el-divider content-position="right">{{ env }}环境</el-divider>

      <el-form :inline="true" class="demo-form-inline">
        <div>
          <el-form-item label="">
            <el-input v-model="tranNo" placeholder="230821-00001" clearable @clear="clearTranNo"
                      style="width: 300px;"></el-input>
          </el-form-item>

          <el-form-item label="">
            <el-button type="primary" @click="onSubmit">查询</el-button>
          </el-form-item>

        </div>

        <!-- 结果 -->
        <div style="margin-top: 15px;">

          <!-- 车次信息 -->
          <div style="margin-top: 10px;" v-loading="loading">
            <el-divider content-position="left">车次信息</el-divider>

            <div style="margin-left: 40px; font-weight: 500; font-size: 14px;">

              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">车次编号:</label><label>&nbsp;&nbsp;&nbsp;{{ storeTran.tranNo }}</label>
                <span v-if="showCopyTranNo">
                              <i @click="copy(storeTran.tranNo)" class="el-icon-document-copy"></i>
                          </span>
                </label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">状态:</label>
                <span v-if="storeTran.tranStatusStr == '已发车'">
                          <span style="color: green;">&nbsp;&nbsp;已发车</span>
                      </span>
                <span v-else>
                          &nbsp;&nbsp;{{ storeTran.tranStatusStr }}
                      </span>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">发车时间:</label><label>&nbsp;&nbsp;&nbsp;{{ storeTran.departTimeStr }}</label>
              </div>
              <span v-if="storeTran.tranStatusStr == '未发车'">
                      <div style="width: 400px; display: block; margin: 5px 0;">
                          <label
                              style="display: inline-block; width: 110px; text-align: right;">距离发车时间:</label><label>&nbsp;&nbsp;&nbsp;{{ storeTran.diffDepartTimeStr }}分钟 <i
                          class="el-icon-time"></i></label>
                      </div>
                  </span>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">车牌号码:</label><label>&nbsp;&nbsp;&nbsp;{{ storeTran.truckNumber }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">企业:</label><label>&nbsp;&nbsp;&nbsp;{{ storeTran.enterpriseName }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">仓库:</label><label>&nbsp;&nbsp;&nbsp;{{ storeTran.warehouseName }}</label>
              </div>

              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">车主:</label><label>&nbsp;&nbsp;&nbsp;{{ storeTran.truckOwner }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">司机:</label><label>&nbsp;&nbsp;&nbsp;{{ storeTran.driverName }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">创建时间:</label><label>&nbsp;&nbsp;&nbsp;{{ storeTran.createTimeStr }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">修改时间:</label><label>&nbsp;&nbsp;&nbsp;{{ storeTran.updateTimeStr }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">SQL:</label><label>
                          <span v-if="showCopySQL">
                              &nbsp;&nbsp;SQL&nbsp;&nbsp;<i @click="copy(storeTran.sql)"
                                                            class="el-icon-document-copy"></i>
                          </span>
              </label>
              </div>
            </div>
          </div>


          <!-- 发货单信息 -->
          <div style="margin-top: 10px;">
            <el-divider content-position="left">发货单信息</el-divider>

            <div style="margin-left: 40px; font-weight: 500; font-size: 14px;">
              <template>
                <el-table :data="storeSendOrderList" border style="width: 90%" :row-style="{ height: 10+'px'}"
                          :cell-style="{padding:0+'px'}"> <!-- height="250" -->
                  <el-table-column fixed label="序号" type="index" width="50"></el-table-column>
                  <el-table-column label="发货单号" width="200">
                    <template slot-scope="scope">
                      <i @click="copy(scope.row.sendOrderNo)" class="el-icon-document-copy"></i>&nbsp;&nbsp;
                      <router-link :to="{path: '/store_send_order', query:{sendOrderNo: scope.row.sendOrderNo}}" target="_blank" style="margin-left: 5px;">
                        <span class="icon-link">{{ scope.row.sendOrderNo }}</span>
                      </router-link>
                    </template>
                  </el-table-column>
                  <el-table-column label="发货状态" width="100">
                    <template slot-scope="scope">
                                  <span v-if="scope.row.sendOrderStatus == '已发货'">
                                      <span style="color: green;">{{ scope.row.sendOrderStatus }}</span>
                                  </span>
                      <span v-else>
                                      <span>{{ scope.row.sendOrderStatus }}</span>
                                  </span>
                    </template>
                  </el-table-column>
                  <el-table-column prop="tmsType" label="运输类型" width="100"></el-table-column>
                  <el-table-column prop="deliveryOrderNo" label="送货单号" width="200"></el-table-column>
                  <el-table-column prop="sendOrderDesc" label="发货备注" max-width="100"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="sendOrderTime" label="发货时间" width="200"></el-table-column>
                  <el-table-column prop="createTime" label="创建时间" width="200"></el-table-column>
                  <el-table-column prop="updateTime" label="更新时间" width="200"></el-table-column>
                </el-table>
              </template>
            </div>
          </div>

          <!-- 商品明细 -->
          <div style="margin-top: 10px;">
            <el-divider content-position="left">商品明细</el-divider>

            <div style="margin-left: 40px; font-weight: 500; font-size: 14px;">
              <template>
                <el-table :data="handle()" border style="width: 100%" :row-style="{ height: 10+'px'}"
                          :cell-style="{padding:0+'px'}"> <!-- height="250" -->
                  <el-table-column fixed label="序号" type="index" width="50"></el-table-column>
                  <el-table-column prop="goodsNo" label="商品编码"></el-table-column>
                  <el-table-column prop="goodsName" label="商品名称" max-width="180"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="externalGoodsNo" label="OMS商品编码" width="160"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="warehouseOwnerGoodsNo" label="仓库货主商品编码" width="160"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="warehouseOwnerGoodsCode" label="自定义编码" min-width="150"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column min-width="150" :show-overflow-tooltip="true">
                    <template slot="header" slot-scope="scope">
                      <el-input v-model="search" size="medium" placeholder="发货单号搜索" clearable/>
                    </template>
                    <template slot-scope="scope">
                      <span>{{ scope.row.sendOrderNo }}</span>
                    </template>
                  </el-table-column>
                  <el-table-column prop="sendQuantity" label="发货数量"></el-table-column>
                  <el-table-column prop="realSendQuantity" label="实货数量"></el-table-column>
                  <el-table-column prop="createTimeDesc" label="创建时间" width="200"></el-table-column>
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
  name: "StoreTran",
  data() {

    return {
      env: Config.env,
      host: Config.host,

      showCopyTranNo: false,
      tranNo: '',
      storeTran: {},

      storeSendOrderList: [],
      mqRecordList: [],
      sodList: [],
      search: '',

      loading: false,
      showCopySQL: false,

      operationRecord: {},
      DETAIL_INDEX: '',
      Operation_Record_Body_Title: '',
      Operation_Record_DETAIL_dialogVisible: false,

    }
  },


  created: function () {
    let tmsNo = this.$route.query.tmsNo;
    if (tmsNo) {
      this.tranNo = tmsNo
      this.onSubmit()
    }
  },
  methods: {
    // 查询
    onSubmit() {

      if (!this.tranNo) {
        this.$message({
          message: '单号不能为空',
          type: 'warning'
        });
        return;
      }

      this.loading = true
      this.storeTran = {}
      this.storeSendOrderList = []
      this.mqRecordList = []
      this.sodList = []
      this.showCopyTranNo = false
      this.showCopySQL = false

      axios({
        url: this.host + '/toolkit/st/getStoreTran',
        method: 'GET',
        params: {
          tranNo: this.tranNo
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

        if (response.data.storeTran) {
          this.storeTran = response.data.storeTran
          this.storeSendOrderList = response.data.storeSendOrderList
          this.mqRecordList = response.data.mqRecordList
          this.sodList = response.data.sodList
          this.loading = false
          this.showCopyTranNo = true

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

    handle() {
      return this.sodList.filter(data => {

        if (this.search) {
          let allKey = this.search.toLowerCase().split(',');
          for (let i = 0; i < allKey.length; i++) {
            if (data.sendOrderNo.toLowerCase().includes(allKey[i].toLowerCase())) {
              return true;
            }
          }
          return false;
        }

        return true;
      })
    },

    clearTranNo() {
      this.tranNo = ''
      this.storeTran = {}
      this.storeSendOrderList = []
      this.mqRecordList = []
      this.sodList = []
      this.showCopyTranNo = false
      this.showCopySQL = false
    },

    // 当前日期格式化
    dateFormat() {
      let date = new Date()
      let year = date.getFullYear()
      let month = date.getMonth() + 1 < 10 ? '0' + (date.getMonth() + 1) : date.getMonth() + 1
      let day = date.getDate() < 10 ? '0' + date.getDate() : date.getDate()
      return year + '-' + month + '-' + day
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