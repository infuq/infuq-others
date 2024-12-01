<template>
  <div>
    <section class="content clearfix" style="width: 97%;">
      <div class="el-backtop" style="right: 40px; top: 130px;">
        <el-link type="primary" :href="'/'" :underline="false" target="_blank"><i class="el-icon-s-home"></i></el-link>
      </div>
      <el-divider content-position="right">{{ env }}环境</el-divider>

      <el-form :inline="true" class="demo-form-inline">

        <el-input v-model="userName" placeholder="用户名" clearable @clear="clearUserName" style="width: 220px;"
                  :disabled="true">
          <template slot="prepend">用户名</template>
        </el-input>
        <el-input v-model="excludeUserName" placeholder="排除用户名" clearable @clear="clearExcludeUserName"
                  style="width: 300px; margin-left: 5px;" :disabled="true">
          <template slot="prepend">排除用户名</template>
        </el-input>
        <el-input v-model="remark" placeholder="动作" clearable @clear="clearRemark"
                  style="width: 300px; margin-left: 5px;" :disabled="true">
          <template slot="prepend">动作</template>
        </el-input>
        <el-input v-model="method" placeholder="方法名" clearable @clear="clearMethod"
                  style="width: 300px; margin-left: 5px;" :disabled="true">
          <template slot="prepend">方法名</template>
        </el-input>


        <div>
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
              类型
            </div>
            <el-select v-model="select_source_type" placeholder="请选择类型"
                       @change="selectSourceType(select_source_type)" filterable clearable @clear="clearSourceType">
              <el-option v-for="item in SourceTypeOptions" :key="item.value" :label="item.label" :value="item.value"
                         :disabled="item.disabled"></el-option>
            </el-select>
          </div>
          <el-input v-model="businessNo" placeholder="例如 RK-230807-000004" clearable @clear="clearBusinessNo"
                    style="width: 300px; margin-left: 5px;">
            <template slot="prepend">业务单号</template>
          </el-input>
        </div>

        <div>
          <el-input v-model="beginTime" placeholder="2023-03-21 09:01:00" clearable @clear="clearBeginTime"
                    style="width: 300px;">
            <template slot="prepend">起时间</template>
          </el-input>
          <el-input v-model="endTime" placeholder="2023-03-21 18:12:20" clearable @clear="clearEndTime"
                    style="width: 300px; margin-left: 5px;">
            <template slot="prepend">止时间</template>
          </el-input>
          <div style="display: inline-block; margin-top: 3px; margin-bottom: 3px; margin-left: 5px;">
            <el-button type="primary" @click="onSubmit(-1)">查询</el-button>
          </div>
        </div>
        <!-- 结果 -->
        <div style="margin-top: 15px;">
          <!-- 操作结果 -->
          <div style="margin-top: 10px;" v-loading="loading">
            <el-divider content-position="left">WMS访问记录</el-divider>

            <div style="margin-left: 40px; font-weight: 500; font-size: 14px;">
              <template>
                <el-table :data="operationRecordList" border style="width: 100%" :row-style="{ height: 10+'px'}"
                          :cell-style="{padding:0+'px'}"> <!-- height="250" -->
                  <el-table-column fixed label="序号" type="index" width="50"></el-table-column>
                  <!--
                  <el-table-column prop="userName" label="用户名" max-width="200" :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="realName" label="实名" max-width="200" :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="moduleName" label="模块名" max-width="200" :show-overflow-tooltip="true"></el-table-column> -->
                  <el-table-column prop="remark" label="动作" max-width="200"
                                   :show-overflow-tooltip="true"></el-table-column>

                  <el-table-column label="业务单号" max-width="220" :show-overflow-tooltip="true">
                    <template slot-scope="scope">
                      <i @click="copy(scope.row.businessNo)" class="el-icon-document-copy"
                         v-if="scope.row.businessNo != null && scope.row.businessNo != ''"></i>
                      <el-button @click="handleOperationDetailClick(scope.row)" type="text" style="margin-left: 3px;">
                        {{ scope.row.businessNo }}
                      </el-button>
                    </template>
                  </el-table-column>


                  <!--
                  <el-table-column prop="businessIdStr" label="业务主键" max-width="220" :show-overflow-tooltip="true"></el-table-column>
                  -->
                  <el-table-column prop="messageId" label="MQ消息ID" max-width="220"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="method" label="方法名" min-width="150"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="sourceName" label="类型" width="120"></el-table-column>

                  <el-table-column prop="desc" label="说明信息" max-width="100"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <!--
                  <el-table-column prop="sourceIp" label="请求IP" width="180"></el-table-column>
                  <el-table-column prop="handleIp" label="事件发生IP" width="140"></el-table-column>
                  <el-table-column label="观测云TRACE_ID" max-width="100" :show-overflow-tooltip="true">
                      <template slot-scope="scope">
                          <span v-if="scope.row.traceId != null && scope.row.traceId != ''">
                              <i @click="copy(scope.row.traceId)" class="el-icon-document-copy"></i>&nbsp;&nbsp;{{ scope.row.traceId }}
                          </span>
                      </template>
                  </el-table-column>
                  -->
                  <el-table-column prop="createTimeStr" label="访问时间" width="200"></el-table-column>
                  <!--
                  <el-table-column fixed="right" label="操作">
                      <template slot-scope="scope">
                          <i @click="copy(scope.row.jsonFormat)" class="el-icon-document-copy"></i>&nbsp;&nbsp;
                          <el-button @click="handleOperationDetailClick(scope.row)" type="text">详情</el-button>
                      </template>
                  </el-table-column>
                  -->
                </el-table>
              </template>


              <el-dialog :title="'序号 [ ' + DETAIL_INDEX + ' ] 内容体'" :visible.sync="DETAIL_dialogVisible"
                         :show-close="false" width="50%">
                <div style="display: block; margin: 5px 0;">
                  <label style="display: inline-block; text-align: right;">[ 主键
                    ]</label><label>&nbsp;&nbsp;&nbsp;{{ operationRecord.recordIdStr }}</label>&nbsp;&nbsp;<i
                    @click="copy(operationRecord.recordIdStr)" class="el-icon-document-copy"></i>
                </div>
                <div style="display: block; margin: 5px 0;">
                  <label style="display: inline-block; text-align: right;">[ 业务单号 ]</label><label>&nbsp;&nbsp;&nbsp;{{ operationRecord.businessNo }}</label>
                  <span v-if="operationRecord.businessNo != null && operationRecord.businessNo != ''"
                        style="vertical-align: bottom;">
                              &nbsp;&nbsp;<i @click="copy(operationRecord.businessNo)"
                                             class="el-icon-document-copy"></i>
                          </span>
                </div>
                <div style="display: block; margin: 5px 0;">
                  <label style="display: inline-block; text-align: right;">[ 业务主键 ]</label><label>&nbsp;&nbsp;&nbsp;{{ operationRecord.businessIdStr }}</label>
                  <span v-if="operationRecord.businessIdStr != null && operationRecord.businessIdStr != ''"
                        style="vertical-align: bottom;">
                              &nbsp;&nbsp;<i @click="copy(operationRecord.businessIdStr)"
                                             class="el-icon-document-copy"></i>
                          </span>
                </div>
                <div style="display: block; margin: 5px 0;">
                  <label style="display: inline-block; text-align: right;">[ 观测云ID ]</label><label>&nbsp;&nbsp;&nbsp;{{ operationRecord.traceId }}</label>
                  <span v-if="operationRecord.traceId != null && operationRecord.traceId != ''">
                              &nbsp;&nbsp;<i @click="copy(operationRecord.traceId)" class="el-icon-document-copy"></i>
                          </span>
                </div>
                <div style="display: block; margin: 5px 0;">
                  <label style="display: inline-block; text-align: right;">[ 动作名称 ]</label><label>&nbsp;&nbsp;&nbsp;{{ operationRecord.remark }}</label>
                </div>
                <div style="display: block; margin: 5px 0;">
                  <label style="display: inline-block; text-align: right;">[ 方法名称 ]</label><label>&nbsp;&nbsp;&nbsp;{{ operationRecord.method }}</label>
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
  name: "OperationRecord",
  data() {

    return {
      env: Config.env,
      host: Config.host,

      loading: false,

      userName: '',
      excludeUserName: '',
      remark: '',
      method: '',
      operationRecordList: [],
      beginTime: this.dateFormat() + " 00:00:00",
      endTime: this.dateFormat() + " 23:59:59",
      businessNo: '',

      select_source_type: '4',
      SourceTypeOptions: [
        {
          label: '浏览器',
          value: '1',
          disabled: true
        },
        {
          label: 'MQ',
          value: '4'
        },
        {
          label: 'OPEN_FEIGN',
          value: '3',
          disabled: true
        },
        {
          label: 'POST_MAN',
          value: '2',
          disabled: true
        }
      ],


      total: 0,
      curPage: 1,

      operationRecord: {},
      DETAIL_INDEX: '',
      DETAIL_dialogVisible: false,

    }
  },

  created: function () {

    //this.onSubmit(1)

    //this.selectSourceType('4');

  },
  methods: {

    selectSourceType(source_type) {
      this.select_source_type = source_type
    },
    // 查询
    onSubmit(curPage) {

      this.operationRecordList = []
      if (curPage == -1) {
        this.curPage = 1
      }
      this.total = 0
      this.loading = true
      axios({
        url: this.host + '/toolkit/or/getOperationRecord',
        method: 'POST',
        data: {
          userName: this.userName,
          excludeUserName: this.excludeUserName,
          remark: this.remark,
          method: this.method,
          businessNo: this.businessNo,
          sourceType: this.select_source_type,
          beginTime: this.beginTime,
          endTime: this.endTime,
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

            this.operationRecordList = response.data.operationRecordList
            this.total = response.data.total
            this.curPage = curPage
            this.loading = false
          }, error => {
            this.loading = false
            this.$message({
              message: '查询失败',
              type: 'warning'
            });

            this.curPage = 1
            this.total = 0
            this.operationRecordList = []
          })

    },

    handleOperationDetailClick(row) {
      this.DETAIL_INDEX = row.index

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
            this.DETAIL_dialogVisible = true
          }, error => {
            this.$message({
              message: '查询操作记录失败',
              type: 'warning'
            });
          })
    },

    handleCurrentChange(current_page) {
      this.curPage = current_page
      this.onSubmit(current_page)
    },

    clearUserName() {
      this.userName = ''
    },
    clearExcludeUserName() {
      this.excludeUserName = ''
    },
    clearRemark() {
      this.remark = ''
    },
    clearMethod() {
      this.method = ''
    },
    clearBusinessNo() {
      this.method = ''
    },
    clearBeginTime() {
      this.beginTime = ''
    },
    clearEndTime() {
      this.endTime = ''
    },
    clearSourceType() {
      this.select_source_type = ''
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