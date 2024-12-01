<template>
  <div>
    <section class="content clearfix" style="width: 97%;">
      <div class="el-backtop" style="right: 40px; top: 130px;">
        <el-link type="primary" :href="'/'" :underline="false" target="_blank"><i class="el-icon-s-home"></i></el-link>
      </div>
      <el-divider content-position="right">{{ env }}环境</el-divider>


      <div style="margin-top: 25px;">

        <template>
          <el-table :data="storageInData" border style="width: 75%" :row-style="{ height: 10+'px'}"
                    :cell-style="{padding:0+'px'}">
            <el-table-column prop="desc" label="描述" width="180"></el-table-column>
            <el-table-column prop="value" label="数值" width="90"></el-table-column>
            <el-table-column prop="eV" label="枚举值"></el-table-column>
          </el-table>
        </template>
        <p style="margin-top: 5px;"></p>
        <template>
          <el-table :data="storageOutData" border style="width: 75%" :row-style="{ height: 10+'px'}"
                    :cell-style="{padding:0+'px'}">
            <el-table-column prop="desc" label="描述" width="180"></el-table-column>
            <el-table-column prop="value" label="数值" width="90"></el-table-column>
            <el-table-column prop="eV" label="枚举值"></el-table-column>
          </el-table>
        </template>


      </div>

    </section>
  </div>

</template>

<script>

import Config from '@/assets/js/route.js'
import axios from 'axios';

export default {
  name: "Enum",
  data() {

    return {
      env: Config.env,
      host: Config.host,


      storageInData: [{
        desc: '采购入库',
        value: '10',
        eV: 'IN_PURCHASE'
      }, {
        desc: '调拨入库',
        value: '11',
        eV: 'IN_ALLOCATION'
      }, {
        desc: '其他入库',
        value: '12',
        eV: 'IN_OTHER'
      }, {
        desc: '盘盈入库',
        value: '13',
        eV: 'IN_INVENTORY_PROFIT'
      }, {
        desc: '退货入库',
        value: '14',
        eV: 'IN_RETURN_GOODS'
      }, {
        desc: '报溢入库',
        value: '15',
        eV: 'IN_OVERFLOW'
      }, {
        desc: '兑换入库',
        value: '16',
        eV: 'IN_EXCHANGE'
      }, {
        desc: '补货入库',
        value: '17',
        eV: 'IN_REPLENISH'
      }, {
        desc: '移库入库',
        value: '18',
        eV: 'IN_TRANSFER'
      }, {
        desc: '其他采购入库',
        value: '19',
        eV: 'OTHER_IN_PURCHASE'
      }, {
        desc: '其他调拨入库',
        value: '31',
        eV: 'OTHER_IN_ALLOCATION'
      }],


      storageOutData: [{
        desc: '销售出库',
        value: '20',
        eV: 'OUT_SELL'
      }, {
        desc: '调拨出库',
        value: '21',
        eV: 'OUT_ALLOCATION'
      }, {
        desc: '其他出库',
        value: '22',
        eV: 'OUT_OTHER'
      }, {
        desc: '盘亏出库',
        value: '23',
        eV: 'OUT_INVENTORY_LOSS'
      }, {
        desc: '报损出库',
        value: '24',
        eV: 'OUT_DAMAGED'
      }, {
        desc: '兑换出库',
        value: '25',
        eV: 'OUT_EXCHANGE'
      }, {
        desc: '补货出库',
        value: '26',
        eV: 'OUT_REPLENISH'
      }, {
        desc: '移库出库',
        value: '27',
        eV: 'OUT_TRANSFER'
      }, {
        desc: '其他销售出库',
        value: '28',
        eV: 'OTHER_OUT_SELL'
      }, {
        desc: '其他调拨出库',
        value: '29',
        eV: 'OTHER_OUT_ALLOCATION'
      }, {
        desc: '采退出库',
        value: '30',
        eV: 'OUT_PURCHASE'
      }],


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