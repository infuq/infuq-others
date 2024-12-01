<template>
  <div>
    <section class="content clearfix" style="width: 60%;">
      <div class="el-backtop" style="right: 40px; top: 130px;">
        <el-link type="primary" :href="'/'" :underline="false" target="_blank"><i class="el-icon-s-home"></i></el-link>
      </div>
      <el-divider content-position="right">{{ env }}环境</el-divider>

      <section class="content clearfix" style="width: 30%;">
        <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm" style="margin-left: -15%;">
          <el-form-item label="账 号" prop="name">
            <el-input v-model="ruleForm.name"></el-input>
          </el-form-item>
          <el-form-item label="密 码" prop="pass">
            <el-input type="password" v-model="ruleForm.pass" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="submitForm()">提交</el-button>
            <el-button @click="resetForm('ruleForm')">重置</el-button>
          </el-form-item>
        </el-form>
      </section>
    </section>
  </div>
</template>

<script>
import Config from '@/assets/js/route.js'
import axios from 'axios';

export default {
  name: "Login",
  data() {

    let validateName = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入账号'));
      }
    };
    let validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'));
      }
    };
    return {
      env: Config.env,
      host: Config.host,

      ruleForm: {
        name: '',
        pass: ''
      },
      rules: {
        name: [
          {validator: validateName, trigger: 'blur'}
        ],
        pass: [
          {validator: validatePass, trigger: 'blur'}
        ]
      }
    }
  },

  created: function () {
  },
  methods: {
    submitForm() {

      let password = this.ruleForm.pass
      let userName = this.ruleForm.name

      if (userName === "" || password === "") {
        this.$message({
          message: '账号和密码不能为空',
          type: 'warning'
        });
        return;
      }

      axios({
        url: this.host + '/toolkit/auth/login',
        method: 'POST',
        data: {
          userName: this.ruleForm.name,
          password: this.ruleForm.pass
        },
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        }
      })
      .then(response => {
        if (response.data === "success") {
          this.$message({
            message: '登录成功',
            type: 'success'
          });
          this.$router.push("/")
        } else {
          this.$message({
            message: '账号或密码错误',
            type: 'warning'
          });
        }
      }, (error) => {
        console.log(error)
        this.$message({
          message: '登录异常',
          type: 'warning'
        });
      })
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
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