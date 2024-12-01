<template>
  <div>
    <section class="content clearfix" style="width: 97%;">
      <div class="el-backtop" style="right: 40px; top: 130px;">
        <el-link type="primary" :href="'/'" :underline="false" target="_blank"><i class="el-icon-s-home"></i></el-link>
      </div>
      <el-divider content-position="right">{{ env }}环境</el-divider>

      <el-form :inline="true" class="demo-form-inline">

        <div style="display: inline-block; margin-top: 3px; margin-bottom: 3px;">
          <div style="display: inline-block;
              background-color: rgb(245, 247, 250);
              color: rgb(144, 147, 153);
              border: 1px solid rgb(220, 223, 230);
              border-radius: 4px 0px 0px 4px;
              height: 40px;
              width: 50px;
              vertical-align: middle;
              text-align: center;
              margin-top: auto;
              margin-right: -6px;
              padding-top: 9px;
              font-size: 14px;">
            企业
          </div>
          <el-select v-model="select_enterprise" placeholder="请选择企业" @change="selectEnterprise(select_enterprise)"
                     filterable clearable @clear="clearEnterprise">
            <el-option v-for="item in EnterpriseOptions" :key="item.value" :label="item.label"
                       :value="item.value"></el-option>
          </el-select>
        </div>


        <div style="display: inline-block; margin-top: 3px; margin-bottom: 3px; margin-left: 5px;">
          <div style="display: inline-block;
              background-color: rgb(245, 247, 250);
              color: rgb(144, 147, 153);
              border: 1px solid rgb(220, 223, 230);
              border-radius: 4px 0px 0px 4px;
              height: 40px;
              width: 50px;
              vertical-align: middle;
              text-align: center;
              margin-top: auto;
              margin-right: -6px;
              padding-top: 9px;
              font-size: 14px;">
            仓库
          </div>
          <el-select v-model="select_warehouse" placeholder="请选择仓库" filterable clearable @clear="clearWarehouse">
            <el-option v-for="item in WarehouseOptions" :key="item.value" :label="item.label"
                       :value="item.value"></el-option>
          </el-select>
        </div>

        <el-input v-model="thirdNo" placeholder="三方单号" clearable @clear="clearThirdNo"
                  style="width: 380px; margin-left: 5px;">
          <template slot="prepend">三方单号</template>
        </el-input>
        <el-input v-model="businessNo" placeholder="业务单号" clearable @clear="clearBusinessNo"
                  style="width: 380px; margin-left: 5px;">
          <template slot="prepend">业务单号</template>
        </el-input>

        <el-input v-model="recordCode" placeholder="记录编码" clearable @clear="clearRecordCode"
                  style="width: 380px; margin-left: 5px;">
          <template slot="prepend">记录编码</template>
        </el-input>


        <div style="display: inline-block; margin-top: 3px; margin-bottom: 3px; margin-left: 5px;">
          <div style="display: inline-block;
              background-color: rgb(245, 247, 250);
              color: rgb(144, 147, 153);
              border: 1px solid rgb(220, 223, 230);
              border-radius: 4px 0px 0px 4px;
              height: 40px;
              width: 50px;
              vertical-align: middle;
              text-align: center;
              margin-top: auto;
              margin-right: -6px;
              padding-top: 9px;
              font-size: 14px;">
            目标
          </div>


          <el-select v-model="select_application" placeholder="请选择目标平台"
                     @change="selectApplication(select_application)" filterable clearable @clear="clearApplication">
            <el-option v-for="item in ApplicationOptions" :key="item.value" :label="item.label"
                       :value="item.value"></el-option>
          </el-select>
        </div>


        <div style="display: inline-block; margin-top: 3px; margin-bottom: 3px; margin-left: 5px;">
          <div style="display: inline-block;
              background-color: rgb(245, 247, 250);
              color: rgb(144, 147, 153);
              border: 1px solid rgb(220, 223, 230);
              border-radius: 4px 0px 0px 4px;
              height: 40px;
              width: 50px;
              vertical-align: middle;
              text-align: center;
              margin-top: auto;
              margin-right: -6px;
              padding-top: 9px;
              font-size: 14px;">
            类型
          </div>

          <el-select v-model="select_pushType" placeholder="请选择推送类型" @change="selectPushType(select_pushType)"
                     filterable clearable @clear="clearPushType">
            <el-option v-for="item in PushTypeOptions" :key="item.value" :label="item.label"
                       :value="item.value"></el-option>
          </el-select>
        </div>


        <div style="display: inline-block; margin-top: 3px; margin-bottom: 3px; margin-left: 5px;">
          <div style="display: inline-block;
              background-color: rgb(245, 247, 250);
              color: rgb(144, 147, 153);
              border: 1px solid rgb(220, 223, 230);
              border-radius: 4px 0px 0px 4px;
              height: 40px;
              width: 50px;
              vertical-align: middle;
              text-align: center;
              margin-top: auto;
              margin-right: -6px;
              padding-top: 9px;
              font-size: 14px;">
            状态
          </div>

          <el-select v-model="select_pushStatus" placeholder="请选择状态" @change="selectPushStatus(select_pushStatus)"
                     filterable clearable @clear="clearPushStatus">
            <el-option v-for="item in PushStatusOptions" :key="item.value" :label="item.label"
                       :value="item.value"></el-option>
          </el-select>
        </div>

        <div>
          <el-input v-model="pushBeginTime" placeholder="2023-03-21 09:01:00" clearable @clear="clearPushBeginTime"
                    style="width: 300px; margin-left: 5px;">
            <template slot="prepend">起时间</template>
          </el-input>
          <el-input v-model="pushEndTime" placeholder="2023-03-21 18:12:20" clearable @clear="clearPushEndTime"
                    style="width: 300px; margin-left: 5px;">
            <template slot="prepend">止时间</template>
          </el-input>
          <div style="display: inline-block; margin-top: 3px; margin-bottom: 3px; margin-left: 5px;">
            <el-button type="primary" @click="onSubmit(-1)">查询</el-button>
          </div>
        </div>


        <!-- 结果 -->
        <div style="margin-top: 15px;">

          <!-- 推送结果 -->
          <div style="margin-top: 10px;" v-loading="loading">
            <el-divider content-position="left">WMS推送记录</el-divider>

            <div style="font-weight: 500; font-size: 14px;">
              <template>
                <el-table :data="pushList" border style="width: 100%" :row-style="{ height: 10+'px'}"
                          :cell-style="{padding:0+'px'}" highlight-current-row @current-change="handleTableChange">
                  <!-- height="250" -->
                  <el-table-column fixed label="序号" type="index" width="50">
                    <template slot-scope="scope">
                                  <span v-if="scope.row.pushStatusName == '处理失败'">
                                      <span style="color: red;">{{ scope.$index + 1 }}</span>
                                  </span>
                      <span v-else>
                                      {{ scope.$index + 1 }}
                                  </span>
                    </template>
                  </el-table-column>
                  <el-table-column prop="warehouseName" label="仓库名称" max-width="220"
                                   :show-overflow-tooltip="true"></el-table-column>

                  <el-table-column label="业务单号" max-width="220" :show-overflow-tooltip="true">
                    <template slot-scope="scope" v-if="scope.row.businessNo != null && scope.row.businessNo != ''">
                                  <span>
                                      <i @click="copy(scope.row.businessNo)" class="el-icon-document-copy"></i>&nbsp;&nbsp;{{ scope.row.businessNo }}
                                  </span>
                    </template>
                  </el-table-column>
                  <el-table-column label="三方单号" max-width="220" :show-overflow-tooltip="true">
                    <template slot-scope="scope" v-if="scope.row.thirdNo != null && scope.row.thirdNo != ''">
                                  <span>
                                      <i @click="copy(scope.row.thirdNo)" class="el-icon-document-copy"></i>&nbsp;&nbsp;{{ scope.row.thirdNo }}
                                  </span>
                    </template>
                  </el-table-column>
                  <el-table-column prop="pushApplicationName" label="推送目标" width="200"></el-table-column>
                  <el-table-column prop="pushTypeName" label="推送类型" width="200"></el-table-column>
                  <el-table-column label="推送状态" width="120">
                    <template slot-scope="scope">
                                  <span
                                      v-if="scope.row.pushStatusName == '处理失败' || scope.row.pushStatusName == '推送失败'">
                                      <span style="color: red;">{{ scope.row.pushStatusName }}</span>
                                  </span>
                      <span v-else>
                                      {{ scope.row.pushStatusName }}
                                  </span>
                    </template>
                  </el-table-column>
                  <el-table-column prop="createTime" label="创建时间" width="200"></el-table-column>
                  <el-table-column prop="updateTime" label="更新时间" width="200"></el-table-column>
                  <el-table-column fixed="right" label="操作">
                    <template slot-scope="scope">
                      <el-button @click="handlePushDetailClick(scope.row)" type="text">查看</el-button>
                      <span
                          v-if="scope.row.pushStatusName == '推送失败' || scope.row.pushStatusName == '处理失败' || scope.row.pushStatusName == '待处理'">
                                      <el-button @click="handlePushRetryClick(scope.row)" type="text">重试</el-button>
                                  </span>
                    </template>
                  </el-table-column>
                </el-table>
              </template>


              <el-dialog :title="'[ ' + Record_Body_Title + ' ] 内容体'" :visible.sync="Record_Body_dialogVisible"
                         :show-close="false" width="50%">
                <div style="display: block; margin: 5px 0;">
                  <label style="display: inline-block; text-align: right;">[ 记录编码 ]</label><label>&nbsp;&nbsp;&nbsp;{{ pushRecord.apiRecordCode }}</label>&nbsp;&nbsp;<i
                    @click="copy(pushRecord.apiRecordCode)" class="el-icon-document-copy"></i>
                </div>
                <div style="display: block; margin: 5px 0;">
                  <label style="display: inline-block; text-align: right;">[ 推送内容 ]</label><label>&nbsp;&nbsp;&nbsp;{{ pushRecord.pushBody }}</label>
                  <span v-if="pushRecord.pushBody != null && pushRecord.pushBody != ''">
                              &nbsp;&nbsp;<i @click="copy(pushRecord.pushBody)" class="el-icon-document-copy"></i>
                          </span>
                </div>
                <div style="display: block; margin: 5px 0;">
                  <label style="display: inline-block; text-align: right;">[ 响应内容 ]</label><label>&nbsp;&nbsp;&nbsp;{{ pushRecord.responseBody }}</label>
                  <span v-if="pushRecord.responseBody != null && pushRecord.responseBody != ''">
                              &nbsp;&nbsp;<i @click="copy(pushRecord.responseBody)" class="el-icon-document-copy"></i>
                          </span>
                </div>
                <div style="display: block; margin: 5px 0;">
                  <label style="display: inline-block; text-align: right;">[ 备注内容 ]</label><label>&nbsp;&nbsp;&nbsp;{{ pushRecord.remark }}</label>
                </div>
              </el-dialog>
            </div>
          </div>

          <div style="text-align: center; margin-top: 10px;">
            <el-pagination
                background
                layout="prev, pager, next"
                :current-page.sync="curPage"
                :total="total" @current-change="handleCurrentChange">
            </el-pagination>
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
  name: "PushRecordOld",
  data() {

    return {
      env: Config.env,
      host: Config.host,

      select_enterprise: '',
      select_warehouse: '',
      select_application: '',
      select_pushType: '',
      select_pushStatus: '',
      EnterpriseOptions: [],
      WarehouseOptions: [],
      ApplicationOptions: [
        {
          label: '伟添',
          value: 'APP-00005'
        },
        {
          label: '蜀海',
          value: 'APP-00003'
        },
      ],
      PushTypeOptions: [
        {
          label: '采购单推送',
          value: 1,
        },
        {
          label: '订货单推送',
          value: 4,
        },


      ],
      PushStatusOptions: [
        {
          label: '待推送',
          value: '1'
        },
        {
          label: '已推送',
          value: '2'
        },
        {
          label: '推送失败',
          value: '3'
        },
        {
          label: '创建成功',
          value: '4'
        },
        {
          label: '待处理',
          value: '6'
        },
        {
          label: '处理失败',
          value: '7'
        },
        {
          label: '取消推送',
          value: '99'
        },
        {
          label: '已完成',
          value: '100'
        },
      ],
      businessNo: '',
      thirdNo: '',
      businessNo: '',
      recordCode: '',

      pushBeginTime: this.dateFormat() + " 00:00:00",
      pushEndTime: this.dateFormat() + " 23:59:59",


      pushList: [],

      loading: false,

      total: 0,
      curPage: 1,

      Record_Body_Title: '',
      Record_Body_dialogVisible: false,
      pushRecord: {
        pushBody: '',
        actionBody: '',
        finishBody: '',
        receiptBody: ''
      },
      currentRow: null,

    }
  },

  created: function () {

    // 获取所有企业
    axios({
      url: this.host + '/toolkit/tools/getAllEnterprise',
      method: 'GET',
      params: {},
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
          let EnterpriseList = response.data

          for (let i = 0; i < EnterpriseList.length; i++) {
            let label = EnterpriseList[i]['enterpriseName']
            let value = EnterpriseList[i]['enterpriseCode']
            this.EnterpriseOptions.push({'label': label, 'value': value})
          }

        }, error => {
          this.$message({
            message: '查询企业失败',
            type: 'warning'
          });

        })

  },
  methods: {
    // 查询
    onSubmit(curPage) {
      let select_enterprise = this.select_enterprise

      this.pushList = []

      if (curPage == -1) {
        this.curPage = 1
      }
      this.loading = true
      axios({
        url: this.host + '/toolkit/tools/getPushRecord2',
        method: 'POST',
        data: {
          enterpriseCode: this.select_enterprise,
          warehouseCode: this.select_warehouse,
          applicationNo: this.select_application,
          pushType: this.select_pushType,
          pushStatus: this.select_pushStatus,
          businessNo: this.businessNo,
          thirdNo: this.thirdNo,
          recordCode: this.recordCode,
          pushBeginTime: this.pushBeginTime,
          pushEndTime: this.pushEndTime,
          curPage: this.curPage
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
            if (response.data.total === 0) {
              this.loading = false
              this.$message({
                message: '未查询到数据',
                type: 'warning'
              });
              this.curPage = 1
              this.total = 0
              return
            }

            this.pushList = response.data.pushRecordList
            this.total = response.data.total
            this.loading = false
          }, error => {
            this.loading = false
            this.$message({
              message: '查询失败',
              type: 'warning'
            });

            this.curPage = 1
            this.total = 0
            this.pushList = []
          })

    },
    handleTableChange(val) {
      this.currentRow = val;
    },

    // 选择企业
    selectEnterprise(enterprise) {

      if (!enterprise) {
        this.$message({
          message: '请选择企业',
          type: 'warning'
        });
        return;
      }
      this.select_enterprise = enterprise
      this.select_warehouse = ''
      this.WarehouseOptions = []
      this.warehouse = {}
      this.resourceList = []
      this.logisticsList = []
      this.pushList = []
      this.total = 0
      this.curPage = 1

      // 查询企业下的仓库
      axios({
        url: this.host + '/toolkit/tools/getWarehouse',
        method: 'GET',
        params: {
          enterpriseCode: enterprise
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
            if (!response.data) {
              this.$message({
                message: '未查询仓库数据',
                type: 'warning'
              });
            }

            let WarehouseList = response.data
            if (WarehouseList.length > 0) {
              for (let i = 0; i < WarehouseList.length; i++) {
                let label = WarehouseList[i]['warehouseName']
                let value = WarehouseList[i]['warehouseCode']
                this.WarehouseOptions.push({'label': label, 'value': value})
              }
            }
          }, error => {
            this.$message({
              message: '查询失败',
              type: 'warning'
            });
          })

    },
    // 选择仓库
    selectWarehouse(warehouse) {

    },
    selectApplication(application) {
      this.select_application = application
    },
    selectPushType(pushType) {
      this.select_pushType = pushType
    },
    selectPushStatus(pushStatus) {
      this.select_pushStatus = pushStatus
    },
    clearEnterprise() {
      this.select_enterprise = ''
      this.select_warehouse = ''
      this.WarehouseOptions = []
    },
    clearWarehouse() {
      this.select_warehouse = ''
    },
    clearBusinessNo() {
      this.businessNo = ''
    },
    clearThirdNo() {
      this.thirdNo = ''
    },
    clearRecordCode() {
      this.recordCode = ''
    },
    clearApplication() {
      this.select_application = ''
    },
    clearPushType() {
      this.select_pushType = ''
    },
    clearPushStatus() {
      this.select_pushStatus = ''
    },
    clearPushBeginTime() {
      this.pushBeginTime = ''
    },
    clearPushEndTime() {
      this.pushEndTime = ''
    },
    handlePushDetailClick(row) {

      this.Record_Body_Title = row.businessNo
      this.pushRecord = {}

      axios({
        url: this.host + '/toolkit/tools/getPushRecordDetail2',
        method: 'GET',
        params: {
          recordCode: row.recordCode
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
            this.pushRecord = response.data
            this.Record_Body_dialogVisible = true
          }, error => {
            console.log(error)
            this.$message({
              message: '查询推送记录失败',
              type: 'warning'
            });
          })
    },
    handleCurrentChange(current_page) {
      this.curPage = current_page
      this.onSubmit(current_page)
    },
    sortPushStatus(a, b) {
      if (a.pushStatus > b.pushStatus) {
        return -1
      }
    },

    handlePushRetryClick(row) {

      axios({
        url: this.host + '/toolkit/tools/retryPushRecord2',
        method: 'GET',
        params: {
          recordId: row.recordId
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
              this.$message({
                message: response.data,
                type: 'warning'
              });
            } else {
              this.$message({
                message: '重试完成',
                type: 'success'
              });
            }

          }, error => {
            console.log(error)
            this.$message({
              message: '重试失败',
              type: 'warning'
            });
          })
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
      if (data.includes(':')) {
        try {
          const obj = JSON.parse(data)
          if (obj.hasOwnProperty('body')) {
            const _obj = JSON.parse(obj.body)
            obj.body = _obj
          }
          if (obj.hasOwnProperty('requestBody')) {
            try {
              const _obj = JSON.parse(obj.requestBody)
              obj.requestBody = _obj
              if (obj.requestBody.hasOwnProperty('requestBody')) {
                const _obj = JSON.parse(obj.requestBody.requestBody)
                obj.requestBody.requestBody = _obj
              }
            } catch (err) {
              console.log(err)
            }
          }

          data = JSON.stringify(obj)
        } catch (err) {
          console.log(err)
        }
      }


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