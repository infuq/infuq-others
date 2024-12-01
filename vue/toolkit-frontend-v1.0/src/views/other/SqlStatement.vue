<template>
  <div>
    <section class="content clearfix" style="width: 55%;">
      <div class="el-backtop" style="right: 40px; top: 130px;">
        <el-link type="primary" :href="'/'" :underline="false" target="_blank"><i class="el-icon-s-home"></i></el-link>
      </div>
      <el-divider content-position="right">{{ env }}环境</el-divider>

      <div style="margin-top: 25px;">

        <el-collapse v-model="activeNames" @change="handleChange">
          <el-collapse-item title="将已完成的盘点单,但是依然锁定库存的异常数据解锁" name="1">
            <div>
              -- 查询哪些批次还处于锁定状态<br>
              SELECT<br>
              &nbsp;&nbsp;&nbsp;sbd.*<br>
              FROM<br>
              &nbsp;&nbsp;&nbsp;store_storage_check ssc<br>
              &nbsp;&nbsp;&nbsp;INNER JOIN store_storage_check_details sscd ON sscd.storage_check_id =
              ssc.storage_check_id<br>
              &nbsp;&nbsp;&nbsp;INNER JOIN store_batch_details sbd ON sbd.batch_details_id = sscd.batch_details_id<br>
              WHERE<br>
              &nbsp;&nbsp;&nbsp;ssc.storage_check_status = 100<br>
              &nbsp;&nbsp;&nbsp;AND sbd.locked = 1<br>
              GROUP BY sbd.batch_details_id ;<br>
              <br>
              <br>
              -- 解锁<br>
              UPDATE store_batch_details<br>
              &nbsp;&nbsp;&nbsp;&nbsp;SET locked = 0<br>
              WHERE<br>
              &nbsp;&nbsp;&nbsp;&nbsp;batch_details_id IN ( SELECT sscd.batch_details_id FROM store_storage_check ssc
              INNER JOIN store_storage_check_details sscd ON sscd.storage_check_id = ssc.storage_check_id WHERE
              ssc.storage_check_status = 100 ) ;

            </div>

            <div style="margin-top: 15px;">
              <el-button type="primary" size="medium" @click="unLock">解锁</el-button>
            </div>
          </el-collapse-item>

          <el-collapse-item title="伟添订货单明细和退货单明细" name="2">
            <div>
              -- 订货明细 (包括退货信息)<br>
              SELECT<br>
              &nbsp;&nbsp;&nbsp;atpr.third_business_no as '伟添单号',<br>
              &nbsp;&nbsp;&nbsp;sco.store_order_code as 'DC单号',<br>
              &nbsp;&nbsp;&nbsp;sco.customer_order_code as 'DW单号',<br>
              &nbsp;&nbsp;&nbsp;w.warehouse_name as '仓库',<br>
              &nbsp;&nbsp;&nbsp;sc.customer_name as '货主',<br>
              &nbsp;&nbsp;&nbsp;sc2.customer_name as '门店',<br>
              &nbsp;&nbsp;&nbsp;scod.goods_name as '商品名称',<br>
              &nbsp;&nbsp;&nbsp;scod.order_quantity as '数量',<br>
              &nbsp;&nbsp;&nbsp;scod.goods_unit_price as '单价',<br>
              &nbsp;&nbsp;&nbsp;sco.pay_time as '支付时间',<br>
              &nbsp;&nbsp;&nbsp;DATE_FORMAT(atpr.create_time, '%Y-%m-%d %H:%i:%s') as '推送时间',<br>
              &nbsp;&nbsp;&nbsp;sro.return_order_no as '退货单号',<br>
              &nbsp;&nbsp;&nbsp;srod.return_quantity as '退货数量',<br>
              &nbsp;&nbsp;&nbsp;srod.already_return_quantity as '已退数量'<br>

              FROM<br>
              &nbsp;&nbsp;&nbsp;api_third_platform_record atpr<br>
              &nbsp;&nbsp;&nbsp;INNER JOIN store_customer_order sco on atpr.source_order_no = sco.customer_order_no<br>
              &nbsp;&nbsp;&nbsp;INNER JOIN store_customer_order_details scod on sco.customer_order_id =
              scod.customer_order_id<br>
              &nbsp;&nbsp;&nbsp;INNER JOIN store_customer sc on sco.goods_owner_id = sc.customer_id<br>
              &nbsp;&nbsp;&nbsp;INNER JOIN store_customer sc2 on sco.customer_id = sc2.customer_id<br>
              &nbsp;&nbsp;&nbsp;INNER JOIN warehouse w on sco.warehouse_id = w.warehouse_id<br>
              &nbsp;&nbsp;&nbsp;LEFT JOIN store_return_order_details srod on scod.customer_order_details_id =
              srod.customer_order_details_id<br>
              &nbsp;&nbsp;&nbsp;LEFT JOIN store_return_order sro on srod.return_order_id = sro.return_order_id<br>
              WHERE<br>
              &nbsp;&nbsp;&nbsp;atpr.app_no = 'APP-00005'<br>
              &nbsp;&nbsp;&nbsp;and atpr.api_call_type = 1<br>
              &nbsp;&nbsp;&nbsp;and w.warehouse_id=354267059846443008<br>
              &nbsp;&nbsp;&nbsp;and atpr.create_time >= '2023-10-01 00:00:00'<br>
              &nbsp;&nbsp;&nbsp;and atpr.create_time < '2023-12-01 00:00:00' ;<br>
              <br>
              <br>

              -- 退货明细<br>
              SELECT<br>
              &nbsp;&nbsp;&nbsp;atpr.third_business_no as '伟添单号',<br>
              &nbsp;&nbsp;&nbsp;sco.store_order_code as 'DC单号',<br>
              &nbsp;&nbsp;&nbsp;sco.customer_order_code as 'DW单号',<br>
              &nbsp;&nbsp;&nbsp;sro.return_order_no as '退货单号',<br>
              &nbsp;&nbsp;&nbsp;w.warehouse_name as '仓库',<br>
              &nbsp;&nbsp;&nbsp;sc.customer_name as '货主',<br>
              &nbsp;&nbsp;&nbsp;sc2.customer_name as '门店',<br>
              &nbsp;&nbsp;&nbsp;srod.goods_name as '商品名称',<br>
              &nbsp;&nbsp;&nbsp;srod.return_quantity as '退货数量',<br>
              &nbsp;&nbsp;&nbsp;srod.already_return_quantity as '已退数量',<br>
              &nbsp;&nbsp;&nbsp;srod.goods_unit_price as '单价'<br>

              FROM<br>
              &nbsp;&nbsp;&nbsp;api_third_platform_record atpr<br>
              &nbsp;&nbsp;&nbsp;INNER JOIN store_customer_order sco on atpr.source_order_no = sco.customer_order_no<br>
              &nbsp;&nbsp;&nbsp;INNER JOIN store_customer_order_details scod on sco.customer_order_id =
              scod.customer_order_id<br>
              &nbsp;&nbsp;&nbsp;INNER JOIN store_customer sc on sco.goods_owner_id = sc.customer_id<br>
              &nbsp;&nbsp;&nbsp;INNER JOIN store_customer sc2 on sco.customer_id = sc2.customer_id<br>
              &nbsp;&nbsp;&nbsp;INNER JOIN warehouse w on sco.warehouse_id = w.warehouse_id<br>
              &nbsp;&nbsp;&nbsp;INNER JOIN store_return_order sro on sco.customer_order_id = sro.customer_order_id<br>
              &nbsp;&nbsp;&nbsp;INNER JOIN store_return_order_details srod on srod.return_order_id = sro.return_order_id
              and scod.customer_order_details_id = srod.customer_order_details_id<br>
              WHERE<br>
              &nbsp;&nbsp;&nbsp;atpr.app_no = 'APP-00005'<br>
              &nbsp;&nbsp;&nbsp;and w.warehouse_id=354267059846443008<br>
              &nbsp;&nbsp;&nbsp;and atpr.create_time >= '2023-10-01 00:00:00'<br>
              &nbsp;&nbsp;&nbsp;and atpr.create_time &lt; '2023-12-01 00:00:00' ;<br>

            </div>
          </el-collapse-item>

          <el-collapse-item title="填充订单明细缺失的自定义编码" name="3">
            <div>
              UPDATE store_customer_order_details scod,<br>
              &nbsp;&nbsp;&nbsp;store_warehouse_owner_goods swog<br>
              SET<br>
              &nbsp;&nbsp;&nbsp;scod.warehouse_owner_goods_code = swog.warehouse_owner_goods_code<br>
              WHERE<br>
              &nbsp;&nbsp;&nbsp;scod.warehouse_owner_goods_no = swog.warehouse_owner_goods_no<br>
              &nbsp;&nbsp;&nbsp;AND scod.warehouse_owner_goods_code IS NULL<br>
              &nbsp;&nbsp;&nbsp;AND scod.enterprise_id = 425339972154118144;<br>
            </div>
          </el-collapse-item>

          <el-collapse-item title="订单明细中包含其他货主的商品" name="4">
            <div>
              SELECT
              sco.customer_order_no,sco.customer_order_code,sco.store_order_code,swog.warehouse_owner_goods_no,aar.business_no,aar.third_no<br>
              FROM<br>
              &nbsp;&nbsp;&nbsp;store_customer_order sco<br>
              &nbsp;&nbsp;&nbsp;INNER JOIN store_customer_order_details scod ON sco.customer_order_id =
              scod.customer_order_id<br>
              &nbsp;&nbsp;&nbsp;INNER JOIN store_warehouse_owner_goods swog ON scod.warehouse_owner_goods_id =
              swog.warehouse_owner_goods_id<br>
              WHERE swog.goods_owner_id != sco.goods_owner_id AND sco.create_time >= '2024-3-17 00:00:00' ;<br>
            </div>
          </el-collapse-item>

        </el-collapse>
      </div>


    </section>
  </div>

