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

        <!--
        <el-input v-model="customerOrderNo" placeholder="MPRJ" clearable @clear="clearCustomerOrderNo" style="width: 300px;">
            <template slot="prepend">订货单号</template>
        </el-input>
-->
        <el-input v-model="beginCreateTime" placeholder="2023-03-21 09:01:00" clearable @clear="clearBeginCreateTime"
                  style="width: 300px; margin-left: 5px;">
          <template slot="prepend">起时间</template>
        </el-input>
        <el-input v-model="endCreateTime" placeholder="2023-03-21 18:12:20" clearable @clear="clearEndCreateTime"
                  style="width: 300px; margin-left: 5px;">
          <template slot="prepend">止时间</template>
        </el-input>

        <div style="display: inline-block; margin-top: 3px; margin-bottom: 3px; margin-left: 5px;">
          <el-button type="primary" @click="onSubmit(-1)">查询</el-button>
        </div>


        <!-- 结果 -->
        <div style="margin-top: 15px;">

          <div style="margin-top: 10px;" v-loading="loading">
            <el-divider content-position="left">订货单</el-divider>

            <div style="margin-left: 40px; font-weight: 500; font-size: 14px;">
              <template>
                <el-table :data="customerOrderList" border style="width: 100%" :row-style="{ height: 10+'px'}"
                          :cell-style="{padding:0+'px'}" highlight-current-row @current-change="handleTableChange">
                  <!-- height="250" -->
                  <el-table-column fixed label="序号" type="index" width="50">
                    <template slot-scope="scope">
                      {{ scope.$index + 1 }}
                    </template>
                  </el-table-column>
                  <el-table-column prop="warehouseName" label="仓库名称" max-width="190"
                                   :show-overflow-tooltip="true"></el-table-column>

                  <el-table-column label="订货单号" max-width="190" :show-overflow-tooltip="true">
                    <template slot-scope="scope">
                      <router-link :to="{path: '/store_customer_order', query:{customerOrderNo: scope.row.customerOrderNo}}" target="_blank" style="margin-left: 5px;">
                        <span class="icon-link">{{ scope.row.customerOrderNo }}</span>
                      </router-link>
                    </template>
                  </el-table-column>
                  <el-table-column label="自定义单号" max-width="190" :show-overflow-tooltip="true">
                    <template slot-scope="scope">
                      <!--                                            <el-link type="primary" :href="'store_customer_order_3.html?customerOrderCode='+scope.row.customerOrderCode" :underline="false" target="_blank">{{scope.row.customerOrderCode}}</el-link>-->

                      <router-link
                          :to="{path: '/store_customer_order', query:{customerOrderCode: scope.row.customerOrderCode}}"
                          target="_blank" style="margin-left: 5px;">

                        <span class="icon-link">{{ scope.row.customerOrderCode }}</span>
                      </router-link>

                    </template>
                  </el-table-column>
                  <el-table-column label="门店订单号" max-width="190" :show-overflow-tooltip="true">
                    <template slot-scope="scope">
                      <!--                                            <el-link type="primary" :href="'store_customer_order_3.html?storeOrderCode='+scope.row.storeOrderCode" :underline="false" target="_blank">{{scope.row.storeOrderCode}}</el-link>-->

                      <router-link
                          :to="{path: '/store_customer_order', query:{storeOrderCode: scope.row.storeOrderCode}}"
                          target="_blank" style="margin-left: 5px;">

                        <span class="icon-link">{{ scope.row.storeOrderCode }}</span>
                      </router-link>


                    </template>
                  </el-table-column>

                  <el-table-column prop="tmsTypeName" label="配送方式" max-width="190"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="customerOrderFinishTypeStr" label="完结类型" max-width="190"
                                   :show-overflow-tooltip="true"></el-table-column>

                  <el-table-column prop="goodsOwnerName" label="货主" max-width="190"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="customerName" label="收获人" max-width="190"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="customerOrderSource" label="来源" max-width="190"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="customerOrderStatusStr" label="订单状态" max-width="190"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="sendOrderStatusStr" label="发货状态" max-width="190"
                                   :show-overflow-tooltip="true"></el-table-column>

                  <el-table-column prop="createTime" label="创建时间" width="200"></el-table-column>
                  <el-table-column prop="updateTime" label="更新时间" width="200"></el-table-column>
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
  name: "WarehouseStoreCustomerOrder",
  data() {

    return {
      env: Config.env,
      host: Config.host,


      select_warehouse: '',
      WarehouseOptions: [],

      warehouse: {
        warehouseName: '',
        warehouseCode: '',
        enterpriseName: '',
        enable: '',
        deleted: '',
      },

      beginCreateTime: this.dateFormat() + " 00:00:00",
      endCreateTime: this.dateFormat() + " 23:59:59",

      customerOrderList: [],
      customerOrderNo: '',

      total: 0,
      curPage: 1,

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

    }, error => {
      console.log(error)
      this.$message({
        message: '查询仓库失败',
        type: 'warning'
      });
    })

  },
  methods: {
    // 查询
    onSubmit(curPage) {
      let select_warehouse = this.select_warehouse
      if (!select_warehouse) {
        this.$message({
          message: '仓库不能为空',
          type: 'warning'
        });
        return;
      }

      this.customerOrderList = []

      if (curPage === -1) {
        this.curPage = 1
      }

      this.loading = true

      axios({
        url: this.host + '/toolkit/tools/selectByWarehouse',
        method: 'POST',
        data: {
          customerOrderNo: this.customerOrderNo,
          warehouseCode: select_warehouse,
          endCreateTime: this.endCreateTime,
          beginCreateTime: this.beginCreateTime,
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

        this.loading = false
        this.total = response.data.total
        this.customerOrderList = response.data.scoList;
        if (!this.customerOrderList) {
          this.$message({
            message: '未查询到数据',
            type: 'warning'
          });
          this.curPage = 1
          this.total = 0
        }

      }, error => {
        console.log(error)
        this.$message({
          message: '查询失败',
          type: 'warning'
        });
        this.curPage = 1
        this.total = 0
        this.loading = false
      })

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

    },
    clearWarehouse() {
      this.select_warehouse = ''
      this.loading = false
    },
    clearCustomerOrderNo() {
      this.customerOrderNo = ''
    },
    sortStatus(a, b) {
      if (a.enable > b.enable) {
        return -1
      }
    },

    handleTableChange(row) {
      this.currentRow = row;
    },

    handleCurrentChange(current_page) {
      this.curPage = current_page
      this.onSubmit(current_page)
    },

    dateFormat() {
      let date = new Date()
      let year = date.getFullYear()
      let month = date.getMonth() + 1 < 10 ? '0' + (date.getMonth() + 1) : date.getMonth() + 1
      let day = date.getDate() < 10 ? '0' + date.getDate() : date.getDate()
      return year + '-' + month + '-' + day
    },

    clearBeginCreateTime() {
      this.beginCreateTime = ''
    },
    clearEndCreateTime() {
      this.endCreateTime = ''
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