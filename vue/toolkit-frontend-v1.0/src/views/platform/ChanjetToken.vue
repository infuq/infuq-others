<template>
  <div>
    <section class="content clearfix" style="width: 97%;">
      <div class="el-backtop" style="right: 40px; top: 130px;">
        <el-link type="primary" :href="'/'" :underline="false" target="_blank"><i class="el-icon-s-home"></i></el-link>
      </div>
      <el-divider content-position="right">{{ env }}环境</el-divider>

      <div style="margin-top: 15px;">
        <!-- 获取畅捷通TOKEN -->
        <div style="margin-top: 10px;">
          <el-divider content-position="left">获取畅捷通TOKEN</el-divider>

          <el-form :inline="true" class="demo-form-inline">
            <el-input v-model="ent" placeholder="ENT码" clearable style="width: 400px;">
              <template slot="prepend">ENT码</template>
            </el-input>

            <div style="display: inline-block; margin-top: 3px; margin-bottom: 3px; margin-left: 5px;">
              <el-button type="primary" @click="onSubmit">查询</el-button>
            </div>

            <!-- 结果 -->
            <div style="margin-top: 15px;">

              <!-- 结果 -->
              <div style="margin-top: 10px;" v-loading="loading">
                <el-divider content-position="left">结果</el-divider>
                <div style="font-weight: 500; font-size: 14px;">
                  <div v-if="res_token != ''" style="margin-top: 20px;">
                    {{ res_token_short }} &nbsp;&nbsp;&nbsp;<i @click="copy()" class="el-icon-document-copy"></i>
                  </div>
                </div>
              </div>
            </div>
          </el-form>
        </div>
      </div>


    </section>
  </div>

</template>

<script>

import Config from '@/assets/js/route.js'
import axios from 'axios';

export default {
  name: "ChanjetToken",
  data() {

    return {
      env: Config.env,
      host: Config.host,

      ent: '',
      loading: false,
      res_token_short: '',
      res_token: '',


    }
  },

  created: function () {

  },
  methods: {
    // 提交
    onSubmit() {
      this.res_token = ''
      this.res_token_short = ''
      if (!this.ent) {
        this.$message({
          message: 'ENT码为空',
          type: 'warning'
        });
        return;
      }
      this.loading = true
      axios({
        url: this.host + '/toolkit/chanjet/ent',
        method: 'POST',
        data: {
          ent: this.ent
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
          this.res_token = response.data
          this.res_token_short = response.data.replaceAll(/(.{50}).*(.{50})/g, "$1......$2")
        } else {
          this.$message({
            message: '未查询到',
            type: 'warning'
          });
        }

        this.loading = false
      }, error => {
        console.log(error)
        this.loading = false
        this.$message({
          message: '查询失败',
          type: 'warning'
        });
      })

    },

    copy() {
      let url = this.res_token;
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