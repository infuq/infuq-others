<template>
  <div>
    <section class="content clearfix" style="width: 97%;">
      <div class="el-backtop" style="right: 40px; top: 130px;">
        <el-link type="primary" :href="'/'" :underline="false" target="_blank"><i class="el-icon-s-home"></i></el-link>
      </div>
      <el-divider content-position="right">{{ env }}环境</el-divider>

      <div style="margin-top: 15px;">

        <!-- 文件上传 -->
        <div style="margin-top: 10px;">
          <el-divider content-position="left">文件上传</el-divider>

          <el-upload
              class="upload-demo"
              drag
              action
              :http-request="uploadFile"
              :show-file-list="false">
            <i class="el-icon-upload"></i>
            <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
          </el-upload>

        </div>
      </div>


    </section>
  </div>

</template>

<script>

import Config from '@/assets/js/route.js'
import axios from 'axios';

export default {
  name: "FileUpload",
  data() {

    return {
      env: Config.env,
      host: Config.host,
    }
  },

  created: function () {

  },
  methods: {

    // https://blog.csdn.net/m0_52313178/article/details/124741663
    uploadFile(item) {
      let _FormData = new FormData()
      _FormData.append('file', item.file);
      axios({
        url: this.host + '/toolkit/file/upload',
        method: 'POST',
        headers: {
          "Content-Type": "multipart/form-data"
        },
        timeout: 30000,
        data: _FormData
      }).then(res => {
        console.log(res)
      })
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