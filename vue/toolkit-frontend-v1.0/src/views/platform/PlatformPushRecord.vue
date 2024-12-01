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
                     filterable clearable @clear="clearEnterprise" disabled>
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

        <div>
          <el-input v-model="businessNo" placeholder="CK-240606-001696,DH-240606-000003" clearable
                    @clear="clearBusinessNo" style="width: 430px;">
            <template slot="prepend">业务单号或三方单号</template>
          </el-input>
          <!--
          <el-input v-model="thirdNo" placeholder="三方单号" clearable @clear="clearThirdNo" style="width: 380px;">
              <template slot="prepend">三方单号</template>
          </el-input>
-->
          <el-input v-model="recordCode" placeholder="AIRPVdRi5whF240322113216199" clearable @clear="clearRecordCode"
                    style="width: 380px; margin-left: 5px;">
            <template slot="prepend">记录编码</template>
          </el-input>
          <el-input v-model="ent" placeholder="ENT码" clearable @clear="clearEnt"
                    style="width: 380px; margin-left: 5px;">
            <template slot="prepend">ENT码</template>
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
          <el-select v-model="select_platform" placeholder="请选择目标平台" @change="selectPlatform(select_platform)" filterable clearable @clear="clearPlatform">
            <el-option v-for="item in PlatformOptions" :key="item.value" :label="item.label"
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
            应用
          </div>
          <el-select v-model="select_app" placeholder="请选择推送应用" @change="selectApp(select_app)" filterable
                     clearable @clear="clearApp">
            <el-option v-for="item in AppOptions" :key="item.value" :label="item.label" :value="item.value"></el-option>
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
                    style="width: 300px;">
            <template slot="prepend">起时间</template>
          </el-input>
          <el-input v-model="pushEndTime" placeholder="2023-03-21 18:12:20" clearable @clear="clearPushEndTime"
                    style="width: 300px; margin-left: 5px;">
            <template slot="prepend">止时间</template>
          </el-input>
          <div style="display: inline-block; margin-top: 3px; margin-bottom: 3px; margin-left: 5px;">
            <el-button type="primary" @click="onSubmit(-1)">查询</el-button>
          </div>

          <div style="display: inline-block; margin-top: 3px; margin-bottom: 3px; margin-left: 5px;">
            <el-button type="primary" @click="allRetry" :disabled="allRetryDisable">全部重试</el-button>
          </div>
        </div>


        <!-- 结果 -->
        <div style="margin-top: 15px;">

          <!-- 推送结果 -->
          <div style="margin-top: 10px;" v-loading="loading" :element-loading-text="loadingText">
            <el-divider content-position="left">对接平台推送记录</el-divider>

            <div style="font-weight: 500; font-size: 14px;">
              <template>
                <el-table :data="pushList" border style="width: 100%" :row-style="{ height: 10+'px'}"
                          :cell-style="{padding:0+'px'}" highlight-current-row @current-change="handleTableChange">
                  <!-- height="250" -->
                  <el-table-column fixed label="序号" type="index" width="50">
                    <template slot-scope="scope">
                                    <span v-if="scope.row.pushStatusName == '推送失败'">
                                        <span style="color: red;">{{ scope.$index + 1 }}</span>
                                    </span>
                      <span v-else>
                                        {{ scope.$index + 1 }}
                                    </span>
                    </template>
                  </el-table-column>
                  <el-table-column prop="warehouseName" label="仓库名称" max-width="90"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column label="业务单号" max-width="90" :show-overflow-tooltip="true">
                    <template slot-scope="scope" v-if="scope.row.businessNo != null && scope.row.businessNo != ''">
                                    <span>
                                        <i @click="copy(scope.row.businessNo)" class="el-icon-document-copy"></i>&nbsp;&nbsp;{{ scope.row.businessNo }}
                                    </span>
                    </template>
                  </el-table-column>
                  <el-table-column label="三方单号" max-width="90" :show-overflow-tooltip="true">
                    <template slot-scope="scope" v-if="scope.row.thirdNo != null && scope.row.thirdNo != ''">
                                    <span>
                                        <i @click="copy(scope.row.thirdNo)" class="el-icon-document-copy"></i>&nbsp;&nbsp;{{ scope.row.thirdNo }}
                                    </span>
                    </template>
                  </el-table-column>
                  <el-table-column prop="pushPlatformName" label="目标平台" width="100"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="pushAppName" label="推送应用" max-width="90"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="ent" label="ENT码" max-width="90"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="pushTypeName" label="推送类型" max-width="100"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column label="推送状态" width="100" :show-overflow-tooltip="true">
                    <template slot-scope="scope">
                                    <span v-if="scope.row.pushStatusName == '推送失败'">
                                        <span
                                            v-if="scope.row.pushBody != null && scope.row.pushBody != '' && scope.row.responseBody != null && scope.row.responseBody != ''">
                                            <span style="color: red;">{{ scope.row.pushStatusName }}[因第三方]</span>
                                        </span>
                                        <span v-else>
                                            <span style="color: red;">{{ scope.row.pushStatusName }}</span>
                                        </span>
                                    </span>
                      <span v-else-if="scope.row.pushStatusName == '推送成功'">
                                        <span style="color: green;">{{ scope.row.pushStatusName }}</span>
                                    </span>
                      <span v-else>
                                        {{ scope.row.pushStatusName }}
                                    </span>
                    </template>
                  </el-table-column>
                  <el-table-column label="回执状态" width="100" :show-overflow-tooltip="true">
                    <template slot-scope="scope">
                                    <span v-if="scope.row.receiptStatusName == '回执失败'">
                                        <span style="color: red;">{{ scope.row.receiptStatusName }}</span>
                                    </span>
                      <span v-else-if="scope.row.receiptStatusName == '回执成功'">
                                        <span style="color: green;">{{ scope.row.receiptStatusName }}</span>
                                    </span>
                      <span v-else-if="scope.row.receiptStatusName == '无需回执'">
                                        <span style="color: #d7b10d;">{{ scope.row.receiptStatusName }}</span>
                                    </span>
                      <span v-else>
                                        {{ scope.row.receiptStatusName }}
                                    </span>
                    </template>
                  </el-table-column>
                  <el-table-column prop="autoRetryNum" label="重试次数" width="90"></el-table-column>
                  <el-table-column prop="createTime" label="创建时间" max-width="150"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="updateTime" label="更新时间" max-width="150"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column fixed="right" label="操作" min-width="90">
                    <template slot-scope="scope">
                      <el-button @click="handlePushDetailClick(scope.row)" type="text">详情</el-button>
                      <span v-if="scope.row.pushStatusName == '推送失败'">
                                        <el-dropdown @command="handleCommand($event, scope.row)">
                                            <span class="el-dropdown-link" style="margin-left: 5px; color: #409EFF;">其他操作</span>
                                            <el-dropdown-menu slot="dropdown">
                                                <span v-if="scope.row.pushStatusName == '推送失败'">
                                                    <el-dropdown-item command="a"
                                                                      icon="el-icon-edit">修改推送内容</el-dropdown-item>
                                                </span>
                                            </el-dropdown-menu>
                                        </el-dropdown>
                                    </span>
                      <span v-if="scope.row.pushStatusName == '推送失败'">
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
                  <label style="display: inline-block; text-align: right;">[ 记录编码 ]</label><label>&nbsp;&nbsp;&nbsp;{{ pushRecord.apiRecordCode }}</label>&nbsp;&nbsp;<i
                    @click="copy(pushRecord.apiRecordCode)" class="el-icon-document-copy"></i>
                </div>
                <div style="display: block; margin: 5px 0;">
                  <label style="display: inline-block; text-align: right;">[ 链路追踪 ]</label>
                  <router-link :to="{path: '/select_trace', query:{traceId: pushRecord.traceId}}" target="_blank" style="margin-left: 5px;">
                    <span class="icon-link" style="display: inline-block;top: 1px; color: #409EFF;">{{ pushRecord.traceId }}</span>
                  </router-link>
                  <span v-if="pushRecord.traceId != null && pushRecord.traceId != ''">
                    <i @click="copy(pushRecord.traceId)" class="el-icon-document-copy"></i>
                  </span>
                </div>
                <div style="display: block; margin: 5px 0;">
                  <label style="display: inline-block; text-align: right;">[ 执行语句 ]</label>
                  <span>
                    &nbsp;&nbsp;SQL&nbsp;&nbsp;<i @click="copy(pushRecord.sql)" class="el-icon-document-copy"></i>
                  </span>
                </div>

                <div style="display: block; margin: 5px 0;">
                  <label style="display: inline-block; text-align: right; color: #e6a23c;">[ 推送内容 ]</label><label>&nbsp;&nbsp;&nbsp;{{ pushRecord.pushBody }}</label>
                  <span v-if="pushRecord.pushBody != null && pushRecord.pushBody != ''">
                                &nbsp;&nbsp;<i @click="copy(pushRecord.pushBody)" class="el-icon-document-copy"></i>
                            </span>
                </div>
                <div style="display: block; margin: 5px 0;">
                  <label style="display: inline-block; text-align: right; color: #e6a23c;">[ 响应内容 ]</label><label>&nbsp;&nbsp;&nbsp;{{ pushRecord.responseBody }}</label>
                </div>
                <div style="display: block; margin: 5px 0;">
                  <label style="display: inline-block; text-align: right; color: #e6a23c;">[ 异常内容 ]</label><label>&nbsp;&nbsp;&nbsp;{{ pushRecord.errorBody }}</label>
                </div>
                <div style="display: block; margin: 5px 0;">
                  <label style="display: inline-block; text-align: right; color: #e6a23c;">[ 历史异常 ]</label><label>&nbsp;&nbsp;&nbsp;{{ pushRecord.previousErrorBody }}</label>
                  <span v-if="pushRecord.previousErrorBody != null && pushRecord.previousErrorBody != ''">
                                &nbsp;&nbsp;<i @click="copy(pushRecord.previousErrorBody)"
                                               class="el-icon-document-copy"></i>
                            </span>
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
                            :autosize="{minRows:4,maxRows:10}" @input="format_event()" @paste.native="format_event()"
                            @blur="format_event()"></el-input>
                </div>
                <div style="margin-top: 25px;">
                  推送内容 &nbsp;&nbsp;&nbsp;
                  <el-button @click="formatBusinessData('推送内容')" type="text" style="padding: 0px 0px;">
                    查看格式化结果
                  </el-button>
                </div>
                <div style="display: block; margin: 5px 0;">
                  <el-input type="textarea" placeholder="请输入推送内容" v-model="push_body"
                            :autosize="{minRows:4,maxRows:10}" @input="format_event()" @paste.native="format_event()"
                            @blur="format_event()"></el-input>
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
  name: "PlatformPushRecord",
  data() {

    return {
      env: Config.env,
      host: Config.host,


      select_enterprise: '',
      select_warehouse: '',
      select_platform: '',
      select_app: '',
      select_pushType: '',
      select_pushStatus: '',
      EnterpriseOptions: [],
      WarehouseOptions: [],
      PlatformOptions: [
        {
          label: 'WMS3.0',
          value: 'APP-00002'
        },
        {
          label: 'OMS3.0',
          value: 'APP-00006'
        },
        {
          label: '畅捷通',
          value: 'APP-00009'
        },
        {
          label: '绝配',
          value: 'APP-00008'
        },
        {
          label: '用友',
          value: 'APP-00013'
        },
        {
          label: '金蝶',
          value: 'APP-00011'
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
          label: '银豹',
          value: 'APP-00010'
        }


      ],
      AppOptions: [],
      PushTypeOptions: [
        {
          label: '供应商',
          value: 'B1800-0001',
        },
        {
          label: '供应商商品',
          value: 'B1900-0001',
        },
        {
          label: '商家/货主',
          value: 'B000-0001,B000-0002,B000-0003',
        },
        {
          label: '门店/收货人',
          value: 'B100-0001,B100-0002,B100-0003',
        },
        {
          label: '商品',
          value: 'B200-0001,B200-0002,B200-0003,B201-0001',
        },
        {
          label: '订货单',
          value: 'B300-0001,B300-0002,B300-0003,B300-0004,B301-0001,B302-0001,B303-0001,B304-0001',
        },
        {
          label: '退货单',
          value: 'B400-0001,B400-0002,B400-0003,B400-0004,B400-0005,B401-0001,B401-0002,B402-0001,B403-0001,B404-0001,B405-0001,B406-0001',
        },
        {
          label: '销退入库单',
          value: 'B700-0001,B700-0002,B701-0001,B701-0002',
        },
        {
          label: '采购单',
          value: 'B900-0001,B900-0002,B900-0003,B900-0004,B901-0001,B902-0001,B2000-0001',
        },
        {
          label: '采退单',
          value: 'B1000-0001,B1000-0002,B1001-0001,B1002-0001,B2100-0001',
        },
        {
          label: '采购入库单',
          value: 'B1100-0001,B1100-0002,B1101-0001,B1102-0001',
        },
        {
          label: '采退出库单',
          value: 'B1200-0003,B1201-0001,B1202-0001,B1203-0001,B1204-0001,B1204-0002',
        },
        {
          label: '发货单',
          value: 'B1300-0001,B1300-0002,B1300-0003,B1301-0001',
        },
        {
          label: '调拨单',
          value: 'B1400-0001,B1400-0002',
        },

        {
          label: '盘点单',
          value: 'B1500-0001,B1500-0002,B1501-0001',
        },
        {
          label: '报损单',
          value: 'B1600-0001,B1600-0002',
        },
        {
          label: '库存',
          value: 'B1700-0001,B1700-0002,B1701-0001,B1701-0002,B1702-0001,B1703-0001',
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
        }
      ],
      businessNo: '',
      thirdNo: '',
      recordCode: '',
      ent: '',

      pushBeginTime: this.dateFormat() + " 00:00:00",
      pushEndTime: this.dateFormat() + " 23:59:59",

      loadingText: '查询中...',
      pushList: [],

      allRetryDisable: true,

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
        pushBody: '',
        responseBody: '',
        errorBody: '',
        previousErrorBody: ''
      },
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
    /*
    axios({
        url: host + '/tools/getAllEnterprise',
        method: 'GET',
        params: { },
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
    })
    .then(response => {
        console.log(response.data);
        EnterpriseList = response.data

        for (i = 0; i < EnterpriseList.length; i++) {
            label = EnterpriseList[i]['enterpriseName']
            value = EnterpriseList[i]['enterpriseCode']
            this.EnterpriseOptions.push({'label': label, 'value': value})
        }

    }, error => {
        this.$message({
          message: '查询企业失败',
          type: 'warning'
        });
        console.log(error.message)
    })
*/


    // 获取所有仓库
    axios({
      url: this.host + '/toolkit/tools/getAllWarehouse',
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

      let WarehouseList = response.data

      for (let i = 0; i < WarehouseList.length; i++) {
        let label = WarehouseList[i]['warehouseName']
        let value = WarehouseList[i]['warehouseCode']
        this.WarehouseOptions.push({'label': label, 'value': value})
      }

    }, error => {
      console.log(error)
      this.$message({
        message: '查询仓库失败',
        type: 'warning'
      });
    })


    this.selectPlatform('')

  },
  methods: {
    handleCommand(command, row) {
      if (command === 'a') {
        this.handlePushBodyClick(row)
      }
    },

    // 查询
    onSubmit(curPage) {
      let select_enterprise = this.select_enterprise

      this.allRetryDisable = true
      this.pushList = []
      this.total = 0
      if (curPage === -1) {
        this.curPage = 1
      }
      this.loading = true
      axios({
        url: this.host + '/toolkit/ab/getPlatformPushRecord',
        method: 'POST',
        data: {
          enterpriseCode: this.select_enterprise,
          warehouseCode: this.select_warehouse,
          platformNo: this.select_platform,
          appNo: this.select_app,
          pushType: this.select_pushType,
          pushStatus: this.select_pushStatus,
          businessNo: this.businessNo,
          thirdNo: this.thirdNo,
          recordCode: this.recordCode,
          ent: this.ent,
          pushBeginTime: this.pushBeginTime,
          pushEndTime: this.pushEndTime,
          curPage: this.curPage
        },
        withCredentials: true,
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

        if (this.select_pushStatus === '92') {
          this.allRetryDisable = false
        }

        this.pushList = response.data.pushRecordList
        this.total = response.data.total
        this.curPage = curPage
        this.loading = false

      }, (error) => {
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

    handleTableChange(val) {
      this.currentRow = val;
    },
    // 选择仓库
    selectWarehouse(warehouse) {

    },
    // 选择平台
    selectPlatform(platform) {
      this.select_platform = platform
      this.select_app = ''
      this.AppOptions = []

      // 查询平台下的应用
      axios({
        url: this.host + '/toolkit/ab/getAppList',
        method: 'GET',
        params: {
          platformCode: platform
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
        let AppList = response.data
        for (let i = 0; i < AppList.length; i++) {
          let label = AppList[i]['appName']
          let value = AppList[i]['appCode']
          this.AppOptions.push({'label': label, 'value': value})
        }
      }, error => {
        console.log(error)
      })


    },
    selectApp(app) {
      this.select_app = app
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
    clearEnt() {
      this.ent = ''
    },
    clearPlatform() {
      this.select_platform = ''
    },
    clearApp() {
      this.select_app = ''
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
      if (row.businessNo) {
        this.Record_Body_Title = row.businessNo
      } else {
        this.Record_Body_Title = row.thirdNo
      }

      this.pushRecord = {}

      axios({
        url: this.host + '/toolkit/ab/getPushRecordDetail',
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

    handlePushBodyClick(row) {
      if (row.businessNo) {
        this.Record_Body_Title = row.businessNo
      } else {
        this.Record_Body_Title = row.thirdNo
      }

      this.push_body = ''
      this.api_param = ''

      axios({
        url: this.host + '/toolkit/ab/getPushRecordDetail',
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
        url: this.host + '/toolkit/ab/updateApiParam',
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
        url: this.host + '/toolkit/ab/updatePushBody',
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
            message: '更新成功',
            type: 'success'
          });
        } else {
          this.$message({
            message: '更新失败',
            type: 'warning'
          });
        }
      }, error => {
        console.log(error)
        this.$message({
          message: '更新失败',
          type: 'warning'
        });
      })
    },


    update_api_param_push_body() {

      axios({
        url: this.host + '/toolkit/ab/updateApiParamPushBody',
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

      axios({
        url: this.host + '/toolkit/ab/retryPushRecord',
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

    allRetry() {

      this.$confirm('将筛选出来的推送记录全部重试吗?', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
        showClose: false
      }).then(() => {

        this.loading = true
        this.loadingText = '重试中...'

        axios({
          url: this.host + '/ab/platformPushRecordAllRetry',
          method: 'POST',
          data: {
            enterpriseCode: this.select_enterprise,
            warehouseCode: this.select_warehouse,
            platformNo: this.select_platform,
            appNo: this.select_app,
            pushType: this.select_pushType,
            pushStatus: this.select_pushStatus,
            businessNo: this.businessNo,
            thirdNo: this.thirdNo,
            recordCode: this.recordCode,
            ent: this.ent,
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

          if (response.data === 'success') {

            this.loading = false

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

          this.loading = false
        })

      }).catch(() => {
      });
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
          //
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
              console.log(err)
            }
          }

          data = JSON.stringify(obj, null, 4)
        } catch (err) {
          console.log(err)
        }
      }

      if (data) {
        // 显示格式化之后的结果
        this.format_result = data
      }

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
  color: #409EFF;
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