</template>

<script>

import Config from '@/assets/js/route.js'
import axios from 'axios';

export default {
  name: "SqlStatement",
  data() {

    return {
      env: Config.env,
      host: Config.host,

      activeNames: ['0'],

    }
  },

  created: function () {

  },
  methods: {

    handleChange(val) {

    },

    unLock() {
      axios({
        url: this.host + '/toolkit/tools/unLock',
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

        this.$message({
          message: '解锁完成',
          type: 'success'
        });
      }, error => {
        console.log(error)
        this.$message({
          message: '请求失败',
          type: 'warning'
        });
      })

    },

    copy(data) {

      if (data.includes(':')) {
        try {
          data = this.t(data)
          const obj = JSON.parse(data)
          if (obj.hasOwnProperty('body')) {
            obj.body = this.t(obj.body)
            const _obj = JSON.parse(obj.body)
            obj.body = _obj
          }
          if (obj.hasOwnProperty('requestBody')) {
            try {
              obj.requestBody = this.t(obj.requestBody)
              const _obj = JSON.parse(obj.requestBody)
              obj.requestBody = _obj
              if (obj.requestBody.hasOwnProperty('requestBody')) {
                obj.requestBody.requestBody = this.t(obj.requestBody.requestBody)
                const _obj = JSON.parse(obj.requestBody.requestBody)
                obj.requestBody.requestBody = _obj
              }
            } catch (err) {
              console.log(err)
            }
          }

          data = JSON.stringify(obj)
        } catch (err) {
          console.log(err)
        }
      }


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

    t(data) {
      // 长整数转成字符串类型, 防止精度丢失
      data = data.replace(/((\W*)s*):s*([0-9]{15,})s*(,?)/g, '$1: $2$3$2 $4')
      return data;
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