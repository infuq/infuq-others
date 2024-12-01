<template>
  <div>
    <section class="content clearfix" style="width: 97%;">
      <div class="el-backtop" style="right: 40px; top: 130px;">
        <el-link type="primary" :href="'/'" :underline="false" target="_blank"><i class="el-icon-s-home"></i></el-link>
      </div>
      <el-divider content-position="right">{{ env }}环境</el-divider>

      <el-form :inline="true" class="demo-form-inline">

        <!-- 结果 -->
        <div style="margin-top: 15px;">

          <!-- 应用 -->
          <div style="margin-top: 10px;">
            <el-divider content-position="left">平台应用</el-divider>

            <div style="margin-left: 40px; font-weight: 500; font-size: 14px;">
              <template>
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
                    平台
                  </div>

                  <el-select v-model="selectPlatformCode" placeholder="请选择平台"
                             @change="selectPlatform(selectPlatformCode)" filterable>
                    <el-option v-for="item in PlatformOptions" :key="item.value" :label="item.label"
                               :value="item.value"></el-option>
                  </el-select>
                </div>


                <div style="margin-top: 10px;">
                  <el-table :data="AppList" border style="width: 100%" :row-style="{ height: 10+'px'}"
                            :cell-style="{padding:0+'px'}"> <!-- height="250" -->
                    <el-table-column prop="platformName" label="平台名称" width="180"></el-table-column>
                    <el-table-column label="应用名称" width="180">
                      <template slot-scope="scope">
                        <el-button @click="handleAppNameClick(scope.row)" type="text">{{ scope.row.appName }}
                        </el-button> <!-- size="small" -->
                      </template>
                    </el-table-column>
                    <el-table-column sortable prop="appCode" label="应用编码" width="120"></el-table-column>
                    <el-table-column prop="enterpriseName" label="企业名称" width="250"></el-table-column>
                    <el-table-column sortable :sort-method="sortStatus" align="center" label="状态" width="80">
                      <template slot-scope="scope">
                        <span v-if="scope.row.appStatus === 1">启用</span>
                        <span v-else>
                          <span style="color: red;">禁用</span>
                        </span>
                      </template>
                    </el-table-column>
                    <el-table-column align="center" prop="createTime" label="创建时间" width="200"></el-table-column>
                    <el-table-column sortable :sort-method="sortDeleteStatus" align="center" label="已删除" width="100">
                      <template slot-scope="scope">
                        <span v-if="scope.row.isDelete === 1">
                          <span style="color: red;">是</span>
                        </span>
                        <span v-else>否</span>
                      </template>
                    </el-table-column>
                    <el-table-column prop="extension" label="扩展信息" :show-overflow-tooltip="true"></el-table-column>
                  </el-table>
                </div>
              </template>

              <div class="third_link">
                <el-dialog :title="'[ ' + appName + ' ]'" :visible.sync="App_dialogVisible" :show-close="false" width="30%">
                  <template>

                  </template>
                </el-dialog>
              </div>


            </div>
          </div>

          <!-- 平台业务 -->
          <div style="margin-top: 10px;">
            <el-divider content-position="left">应用业务</el-divider>

            <div style="margin-left: 40px; font-weight: 500; font-size: 14px;">
              <template>
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
                    应用
                  </div>

                  <el-select v-model="selectAppCode" placeholder="请选择应用" @change="selectApp(selectAppCode)" filterable>
                    <el-option v-for="item in AppOptions" :key="item.value" :label="item.label" :value="item.value"></el-option>
                  </el-select>
                </div>


                <span style="display: inline; margin-left: 15px;" v-if="total_app_business > 0">
                          <el-tag size="small">{{ total_app_business }}</el-tag>
                      </span>

              </template>

              <div style="margin-top: 10px;" v-loading="loading">
                <template>
                  <el-table :data="appBusinessList" border style="width: 100%" :row-style="appBusinessRowStyle"
                            :cell-style="{padding:0+'px'}"> <!-- height="250" -->
                    <el-table-column fixed prop="businessName" label="业务名称" min-width="120"
                                     :show-overflow-tooltip="true"></el-table-column>
                    <el-table-column prop="platformBusinessCode" label="平台业务编码" width="140"></el-table-column>
                    <el-table-column prop="businessType" label="程序员编码(旧)" width="130"></el-table-column>
                    <el-table-column prop="businessOperationType" label="程序员编码(新)" width="130"></el-table-column>
                    <el-table-column prop="appCode" label="应用编码" width="100"></el-table-column>
                    <el-table-column prop="appName" label="应用名称" min-width="120"
                                     :show-overflow-tooltip="true"></el-table-column>
                    <el-table-column prop="platformCode" label="平台编码" width="100"></el-table-column>
                    <el-table-column prop="platformName" label="平台名称" min-width="120"
                                     :show-overflow-tooltip="true"></el-table-column>
                    <el-table-column prop="enterpriseCode" label="企业编码" min-width="120"
                                     :show-overflow-tooltip="true"></el-table-column>
                    <el-table-column prop="enterpriseName" label="企业名称" min-width="120"
                                     :show-overflow-tooltip="true"></el-table-column>

                    <el-table-column sortable :sort-method="sortBusinessStatus" align="center" label="状态" width="120">
                      <template slot-scope="scope">
                                      <span v-if="scope.row.status == 0">
                                          <span style="color: red;">禁用</span>
                                      </span>
                        <span v-else>
                                          启用
                                      </span>
                      </template>

                    </el-table-column>
                    <el-table-column sortable :sort-method="sortDeleteStatus" align="center" label="已删除" width="100">
                      <template slot-scope="scope">
                                      <span v-if="scope.row.del == 1">
                                          <span style="color: red;">是</span>
                                      </span>
                        <span v-else>
                                          否
                                      </span>
                      </template>
                    </el-table-column>

                    <el-table-column fixed="right" label="操作">
                      <template slot-scope="scope">
                                      <span v-if="scope.row.status == 0">
                                          <el-button @click="enableAppBusiness(scope.row)" type="text">启用</el-button>
                                      </span>
                        <span v-else>
                                          <el-button @click="disableAppBusiness(scope.row)" type="text">禁用</el-button>
                                      </span>
                      </template>
                    </el-table-column>

                  </el-table>
                </template>
              </div>
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
  name: "AppBusiness",
  data() {

    return {
      env: Config.env,
      host: Config.host,

      selectPlatformCode: '',
      selectAppCode: '',
      PlatformOptions: [],
      AppOptions: [],

      App_dialogVisible: false,
      appName: '',

      AppList: [],

      appBusinessList: [],
      total_app_business: 0,


      UsePlatformBusiness_dialogVisible: false,
      UsePlatformBusinessList: [],

      PlatformName_dialogVisible: false,


      loading: false,

    }
  },
  created: function () {
    // 查询所有平台
    axios({
      url: this.host + '/toolkit/ab/getAllPlatform',
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

      let PlatformList = response.data
      if (PlatformList) {
        for (let i = 0; i < PlatformList.length; i++) {
          let label = PlatformList[i]['platformName']
          let value = PlatformList[i]['platformCode']
          this.PlatformOptions.push({'label': label, 'value': value})
        }
        // 默认选择第一个平台
        this.selectPlatformCode = PlatformList[0]['platformCode']
        this.getAppByPlatformCode()
      }
    }, error => {
      console.log(error)
      this.$message({
        message: '查询平台失败',
        type: 'warning'
      });
    })


    // 查询所有应用
    axios({
      url: this.host + '/toolkit/ab/getAllApp',
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

      let AppList = response.data
      if (AppList) {
        for (let i = 0; i < AppList.length; i++) {
          let label = AppList[i]['appName']
          let value = AppList[i]['appCode']
          this.AppOptions.push({'label': label, 'value': value})
        }
      }
    }, error => {
      console.log(error)
      this.$message({
        message: '查询应用失败',
        type: 'warning'
      });
    })

  },
  methods: {

    getAppByPlatformCode() {
      this.AppList = []
      axios({
        url: this.host + '/toolkit/ab/getAppByPlatformCode',
        method: 'GET',
        params: {
          platformCode: this.selectPlatformCode
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

        this.AppList = response.data
      }, error => {
        console.log(error)
        this.$message({
          message: '查询应用失败',
          type: 'warning'
        });
      })
    },


    // 选择平台
    selectPlatform(platformCode) {
      this.selectPlatformCode = platformCode
      this.getAppByPlatformCode()
    },
    handleAppNameClick(row) {
      this.appName = row.appName
      this.App_dialogVisible = true
    },


    // 选择应用
    selectApp(appCode) {
      this.appBusinessList = []
      this.total_app_business = 0
      this.selectAppCode = appCode

      this.loading = true

      axios({
        url: this.host + '/toolkit/ab/getAllAppBusiness',
        method: 'GET',
        params: {
          appCode: this.selectAppCode,
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
        if (response.data && response.data.length > 0) {
          this.appBusinessList = response.data
          this.total_app_business = response.data.length
        }
        this.loading = false
      }, error => {
        console.log(error)
        this.$message({
          message: '查询应用业务失败',
          type: 'warning'
        });
        this.loading = false
      })
    },

    appBusinessRowStyle({row, column, rowIndex, columnIndex}) {
      if (row.isCallback === 1) {
        return {
          background: 'rgb(225 222 235)',
          height: 10 + 'px'
        }
      }

      return {height: 10 + 'px'}
    },


    handlePlatformBusinessClick(row) {

    },

    sortStatus(a, b) {
      if (a.appStatus > b.appStatus) {
        return -1
      }
    },
    sortBusinessStatus(a, b) {
      if (a.status > b.status) {
        return -1
      }
    },
    sortDeleteStatus(a, b) {
      if (a.isDelete > b.isDelete) {
        return -1
      }
    },
    // 启用应用业务
    enableAppBusiness(row) {

      this.$confirm('确定启用?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
        showClose: false
      }).then(() => {

        axios({
          url: this.host + '/toolkit/ab/enableAppBusiness',
          method: 'GET',
          params: {
            appBusinessId: row.appBusinessId
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

          this.selectApp(this.selectAppCode);
          this.$message({
            message: '启用成功',
            type: 'success'
          });
        }, error => {
          console.log(error)
          this.$message({
            message: '启用失败',
            type: 'warning'
          });
        })
      }).catch(() => {
        /*
        this.$message({
            type: 'info',
            message: '已取消删除'
        });
        */
      });


    },
    // 禁用应用业务
    disableAppBusiness(row) {
      this.$confirm('确定禁用?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
        showClose: false
      }).then(() => {

        axios({
          url: this.host + '/toolkit/ab/disableAppBusiness',
          method: 'GET',
          params: {
            appBusinessId: row.appBusinessId,
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

          this.selectApp(this.selectAppCode);
          this.$message({
            message: '禁用成功',
            type: 'success'
          });
        }, error => {
          console.log(error)
          this.$message({
            message: '禁用失败',
            type: 'warning'
          });
        })
      }).catch(() => {
        /*
        this.$message({
            type: 'info',
            message: '已取消删除'
        });
        */
      });

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