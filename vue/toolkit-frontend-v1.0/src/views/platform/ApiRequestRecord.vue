<template>
  <div>
    <section class="content clearfix" style="width: 97%;">
      <div class="el-backtop" style="right: 40px; top: 130px;">
        <el-link type="primary" :href="'/'" :underline="false" target="_blank"><i class="el-icon-s-home"></i></el-link>
      </div>
      <el-divider content-position="right">{{ env }}环境</el-divider>

      <el-form :inline="true" class="demo-form-inline">

        <el-input v-model="APIKey" placeholder="PPY1990010203049" clearable @clear="clearAPIKey" style="width: 350px;">
          <template slot="prepend">开发者APIKey</template>
        </el-input>
        <el-input v-model="appCode" placeholder="ENT1990" clearable @clear="clearAppCode"
                  style="width: 250px; margin-left: 5px;">
          <template slot="prepend">应用编码</template>
        </el-input>
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
            <el-divider content-position="left">对接平台API接口请求记录</el-divider>

            <div style="font-weight: 500; font-size: 14px;">
              <template>
                <el-table :data="recordList" border style="width: 100%" :row-style="{ height: 10+'px'}"
                          :cell-style="{padding:0+'px'}"> <!-- height="250" -->
                  <el-table-column fixed label="序号" type="index" width="50">
                    <template slot-scope="scope">
                                  <span v-if="scope.row.requestStatus == 2">
                                      <span style="color: red;">{{ scope.$index + 1 }}</span>
                                  </span>
                      <span v-else>
                                      {{ scope.$index + 1 }}
                                  </span>
                    </template>
                  </el-table-column>
                  <el-table-column fixed label="记录编码" min-width="100" :show-overflow-tooltip="true">
                    <template slot-scope="scope">
                      <i @click="copy(scope.row.recordCode)" class="el-icon-document-copy"></i>
                      <el-button @click="handleDetailClick(scope.row)" type="text">
                        {{ scope.row.recordCode }}
                      </el-button>
                    </template>
                  </el-table-column>
                  <el-table-column prop="developerApiKey" label="开发者APIKey" max-width="150"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="appCode" label="应用编码" max-width="50"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="businessCode" label="业务编码" max-width="50"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="businessName" label="业务名称" width="200"></el-table-column>

                  <el-table-column label="请求状态" width="120">
                    <template slot-scope="scope">
                                  <span v-if="scope.row.requestStatus == 2">
                                      <span style="color: red;">失败</span>
                                  </span>
                      <span v-else>
                                      成功
                                  </span>
                    </template>
                  </el-table-column>
                  <el-table-column prop="requestIp" label="请求地址" width="180"></el-table-column>
                  <el-table-column prop="errorMsg" label="错误信息" max-width="250"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="createTimeStr" label="创建时间" width="200"></el-table-column>

                  <!--
                  <el-table-column fixed="right" label="操作">
                      <template slot-scope="scope">
                          <el-button @click="handleDetailClick(scope.row)" type="text">详情</el-button>
                      </template>
                  </el-table-column>
                  -->
                </el-table>
              </template>


              <el-dialog :title="'[' + DETAIL_INDEX + '][ ' + TITLE + ' ] 内容体'" :visible.sync="DETAIL_dialogVisible"
                         :show-close="false" width="50%">
                <div style="display: block; margin: 5px 0;">
                  <label style="display: inline-block; text-align: right;">[ 记录编码 ]</label><label>&nbsp;&nbsp;&nbsp;{{ operationRecord.recordCode }}</label>
                </div>
                <div style="display: block; margin: 5px 0;">
                  <label style="display: inline-block; text-align: right;">[ 开发者APIKey ]</label><label>&nbsp;&nbsp;&nbsp;{{ operationRecord.developerApiKey }}</label>
                </div>
                <div style="display: block; margin: 5px 0;">
                  <label style="display: inline-block; text-align: right;">[ 应用编码 ]</label><label>&nbsp;&nbsp;&nbsp;{{ operationRecord.appCode }}</label>
                </div>
                <div style="display: block; margin: 5px 0;">
                  <label style="display: inline-block; text-align: right;">[ 业务编码 ]</label><label>&nbsp;&nbsp;&nbsp;{{ operationRecord.businessCode }}</label>
                </div>
                <div style="display: block; margin: 5px 0;">
                  <label style="display: inline-block; text-align: right;">[ 业务名称 ]</label><label>&nbsp;&nbsp;&nbsp;{{ operationRecord.businessName }}</label>
                </div>
                <div style="display: block; margin: 5px 0;">
                  <label style="display: inline-block; text-align: right;">[ 请求地址 ]</label><label>&nbsp;&nbsp;&nbsp;{{ operationRecord.requestIp }}</label>
                </div>
                <div style="display: block; margin: 5px 0;">
                  <label style="display: inline-block; text-align: right;">[ 请求耗时 ]</label><label>&nbsp;&nbsp;&nbsp;{{ operationRecord.requestTime }}</label>
                </div>
                <div style="display: block; margin: 5px 0;">
                  <label style="display: inline-block; text-align: right;">[ 请求参数 ]</label>
                  <span v-if="operationRecord.requestParamUrl != null && operationRecord.requestParamUrl != ''"
                        style="vertical-align: bottom;">
                              &nbsp;&nbsp;<el-link type="primary" :href="requestParamUrl"
                                                   target="_blank">查看参数</el-link>
                          </span>
                </div>
                <div style="display: block; margin: 5px 0;">
                  <label style="display: inline-block; text-align: right;">[ 请求状态 ]</label>
                  <span v-if="operationRecord.requestStatus == 2">
                              <span style="color: red;">&nbsp;&nbsp;失败</span>
                          </span>
                  <span v-if="operationRecord.requestStatus != 2">
                              <span>&nbsp;&nbsp;成功</span>
                          </span>
                </div>
                <div style="display: block; margin: 5px 0;">
                  <label style="display: inline-block; text-align: right;">[ 错误信息 ]</label><label>&nbsp;&nbsp;&nbsp;{{ operationRecord.errorMsg }}</label>
                </div>
                <div style="display: block; margin: 5px 0;">
                  <label style="display: inline-block; text-align: right;">[ 创建时间 ]</label><label>&nbsp;&nbsp;&nbsp;{{ operationRecord.createTimeStr }}</label>
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
  name: "ApiRequestRecord",
  data() {

    return {
      env: Config.env,
      host: Config.host,
      loading: false,

      APIKey: '',
      appCode: '',

      recordList: [],
      beginTime: this.dateFormat() + " 00:00:00",
      endTime: this.dateFormat() + " 23:59:59",

      total: 0,
      curPage: 1,

      DETAIL_INDEX: '',
      TITLE: '',
      DETAIL_dialogVisible: false,
      operationRecord: {},

      requestParamUrl: '',


    }
  },

  created: function () {

    //this.onSubmit(1)

  },
  methods: {
    // 查询
    onSubmit(curPage) {

      this.operationRecordList = []
      if (curPage === -1) {
        this.curPage = 1
      }
      this.total = 0
      this.loading = true
      axios({
        url: this.host + '/toolkit/developer/findAll',
        method: 'POST',
        data: {
          apiKey: this.APIKey,
          appCode: this.appCode,
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

        this.recordList = response.data.recordList
        this.total = response.data.total
        this.curPage = curPage
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
        this.recordList = []
      })

    },

    handleDetailClick(row) {
      this.TITLE = row.recordCode
      this.DETAIL_INDEX = row.index

      this.operationRecord = {}

      axios({
        url: this.host + '/toolkit/developer/detail',
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
        this.requestParamUrl = this.operationRecord.requestParamUrl
      }, error => {
        console.log(error)
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

    clearAPIKey() {
      this.APIKey = ''
    },
    clearAppCode() {
      this.appCode = ''
    },

    clearBeginTime() {
      this.beginTime = ''
    },
    clearEndTime() {
      this.endTime = ''
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