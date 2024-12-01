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

        <el-input v-model="username" placeholder="zhangsan" clearable @clear="clearUsername"
                  style="width: 300px; margin-left: 5px;">
          <template slot="prepend">账号</template>
        </el-input>
        <div style="display: inline-block; margin-top: 3px; margin-bottom: 3px; margin-left: 5px;">
          <el-button type="primary" @click="onSubmit" disabled>查询</el-button>
        </div>

        <!-- 结果 -->
        <div style="margin-top: 15px;">

          <!-- 推送结果 -->
          <div style="margin-top: 10px;" v-loading="loading">
            <el-divider content-position="left">仓配账号信息</el-divider>

            <div style="margin-left: 40px; font-weight: 500; font-size: 14px;">
              <template>
                <el-table :data="accountList" border style="width: 100%" :row-style="{ height: 10+'px'}"
                          :cell-style="{padding:0+'px'}"> <!-- height="250" -->
                  <el-table-column fixed label="序号" type="index" width="50">
                    <template slot-scope="scope">
                                    <span>
                                        {{ scope.$index + 1 }}
                                    </span>
                    </template>
                  </el-table-column>
                  <el-table-column prop="enterpriseName" label="企业名称" max-width="220"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="owner" label="企业拥有者" max-width="220"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="accountCode" label="账号编码" max-width="220"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="mobile" label="手机号" max-width="220"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="username" label="账号" max-width="220"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="realName" label="姓名" max-width="220"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="enable" label="启用" max-width="220"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="allWarehouse" label="全部仓库权限" max-width="220"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="email" label="邮箱" max-width="220"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="deleted" label="删除" max-width="220"
                                   :show-overflow-tooltip="true"></el-table-column>

                </el-table>
              </template>
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
  name: "Account",
  data() {

    return {
      env: Config.env,
      host: Config.host,

      select_enterprise: '',
      EnterpriseOptions: [],
      username: '',

      total: 0,
      curPage: 1,
      loading: false,
      accountList: [],

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
        }, (error) => {
          console.log(error)
          this.$message({
            message: '查询企业失败',
            type: 'warning'
          });
        })

  },
  methods: {
    // 查询
    onSubmit() {
      this.loading = true
      axios({
        url: this.host + '/toolkit/tools/getAccount',
        method: 'GET',
        params: {
          enterpriseCode: this.select_enterprise,
          username: this.username
        },
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        }
      })
          .then((response) => {

            if (response.data['code'] && response.data['code'] === 1126) {
              this.$router.push("/login")
              return
            }

            this.loading = false

          }, (error) => {
            console.log(error)
            this.$message({
              message: '查询失败',
              type: 'warning'
            });
            this.loading = false
          })

    },

    selectEnterprise(enterprise) {
      this.select_enterprise = enterprise
    },


    clearEnterprise() {
      this.select_enterprise = ''
      this.select_warehouse = ''
      this.WarehouseOptions = []

      this.loading = false
    },
    clearUsername() {
      this.username = ''
    },
    handleCurrentChange(current_page) {
      this.curPage = current_page
      this.onSubmit(current_page)
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