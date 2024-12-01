<template>
  <div>
    <section class="content clearfix" style="width: 97%;">
      <div class="el-backtop" style="right: 40px; top: 130px;">
        <el-link type="primary" :href="'/'" :underline="false" target="_blank"><i class="el-icon-s-home"></i></el-link>
      </div>
      <el-divider content-position="right">{{ env }}环境</el-divider>

      <el-form :inline="true" class="demo-form-inline">

        <div v-if="isShowQuery">
          <el-input v-model="businessNo" placeholder="DB-230919-000005" clearable @clear="clearBusinessNo" style="width: 330px;">
            <template slot="prepend">调拨单号</template>
          </el-input>
          <div style="display: inline-block; margin-top: 3px; margin-bottom: 3px; margin-left: 5px;">
            <el-button type="primary" @click="onSubmit">查询</el-button>
          </div>
        </div>

        <!-- 结果 -->
        <div style="margin-top: 15px;">

          <!-- 调拨单 -->
          <div style="margin-top: 10px;" v-loading="loading">
            <el-divider content-position="left">调拨单</el-divider>

            <div style="margin-left: 40px; font-weight: 500; font-size: 14px;">

              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">调拨单号:</label><label>&nbsp;&nbsp;&nbsp;{{ allocateOrder.allocateOrderNo }}</label>
                <span v-if="showCopyNo">&nbsp;&nbsp;<i @click="copy(allocateOrder.allocateOrderNo)" class="el-icon-document-copy"></i>
                </span>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">企业:</label><label>&nbsp;&nbsp;&nbsp;{{ allocateOrder.enterpriseName }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">货主:</label><label>&nbsp;&nbsp;&nbsp;{{ allocateOrder.ownerName }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">调出仓库:</label><label>&nbsp;&nbsp;&nbsp;{{ allocateOrder.outWarehouseName }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">调入仓库:</label><label>&nbsp;&nbsp;&nbsp;{{ allocateOrder.inWarehouseName }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">状态:</label>
                <span v-if="allocateOrder.allocateStatusStr === '已调拨'">
                  <span style="color: green;">&nbsp;&nbsp;已调拨</span>
                </span>
                <span v-else-if="allocateOrder.allocateStatusStr === '已作废'">
                  <span style="color: red;">&nbsp;&nbsp;已作废</span>
                </span>
                <span v-else-if="allocateOrder.allocateStatusStr === '待调拨'">
                  <span style="">&nbsp;&nbsp;待调拨</span>
                  <span>&nbsp;&nbsp;<i @click="invalid()" class="fa fa-ban" aria-hidden="true"></i>
                  </span>
                </span>
                <span v-else>&nbsp;&nbsp;{{ allocateOrder.allocateStatusStr }}
                </span>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">创建时间:</label><label>&nbsp;&nbsp;&nbsp;{{ allocateOrder.createTimeDesc }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">更新时间:</label><label>&nbsp;&nbsp;&nbsp;{{ allocateOrder.updateTimeDesc }}</label>
              </div>

              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">SQL:</label><label>
                <span v-if="showCopyNo">&nbsp;&nbsp;SQL&nbsp;&nbsp;<i @click="copy(allocateOrder.sql)" class="el-icon-document-copy"></i>
                </span>
              </label>
              </div>
            </div>
          </div>

          <!-- 调拨单明细 -->
          <div style="margin-top: 10px;">
            <el-divider content-position="left">调拨单明细</el-divider>

            <div style="margin-left: 40px; font-weight: 500; font-size: 14px;">
              <template>
                <el-table :data="saodList" border style="width: 90%" :row-style="{ height: 10+'px'}" :cell-style="{padding:0+'px'}"> <!-- height="250" -->
                  <el-table-column fixed label="序号" type="index" width="50"></el-table-column>
                  <el-table-column prop="goodsNo" label="商品编码"></el-table-column>
                  <el-table-column prop="goodsName" label="商品名称" max-width="180" :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="allocateQuantity" label="调拨数量"></el-table-column>
                  <el-table-column prop="outQuantity" label="已调出数量"></el-table-column>
                  <el-table-column prop="inQuantity" label="已调入数量"></el-table-column>
                  <el-table-column prop="createTimeStr" label="创建时间" width="200"></el-table-column>
                  <el-table-column prop="updateTimeStr" label="更新时间" width="200"></el-table-column>
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
  name: "AllocateOrder",
  data() {

    return {
      env: Config.env,
      host: Config.host,

      businessNo: '',
      allocateOrder: {},
      saodList: [],

      loading: false,
      showCopyNo: false,
      isTran: false,
      isShowQuery: true,


    }
  },

  created: function () {

    let allocateOrderNo = this.$route.query.allocateOrderNo;

    if (allocateOrderNo) {
      this.businessNo = allocateOrderNo
      this.onSubmit()
    }
  },
  methods: {
    // 查询
    onSubmit() {
      this.showCopyNo = false
      this.isTran = false

      if (!this.businessNo) {
        this.$message({
          message: '单号不能为空',
          type: 'warning'
        });
        return;
      }

      let success = this.businessNo.search(/^DB-\d{6}-\d{6}$/g)
      if (success !== 0) {
        this.$message({
          message: '单号格式不正确',
          type: 'warning'
        });
        return;
      }


      this.loading = true
      this.allocateOrder = {}
      this.saodList = []

      axios({
        url: this.host + '/toolkit/allocate/getAllocateOrder',
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
        if (response.data.allocateOrder) {
          this.allocateOrder = response.data.allocateOrder
          this.saodList = response.data.saodList
          this.loading = false

          this.showCopyNo = true

        } else {
          this.loading = false
          this.$message({
            message: '没有数据',
            type: 'warning'
          });
        }
      }, (error) => {
        console.log(error)
        this.$message({
          message: '查询失败',
          type: 'warning'
        });
        this.loading = false
      })

    },

    // 作废
    invalid() {
      this.$confirm('确定作废该调拨单?', '[ ' + this.allocateOrder.allocateOrderNo + ' ]', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
        showClose: false
      }).then(() => {
        axios({
          url: this.host + '/toolkit/allocate/invalid',
          method: 'GET',
          params: {
            businessNo: this.allocateOrder.allocateOrderNo
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
                  message: '作废成功',
                  type: 'success'
                });
                this.onSubmit()
              }
            }, (error) => {
              console.log(error)
              this.$message({
                message: '作废失败',
                type: 'warning'
              });
            })
      }).catch(() => {
      });

    },


    clearBusinessNo() {
      this.businessNo = ''
      this.allocateOrder = {}
      this.saodList = []
      this.showCopyNo = false
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