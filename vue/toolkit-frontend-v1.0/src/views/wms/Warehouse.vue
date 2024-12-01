<template>
  <div>
    <section class="content clearfix" style="width: 97%;">
      <div class="el-backtop" style="right: 40px; top: 130px;">
        <el-link type="primary" :href="'/'" :underline="false" target="_blank"><i class="el-icon-s-home"></i></el-link>
      </div>
      <el-divider content-position="right">{{ env }}环境</el-divider>


      <el-form :inline="true" class="demo-form-inline">

        <div>
          <el-input v-model="warehouseCode" placeholder="YENU" clearable @clear="clearWarehouseCode"
                    style="width: 300px;">
            <template slot="prepend">仓库编码</template>
          </el-input>
          <el-input v-model="thirdNo" placeholder="MPRJ" clearable @clear="clearThirdNo"
                    style="width: 300px; margin-left: 5px;">
            <template slot="prepend">三方编码</template>
          </el-input>
          <div style="display: inline-block; margin-top: 3px; margin-bottom: 3px; margin-left: 5px;">
            <el-button type="primary" @click="onSubmit">查询</el-button>
          </div>
        </div>

        <!-- 结果 -->
        <div style="margin-top: 15px;">

          <!-- 仓库信息 -->
          <div style="margin-top: 10px;" v-loading="loading">
            <el-divider content-position="left">仓库信息</el-divider>

            <div style="margin-left: 40px; font-weight: 500; font-size: 14px;">

              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">仓库名称:</label><label>&nbsp;&nbsp;&nbsp;{{ warehouse.warehouseName }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">仓库名称:</label><label>&nbsp;&nbsp;&nbsp;{{ warehouse.warehouseCode }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">状态:</label><label>&nbsp;&nbsp;&nbsp;{{ warehouse.enable }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">已删除:</label><label>&nbsp;&nbsp;&nbsp;{{ warehouse.deleted }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">企业名称:</label><label>&nbsp;&nbsp;&nbsp;{{ warehouse.enterpriseName }}</label>
              </div>

            </div>
          </div>


          <!-- 资源信息 -->
          <div style="margin-top: 10px;">
            <el-divider content-position="left">资源信息</el-divider>

            <div style="margin-left: 40px; font-weight: 500; font-size: 14px;">
              <template>
                <el-table :data="resourceList" border style="width: 40%" :row-style="{ height: 10+'px'}"
                          :cell-style="{padding:0+'px'}"> <!-- height="250" -->
                  <el-table-column fixed label="序号" type="index" width="50"></el-table-column>
                  <el-table-column prop="resourceName" label="资源名称"></el-table-column>
                </el-table>
              </template>
            </div>
          </div>

          <!-- 物流公司信息 -->
          <div style="margin-top: 10px;">
            <el-divider content-position="left">物流公司信息</el-divider>

            <div style="margin-left: 40px; font-weight: 500; font-size: 14px;">
              <template>
                <el-table :data="logisticsList" border style="width: 40%" :row-style="{ height: 10+'px'}"
                          :cell-style="{padding:0+'px'}"> <!-- height="250" -->
                  <el-table-column fixed label="序号" type="index" width="50"></el-table-column>
                  <el-table-column prop="logisticsName" label="物流公司"></el-table-column>
                  <el-table-column sortable :sort-method="sortStatus" align="center" label="状态" width="80">
                    <template slot-scope="scope">
                                            <span v-if="scope.row.enableDesc == '禁用'">
                                                <span style="color: red;">禁用</span>
                                            </span>
                      <span v-else>
                                                启用
                                            </span>
                    </template>
                  </el-table-column>
                  <el-table-column prop="createTime" label="创建时间" width="200"></el-table-column>
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
  name: "Warehouse",
  data() {

    return {
      env: Config.env,
      host: Config.host,

      warehouseCode: '',
      thirdNo: '',

      warehouse: {
        warehouseName: '',
        warehouseCode: '',
        enterpriseName: '',
        enable: '',
        deleted: '',
      },

      resourceList: [],
      logisticsList: [],

      loading: false


    }
  },

  created: function () {
  },
  methods: {
    // 查询
    onSubmit() {
      if (!this.warehouseCode && !this.thirdNo) {
        this.$message({
          message: '编码为空',
          type: 'warning'
        });
        return;
      }
      this.loading = true

      axios({
        url: this.host + '/toolkit/tools/getWarehouseInfo2',
        method: 'GET',
        params: {
          warehouseCode: this.warehouseCode,
          thirdNo: this.thirdNo
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

        this.warehouse = {}
        this.resourceList = []
        this.logisticsList = []

        this.loading = false

        let warehouse = response.data.warehouse
        if (!warehouse) {
          this.$message({
            message: '未查询到数据',
            type: 'warning'
          });
          return;
        }

        let warehouse_response = response.data.warehouse
        this.warehouse.warehouseName = warehouse_response['warehouseName']
        this.warehouse.warehouseCode = warehouse_response['warehouseCode']
        this.warehouse.enable = warehouse_response['enable']
        this.warehouse.deleted = warehouse_response['deleted']

        let enterprise_response = response.data.enterprise
        this.warehouse.enterpriseName = enterprise_response['enterpriseName']

        this.resourceList = response.data.warehouseResourceList
        this.logisticsList = response.data.logisticsList


      }, error => {
        console.log(error)
        this.$message({
          message: '查询失败',
          type: 'warning'
        });
        this.loading = false
      })

    },


    clearWarehouseCode() {
      this.warehouseCode = ''
      //this.thirdNo = ''

      this.warehouse = {}
      this.resourceList = []
      this.logisticsList = []
      this.loading = false
    },
    clearThirdNo() {
      //this.warehouseCode = ''
      this.thirdNo = ''

      this.warehouse = {}
      this.resourceList = []
      this.logisticsList = []
      this.loading = false
    },
    sortStatus(a, b) {
      if (a.enable > b.enable) {
        return -1
      }
    }
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