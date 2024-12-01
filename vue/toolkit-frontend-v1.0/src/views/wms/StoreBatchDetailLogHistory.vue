<template>
  <div>
    <section class="content clearfix" style="width: 97%;">
      <div class="el-backtop" style="right: 40px; top: 130px;">
        <el-link type="primary" :href="'/'" :underline="false" target="_blank"><i class="el-icon-s-home"></i></el-link>
      </div>
      <el-divider content-position="right">{{ env }}环境</el-divider>

      <el-form :inline="true" class="demo-form-inline">

        <div>
          <el-input v-model="batchDetailId" placeholder="115095686080991232" clearable @clear="clearBatchDetailId"
                    style="width: 400px;">
            <template slot="prepend">批次明细ID</template>
          </el-input>

          <el-form-item>
            <el-button type="primary" @click="onSubmit" style="margin-left: 5px;">查询</el-button>
          </el-form-item>
        </div>


        <!-- 结果 -->
        <div style="margin-top: 15px;">

          <!-- 批次日志记录 -->
          <div style="margin-top: 10px;">
            <el-divider content-position="left">批次日志记录结果</el-divider>

            <div style="margin-left: 40px; font-weight: 500; font-size: 14px;">
              <template>
                <el-table :data="GoodsBatchDetailHistoryList" border style="width: 100%" :row-style="{ height: 10+'px'}"
                          :cell-style="{padding:0+'px'}"> <!-- height="250" -->


                  <el-table-column fixed label="序号" type="index" width="50">
                    <template slot-scope="scope">
                                          <span v-if="scope.row.hasError == 1">
                                              <span style="color: red;">{{ scope.$index + 1 }}</span>
                                          </span>
                      <span v-else>
                                              {{ scope.$index + 1 }}
                                          </span>
                    </template>
                  </el-table-column>

                  <el-table-column align="center" prop="beforeQuantity" label="期初库存" width="80"></el-table-column>
                  <el-table-column align="left" label="操作数量" width="100">
                    <template slot-scope="scope">
                                          <span v-if="scope.row.storageCategory == 0">
                                              <span>加{{ scope.row.quantity }}</span>
                                          </span>
                      <span v-else>
                                              <span>减{{ scope.row.quantity }}</span>
                                          </span>
                    </template>
                  </el-table-column>
                  <el-table-column align="center" prop="afterQuantity" label="期末库存"></el-table-column>
                  <el-table-column align="center" prop="batchDetailsLogDesc" label="操作类型"></el-table-column>
                  <el-table-column align="center" prop="storageNo" label="出入库单号" width="180"></el-table-column>
                  <el-table-column align="center" prop="sourceOrderNo" label="源单号" width="180"></el-table-column>
                  <el-table-column align="center" prop="createTime" label="创建时间" width="200"></el-table-column>
                  <el-table-column align="center" label="说明">
                    <template slot-scope="scope">
                                              <span v-if="scope.row.hasError == 1">
                                                  <span style="color: red;">有问题</span>
                                              </span>
                      <span v-if="scope.row.hasError == 0 && scope.row.hasNegative == 1">
                                                  <span style="color: orange;">有负数</span>
                                              </span>
                    </template>
                  </el-table-column>
                  <!--
                  <el-table-column align="center" label="操作">
                      <template slot-scope="scope">
                          <span v-if="scope.row.hasError == 1 || (scope.row.hasError == 0 && scope.row.hasNegative == 1)">
                              <el-link type="primary" :underline="false" @click="handleFixStockRowClick(select_batch_detail, scope.row.batchDetailsLogId, scope.row.login)">修复该行及以上数据</el-link>
                          </span>
                      </template>
                  </el-table-column> -->
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
  name: "StoreBatchDetailLogHistory",
  data() {

    return {
      env: Config.env,
      host: Config.host,

      batchDetailId: '',
      GoodsBatchDetailHistoryList: [],
      loading: false,

    }
  },

  created: function () {

  },
  methods: {
    // 查询
    onSubmit() {

      if (!this.batchDetailId) {
        this.$message({
          message: '批次明细ID不能为空',
          type: 'warning'
        });
        return;
      }

      this.loading = true
      this.GoodsBatchDetailHistoryList = []

      axios({
        url: this.host + '/toolkit/tools/getBatchDetailHistory',
        method: 'GET',
        params: {
          batchDetailId: this.batchDetailId
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

        this.GoodsBatchDetailHistoryList = response.data.historyList
      }, error => {
        console.log(error)
        this.$message({
          message: '查询失败',
          type: 'warning'
        });
        this.loading = false
      })

    },


    clearBatchDetailId() {
      this.batchDetailId = ''
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