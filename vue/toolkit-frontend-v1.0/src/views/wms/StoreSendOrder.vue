<template>
  <div>
    <section class="content clearfix" style="width: 97%;">
      <div class="el-backtop" style="right: 40px; top: 130px;">
        <el-link type="primary" :href="'/'" :underline="false" target="_blank"><i class="el-icon-s-home"></i></el-link>
      </div>
      <el-divider content-position="right">{{ env }}环境</el-divider>


      <el-form :inline="true" class="demo-form-inline">

        <div v-if="isShowQuery">
          <el-input v-model="businessNo" placeholder="FH-230828-002610" clearable @clear="clearBusinessNo"
                    style="width: 330px;">
            <template slot="prepend">发货单号</template>
          </el-input>
          <div style="display: inline-block; margin-top: 3px; margin-bottom: 3px; margin-left: 5px;">
            <el-button type="primary" @click="onSubmit">查询</el-button>
          </div>
        </div>

        <!-- 结果 -->
        <div style="margin-top: 15px;">

          <!-- 发货单 -->
          <div style="margin-top: 10px;" v-loading="loading">
            <el-divider content-position="left">发货单</el-divider>

            <div style="margin-left: 40px; font-weight: 500; font-size: 14px;">

              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">发货单号:</label><label>&nbsp;&nbsp;&nbsp;{{ sendOrder.sendOrderNo }}</label>
                <span v-if="showCopyNo">
                              &nbsp;&nbsp;<i @click="copy(sendOrder.sendOrderNo)" class="el-icon-document-copy"></i>
                          </span>
                </label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">订货单号:</label><label>&nbsp;&nbsp;&nbsp;{{ sendOrder.customerOrderNo }}</label>
                <span v-if="showCopyNo">
                              &nbsp;&nbsp;<i @click="copy(sendOrder.customerOrderNo)" class="el-icon-document-copy"></i>
                          </span>
                </label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">送货单号:</label><label>&nbsp;&nbsp;&nbsp;{{ sendOrder.deliveryOrderNo }}</label>
                <span v-if="showCopyDeliveryOrderNo">
                              &nbsp;&nbsp;<i @click="copy(sendOrder.deliveryOrderNo)" class="el-icon-document-copy"></i>
                          </span>
                </label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">状态:</label>
                <span v-if="sendOrder.sendOrderStatusName == '已发货'">
                          <span style="color: green;">&nbsp;&nbsp;已发货</span>
                      </span>
                <span v-else>
                          &nbsp;&nbsp;{{ sendOrder.sendOrderStatusName }}
                      </span>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">企业:</label><label>&nbsp;&nbsp;&nbsp;{{ sendOrder.enterpriseName }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">仓库:</label><label>&nbsp;&nbsp;&nbsp;{{ sendOrder.warehouseName }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">货主:</label><label>&nbsp;&nbsp;&nbsp;{{ sendOrder.goodsOwnerName }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">收货人:</label><label>&nbsp;&nbsp;&nbsp;{{ sendOrder.customerName }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">创建人:</label><label>&nbsp;&nbsp;&nbsp;{{ sendOrder.creater }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">运输类型:</label><label>&nbsp;&nbsp;&nbsp;{{ sendOrder.tmsTypeName }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">运输单号:</label><label>&nbsp;&nbsp;&nbsp;{{ sendOrder.tmsNo }}</label>
              </div>
              <span v-if="isTran">
                      <div style="width: 400px; display: block; margin: 5px 0;">
                          <label style="display: inline-block; width: 110px; text-align: right;">车次状态:</label>
                          <span v-if="sendOrder.tranStatus == '已发车'">
                              <span style="color: green;">&nbsp;&nbsp;已发车</span>
                          </span>
                          <span v-else>
                              &nbsp;&nbsp;{{ sendOrder.tranStatus }}
                          </span>
                      </div>
                  </span>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">发货时间:</label><label>&nbsp;&nbsp;&nbsp;{{ sendOrder.sendOrderTimeDesc }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">创建时间:</label><label>&nbsp;&nbsp;&nbsp;{{ sendOrder.createTimeDesc }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">更新时间:</label><label>&nbsp;&nbsp;&nbsp;{{ sendOrder.updateTimeDesc }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">SQL:</label><label>
                      <span v-if="showCopyNo">
                          &nbsp;&nbsp;SQL&nbsp;&nbsp;<i @click="copy(sendOrder.sql)" class="el-icon-document-copy"></i>
                      </span>
              </label>
              </div>
            </div>
          </div>


          <!-- 发货明细 -->
          <div style="margin-top: 10px;">
            <el-divider content-position="left">发货明细</el-divider>

            <div style="margin-left: 40px; font-weight: 500; font-size: 14px;">
              <template>
                <el-table :data="sodList" border style="width: 90%" :row-style="{ height: 10+'px'}"
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
                  <el-table-column prop="sendQuantity" label="发货数量"></el-table-column>
                  <el-table-column prop="realSendQuantity" label="实货数量"></el-table-column>
                  <el-table-column prop="createTime" label="创建时间" width="200"></el-table-column>
                </el-table>
              </template>
            </div>
          </div>

          <!-- 发货操作记录(不完整) -->
          <!--                    <div style="margin-top: 10px;">-->
          <!--                        <el-divider content-position="left">发货操作记录(不完整)</el-divider>-->

          <!--                        <div style="margin-left: 40px; font-weight: 500; font-size: 14px;">-->
          <!--                            <template>-->
          <!--                                <el-table :data="operationRecordList" border style="width: 100%" :row-style="{ height: 10+'px'}" :cell-style="{padding:0+'px'}"> &lt;!&ndash; height="250" &ndash;&gt;-->
          <!--                                    <el-table-column fixed label="序号" type="login" width="50"></el-table-column>-->
          <!--                                    <el-table-column prop="userName" label="用户名" width="100"></el-table-column>-->
          <!--                                    <el-table-column prop="realName" label="实名" width="100"></el-table-column>-->
          <!--                                    <el-table-column prop="moduleName" label="模块名" width="170"></el-table-column>-->
          <!--                                    <el-table-column prop="remark" label="动作" max-width="200" :show-overflow-tooltip="true"></el-table-column>-->
          <!--                                    <el-table-column prop="businessNo" label="业务单号" max-width="220" :show-overflow-tooltip="true"></el-table-column>-->
          <!--                                    <el-table-column prop="businessIdStr" label="业务主键" max-width="220" :show-overflow-tooltip="true"></el-table-column>-->
          <!--                                    <el-table-column prop="method" label="方法名" min-width="150" :show-overflow-tooltip="true"></el-table-column>-->
          <!--                                    <el-table-column prop="sourceName" label="请求来源" width="120"></el-table-column>-->

          <!--                                    <el-table-column prop="desc" label="说明信息" max-width="100" :show-overflow-tooltip="true"></el-table-column>-->
          <!--                                    <el-table-column prop="createTimeStr" label="访问时间" width="200"></el-table-column>-->
          <!--                                </el-table>-->
          <!--                            </template>-->
          <!--                        </div>-->
          <!--                    </div>-->


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
                                  <span
                                      v-if="scope.row.pushStatusName == '处理失败' || scope.row.pushStatusName == '推送失败'">
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
  name: "StoreSendOrder",
  data() {

    return {
      env: Config.env,
      host: Config.host,

      businessNo: '',
      sendOrder: {},
      sodList: [],
      operationRecordList: [],
      pushRecordList: [],
      autoRecordList: [],
      mqRecordList: [],

      loading: false,
      showCopyNo: false,
      showCopyDeliveryOrderNo: false,
      isTran: false,
      isShowQuery: true,

      operationRecord: {},
      DETAIL_INDEX: '',
      Operation_Record_Body_Title: '',
      Operation_Record_DETAIL_dialogVisible: false,


    }
  },


  created: function () {
    let sendOrderNo = this.$route.query.sendOrderNo;
    if (sendOrderNo) {
      this.businessNo = sendOrderNo
      this.onSubmit()
      // this.isShowQuery = false
    }
  },
  methods: {
    // 查询
    onSubmit() {
      if (!this.businessNo) {
        this.$message({
          message: '单号不能为空',
          type: 'warning'
        });
        return;
      }

      let success = this.businessNo.search(/^FH-\d{6}-\d{6}$/g)
      if (success !== 0) {
        this.$message({
          message: '单号格式不正确',
          type: 'warning'
        });
        return;
      }

      this.showCopyNo = false
      this.showCopyDeliveryOrderNo = false
      this.isTran = false


      this.loading = true
      this.sendOrder = {}
      this.sodList = []
      this.operationRecordList = []
      this.pushRecordList = []
      this.autoRecordList = []
      this.mqRecordList = []

      axios({
        url: this.host + '/toolkit/sso/getSendOrder',
        method: 'GET',
        params: {
          businessNo: this.businessNo
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

        if (response.data.sendOrder) {
          this.sendOrder = response.data.sendOrder
          this.sodList = response.data.sodList
          this.operationRecordList = response.data.operationRecordList
          this.pushRecordList = response.data.pushRecordList
          this.autoRecordList = response.data.autoRecordList
          this.mqRecordList = response.data.mqRecordList
          this.loading = false

          if (response.data.sendOrder.deliveryOrderNo) {
            this.showCopyDeliveryOrderNo = true
          }
          if (response.data.sendOrder.tmsTypeName === '城配') {
            this.isTran = true
          }

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


    clearBusinessNo() {
      this.businessNo = ''
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