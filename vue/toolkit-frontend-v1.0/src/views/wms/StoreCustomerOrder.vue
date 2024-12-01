<template>
  <div>
    <section class="content clearfix" style="width: 97%;">
      <div class="el-backtop" style="right: 40px; top: 130px;">
        <el-link type="primary" :href="'/'" :underline="false" target="_blank"><i class="el-icon-s-home"></i></el-link>
      </div>

      <el-divider content-position="right">{{ env }}环境</el-divider>

      <el-form :inline="true" :model="condition" class="demo-form-inline">

        <div style="height: 50px;">
          <el-form-item label="">
            <el-input v-model="condition.storeOrderCode" placeholder="DC20230702195052771996434" clearable
                      @clear="clearStoreOrderCode" style="width: 300px;"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="onSubmit(2)">查询</el-button>
          </el-form-item>
          <span style="display: inline-block; padding-top: 10px;"
                v-if="sizeOfStoreOrderCode > 0">{{ sizeOfCustomerOrderCode2 }}个DW单&nbsp;&nbsp;{{
              sizeOfStoreOrderCode
            }}个DH单</span>
        </div>
        <div style="height: 50px;">
          <el-form-item label="">
            <el-input v-model="condition.customerOrderCode" placeholder="DWL1UEX620230702195052783" clearable
                      @clear="clearCustomerOrderCode" style="width: 300px;"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="onSubmit(3)">查询</el-button>
          </el-form-item>
          <span style="display: inline-block; padding-top: 10px;"
                v-if="sizeOfCustomerOrderCode > 0">{{ sizeOfCustomerOrderCode }}个DH单</span>
        </div>

        <div style="height: 50px;">
          <el-form-item label="">
            <el-input v-model="condition.customerOrderNo" placeholder="DH-230703-000004" clearable
                      @clear="clearCustomerOrderNo" style="width: 300px;"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="onSubmit(4)">查询</el-button>
          </el-form-item>
        </div>

        <div>
          <template>
            <el-tabs v-model="activeName" type="card" @tab-click="handleTabClick">
              <el-tab-pane v-for="(item,index) in this.tabsData" :key="index" :label="item.labelName"
                           :name="item.tabName">

              </el-tab-pane>
            </el-tabs>
          </template>
        </div>

        <!-- 结果 -->
        <div style="margin-top: 15px;" v-loading="loading">

          <el-steps :active="active_0" finish-status="success" simple style="margin-top: 20px">
            <el-step title="待出库"></el-step>
            <el-step title="出库中"></el-step>
            <el-step title="部分出库"></el-step>
            <el-step title="已出库"></el-step>
          </el-steps>

          <el-steps :active="active_1" finish-status="success" simple style="margin-top: 20px">
            <el-step title="待发货"></el-step>
            <el-step title="发货中"></el-step>
            <el-step title="部分发货"></el-step>
            <el-step title="已发货"></el-step>
          </el-steps>


          <!-- 订货单 -->
          <div style="margin-top: 10px;">
            <el-divider content-position="left">订货单</el-divider>

            <div style="margin-left: 40px; font-weight: 500; font-size: 14px;">

              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">单号:</label><label>&nbsp;&nbsp;&nbsp;{{ storeCustomerOrder.customerOrderNo }}
                <span v-if="showCopyCustomerOrderNo">
                                &nbsp;&nbsp;<i @click="copy(storeCustomerOrder.customerOrderNo)"
                                               class="el-icon-document-copy"></i>
                            </span>

              </label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">企业:</label><label>&nbsp;&nbsp;&nbsp;{{ storeCustomerOrder.enterpriseName }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">仓库:</label><label>&nbsp;&nbsp;&nbsp;{{ storeCustomerOrder.warehouseName }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">货主:</label><label>&nbsp;&nbsp;&nbsp;{{ storeCustomerOrder.goodsOwner }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">收货人:</label><label>&nbsp;&nbsp;&nbsp;{{ storeCustomerOrder.customer }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">联系人:</label><label>&nbsp;&nbsp;&nbsp;{{ storeCustomerOrder.linkman }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">配送方式:</label><label>&nbsp;&nbsp;&nbsp;{{ storeCustomerOrder.deliveryMethod }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">运费:</label><label>&nbsp;&nbsp;&nbsp;{{ storeCustomerOrder.freightFee }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">重量:</label><label>&nbsp;&nbsp;&nbsp;{{ storeCustomerOrder.sumTotalGrossWeight }}
                <span v-if="storeCustomerOrder.sumTotalGrossWeight > 0">KG</span></label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">来源:</label><label>&nbsp;&nbsp;&nbsp;{{ storeCustomerOrder.customerOrderSource }}</label>
              </div>
              <!--
              <div style="width: 400px; display: block; margin: 5px 0;">
                  <label style="display: inline-block; width: 110px; text-align: right;">来源:</label>
                  <span v-if="storeCustomerOrder.customerOrderSource == 'OMS3.0'">
                      <label @click="handleOMSOrigDataClick()" style="color: #409EFF; cursor: pointer;">&nbsp;&nbsp;{{storeCustomerOrder.customerOrderSource}}</label>
                  </span>
                  <span v-else>
                      <label>&nbsp;&nbsp;{{storeCustomerOrder.customerOrderSource}}</label>
                  </span>
              </div>-->
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">订货配送方式:</label><label>&nbsp;&nbsp;&nbsp;{{ storeCustomerOrder.transportType }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">完结类型:</label><label>&nbsp;&nbsp;&nbsp;{{ storeCustomerOrder.customerOrderFinishType }}</label>
              </div>
              <div style="width: 500px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">自定义单号:</label><label>&nbsp;&nbsp;&nbsp;{{ storeCustomerOrder.customerOrderCode }}
                <span v-if="showCopyCustomerOrderCode">&nbsp;&nbsp;<i @click="copy(storeCustomerOrder.customerOrderCode)" class="el-icon-document-copy"></i>
                  <router-link :to="{path: '/receive_record', query:{customerOrderCode: storeCustomerOrder.customerOrderCode, time: storeCustomerOrder.createTime}}" target="_blank" style="margin-left: 5px;">
                    <span class="icon-link" style="position: static;">查看接收记录</span>
                  </router-link>
                </span>
              </label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">OMS门店订单号:</label><label>&nbsp;&nbsp;&nbsp;{{ storeCustomerOrder.storeOrderCode }}
                <span v-if="showCopyStoreOrderCode">
                                &nbsp;&nbsp;<i @click="copy(storeCustomerOrder.storeOrderCode)"
                                               class="el-icon-document-copy"></i>
                            </span>
              </label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">创建时间:</label><label>&nbsp;&nbsp;&nbsp;{{ storeCustomerOrder.createTime }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">更新时间:</label><label>&nbsp;&nbsp;&nbsp;{{ storeCustomerOrder.updateTime }}</label>
              </div>
              <div style="width: 400px; display: block; margin: 5px 0;">
                <label style="display: inline-block; width: 110px; text-align: right;">SQL:</label><label>
                            <span v-if="showCopySQL">
                                &nbsp;&nbsp;SQL&nbsp;&nbsp;<i @click="copy(storeCustomerOrder.sql)"
                                                              class="el-icon-document-copy"></i>
                            </span>
              </label>
              </div>
            </div>

            <el-dialog
                :title="'[ '+storeCustomerOrder.customerOrderNo+' ][ '+storeCustomerOrder.storeOrderCode+' ][ '+storeCustomerOrder.customerOrderCode+' ] 来自OMS的原数据'"
                :visible.sync="OMSOrigData_dialogVisible" :show-close="false" width="65%">
              <div>
                <pre>{{ this.storeCustomerOrder.orgDataFromOMS }}</pre>
                <i @click="copy(storeCustomerOrder.orgDataFromOMS)" class="el-icon-document-copy"></i>
              </div>
            </el-dialog>

          </div>

          <!-- 订货明细 -->
          <div style="margin-top: 10px;">
            <el-divider content-position="left">订货明细</el-divider>

            <div style="margin-left: 40px; font-weight: 500; font-size: 14px;">
              <div style="padding-bottom: 10px;width: 700px">
                <el-input v-model="search" size="medium" placeholder="商品名称,商品编码,OMS商品编码,仓库货主商品编码,STOCK码" clearable/>
              </div>
              <template>
                <el-table :data="handle()" border show-summary :summary-method="storeCustomerOrderDetailsSummaries"
                          style="width: 100%" :row-style="{ height: 10+'px'}" :cell-style="{padding:0+'px'}"
                          :row-class-name="tableRowClassName"> <!-- height="250" -->
                  <el-table-column fixed label="序号" type="index" width="50"></el-table-column>
                  <el-table-column fixed label="商品名称" min-width="150" :show-overflow-tooltip="true">
                    <template slot-scope="scope">
                      <i @click="copy(scope.row.goodsName)" class="el-icon-document-copy"></i>
                      <el-button @click="handleGoodsBatchHistoryClick(scope.row)" type="text">
                        {{ scope.row.goodsName }}
                      </el-button>
                    </template>
                  </el-table-column>
                  <el-table-column fixed prop="goodsNo" label="商品编码" width="100"></el-table-column>
                  <el-table-column prop="externalGoodsNo" label="OMS商品编码" width="170"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="warehouseOwnerGoodsNo" label="仓库货主商品编码" width="160"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="thirdNo" label="STOCK码" width="250"
                                   :show-overflow-tooltip="true"></el-table-column>
                  <!--
                  <el-table-column prop="goodsOwnerBusinessNo" label="货主业务编码" min-width="200" :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="orderItemCode" label="套餐商品编码" min-width="200" :show-overflow-tooltip="true"></el-table-column>
                  -->
                  <!--
                                              <el-table-column label="套餐商品" width="100" align="center">
                                                  <template slot-scope="scope">
                                                      <span v-if="scope.row.isSetMeal == '是'">
                                                          <svg t="1691468608589" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="4016" width="16" height="16"><path d="M414.245926 751.028148l437.57037-453.12c7.300741-7.49037 7.111111-19.531852-0.474074-26.832593-7.49037-7.300741-19.531852-7.111111-26.832593 0.474074L398.506667 712.722963 199.111111 513.327407c-7.395556-7.395556-19.437037-7.395556-26.832593 0l0 0c-7.395556 7.395556-7.395556 19.437037 0 26.832593l212.574815 212.574815c6.731852 6.731852 17.161481 7.300741 24.557037 1.896296C411.211852 753.682963 412.823704 752.545185 414.245926 751.028148z" fill="#d4237a" p-id="4017"></path></svg>
                                                      </span>
                                                  </template>
                                              </el-table-column>
                  -->
                  <el-table-column align="center" prop="setMealDesc" label="套餐商品" width="80"></el-table-column>
                  <el-table-column align="center" prop="orderQuantity" label="订货数量" width="80"></el-table-column>

                  <el-table-column align="center" prop="processedQuantity" width="80">
                    <template slot-scope="scope" slot="header">
                      <span style="color: #df3327;">已出库数</span>
                    </template>
                    <template slot-scope="scope">
                                    <span v-if="scope.row.processedQuantity > scope.row.orderQuantity">
                                        <span style="color: red;">{{ scope.row.processedQuantity }}</span>
                                    </span>
                      <span v-else>
                                        {{ scope.row.processedQuantity }}
                                    </span>
                    </template>
                  </el-table-column>

                  <el-table-column align="center" prop="processingQuantity" width="80">
                    <template slot-scope="scope" slot="header">
                      <span style="color: #df3327;">出库中数</span>
                    </template>
                  </el-table-column>

                  <el-table-column align="center" prop="deliveredQuantity" width="80">
                    <template slot-scope="scope" slot="header">
                      <span style="color: #0ca5e6;">已发货数</span>
                    </template>
                    <template slot-scope="scope">
                      <span v-if="scope.row.deliveredQuantity > scope.row.processedQuantity">
                        <span style="color: red;">{{ scope.row.deliveredQuantity }}</span>
                      </span>
                      <span v-else>
                        {{ scope.row.deliveredQuantity }}
                      </span>
                    </template>
                  </el-table-column>

                  <el-table-column align="center" prop="deliveringQuantity" width="80">
                    <template slot-scope="scope" slot="header">
                      <span style="color: #0ca5e6;">发货中数</span>
                    </template>
                  </el-table-column>

                  <el-table-column label="已退货数=待出库退货数+已出库退货数" align="center">
                    <el-table-column align="center" prop="returnedQuantity" width="90">
                      <template slot-scope="scope" slot="header">
                        <span style="color: #dc0e49;">已退货数</span>
                      </template>
                    </el-table-column>
                    <el-table-column align="center" prop="waitOutReturnQuantity" width="110">
                      <template slot-scope="scope" slot="header">
                        <span style="color: #dc0e49;">待出库退货数</span>
                      </template>
                    </el-table-column>
                    <el-table-column align="center" prop="alreadyOutReturnQuantity" width="110">
                      <template slot-scope="scope" slot="header">
                        <span style="color: #dc0e49;">已出库退货数</span>
                      </template>
                    </el-table-column>
                  </el-table-column>

                  <el-table-column align="center" prop="returningQuantity" width="80">
                    <template slot-scope="scope" slot="header">
                      <span style="color: #dc0e49;">退货中数</span>
                    </template>
                  </el-table-column>

                  <el-table-column align="center" label="可用/冻结库存" width="120">
                    <template slot-scope="scope">
                      <span>{{ scope.row.available_quantity }}/{{ scope.row.out_frozen_quantity }}</span>
                    </template>
                  </el-table-column>
                  <el-table-column align="center" prop="goodsUnitPrice" label="销售单价(元)" width="120"></el-table-column>
                  <el-table-column align="center" prop="totalPrice" label="小计(元)" width="80"></el-table-column>
                  <el-table-column align="center" prop="goodsValue" label="货值(元)" width="120"></el-table-column>
                  <el-table-column align="center" prop="businessIncome" label="商家收入(元)" width="120"></el-table-column>
                  <el-table-column align="center" prop="totalGrossWeight" label="重量(KG)" width="120"></el-table-column>
                  <el-table-column align="center" label="扩展信息" max-width="120" :show-overflow-tooltip="true">
                    <template slot-scope="scope">
                      <span v-if="scope.row.extension !== 'null'">{{ scope.row.extension }}</span>
                      <span v-else></span>
                    </template>
                  </el-table-column>
                  <el-table-column align="center" fixed="right" label="出库明细" width="80">
                    <template slot-scope="scope">
                      <span v-if="scope.row.outList == undefined || scope.row.outList.length <= 0">
                        -
                      </span>
                      <span v-else>
                        <el-button @click="handleOutDetailClick(scope.row)" type="text">查看({{ scope.row.outList.length }})</el-button>
                      </span>
                    </template>
                  </el-table-column>
                  <el-table-column align="center" fixed="right" label="已出库未发货的入库明细" width="80">
                    <template slot-scope="scope">
                      <span v-if="scope.row.noOutInList == undefined || scope.row.noOutInList.length <= 0">
                        -
                      </span>
                      <span v-else>
                        <el-button @click="handleNoOutInDetailClick(scope.row)" type="text">查看({{ scope.row.noOutInList.length }})</el-button>
                      </span>
                    </template>
                  </el-table-column>
                  <el-table-column align="center" fixed="right" label="发货明细" width="80">
                    <template slot-scope="scope">
                      <span v-if="scope.row.sendList == undefined || scope.row.sendList.length <= 0">
                        -
                      </span>
                      <span v-else>
                        <el-button @click="handleSendDetailClick(scope.row)" type="text">查看({{ scope.row.sendList.length }})</el-button>
                      </span>
                    </template>
                  </el-table-column>
                  <el-table-column align="center" fixed="right" label="退货明细" width="80">
                    <template slot-scope="scope">
                      <span v-if="scope.row.returnList == undefined || scope.row.returnList.length <= 0">
                        -
                      </span>
                      <span v-else>
                        <el-button @click="handleReturnDetailClick(scope.row)" type="text">查看({{ scope.row.returnList.length }})</el-button>
                      </span>
                    </template>
                  </el-table-column>
                </el-table>
              </template>

              <!-- 出库明细 -->
              <el-dialog :title="'[ ' + GoodsName_Batch + ' ] 出库明细'" :visible.sync="OutDetailClick_dialogVisible" :show-close="false" width="80%">
                <template>
                  <el-table :data="OutDetailClickList" border style="width: 100%" :row-style="{ height: 10+'px'}" :cell-style="{padding:0+'px'}"> <!-- height="250" -->
                    <el-table-column align="center" prop="goodsNo" label="商品编码" width="100"></el-table-column>
                    <el-table-column align="center" prop="storageNo" label="出库单号" width="150"></el-table-column>
                    <el-table-column align="center" label="出库状态" width="80">
                      <template slot-scope="scope">
                        <span v-if="scope.row.storageStatusDesc == '已出库' || scope.row.storageStatusDesc == '已入库'">
                          <span style="color: green;">{{ scope.row.storageStatusDesc }}</span>
                        </span>
                        <span v-else>
                            <span>{{ scope.row.storageStatusDesc }}</span>
                        </span>
                      </template>
                    </el-table-column>
                    <el-table-column align="center" label="仓库" width="220">
                      <template slot-scope="scope">
                        <span v-if="scope.row.changeWarehouseId == null">
                          <span>原仓: {{ scope.row.warehouseName }}</span>
                        </span>
                        <span v-else>
                            <span style="color: red;">换仓: {{ scope.row.changeWarehouseName }}</span>
                        </span>
                      </template>
                    </el-table-column>
                    <el-table-column align="center" prop="expectQuantity" label="预期出库数量" width="120"></el-table-column>

                    <el-table-column align="center" label="实际出库数量" width="120">
                      <template slot-scope="scope">
                        <span v-if="scope.row.realQuantity > scope.row.expectQuantity">
                          <span style="color: red;">{{ scope.row.realQuantity }}</span>
                        </span>
                        <span v-else>
                          {{ scope.row.realQuantity }}
                        </span>
                      </template>
                    </el-table-column>

                    <el-table-column align="center" prop="batchNo" label="批次号" min-width="150" :show-overflow-tooltip="true"></el-table-column>
                    <!--
                    <el-table-column align="center" prop="productionDate" label="生产日期" min-width="150" :show-overflow-tooltip="true"></el-table-column> -->
                    <el-table-column align="center" prop="batchDetailId" label="批次详情ID" min-width="150" :show-overflow-tooltip="true"></el-table-column>
                  </el-table>
                </template>
              </el-dialog>
              <!-- 发货明细 -->
              <el-dialog :title="'[ ' + GoodsName_Batch + ' ] 发货明细'" :visible.sync="SendDetailClick_dialogVisible" :show-close="false" width="65%">
                <template>
                  <el-table :data="SendDetailClickList" border style="width: 100%" :row-style="{ height: 10+'px'}" :cell-style="{padding:0+'px'}"> <!-- height="250" -->
                    <el-table-column align="center" prop="goodsNo" label="商品编码" width="100"></el-table-column>
                    <el-table-column align="center" prop="sendOrderNo" label="发货单号" width="160"></el-table-column>
                    <el-table-column align="center" label="发货状态" width="80">
                      <template slot-scope="scope">
                        <span v-if="scope.row.sendOrderStatusDesc == '已发货'">
                          <span style="color: green;">{{ scope.row.sendOrderStatusDesc }}</span>
                        </span>
                        <span v-else>
                            <span>{{ scope.row.sendOrderStatusDesc }}</span>
                        </span>
                      </template>
                    </el-table-column>
                    <el-table-column align="center" label="仓库" width="220">
                      <template slot-scope="scope">
                        <span v-if="scope.row.changeWarehouseId == null">
                            <span>原仓: {{ scope.row.warehouseName }}</span>
                        </span>
                        <span v-else>
                            <span style="color: red;">换仓: {{ scope.row.changeWarehouseName }}</span>
                        </span>
                      </template>
                    </el-table-column>
                    <el-table-column align="center" prop="sendQuantity" label="发货数量" width="120"></el-table-column>
                    <el-table-column align="center" prop="realSendQuantity" label="实发数量" width="120"></el-table-column>
                    <el-table-column align="center" prop="tmsTypeDesc" label="运输类型"></el-table-column>
                  </el-table>
                </template>
              </el-dialog>
              <!-- 退货明细 -->
              <el-dialog :title="'[ ' + GoodsName_Batch + ' ] 退货明细'" :visible.sync="ReturnDetailClick_dialogVisible" :show-close="false" width="80%">
                <template>
                  <el-table :data="ReturnDetailClickList" border style="width: 100%" :row-style="{ height: 10+'px'}" :cell-style="{padding:0+'px'}"> <!-- height="250" -->
                    <el-table-column align="center" prop="goodsNo" label="商品编码" width="100"></el-table-column>
                    <el-table-column align="center" prop="returnOrderNo" label="退货单号" width="160"></el-table-column>
                    <el-table-column align="center" label="退货状态" width="80">
                      <template slot-scope="scope">
                        <span v-if="scope.row.returnOrderStatusDesc === '已完成'">
                          <span style="color: green;">{{ scope.row.returnOrderStatusDesc }}</span>
                        </span>
                        <span v-else>
                          <span>{{ scope.row.returnOrderStatusDesc }}</span>
                        </span>
                      </template>
                    </el-table-column>
                    <el-table-column align="center" label="仓库" width="220">
                      <template slot-scope="scope">
                        <span v-if="scope.row.changeWarehouseId == null">
                            <span>原仓: {{ scope.row.warehouseName }}</span>
                        </span>
                        <span v-else>
                            <span style="color: red;">换仓: {{ scope.row.changeWarehouseName }}</span>
                        </span>
                      </template>
                    </el-table-column>
                    <el-table-column align="center" prop="returnQuantity" label="退货数量" width="80"></el-table-column>
                    <el-table-column label="已退货数=待出库退货数+已出库退货数" align="center">
                      <el-table-column align="center" prop="alreadyReturnQuantity" width="90">
                        <template slot-scope="scope" slot="header">
                          <span style="color: #dc0e49;">已退货数</span>
                        </template>
                      </el-table-column>
                      <el-table-column align="center" prop="waitOutReturnQuantity" width="110">
                        <template slot-scope="scope" slot="header">
                          <span style="color: #dc0e49;">待出库退货数</span>
                        </template>
                      </el-table-column>
                      <el-table-column align="center" prop="alreadyOutReturnQuantity" width="110">
                        <template slot-scope="scope" slot="header">
                          <span style="color: #dc0e49;">已出库退货数</span>
                        </template>
                      </el-table-column>
                    </el-table-column>
                    <el-table-column align="center" prop="processingQuantity" label="退货中数" width="80"></el-table-column>
                    <el-table-column align="center" prop="returnOrderFinishTypeDesc" label="完结类型" width="80"></el-table-column>
                    <el-table-column align="center" prop="returnOrderCode" label="自定义单号" min-width="150" :show-overflow-tooltip="true"></el-table-column>
                  </el-table>
                </template>
              </el-dialog>
              <!-- 库存操作 -->
              <el-dialog :title="'[ ' + GoodsName_Batch + ' ] 库存操作记录'" :visible.sync="GoodsBatchClick_dialogVisible" :show-close="false" width="70%">

                <el-select v-model="select_batch" placeholder="请选择批次" @change="selectBatch()" filterable>
                  <el-option v-for="item in BatchOptions" :key="item.value" :label="item.label" :value="item.value"></el-option>
                </el-select>
                <el-select v-model="select_batch_detail" placeholder="请选择库位" @change="selectBatchDetail(1)" filterable>
                  <el-option v-for="item in BatchDetailOptions" :key="item.value" :label="item.label" :value="item.value"></el-option>
                </el-select>
                <span style="display: inline; margin-left: 25px;" v-if="GoodsBatchDetailHistoryTotal > 0">
                        <span>共计{{ GoodsBatchDetailHistoryTotal }}条记录</span>
                        &nbsp;&nbsp;<i @click="copy(GoodsBatchDetailHistorySQL)" class="el-icon-document-copy"></i>SQL
                        </span>
                <span style="display: inline; margin-left: 25px;" v-if="GoodsBatchDetailHistoryErrorTotal > 0">
                  <el-button @click="handleFixStockClick(select_batch_detail)" type="text">修复库存({{ GoodsBatchDetailHistoryErrorTotal }}条)</el-button>
                </span>
                <span style="display: inline; margin-left: 25px;" v-if="(GoodsBatchDetailHistoryAvailableQuantity + GoodsBatchDetailHistoryOutFrozenQuantity) != GoodsBatchDetailHistoryLastAfterQuantity">
                  <el-button @click="handleFixAvailableQuantityClick(select_batch_detail)" type="text">修复可用库存的值</el-button>
                </span>

                <div style="margin-top: 10px;" v-loading="goods_batch_loading">
                  <template>
                    <div style="margin-bottom: 10px;" v-if="showAvailableQuantity">
                      <div>
                        [ 可用库存 ] {{ GoodsBatchDetailHistoryAvailableQuantity }}
                      </div>
                      <div>
                        [ 冻结库存 ] {{ GoodsBatchDetailHistoryOutFrozenQuantity }}
                      </div>
                    </div>

                    <el-table :data="GoodsBatchDetailHistoryList" border style="width: 100%" :row-style="{ height: 10+'px'}" :cell-style="{padding:0+'px'}"> <!-- height="250" -->
                      <!--
                      <el-table-column fixed label="序号" type="login" width="50"></el-table-column>
                      -->
                      <el-table-column align="center" prop="beforeQuantity" label="期初库存" width="150"></el-table-column>
                      <el-table-column align="left" label="操作数量" width="80">
                        <template slot-scope="scope">
                          <span v-if="scope.row.storageCategory === 0">
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
                          <span v-if="scope.row.hasError === 1">
                            <span style="color: red;">有问题</span>
                          </span>
                          <span v-if="scope.row.hasError === 0 && scope.row.hasNegative === 1">
                            <span style="color: orange;">有负数</span>
                          </span>
                        </template>
                      </el-table-column>
                    </el-table>

                    <div v-if="fix_error != ''" style="margin-top: 20px;">
                      [ 修复结果 ] {{ fix_error }}
                    </div>

                  </template>
                </div>
              </el-dialog>

            </div>

          </div>


          <!-- 仓库信息 -->
          <div style="margin-top: 10px;">
            <el-divider content-position="left">仓库</el-divider>

            <div style="margin-left: 40px; font-weight: 500; font-size: 14px;">
              <el-collapse v-model="warehouseActiveNames">
                <el-collapse-item title="资源名称" name="1">
                  <div style="font-weight: 500; font-size: 14px;">
                    <div>
                      <template>
                        <el-table :data="resourceList" border style="width: 60%" :row-style="{ height: 10+'px'}" :cell-style="{padding:0+'px'}"> <!-- height="250" -->
                          <el-table-column fixed label="序号" type="index" width="50"></el-table-column>
                          <el-table-column prop="resourceName" label="资源名称" width="200"></el-table-column>
                          <el-table-column prop="createTime" label="创建时间" width="200"></el-table-column>
                          <el-table-column prop="updateTime" label="更新时间"></el-table-column>
                        </el-table>
                      </template>
                    </div>
                  </div>
                </el-collapse-item>

                <el-collapse-item title="物流公司" name="2">
                  <div style="font-weight: 500; font-size: 14px;">
                    <div style="margin-top: 10px;">
                      <template>
                        <el-table :data="logisticsList" border style="width: 60%" :row-style="{ height: 10+'px'}" :cell-style="{padding:0+'px'}"> <!-- height="250" -->
                          <el-table-column fixed label="序号" type="index" width="50"></el-table-column>
                          <el-table-column prop="logisticsName" label="物流公司" width="200"></el-table-column>
                          <el-table-column prop="createTime" label="创建时间" width="200"></el-table-column>
                          <el-table-column align="center" label="状态">
                            <template slot-scope="scope">
                              <span v-if="scope.row.enable == 0">
                                  <span style="color: red;">禁用</span>
                              </span>
                              <span v-else>
                                  启用
                              </span>
                            </template>
                          </el-table-column>
                        </el-table>
                      </template>
                    </div>
                  </div>
                </el-collapse-item>
              </el-collapse>
            </div>

          </div>


          <!-- 出库单 -->
          <div style="margin-top: 10px;">
            <el-divider content-position="left">出库单</el-divider>

            <div style="margin-left: 40px; font-weight: 500; font-size: 14px;">
              <template>
                <el-table :data="ssList" border style="width: 100%" :row-style="{ height: 10+'px'}" :cell-style="{padding:0+'px'}"> <!-- height="250" -->
                  <el-table-column fixed label="单号" width="180">
                    <template slot-scope="scope">
                      <i @click="copy(scope.row.storageNo)" class="el-icon-document-copy"></i>&nbsp;&nbsp;{{ scope.row.storageNo }}
                    </template>
                  </el-table-column>
                  <el-table-column prop="storageType" label="出库类型" width="80"></el-table-column>
                  <el-table-column label="出库状态" width="80">
                    <template slot-scope="scope">
                      <span v-if="scope.row.storageStatus == '已出库'">
                        <span style="color: green;">{{ scope.row.storageStatus }}</span>
                      </span>
                      <span v-else>
                        <span>{{ scope.row.storageStatus }}</span>
                      </span>
                    </template>
                  </el-table-column>
                  <el-table-column align="center" label="仓库" width="220">
                    <template slot-scope="scope">
                      <span v-if="scope.row.changeWarehouseId == null">
                          <span>原仓: {{ scope.row.warehouseName }}</span>
                      </span>
                      <span v-else>
                          <span style="color: red;">换仓: {{ scope.row.changeWarehouseName }}</span>
                      </span>
                    </template>
                  </el-table-column>

                  <el-table-column prop="sourceOrderNo" label="关联单号"></el-table-column>
                  <el-table-column prop="createTime" label="创建时间" width="200"></el-table-column>
                  <el-table-column prop="updateTime" label="更新时间" width="200"></el-table-column>
                  <el-table-column fixed="right" label="操作" width="210">
                    <template slot-scope="scope">
                      <router-link :to="{path: '/store_storage', query:{storeStorageNo: scope.row.storageNo}}" target="_blank" style="margin-left: 5px;">
                        <span class="icon-link">查看明细</span>
                      </router-link>
                    </template>
                  </el-table-column>
                </el-table>
              </template>
            </div>
          </div>

          <!-- 入库单 -->
          <div style="margin-top: 10px;">
            <el-divider content-position="left">已出库未发货的入库单(手动完结场景)</el-divider>

            <div style="margin-left: 40px; font-weight: 500; font-size: 14px;">
              <template>
                <el-table :data="ssInList" border style="width: 100%" :row-style="{ height: 10+'px'}" :cell-style="{padding:0+'px'}"> <!-- height="250" -->
                  <el-table-column fixed label="单号" width="180">
                    <template slot-scope="scope">
                      <i @click="copy(scope.row.storageNo)"
                         class="el-icon-document-copy"></i>&nbsp;&nbsp;{{ scope.row.storageNo }}
                    </template>
                  </el-table-column>
                  <el-table-column prop="storageType" label="入库类型" width="80"></el-table-column>
                  <el-table-column label="入库状态" width="80">
                    <template slot-scope="scope">
                                <span v-if="scope.row.storageStatus == '已入库'">
                                    <span style="color: green;">{{ scope.row.storageStatus }}</span>
                                </span>
                      <span v-else>
                                    <span>{{ scope.row.storageStatus }}</span>
                                </span>
                    </template>
                  </el-table-column>
                  <el-table-column align="center" label="仓库" width="220">
                    <template slot-scope="scope">
                      <span v-if="scope.row.changeWarehouseId == null">
                          <span>原仓: {{ scope.row.warehouseName }}</span>
                      </span>
                      <span v-else>
                          <span style="color: red;">换仓: {{ scope.row.changeWarehouseName }}</span>
                      </span>
                    </template>
                  </el-table-column>

                  <el-table-column prop="sourceOrderNo" label="关联单号"></el-table-column>
                  <el-table-column prop="createTime" label="创建时间" width="200"></el-table-column>
                  <el-table-column prop="updateTime" label="更新时间" width="200"></el-table-column>
                  <el-table-column fixed="right" label="操作" width="210">
                    <template slot-scope="scope">
                      <router-link :to="{path: '/store_storage', query:{storeStorageNo: scope.row.storageNo}}" target="_blank" style="margin-left: 5px;">
                        <span class="icon-link">查看明细</span>
                      </router-link>
                    </template>
                  </el-table-column>
                </el-table>
              </template>
            </div>
          </div>


          <!-- 发货单 -->
          <div style="margin-top: 10px;">
            <el-divider content-position="left">发货单</el-divider>

            <div style="margin-left: 40px; font-weight: 500; font-size: 14px;">
              <template>
                <el-table :data="ssoList" border style="width: 100%" :row-style="{ height: 10+'px'}" :cell-style="{padding:0+'px'}"> <!-- height="250" -->
                  <el-table-column fixed label="单号" width="180">
                    <template slot-scope="scope">
                      <i @click="copy(scope.row.sendOrderNo)" class="el-icon-document-copy"></i>&nbsp;&nbsp;{{ scope.row.sendOrderNo }}
                    </template>
                  </el-table-column>
                  <el-table-column prop="tmsType" label="运输类型" width="80"></el-table-column>
                  <el-table-column label="发货状态" width="80">
                    <template slot-scope="scope">
                      <span v-if="scope.row.sendOrderStatus === '已发货'">
                          <span style="color: green;">{{ scope.row.sendOrderStatus }}</span>
                      </span>
                      <span v-else>
                          <span>{{ scope.row.sendOrderStatus }}</span>
                      </span>
                    </template>
                  </el-table-column>
                  <el-table-column align="center" label="仓库" width="220">
                    <template slot-scope="scope">
                      <span v-if="scope.row.changeWarehouseId == null">
                          <span>原仓: {{ scope.row.warehouseName }}</span>
                      </span>
                      <span v-else>
                          <span style="color: red;">换仓: {{ scope.row.changeWarehouseName }}</span>
                      </span>
                    </template>
                  </el-table-column>
                  <el-table-column label="运输单号">
                    <template slot-scope="scope">
                      <span v-if="scope.row.tmsType === '城配'">
                          <span v-if="scope.row.diffDepartTimeStr === 0">
                            <router-link :to="{path: '/store_tran', query:{tmsNo: scope.row.tmsNo}}" target="_blank" style="margin-left: 5px;">
                              <span class="icon-link">{{ scope.row.tmsNo }}</span>
                            </router-link>
                          </span>
                          <span v-else>
                            <router-link :to="{path: '/store_tran', query:{tmsNo: scope.row.tmsNo}}" target="_blank" style="margin-left: 5px;">
                              <span class="icon-link">{{ scope.row.tmsNo }} [ 距离发车{{ scope.row.diffDepartTimeStr }}分钟 ]</span>
                            </router-link>
                          </span>
                      </span>
                      <span v-else>
                          <span>{{ scope.row.tmsNo }}</span>
                      </span>
                    </template>
                  </el-table-column>


                  <el-table-column prop="sendOrderTime" label="发货时间" width="200"></el-table-column>
                  <el-table-column prop="createTime" label="创建时间" width="200"></el-table-column>
                  <el-table-column prop="updateTime" label="更新时间" width="200"></el-table-column>
                  <el-table-column fixed="right" label="操作" width="210">
                    <template slot-scope="scope">
                      <router-link :to="{path: '/store_send_order', query:{sendOrderNo: scope.row.sendOrderNo}}" target="_blank" style="margin-left: 5px;">
                        <span class="icon-link">查看明细</span>
                      </router-link>
                    </template>
                  </el-table-column>
                </el-table>
              </template>

              <!-- 发货单推送记录 -->
              <el-dialog :title="'[ ' + SendOrder_Push + ' ] 推送记录'" :visible.sync="SendOrderPush_dialogVisible" :show-close="false" width="80%">
                <template>
                  <el-table :data="SendOrderPushHistoryList" border style="width: 100%" :row-style="{ height: 10+'px'}" :cell-style="{padding:0+'px'}"> <!-- height="250" -->
                    <el-table-column align="center" prop="apiRecordCode" label="记录编码" width="270"></el-table-column>
                    <el-table-column align="center" prop="pushApplicationName" label="平台名称" width="120"></el-table-column>
                    <el-table-column align="center" prop="pushStatusName" label="状态" width="160"></el-table-column>
                    <el-table-column align="center" label="仓库" width="220">
                      <template slot-scope="scope">
                                    <span v-if="scope.row.changeWarehouseName == null">
                                        <span>原仓: {{ scope.row.warehouseName }}</span>
                                    </span>
                        <span v-else>
                                        <span style="color: red;">换仓: {{ scope.row.changeWarehouseName }}</span>
                                    </span>
                      </template>
                    </el-table-column>

                    <el-table-column align="center" prop="pushTimeStr" label="推送时间" min-width="150" :show-overflow-tooltip="true"></el-table-column>
                  </el-table>
                </template>
              </el-dialog>
            </div>
          </div>


          <!-- 退货单 -->
          <div style="margin-top: 10px;">
            <el-divider content-position="left">退货单</el-divider>

            <div style="margin-left: 40px; font-weight: 500; font-size: 14px;">
              <template>
                <el-table :data="sroList" border style="width: 100%" :row-style="{ height: 10+'px'}" :cell-style="{padding:0+'px'}"> <!-- height="250" -->
                  <el-table-column fixed label="单号" width="180">
                    <template slot-scope="scope">
                      <i @click="copy(scope.row.returnOrderNo)"
                         class="el-icon-document-copy"></i>&nbsp;&nbsp;{{ scope.row.returnOrderNo }}
                    </template>

                  </el-table-column>
                  <el-table-column prop="returnOrderFinishType" label="完结类型" width="80"></el-table-column>
                  <el-table-column label="退货状态" width="80">
                    <template slot-scope="scope">
                                <span v-if="scope.row.returnOrderStatus == '已完成'">
                                    <span style="color: green;">{{ scope.row.returnOrderStatus }}</span>
                                </span>
                      <span v-else>
                                    <span>{{ scope.row.returnOrderStatus }}</span>
                                </span>
                    </template>
                  </el-table-column>
                  <el-table-column align="center" label="仓库" width="220">
                    <template slot-scope="scope">
                                    <span v-if="scope.row.changeWarehouseId == null">
                                        <span>原仓: {{ scope.row.warehouseName }}</span>
                                    </span>
                      <span v-else>
                                        <span style="color: red;">换仓: {{ scope.row.changeWarehouseName }}</span>
                                    </span>
                    </template>
                  </el-table-column>
                  <el-table-column prop="returnOrderCode" label="自定义单号"></el-table-column>
                  <el-table-column prop="createTime" label="创建时间" width="200"></el-table-column>
                  <el-table-column prop="updateTime" label="更新时间" width="200"></el-table-column>
                  <el-table-column fixed="right" label="操作" width="210">
                    <template slot-scope="scope">
                      <router-link :to="{path: '/store_return_order', query:{returnOrderNo: scope.row.returnOrderNo}}" target="_blank" style="margin-left: 5px;">
                        <span class="icon-link">查看明细</span>
                      </router-link>
                    </template>
                  </el-table-column>
                </el-table>
              </template>
            </div>
          </div>


          <!-- 自动作业记录 -->
          <div style="margin-top: 10px;">
            <el-divider content-position="left">自动作业记录</el-divider>

            <div style="margin-left: 40px; font-weight: 500; font-size: 14px;">
              <template>
                <el-table :data="autoRecordList" border style="width: 100%" :row-style="{ height: 10+'px'}" :cell-style="{padding:0+'px'}"> <!-- height="250" -->
                  <el-table-column fixed label="序号" type="index" width="50"></el-table-column>
                  <el-table-column prop="applicationType" label="类型" width="120"
                                   :show-overflow-tooltip="true"></el-table-column>

                  <el-table-column label="状态" width="200">
                    <template slot-scope="scope">
                      <span v-if="scope.row.status === '执行失败'">
                          <span style="color: red;">{{ scope.row.status }}</span>
                      </span>
                      <span v-else>
                          <span>{{ scope.row.status }}</span>
                      </span>
                    </template>
                  </el-table-column>
                  <el-table-column prop="exception" label="异常信息"></el-table-column>
                  <el-table-column prop="createTime" label="创建时间" width="200"></el-table-column>
                  <el-table-column prop="updateTime" label="更新时间" width="200"></el-table-column>
                </el-table>
              </template>
            </div>
          </div>

          <!-- MQ消息记录 -->
          <div style="margin-top: 10px;">
            <el-divider content-position="left">MQ消息记录</el-divider>

            <div style="margin-left: 40px; font-weight: 500; font-size: 14px;">
              <template>
                <el-table :data="mqRecordList" border style="width: 100%" :row-style="{ height: 10+'px'}" :cell-style="{padding:0+'px'}"> <!-- height="250" -->
                  <el-table-column fixed label="序号" type="index" width="50"></el-table-column>
                  <el-table-column label="业务单号" width="220" :show-overflow-tooltip="true">
                    <template slot-scope="scope">
                      <el-button @click="handleMqOperationRecordClick(scope.$index, scope.row)" type="text">
                        {{ scope.row.businessNo }}
                      </el-button>
                    </template>
                  </el-table-column>
                  <el-table-column prop="method" label="方法名" min-width="120" :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="messageId" label="MQ消息ID" width="305" :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="remark" label="动作" width="200" :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="desc" label="说明信息" min-width="100" :show-overflow-tooltip="true"></el-table-column>
                  <el-table-column prop="createTimeStr" label="创建时间" width="200"></el-table-column>
                </el-table>

                <el-dialog :title="'[ ' + DETAIL_INDEX + ' ][ ' + Operation_Record_Body_Title + ' ] 内容体'" :visible.sync="Operation_Record_DETAIL_dialogVisible" :show-close="false" width="50%">
                  <div style="display: block; margin: 5px 0;">
                    <label style="display: inline-block; text-align: right;">[ 阿里云ID ]</label><label>&nbsp;&nbsp;&nbsp;{{ operationRecord.messageId }}</label>
                  </div>
                  <div style="display: block; margin: 5px 0;">
                    <label style="display: inline-block; text-align: right;">[ 观测云ID ]</label><label>&nbsp;&nbsp;&nbsp;{{ operationRecord.traceId }}</label>
                  </div>
                  <div style="display: block; margin: 5px 0;">
                    <label style="display: inline-block; text-align: right;">[ 服务名称 ]</label><label>&nbsp;&nbsp;&nbsp;{{ operationRecord.serviceName }}</label>
                  </div>
                  <div style="display: block; margin: 5px 0;">
                    <label style="display: inline-block; text-align: right;">[ 方法名称 ]</label><label>&nbsp;&nbsp;&nbsp;{{ operationRecord.method }}</label>
                  </div>
                  <div style="display: block; margin: 5px 0;">
                    <label style="display: inline-block; text-align: right;">[ 动作名称 ]</label><label>&nbsp;&nbsp;&nbsp;{{ operationRecord.remark }}</label>
                  </div>
                  <div style="display: block; margin: 5px 0;">
                    <label style="display: inline-block; text-align: right;">[ 说明信息 ]</label><label>&nbsp;&nbsp;&nbsp;{{ operationRecord.desc }}</label>
                  </div>
                  <div style="display: block; margin: 5px 0;">
                    <label style="display: inline-block; text-align: right;">[ 请求地址 ]</label><label>&nbsp;&nbsp;&nbsp;{{ operationRecord.sourceIp }}</label>
                  </div>
                  <div style="display: block; margin: 5px 0;">
                    <label style="display: inline-block; text-align: right;">[ 事件地址 ]</label><label>&nbsp;&nbsp;&nbsp;{{ operationRecord.handleIp }}</label>
                  </div>
                </el-dialog>

              </template>
            </div>
          </div>

          <!-- 推送记录 -->
          <div style="margin-top: 10px;">
            <el-divider content-position="left">推送记录</el-divider>

            <div style="margin-left: 40px; font-weight: 500; font-size: 14px;">
              <template>
                <el-table :data="pushRecordList" border style="width: 100%" :row-style="{ height: 10+'px'}"
                          :cell-style="{padding:0+'px'}">
                  <el-table-column fixed label="序号" type="index" width="50"></el-table-column>
                  <el-table-column label="记录编码" min-width="150" :show-overflow-tooltip="true">
                    <template slot-scope="scope">
                      <i @click="copy(scope.row.recordCode)" class="el-icon-document-copy"></i>
                      <el-button @click="handlePushDetailClick(scope.row)" type="text">
                        {{ scope.row.recordCode }}
                      </el-button>
                    </template>
                  </el-table-column>
                  <el-table-column prop="pushApplicationName" label="平台名称" width="120"></el-table-column>
                  <el-table-column label="状态" width="110">
                    <template slot-scope="scope">
                      <span v-if="scope.row.pushStatusName === '完成失败' || scope.row.pushStatusName === '处理失败' || scope.row.pushStatusName === '创建失败' || scope.row.pushStatusName === '推送失败'">
                        <span style="color: red;">{{ scope.row.pushStatusName }}</span>
                      </span>
                      <span v-else>
                        <span style="color: green;">{{ scope.row.pushStatusName }}</span>
                      </span>
                    </template>
                  </el-table-column>
                  <el-table-column prop="pushTypeName" label="类型" width="180"></el-table-column>
                  <el-table-column prop="createTime" label="创建时间"></el-table-column>
                  <el-table-column prop="pushTime" label="推送时间"></el-table-column>
                  <el-table-column label="链路ID">
                    <template slot-scope="scope">
                      <router-link :to="{path: '/select_trace', query:{traceId: scope.row.traceId}}" target="_blank" style="margin-left: 5px;">
                        <span class="icon-link">{{ scope.row.traceId }}</span>
                      </router-link>
                    </template>
                  </el-table-column>
                </el-table>
              </template>

              <el-dialog :title="'[ ' + Record_Body_Title + ' ] 推送内容体'" :visible.sync="Record_Body_dialogVisible" :show-close="false" width="60%">
                <div style="display: block; margin: 5px 0;">
                  <label style="display: inline-block; text-align: right;">[ 记录编码 ]</label><label>&nbsp;&nbsp;&nbsp;{{ pushRecord.apiRecordCode }}</label>&nbsp;&nbsp;<i
                    @click="copy(pushRecord.apiRecordCode)" class="el-icon-document-copy"></i>
                </div>
                <div style="display: block; margin: 5px 0;">
                  <label style="display: inline-block; text-align: right;">[ 推送内容 ]</label>
                  <pre>{{ pushRecord.pushBody }}</pre>
                  <span v-if="pushRecord.pushBody != null && pushRecord.pushBody != ''">
                      <i @click="copy(pushRecord.pushBody)" class="el-icon-document-copy"></i>
                  </span>
                </div>
                <div style="display: block; margin: 5px 0;">
                  <label style="display: inline-block; text-align: right;">[ 响应内容 ]</label>
                  <pre>{{ pushRecord.responseBody }}</pre>
                  <span v-if="pushRecord.responseBody != null && pushRecord.responseBody != ''">
                      <i @click="copy(pushRecord.responseBody)" class="el-icon-document-copy"></i>
                  </span>
                </div>
                <div style="display: block; margin: 5px 0;">
                  <label style="display: inline-block; text-align: right;">[ 处理内容 ]</label>
                  <pre>{{ pushRecord.actionBody }}</pre>
                  <span v-if="pushRecord.actionBody != null && pushRecord.actionBody != ''">
                      <i @click="copy(pushRecord.actionBody)" class="el-icon-document-copy"></i>
                  </span>
                </div>
                <div style="display: block; margin: 5px 0;">
                  <label style="display: inline-block; text-align: right;">[ 备注内容 ]</label><label>&nbsp;&nbsp;&nbsp;{{ pushRecord.remark }}</label>
                </div>
              </el-dialog>
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
  name: "StoreCustomerOrder",
  components: {},
  data() {
    return {

      env: Config.env,
      host: Config.host,

      condition: {
        customerOrderNo: '',
        customerOrderCode: '',
        storeOrderCode: ''
      },


      sizeOfStoreOrderCode: 0,
      sizeOfCustomerOrderCode2: 0,
      sizeOfCustomerOrderCode: 0,
      select_customer_order_no: '',


      active_0: 0,
      active_1: 0,

      storeCustomerOrder: {
        customerOrderNo: '',
        enterpriseName: '',
        enterpriseId: '',
        warehouseName: '',
        warehouseId: '',
        goodsOwner: '',
        goodsOwnerId: '',
        customer: '',
        linkman: '',
        createTime: '',
        updateTime: '',
        deliveryMethod: '',
        freightFee: '',
        sumTotalGrossWeight: '',
        customerOrderSource: '',
        orgDataFromOMS: '',
        transportType: '',
        customerOrderFinishType: '',
        customerOrderCode: '',
        storeOrderCode: '',
        sql: '',

      },

      storeCustomerOrderDetailsList: [],

      ssList: [],
      ssInList: [],

      ssoList: [],

      sroList: [],

      pushRecordList: [],
      autoRecordList: [],
      mqRecordList: [],

      OutDetailClick_dialogVisible: false,
      SendDetailClick_dialogVisible: false,
      ReturnDetailClick_dialogVisible: false,
      GoodsBatchClick_dialogVisible: false,
      OMSOrigData_dialogVisible: false,
      SendOrderPush_dialogVisible: false,
      OutDetailClickList: [],
      SendDetailClickList: [],
      ReturnDetailClickList: [],
      GoodsBatchDetailHistoryList: [],
      SendOrderPushHistoryList: [],
      GoodsBatchDetailHistoryHasError: 0,

      resourceList: [],
      logisticsList: [],
      loading: false,
      goods_batch_loading: false,

      select_batch: '',
      select_batch_label: '',
      select_batch_detail: '',
      select_batch_detail_label: '',
      fix_error: '',

      BatchOptions: [],
      BatchDetailOptions: [],
      GoodsName_Batch: '',
      GoodsBatchDetailHistoryErrorTotal: 0,
      GoodsBatchDetailHistoryAvailableQuantity: 0,
      GoodsBatchDetailHistoryOutFrozenQuantity: 0,
      GoodsBatchDetailHistoryLastAfterQuantity: 0,
      GoodsBatchDetailHistorySQL: '',
      GoodsBatchDetailHistoryTotal: 0,
      showAvailableQuantity: false,

      showCopyCustomerOrderNo: false,
      showCopyStoreOrderCode: false,
      showCopyCustomerOrderCode: false,
      showCopySQL: false,


      SendOrder_Push: '',
      warehouseActiveNames: ['-1'],


      Record_Body_Title: '',
      pushRecord: {},
      Record_Body_dialogVisible: false,

      tabsData: [],
      activeName: '',

      operationRecord: {},
      DETAIL_INDEX: '',
      Operation_Record_Body_Title: '',
      Operation_Record_DETAIL_dialogVisible: false,


      search: '',

    }
  },

  created: function () {

    let customerOrderNo = this.$route.query.customerOrderNo;
    let customerOrderCode = this.$route.query.customerOrderCode;
    let storeOrderCode = this.$route.query.storeOrderCode;
    // DH
    if (customerOrderNo) {
      this.condition.customerOrderNo = customerOrderNo
      this.onSubmit(4)
    }
    // DW
    if (customerOrderCode) {
      this.condition.customerOrderCode = customerOrderCode
      this.onSubmit(3)
    }
    // DC
    if (storeOrderCode) {
      this.condition.storeOrderCode = storeOrderCode
      this.onSubmit(2)
    }

  },
  methods: {
    handleTabClick(tab, event) {
      this.select_customer_order_no = tab.name
      this.onSubmit(1);
    },

    // 列表行有问题的情况下, 标记颜色
    tableRowClassName(row) {
      let r = row.row
      if (r.processedQuantity > r.orderQuantity || r.deliveredQuantity > r.processedQuantity) {
        return "warning-row";
      }
    },

    onSubmit(type) {
      let customerOrderNo = this.select_customer_order_no
      if (type === 2) {
        let storeOrderCode = this.condition.storeOrderCode
        if (!storeOrderCode) {
          this.$message({
            message: '单号不能为空',
            type: 'warning'
          });
          return;
        }

        this.loading = true
        this.tabsData = []
        this.select_customer_order_no = ''
        let activeName = ''
        this.sizeOfStoreOrderCode = 0
        this.sizeOfCustomerOrderCode2 = 0
        axios({
          url: this.host + '/toolkit/tools/getStoreCustomerOrderByDC',
          method: 'GET',
          params: {
            storeOrderCode: storeOrderCode
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
            if (response.data.scoList.length === 0) {
              this.$message({
                message: '未查询到数据',
                type: 'warning'
              });

              this.loading = false
              return;
            }

            this.sizeOfCustomerOrderCode2 = response.data.sizeOfCustomerOrderCode;

            let scoList = response.data.scoList
            for (let i = 0; i < scoList.length; i++) {
              let label = scoList[i]['customerOrderNo']
              let value = scoList[i]['customerOrderNo']

              this.tabsData.push({'labelName': label, 'tabName': value})
            }

            this.activeName = this.tabsData[0]['tabName']
            this.select_customer_order_no = this.tabsData[0]['tabName']
            this.onSubmit(1);

            this.sizeOfStoreOrderCode = scoList.length
          }
        }, (error) => {
          console.log(error)
          this.$message({
            message: '查询失败',
            type: 'warning'
          });

          this.loading = false
        })
        return;
      } else if (type === 3) {
        let customerOrderCode = this.condition.customerOrderCode
        if (!customerOrderCode) {
          this.$message({
            message: '单号不能为空',
            type: 'warning'
          });
          return;
        }

        this.loading = true
        this.tabsData = []
        this.select_customer_order_no = ''
        this.activeName = ''
        this.sizeOfCustomerOrderCode = 0
        axios({
          url: this.host + '/toolkit/tools/getStoreCustomerOrderByDW',
          method: 'GET',
          params: {
            customerOrderCode: customerOrderCode
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
            if (response.data.length === 0) {
              this.$message({
                message: '未查询到数据',
                type: 'warning'
              });

              this.loading = false
              return;
            }

            for (let i = 0; i < response.data.length; i++) {
              let label = response.data[i]['customerOrderNo']
              let value = response.data[i]['customerOrderNo']

              this.tabsData.push({'labelName': label, 'tabName': value})
            }
            this.activeName = this.tabsData[0]['tabName']
            this.select_customer_order_no = this.tabsData[0]['tabName']
            this.onSubmit(1);

            this.sizeOfCustomerOrderCode = response.data.length

          } else {
            this.loading = false
          }
        }, (error) => {
          console.log(error)
          this.$message({
            message: '查询失败',
            type: 'warning'
          });
          this.loading = false
        })
        return;
      } else if (type === 4) {
        let customerOrderNo = this.condition.customerOrderNo
        if (!customerOrderNo) {
          this.$message({
            message: '单号不能为空',
            type: 'warning'
          });
          return;
        }

        this.tabsData = []

        let label = customerOrderNo
        let value = customerOrderNo
        this.tabsData.push({'labelName': label, 'tabName': value})

        this.activeName = customerOrderNo
        this.select_customer_order_no = customerOrderNo
        this.onSubmit(1);
        return;
      }


      this.loading = true

      this.active_0 = 0
      this.active_1 = 0
      this.storeCustomerOrder = {}
      this.storeCustomerOrderDetailsList = []
      this.ssList = []
      this.ssInList = []
      this.ssoList = []
      this.sroList = []
      this.pushRecordList = []
      this.autoRecordList = []
      this.mqRecordList = []
      this.OutDetailClickList = []
      this.SendDetailClickList = []
      this.ReturnDetailClickList = []
      this.resourceList = []
      this.logisticsList = []
      this.showCopyCustomerOrderNo = false
      this.showCopyStoreOrderCode = false
      this.showCopyCustomerOrderCode = false
      this.showCopySQL = false


      axios({
        url: this.host + '/toolkit/tools/getStoreCustomerOrder',
        method: 'GET',
        params: {
          customerOrderNo: customerOrderNo
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

        let storeCustomerOrder = response.data.storeCustomerOrder
        if (!storeCustomerOrder) {
          this.$message({
            message: '未查询到数据',
            type: 'warning'
          });
        }
        this.storeCustomerOrder.warehouseId = response.data.storeCustomerOrder['warehouseId']
        this.storeCustomerOrder.warehouseName = response.data.warehouse['warehouseName']
        this.storeCustomerOrder.enterpriseName = response.data.enterprise['enterpriseName']
        this.storeCustomerOrder.enterpriseId = response.data.storeCustomerOrder['enterpriseId']
        this.storeCustomerOrder.goodsOwner = response.data.goodsOwner['customerName']
        this.storeCustomerOrder.goodsOwnerId = response.data.storeCustomerOrder['goodsOwnerId']
        this.storeCustomerOrder.sql = response.data.storeCustomerOrder['sql']
        this.storeCustomerOrder.customer = response.data.customer['customerName']
        this.storeCustomerOrder.linkman = response.data.customer['linkman']

        this.storeCustomerOrder.customerOrderNo = response.data.storeCustomerOrder['customerOrderNo']
        this.storeCustomerOrder.createTime = response.data.storeCustomerOrder['createTime']
        this.storeCustomerOrder.updateTime = response.data.storeCustomerOrder['updateTime']
        this.storeCustomerOrder.deliveryMethod = response.data.storeCustomerOrder['deliveryMethod']
        this.storeCustomerOrder.freightFee = response.data.storeCustomerOrder['freightFee']
        this.storeCustomerOrder.sumTotalGrossWeight = response.data.storeCustomerOrder['sumTotalGrossWeight']
        this.storeCustomerOrder.customerOrderSource = response.data.storeCustomerOrder['customerOrderSource']

        if (response.data.storeCustomerOrder['orgDataFromOMS']) {
          this.storeCustomerOrder.orgDataFromOMS = this.format0(response.data.storeCustomerOrder['orgDataFromOMS'])
        }

        this.storeCustomerOrder.transportType = response.data.storeCustomerOrder['transportType']
        this.storeCustomerOrder.customerOrderFinishType = response.data.storeCustomerOrder['customerOrderFinishType']
        this.storeCustomerOrder.customerOrderCode = response.data.storeCustomerOrder['customerOrderCode']
        this.storeCustomerOrder.storeOrderCode = response.data.storeCustomerOrder['storeOrderCode']
        this.active_0 = response.data.storeCustomerOrder['customerOrderStatus']
        this.active_1 = response.data.storeCustomerOrder['sendOrderStatus']


        this.storeCustomerOrderDetailsList = response.data.storeCustomerOrderDetailsList
        this.ssList = response.data.ssList
        this.ssInList = response.data.ssInList
        this.ssoList = response.data.ssoList
        this.sroList = response.data.sroList

        if (this.storeCustomerOrder.customerOrderNo) {
          this.showCopyCustomerOrderNo = true
        }
        if (this.storeCustomerOrder.storeOrderCode) {
          this.showCopyStoreOrderCode = true
        }
        if (this.storeCustomerOrder.customerOrderCode) {
          this.showCopyCustomerOrderCode = true
        }
        if (this.storeCustomerOrder.sql) {
          this.showCopySQL = true
        }

        this.pushRecordList = response.data.pushRecordList
        this.autoRecordList = response.data.autoRecordList
        this.mqRecordList = response.data.mqRecordList

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
    storeCustomerOrderDetailsSummaries(param) {
      const {columns, data} = param;
      const sums = [];
      columns.forEach((column, index) => {
        if (index === 0) {
          sums[index] = '合计';
          return;
        }
        if (index === 1 || index === 2 || index === 3 || index === 4 || index === 5 || index === 6 || index === 16 || index === 21 || index === 22 || index === 23) {
          sums[index] = '';
          return;
        }

        const values = data.map(item => Number(item[column.property]));
        if (!values.every(value => isNaN(value))) {
          sums[index] = values.reduce((prev, curr) => {
            const value = Number(curr);
            if (!isNaN(value)) {
              return parseFloat((prev + curr).toFixed(10))
              // return prev + curr;
            } else {
              return prev;
            }
          }, 0);
          // sums[index] += ' 元';
        } else {
          // sums[index] = 'N/A';
        }
      });
      return sums;
    },

    // 出库单操作
    handleStoreStorageClick(row) {
      console.log(row)
    },
    // 发货单操作
    handleSendOrderClick(row) {
      console.log(row)
    },
    // 退货单操作

    // 出库明细
    handleOutDetailClick(row) {
      let customerOrderDetailsId = row.customerOrderDetailsId

      this.GoodsName_Batch = row.goodsName

      axios({
        url: this.host + '/toolkit/ssd/getStoreStorageDetails',
        method: 'GET',
        params: {
          customerOrderDetailsId: customerOrderDetailsId,
          storageType: 1
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

        this.OutDetailClick_dialogVisible = true
        this.OutDetailClickList = response.data
      }, (error) => {
        console.log(error)
        this.$message({
          message: '查询出库明细失败',
          type: 'warning'
        });
      })

    },
    // 已出库未发货的入库明细
    handleNoOutInDetailClick(row) {
      let customerOrderDetailsId = row.customerOrderDetailsId

      this.GoodsName_Batch = row.goodsName

      axios({
        url: this.host + '/toolkit/ssd/getStoreStorageDetails',
        method: 'GET',
        params: {
          customerOrderDetailsId: customerOrderDetailsId,
          storageType: 0
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
        this.OutDetailClick_dialogVisible = true
        this.OutDetailClickList = response.data
      }, (error) => {
        console.log(error)
        this.$message({
          message: '查询入库明细失败',
          type: 'warning'
        });
      })

    },
    // 发货明细
    handleSendDetailClick(row) {

      this.GoodsName_Batch = row.goodsName

      let customerOrderDetailsId = row.customerOrderDetailsId

      axios({
        url: this.host + '/toolkit/sso/getStoreSendDetails',
        method: 'GET',
        params: {
          customerOrderDetailsId: customerOrderDetailsId
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

        this.SendDetailClick_dialogVisible = true
        this.SendDetailClickList = response.data
      }, (error) => {
        console.log(error)
        this.$message({
          message: '查询发货明细失败',
          type: 'warning'
        });
      })
    },
    // 退货明细
    handleReturnDetailClick(row) {

      this.GoodsName_Batch = row.goodsName

      let customerOrderDetailsId = row.customerOrderDetailsId

      axios({
        url: this.host + '/toolkit/srod/getStoreReturnDetails',
        method: 'GET',
        params: {
          customerOrderDetailsId: customerOrderDetailsId
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
        this.ReturnDetailClick_dialogVisible = true
        this.ReturnDetailClickList = response.data
      }, (error) => {
        console.log(error)
        this.$message({
          message: '查询退货明细失败',
          type: 'warning'
        });
      })
    },
    // 查看商品库存操作记录
    handleGoodsBatchHistoryClick(row) {

      this.GoodsBatchClick_dialogVisible = true
      this.BatchOptions = []
      this.BatchDetailOptions = []
      this.GoodsBatchDetailHistoryList = []
      this.GoodsBatchDetailHistoryErrorTotal = 0
      this.GoodsBatchDetailHistoryAvailableQuantity = 0
      this.GoodsBatchDetailHistoryOutFrozenQuantity = 0
      this.GoodsBatchDetailHistoryLastAfterQuantity = 0
      this.GoodsBatchDetailHistorySQL = ''
      this.GoodsBatchDetailHistoryTotal = 0
      this.select_batch = ''
      this.select_batch_label = ''
      this.select_batch_detail = ''
      this.select_batch_detail_label = ''
      this.fix_error = ''
      this.showAvailableQuantity = false

      this.GoodsName_Batch = row.goodsName

      axios({
        url: this.host + '/toolkit/tools/getGoodsBatchHistoryByWarehouseOwnerGoodsId',
        method: 'GET',
        params: {
          warehouseOwnerGoodsId: row.warehouseOwnerGoodsId
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
        let batchList = response.data.batchList

        if (batchList.length > 0) {
          for (let i = 0; i < batchList.length; i++) {
            let _label = batchList[i]['batchNo']
            let _value = batchList[i]['batchId']
            this.BatchOptions.push({'label': _label, 'value': _value})
          }

          this.select_batch = this.BatchOptions[0]['value']
          this.selectBatch()
        }

      }, (error) => {
        console.log(error)
        this.$message({
          message: '查询商品库存操作记录失败',
          type: 'warning'
        });
      })

    },

    // 发货单推送记录
    handleSendOrderToThirdClick(row) {
      this.SendOrder_Push = row.sendOrderNo

      axios({
        url: this.host + '/toolkit/sso/findSendOrderPush',
        method: 'GET',
        params: {
          sendOrderNo: row.sendOrderNo
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

        this.SendOrderPush_dialogVisible = true
        this.SendOrderPushHistoryList = response.data
      }, (error) => {
        console.log(error)
        this.$message({
          message: '查询发货单推送记录失败',
          type: 'warning'
        });
      })
    },

    // 选中批次
    selectBatch() {
      for (const obj of this.BatchOptions) {
        if (obj.value === this.select_batch) {
          this.select_batch_label = obj.label
          break
        }
      }

      this.BatchDetailOptions = []
      this.fix_error = ''
      this.select_batch_detail = ''
      this.select_batch_detail_label = ''
      this.GoodsBatchDetailHistorySQL = ''
      this.GoodsBatchDetailHistoryList = []
      this.GoodsBatchDetailHistoryErrorTotal = 0
      this.GoodsBatchDetailHistoryAvailableQuantity = 0
      this.GoodsBatchDetailHistoryOutFrozenQuantity = 0
      this.GoodsBatchDetailHistoryLastAfterQuantity = 0
      this.showAvailableQuantity = false

      axios({
        url: this.host + '/toolkit/tools/getBatchDetailList',
        method: 'GET',
        params: {
          batchId: this.select_batch
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
        let batchDetailList = response.data.batchDetailList

        if (batchDetailList.length > 0) {
          for (let i = 0; i < batchDetailList.length; i++) {
            let _label = batchDetailList[i]['warehouseLocationName']
            let _value = batchDetailList[i]['batchDetailsId']
            this.BatchDetailOptions.push({'label': _label, 'value': _value})
          }
          if (batchDetailList.length === 1) {
            this.select_batch_detail = this.BatchDetailOptions[0]['value']
            this.selectBatchDetail(1)
          }
        } else {
          this.select_batch_detail = ''
          this.select_batch_detail_label = ''
        }
      }, (error) => {
        console.log(error)
        this.$message({
          message: '查询商品库存操作记录失败',
          type: 'warning'
        });
      })

    },
    // 选中库位
    selectBatchDetail(clear) {

      for (const obj of this.BatchDetailOptions) {
        if (obj.value === this.select_batch_detail) {
          this.select_batch_detail_label = obj.label
          break
        }
      }

      this.GoodsBatchDetailHistorySQL = ''
      if (clear === 1) {
        this.fix_error = ''
      }

      this.goods_batch_loading = true

      axios({
        url: this.host + '/toolkit/tools/getBatchDetailHistory',
        method: 'GET',
        params: {
          batchDetailId: this.select_batch_detail
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
            this.GoodsBatchDetailHistoryErrorTotal = response.data.errorTotal
            this.GoodsBatchDetailHistoryAvailableQuantity = response.data.availableQuantity
            this.GoodsBatchDetailHistoryOutFrozenQuantity = response.data.outFrozenQuantity
            this.GoodsBatchDetailHistoryLastAfterQuantity = response.data.lastAfterQuantity
            this.GoodsBatchDetailHistorySQL = response.data.sql
            this.GoodsBatchDetailHistoryTotal = response.data.historyList.length
            this.goods_batch_loading = false
            this.showAvailableQuantity = true
          }, (error) => {
            console.log(error)
            this.$message({
              message: '查询商品库存操作记录失败',
              type: 'warning'
            });
            this.goods_batch_loading = false
          })
    },

    clearCustomerOrderCode() {
      this.sizeOfCustomerOrderCode = 0
    },
    clearStoreOrderCode() {
      this.sizeOfStoreOrderCode = 0
    },
    clearCustomerOrderNo() {

    },

    // 修复库存
    handleFixStockClick(select_batch_detail) {

      this.$confirm('确定修复库存?', '[ ' + this.GoodsName_Batch + ' ]', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
        showClose: false
      }).then(() => {
        this.fix_error = ''
        axios({
          url: this.host + '/toolkit/tools/fixStock',
          method: 'GET',
          params: {
            batchDetailId: select_batch_detail
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

          let data = response.data
          if (data) {
            this.$message({
              message: data,
              type: 'warning'
            });
            this.fix_error = data
          } else {
            this.$message({
              message: '修复成功',
              type: 'success'
            });
          }
          // 重新刷新该列表
          this.selectBatchDetail(0)
        }, (error) => {
          console.log(error)
          this.$message({
            message: '修复失败',
            type: 'warning'
          });
        })
      }).catch(() => {
      });
    },
    // 修复可用库存的值
    handleFixAvailableQuantityClick(select_batch_detail) {

      this.$confirm('确定修复批次[' + this.select_batch_label + ']库位[' + this.select_batch_detail_label + ']的可用库存值? 从 ' + this.GoodsBatchDetailHistoryAvailableQuantity + ' 修改成 ' + (this.GoodsBatchDetailHistoryLastAfterQuantity - this.GoodsBatchDetailHistoryOutFrozenQuantity), '[ ' + this.GoodsName_Batch + ' ]', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
        showClose: false
      }).then(() => {

        this.fix_error = ''
        axios({
          url: this.host + '/toolkit/tools/AvailableQuantity',
          method: 'GET',
          params: {
            batchDetailId: select_batch_detail
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

              let data = response.data
              if (data) {
                this.$message({
                  message: data,
                  type: 'warning'
                });
                this.fix_error = data
              } else {
                this.$message({
                  message: '修复成功',
                  type: 'success'
                });
              }
              // 重新刷新该列表
              this.selectBatchDetail(0)
            }, (error) => {
              console.log(error)
              this.$message({
                message: '修复失败',
                type: 'warning'
              });
            })
      }).catch(() => {
      });

    },

    handle() {
      return this.storeCustomerOrderDetailsList.filter(data => {
        if (this.search) {
          var allKey = this.search.split(/[,，]/);
          for (let i = 0; i < allKey.length; i++) {
            if (data.goodsName && data.goodsName.toLowerCase().includes(allKey[i].toLowerCase())) {
              return true;
            }
            if (data.goodsNo && data.goodsNo.toLowerCase().includes(allKey[i].toLowerCase())) {
              return true;
            }
            if (data.warehouseOwnerGoodsNo && data.warehouseOwnerGoodsNo.toLowerCase().includes(allKey[i].toLowerCase())) {
              return true;
            }
            if (data.thirdNo && data.thirdNo.toLowerCase().includes(allKey[i].toLowerCase())) {
              return true;
            }
            if (data.externalGoodsNo && data.externalGoodsNo.toLowerCase().includes(allKey[i].toLowerCase())) {
              return true;
            }
          }
          return false;
        }

        return true;
      })
    },


    handlePushDetailClick(row) {

      this.Record_Body_Title = row.businessNo
      this.pushRecord = {}

      let success = row.recordCode.search(/^TS.*$/g)

      let _url = ''
      if (success === 0) {
        _url = this.host + '/toolkit/tools/getPushRecordDetail2'
      } else {
        _url = this.host + '/toolkit/tools/getPushRecordDetail'
      }

      axios({
        url: _url,
        method: 'GET',
        params: {
          recordCode: row.recordCode
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

            this.pushRecord = response.data
            if (this.pushRecord['pushBody']) {
              this.pushRecord['pushBody'] = this.format0(this.pushRecord['pushBody']);
            }

            if (this.pushRecord['responseBody']) {
              this.pushRecord['responseBody'] = this.format0(this.pushRecord['responseBody']);
            }

            this.Record_Body_dialogVisible = true
          }, (error) => {
            console.log(error)
            this.$message({
              message: '查询推送记录失败',
              type: 'warning'
            });
          })
    },

    handleMqOperationRecordClick(index, row) {
      this.DETAIL_INDEX = index + 1
      this.Operation_Record_Body_Title = row.businessNo

      this.operationRecord = {}

      axios({
        url: this.host + '/toolkit/or/detail',
        method: 'GET',
        params: {
          recordId: row.recordIdStr
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
            this.operationRecord = response.data
            this.operationRecord['businessNo'] = row.businessNo
            this.Operation_Record_DETAIL_dialogVisible = true
          }, (error) => {
            console.log(error)
            this.$message({
              message: '查询失败',
              type: 'warning'
            });
          })
    },

    format0(data) {

      if (data.includes(':')) {
        try {
          //
          let data = this.t(data)
          const obj = JSON.parse(data)
          if (obj.hasOwnProperty('body')) {
            // 第一层
            obj.body = this.t(obj.body)
            const _obj = JSON.parse(obj.body)
            obj.body = _obj
          }
          if (obj.hasOwnProperty('requestBody')) {
            try {
              // 第一层
              obj.requestBody = this.t(obj.requestBody)
              const _obj = JSON.parse(obj.requestBody)
              obj.requestBody = _obj
              if (obj.requestBody.hasOwnProperty('requestBody')) {
                // 第二层
                obj.requestBody.requestBody = this.t(obj.requestBody.requestBody)
                const _obj = JSON.parse(obj.requestBody.requestBody)
                obj.requestBody.requestBody = _obj
              }
            } catch (err) {
              console.log(err)
            }
          }

          data = JSON.stringify(obj, null, 4)
        } catch (err) {
          console.log(err)
        }
      }
      return data;
    },
    t(data) {
      // 长整数转成字符串类型, 防止精度丢失
      data = data.replace(/((\W*)s*):s*([0-9]{15,})s*(,?)/g, '$1: $2$3$2 $4')
      return data;
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
    handleOMSOrigDataClick() {
      this.OMSOrigData_dialogVisible = true
    },

  }
};
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
  font-family: "Microsoft YaHei";
  white-space: pre-wrap;
  word-wrap: break-word;
}


</style>