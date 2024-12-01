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
            仓库
          </div>
          <el-select v-model="select_warehouse" placeholder="请选择仓库" @change="selectWarehouse(select_warehouse)"
                     filterable clearable @clear="clearWarehouse">
            <el-option v-for="item in WarehouseOptions" :key="item.value" :label="item.label"
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
            企业
          </div>
          <el-select v-model="select_enterprise" placeholder="请选择企业" @change="selectEnterprise(select_enterprise)"
                     filterable>
            <el-option v-for="item in EnterpriseOptions" :key="item.value" :label="item.label"
                       :value="item.value"></el-option>
          </el-select>
        </div>

        <!--
        <el-form-item>
            <el-button type="primary" @click="onSubmit">查询</el-button>
        </el-form-item>
-->
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
  name: "EnterpriseWarehouse",
  data() {
    return {
      env: Config.env,
      host: Config.host,

      select_enterprise: '',
      select_warehouse: '',
      EnterpriseOptions: [],
      WarehouseOptions: [],

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
        }, (error) => {
          console.log(error)
          this.$message({
            message: '查询仓库失败',
            type: 'warning'
          });
        })

  },
  methods: {
    // 查询
    onSubmit() {
      let select_enterprise = this.select_enterprise
      if (!select_enterprise) {
        this.$message({
          message: '企业不能为空',
          type: 'warning'
        });
        return;
      }
      let select_warehouse = this.select_warehouse
      if (!select_warehouse) {
        this.$message({
          message: '仓库不能为空',
          type: 'warning'
        });
        return;
      }

      this.loading = true

      axios({
        url: this.host + '/toolkit/tools/getWarehouseInfo',
        method: 'GET',
        params: {
          enterpriseCode: select_enterprise,
          warehouseCode: select_warehouse
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

          }, (error) => {
            console.log(error)
            this.$message({
              message: '查询失败',
              type: 'warning'
            });
            this.loading = false
          })

    },

    // 选择企业
    selectEnterprise(enterprise) {
      this.select_enterprise = enterprise
      this.onSubmit()
    },
    // 选择仓库
    selectWarehouse(warehouse) {

      if (!warehouse) {
        this.$message({
          message: '请选择仓库',
          type: 'warning'
        });
        return;
      }

      this.select_warehouse = warehouse

      this.select_enterprise = ''
      this.EnterpriseOptions = []
      this.warehouse = {}
      this.resourceList = []
      this.logisticsList = []

      // 查询仓库下的企业
      axios({
        url: this.host + '/toolkit/tools/getEnterprise',
        method: 'GET',
        params: {
          warehouseCode: warehouse
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
                message: '未查询企业数据',
                type: 'warning'
              });
            }

            let EnterpriseList = response.data
            if (EnterpriseList.length > 0) {
              for (let i = 0; i < EnterpriseList.length; i++) {
                let label = EnterpriseList[i]['enterpriseName']
                let value = EnterpriseList[i]['enterpriseCode']
                this.EnterpriseOptions.push({'label': label, 'value': value})
              }
              // 默认选中第一个
              this.select_enterprise = EnterpriseList[0]['enterpriseCode']

              this.onSubmit()
            }

          }, (error) => {
            console.log(error)
            this.$message({
              message: '查询失败',
              type: 'warning'
            });
          })


    },
    clearWarehouse() {
      this.select_enterprise = ''
      this.select_warehouse = ''

      this.EnterpriseOptions = []
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