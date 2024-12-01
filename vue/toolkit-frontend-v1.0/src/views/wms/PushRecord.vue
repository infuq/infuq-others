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
          <el-select v-model="select_enterprise" placeholder="请选择企业" @change="selectEnterprise(select_enterprise)" filterable clearable @clear="clearEnterprise">
            <el-option v-for="item in EnterpriseOptions" :key="item.value" :label="item.label" :value="item.value"></el-option>
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
            <el-option v-for="item in WarehouseOptions" :key="item.value" :label="item.label" :value="item.value"></el-option>
          </el-select>
        </div>

        <div>
          <el-input v-model="businessNo" placeholder="业务单号" clearable @clear="clearBusinessNo" style="width: 380px;">
            <template slot="prepend">业务单号</template>
          </el-input>
          <el-input v-model="thirdNo" placeholder="三方单号" clearable @clear="clearThirdNo" style="width: 380px; margin-left: 5px;">
            <template slot="prepend">三方单号</template>
          </el-input>
          <el-input v-model="recordCode" placeholder="记录编码" clearable @clear="clearRecordCode" style="width: 380px; margin-left: 5px;">
            <template slot="prepend">记录编码</template>
          </el-input>
        </div>
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
                                  <span
                                      v-if="scope.row.pushStatusName === '推送失败' || scope.row.pushStatusName === '处理失败' || scope.row.pushStatusName === '超时未处理'">
                                      <span style="color: red;">{{ scope.$index + 1 }}</span>
                                  </span>
                      <span v-else>
                                      {{ scope.$index + 1 }}
                                  </span>
                    </template>
                  </el-table-column>
                  <el-table-column sortable prop="warehouseName" label="仓库名称" max-width="190"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column label="业务单号" max-width="220" :show-overflow-tooltip="true">
                    <template slot-scope="scope" v-if="scope.row.businessNo != null && scope.row.businessNo !== ''">
                                  <span>
                                      <i @click="copy(scope.row.businessNo)" class="el-icon-document-copy"></i>&nbsp;&nbsp;{{ scope.row.businessNo }}
                                  </span>
                    </template>
                  </el-table-column>
                  <el-table-column label="三方单号" max-width="220" :show-overflow-tooltip="true">
                    <template slot-scope="scope" v-if="scope.row.thirdNo != null && scope.row.thirdNo !== ''">
                                  <span>
                                      <i @click="copy(scope.row.thirdNo)" class="el-icon-document-copy"></i>&nbsp;&nbsp;{{ scope.row.thirdNo }}
                                  </span>
                    </template>
                  </el-table-column>
                  <el-table-column prop="pushApplicationName" label="推送应用" width="110"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="pushTypeName" label="推送类型" max-width="220"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column sortable :sort-method="sortPushStatus" label="推送状态" width="120">
                    <template slot-scope="scope">
                                  <span
                                      v-if="scope.row.pushStatusName == '推送失败' || scope.row.pushStatusName == '处理失败' || scope.row.pushStatusName == '超时未处理'">
                                      <span style="color: red;">{{ scope.row.pushStatusName }}</span>
                                  </span>
                      <span v-else-if="scope.row.pushStatusName == '已完成'">
                                      <span style="color: green;">{{ scope.row.pushStatusName }}</span>
                                  </span>
                      <span v-else>
                                      {{ scope.row.pushStatusName }}
                                  </span>
                    </template>
                  </el-table-column>
                  <el-table-column prop="autoRetryNum" label="重试次数" width="100"></el-table-column>
                  <el-table-column prop="createTime" label="创建时间" width="200"></el-table-column>
                  <el-table-column prop="updateTime" label="更新时间" width="200"></el-table-column>
                  <!--
                  <el-table-column prop="pushTime" label="推送时间" width="180"></el-table-column>
                  -->
                  <el-table-column fixed="right" label="操作" min-width="70">
                    <template slot-scope="scope">
                      <el-button @click="handlePushDetailClick(scope.row)" type="text">详情</el-button>
                      <span
                          v-if="scope.row.pushStatusName == '推送失败' || scope.row.pushStatusName == '处理失败' || scope.row.pushStatusName == '超时未处理'">
                                      <el-dropdown @command="handleCommand($event, scope.row)">
                                          <span class="el-dropdown-link" style="margin-left: 5px;">其他操作</span>
                                          <el-dropdown-menu slot="dropdown">
                                              <span
                                                  v-if="scope.row.pushStatusName == '推送失败' || scope.row.pushStatusName == '处理失败' || scope.row.pushStatusName == '超时未处理'">
                                                  <el-dropdown-item command="a"
                                                                    icon="el-icon-edit">修改推送内容</el-dropdown-item>
                                              </span>
                                          </el-dropdown-menu>
                                      </el-dropdown>
                                  </span>
                      <span
                          v-if="scope.row.pushStatusName == '推送失败' || scope.row.pushStatusName == '处理失败' || scope.row.pushStatusName == '超时未处理'">
                                      <el-button @click="handlePushRetryClick(scope.row)" type="text"
                                                 style="margin-left: 5px;">重试</el-button>
                                  </span>
                    </template>
                  </el-table-column>
                </el-table>
              </template>

              <el-dialog :title="'[ ' + Record_Body_Title + ' ] 内容体'" :visible.sync="Record_Body_dialogVisible"
                         :show-close="false" width="50%">
                <div style="display: block; margin: 5px 0;">
                  <label style="display: inline-block; text-align: right;">[ 记录编码 ]</label><label>&nbsp;&nbsp;&nbsp;{{ pushRecord.apiRecordCode }}</label>
                  &nbsp;&nbsp;<i @click="copy(pushRecord.apiRecordCode)" class="el-icon-document-copy"></i>
                  <span v-if="pushRecord.guance != null && pushRecord.guance != ''" style="vertical-align: bottom;">
                              &nbsp;&nbsp;<el-link type="primary" :href="guance" target="_blank">观测云</el-link>
                          </span>
                </div>
                <div style="display: block; margin: 5px 0;">
                  <label style="display: inline-block; text-align: right;">[ 链路追踪 ]</label>
                  <router-link :to="{path: '/select_trace', query:{traceId: pushRecord.traceId}}" target="_blank" style="margin-left: 5px;">
                    <span class="icon-link" style="display: inline-block; top: 1px;">{{ pushRecord.traceId }}</span>
                  </router-link>
                  <span v-if="pushRecord.traceId != null && pushRecord.traceId !== ''">
                    <i @click="copy(pushRecord.traceId)" class="el-icon-document-copy"></i>
                  </span>
                </div>
                <div style="display: block; margin: 5px 0;">
                  <label style="display: inline-block; text-align: right;">[ 推送内容 ]</label><label>&nbsp;&nbsp;&nbsp;{{ pushRecord.pushBody }}</label>
                  <span v-if="pushRecord.pushBody != null && pushRecord.pushBody != ''">
                              &nbsp;&nbsp;<i @click="copy(pushRecord.pushBody)" class="el-icon-document-copy"></i>
                          </span>
                </div>
                <div style="display: block; margin: 5px 0;">
                  <label style="display: inline-block; text-align: right;">[ 处理内容 ]</label><label>&nbsp;&nbsp;&nbsp;{{ pushRecord.actionBody }}</label>
                </div>
                <div style="display: block; margin: 5px 0;">
                  <label style="display: inline-block; text-align: right;">[ 完成内容 ]</label><label>&nbsp;&nbsp;&nbsp;{{ pushRecord.finishBody }}</label>
                </div>
                <div style="display: block; margin: 5px 0;">
                  <label style="display: inline-block; text-align: right;">[ 回执内容 ]</label><label>&nbsp;&nbsp;&nbsp;{{ pushRecord.receiptBody }}</label>
                </div>
              </el-dialog>


              <el-dialog :title="'[ ' + Record_Body_Title + ' ] 业务数据和推送内容'"
                         :visible.sync="Push_Body_dialogVisible" :show-close="false" width="50%">

                <div>
                  业务数据 &nbsp;&nbsp;&nbsp;
                  <el-button @click="formatBusinessData('业务数据')" type="text" style="padding: 0px 0px;">
                    查看格式化结果
                  </el-button>
                </div>
                <div style="display: block; margin: 5px 0;">
                  <el-input type="textarea" placeholder="请输入业务数据" v-model="api_param"
                            :autosize="{minRows:4,maxRows:10}"></el-input>
                </div>
                <div style="margin-top: 25px;">
                  推送内容 &nbsp;&nbsp;&nbsp;
                  <el-button @click="formatBusinessData('推送内容')" type="text" style="padding: 0px 0px;">
                    查看格式化结果
                  </el-button>
                </div>
                <div style="display: block; margin: 5px 0;">
                  <el-input type="textarea" placeholder="请输入推送内容" v-model="push_body"
                            :autosize="{minRows:4,maxRows:10}"></el-input>
                </div>

                <div style="margin-top: 20px;">
                  <el-button type="primary" @click="update_api_param()">更新业务数据</el-button>
                  <el-button type="primary" @click="update_push_body()">更新推送内容</el-button>
                  <el-button type="primary" @click="update_api_param_push_body()">更新业务数据和推送内容</el-button>
                  <!--
                  <el-button type="primary" @click="format()">格式化</el-button> -->
                </div>
              </el-dialog>

              <el-dialog :title="'[ ' + FORMAT_TITLE + ' ] 格式化结果'" :visible.sync="FORMAT_TITLE_dialogVisible"
                         :show-close="false" width="70%">

                <el-alert title="说明" type="warning" style="width: 26%;" :closable="false">
                  <template slot='title'>
                    <div>不可以将格式化结果内容更新到数据库</div>
                  </template>
                </el-alert>
                <div
                    style="margin-top: 5px; border: 1px solid #eae3e3; padding: 10px; background: aliceblue; overflow: auto;">
                  <pre>{{ format_result }}</pre>
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
  name: "PushRecord",
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
          label: 'OMS3.0',
          value: 'APP-00006'
        },
        {
          label: '蜀海',
          value: 'APP-00003'
        },
        {
          label: '伟添',
          value: 'APP-00005'
        },
        {
          label: '绝配',
          value: 'APP-00008'
        },
        {
          label: '银豹',
          value: 'APP-00010'
        },
        {
          label: '开放平台',
          value: 'APP-00007'
        }
      ],
      PushTypeOptions: [
        {
          label: '仓库信息',
          value: 1,
        },
        {
          label: '商品库存',
          value: 2,
        },
        {
          label: '发货单',
          value: 3,
        },
        {
          label: '门店信息回调',
          value: 4,
        },
        {
          label: '发货单修改快递物流',
          value: 5,
        },
        {
          label: '订货单完结回调',
          value: 6,
        },
        {
          label: 'wms库存同步',
          value: 7,
        },
        {
          label: 'wms退货单退货',
          value: 8,
        },
        {
          label: 'wms退货单手动完结',
          value: 9,
        },
        {
          label: '库存自定义编码',
          value: 10,
        },
        {
          label: '收货人同步',
          value: 11,
        },
        {
          label: '商品同步',
          value: 12,
        },
        {
          label: '销售退货单同步',
          value: 13,
        },
        {
          label: '收货人(更新)同步',
          value: 14,
        },
        {
          label: '采购单完结回调',
          value: 15,
        },
        {
          label: '采购退货单完结回调',
          value: 16,
        },
        {
          label: '调拨单',
          value: 17,
        },
        {
          label: '采购单同步',
          value: 18,
        },
        {
          label: '采购退货单同步',
          value: 19,
        },
        {
          label: '入库单同步',
          value: 20,
        },
        {
          label: '出库单同步',
          value: 21,
        },
        {
          label: '采购退货单退货',
          value: 22,
        },
        {
          label: '订货单',
          value: 23,
        },
        {
          label: '盘点单',
          value: 24,
        },
        {
          label: '报损单',
          value: 25,
        },
        {
          label: '退货入库单同步',
          value: 26,
        }
      ],
      PushStatusOptions: [
        {
          label: '创建成功',
          value: '1'
        },
        {
          label: '推送成功',
          value: '2'
        },
        {
          label: '推送失败',
          value: '92'
        },
        {
          label: '已处理',
          value: '5'
        },
        {
          label: '处理失败',
          value: '95'
        },
        {
          label: '已完成',
          value: '6'
        },
        {
          label: '超时未处理',
          value: '97'
        }
      ],
      businessNo: '',
      thirdNo: '',
      recordCode: '',

      pushBeginTime: this.dateFormat() + " 00:00:00",
      pushEndTime: this.dateFormat() + " 23:59:59",


      pushList: [],

      loading: false,

      total: 0,
      curPage: 1,

      Record_Body_Title: '',
      Record_Body_dialogVisible: false,
      Push_Body_dialogVisible: false,
      push_body: '',
      api_param: '',
      update_record_code: '',
      pushRecord: {
        receiveBody: '',
        actionBody: '',
        finishBody: '',
        receiptBody: ''
      },
      guance: '',

      currentRow: null,

      FORMAT_TITLE: null,
      FORMAT_TITLE_dialogVisible: false,
      format_result: '',

    }
  },

  created: function () {

    let recordCode = this.$route.query.recordCode;
    // 从其他页面跳转而来
    if (recordCode) {
      this.pushBeginTime = null
      this.pushEndTime = null
      this.recordCode = recordCode
      this.onSubmit(-1);
      return
    }


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
          console.log(error.message)
        })

  },
  methods: {

    handleCommand(command, row) {
      if (command == 'a') {
        this.handlePushBodyClick(row)
      }
    },


    // 查询
    onSubmit(curPage) {
      let select_enterprise = this.select_enterprise

      this.pushList = []

      if (curPage === -1) {
        this.curPage = 1
      }
      this.loading = true
      axios({
        url: this.host + '/toolkit/tools/getPushRecord',
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
            console.log(error)
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

    handleTableChange(row) {
      this.currentRow = row;
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
            console.log(error)
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
      this.select_pushType = ''
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
        url: this.host + '/toolkit/tools/getPushRecordDetail',
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
            this.guance = this.pushRecord.guance
          }, error => {
            console.log(error)
            this.$message({
              message: '查询推送记录失败',
              type: 'warning'
            });
          })
    },
    handlePushBodyClick(row) {
      // 点亮当前行
      //this.handleTableChange(row)

      this.Record_Body_Title = row.businessNo
      this.push_body = ''
      this.api_param = ''
      this.update_record_code = ''

      axios({
        url: this.host + '/toolkit/tools/getPushRecordDetail',
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
            this.push_body = response.data.pushBody
            this.api_param = response.data.apiParam
            this.update_record_code = response.data.apiRecordCode
            this.Push_Body_dialogVisible = true
          }, error => {
            console.log(error)
            this.$message({
              message: '查询推送记录失败',
              type: 'warning'
            });
          })
    },

    update_api_param() {

      axios({
        url: this.host + '/toolkit/tools/updateApiParam',
        method: 'POST',
        data: {
          recordCode: this.update_record_code,
          apiParam: this.api_param
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
            this.Push_Body_dialogVisible = false
            if (response.data === 'success') {
              this.$message({
                message: '更新业务数据成功',
                type: 'success'
              });
            } else {
              this.$message({
                message: '更新业务数据失败',
                type: 'warning'
              });
            }
          }, error => {
            console.log(error)
            this.$message({
              message: '更新业务数据失败',
              type: 'warning'
            });
          })
    },
    update_push_body() {

      axios({
        url: this.host + '/toolkit/tools/updatePushBody',
        method: 'POST',
        data: {
          recordCode: this.update_record_code,
          pushBody: this.push_body
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

            this.Push_Body_dialogVisible = false
            if (response.data === 'success') {
              this.$message({
                message: '更新推送内容成功',
                type: 'success'
              });
            } else {
              this.$message({
                message: '更新推送内容失败',
                type: 'warning'
              });
            }
          }, error => {
            console.log(error)
            this.$message({
              message: '更新推送内容失败',
              type: 'warning'
            });
          })
    },

    update_api_param_push_body() {

      axios({
        url: this.host + '/toolkit/tools/updateApiParamPushBody',
        method: 'POST',
        data: {
          recordCode: this.update_record_code,
          pushBody: this.push_body,
          apiParam: this.api_param
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

            this.Push_Body_dialogVisible = false
            if (response.data === 'success') {
              this.$message({
                message: '更新业务数据和推送内容成功',
                type: 'success'
              });
            } else {
              this.$message({
                message: '更新业务数据和推送内容失败',
                type: 'warning'
              });
            }
          }, error => {
            console.log(error)
            this.$message({
              message: '更新业务数据和推送内容失败',
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

      // 点亮当前行
      //this.handleTableChange(row)


      axios({
        url: this.host + '/toolkit/tools/retryPushRecord',
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

    formatBusinessData(title) {
      this.format_result = ''
      this.FORMAT_TITLE = title
      this.FORMAT_TITLE_dialogVisible = true

      if (title === '业务数据' && this.api_param) {
        this.format1(this.api_param)
      }
      if (title === '推送内容' && this.push_body) {
        this.format1(this.push_body)
      }
    },

    // 当前日期格式化
    dateFormat() {
      let date = new Date()
      let year = date.getFullYear()
      let month = date.getMonth() + 1 < 10 ? '0' + (date.getMonth() + 1) : date.getMonth() + 1
      let day = date.getDate() < 10 ? '0' + date.getDate() : date.getDate()
      return year + '-' + month + '-' + day
    },

    t(data) {
      // 长整数转成字符串类型, 防止精度丢失
      data = data.replace(/((\W*)s*):s*([0-9]{15,})s*(,?)/g, '$1: $2$3$2 $4')
      return data;
    },

    format1(data) {

      if (data.includes(':')) {
        try {
          data = this.t(data)
          const obj = JSON.parse(data)
          if (obj.hasOwnProperty('body')) {
            // 第一层
            obj.body = this.t(obj.body)
            const _obj = JSON.parse(obj.body)
            obj.body = _obj
          }
          if (obj.hasOwnProperty('requestBody')) {
            try {
              // 第一层
              obj.requestBody = this.t(obj.requestBody)
              const _obj = JSON.parse(obj.requestBody)
              obj.requestBody = _obj
              if (obj.requestBody.hasOwnProperty('requestBody')) {
                // 第二层
                obj.requestBody.requestBody = this.t(obj.requestBody.requestBody)
                const _obj = JSON.parse(obj.requestBody.requestBody)
                obj.requestBody.requestBody = _obj
              }
            } catch (err) {
              console.log(error)
            }
          }

          data = JSON.stringify(obj, null, 4)
        } catch (err) {
          console.log(error)
        }
      }

      if (data) {
        // 显示格式化之后的结果
        this.format_result = data
      }

    },
    copy(data) {
      if (data.includes(':')) {
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
            console.log(error)
          }
        }

        data = JSON.stringify(obj)
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
    }


  }


}
</script>

<style>
@import '@/assets/css/common.css';

.el-link.el-link--primary {
  color: #0000FF;
}

a {
  color: #0000FF;
  text-decoration: none;
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

.el-step__title.is-process {
  font-size: 15px;
}

.el-divider__text.is-left {
  color: #FA8919;
  font-weight: bold;
}

.el-input__inner {
  border-radius: 0 4px 4px 0;
}

.el-select {
  vertical-align: middle;
}

.el-table__body tr.current-row > td {
  background: #b8e2e8;
}

.el-dropdown-link {
  cursor: pointer;
  color: #0000FF;
}

.el-icon-arrow-down {
  font-size: 12px;
}

</style>