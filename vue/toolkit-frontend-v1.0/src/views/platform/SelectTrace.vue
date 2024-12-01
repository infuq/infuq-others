<template>
  <div>
    <section class="content clearfix" style="width: 97%;">
      <div class="el-backtop" style="right: 40px; top: 130px;">
        <el-link type="primary" :href="'/'" :underline="false" target="_blank"><i class="el-icon-s-home"></i></el-link>
      </div>
      <el-divider content-position="right">{{ env }}环境</el-divider>

      <div style="margin-top: 15px;">
        <!-- 全局链路ID -->
        <div style="margin-top: 10px;">

          <el-form :inline="true" class="demo-form-inline">
            <div v-if="isShowQuery">
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

              <el-select v-model="selectAppCode" placeholder="请选择应用" @change="selectApp(selectAppCode)" filterable clearable @clear="clearSelectAppCode">
                <el-option v-for="item in AppOptions" :key="item.value" :label="item.label" :value="item.value"></el-option>
              </el-select>

              <el-input v-model="traceId" placeholder="410499046604926976" clearable style="width: 400px; margin-left: 5px;">
                <template slot="prepend">全局链路ID</template>
              </el-input>
              <div style="display: inline-block; margin-top: 3px; margin-bottom: 3px; margin-left: 5px;">
                <el-button type="primary" @click="onSubmit">查询</el-button>
              </div>
            </div>

            <div v-if="isShowQuery">

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

              <el-select v-model="selectAppCode2" placeholder="请选择应用" @change="selectApp2(selectAppCode2)" filterable clearable @clear="clearSelectAppCode2">
                <el-option v-for="item in AppOptions" :key="item.value" :label="item.label" :value="item.value"></el-option>
              </el-select>

              <el-input v-model="businessNo" placeholder="DH-231008-000007 或 IIC-2023-10-0038 或 AIRP6jHQOlGv231009094307298" clearable style="width: 790px; margin-left: 5px;">
                <template slot="prepend">业务单号或三方单号或记录编码</template>
              </el-input>

              <div style="display: inline-block; margin-top: 3px; margin-bottom: 3px; margin-left: 5px;">
                <el-button type="primary" @click="onSubmit2">查询</el-button>
              </div>
            </div>

            <div v-if="isShowQuery" style="margin-top: 10px;">
              <template>
                <el-radio v-model="switchRadio" label="1">不包含已删除的数据</el-radio>
                <el-radio v-model="switchRadio" label="2">包含已删除的数据</el-radio>
              </template>
            </div>

            <!-- 结果 -->
            <div style="margin-top: 15px;">
              <!-- 结果 -->
              <div style="margin-top: 10px;" v-loading="loading">

                <!-- 仅仅是为了没有数据的情况下展示使用 -->
                <span v-if="allDataList.length < 1">
                  <el-divider content-position="left">结果</el-divider>
                  <template>
                    <el-table :data="allDataList" border style="width: 100%" :row-style="{ height: 10+'px'}" :cell-style="{padding:0+'px'}"> <!-- height="250" -->
                      <el-table-column fixed label="序号" type="index" width="50"></el-table-column>
                      <el-table-column label="三方单号" max-width="220" :show-overflow-tooltip="true"></el-table-column>
                      <el-table-column label="业务单号" max-width="220" :show-overflow-tooltip="true"></el-table-column>
                      <el-table-column prop="appName" label="应用名称" width="100" :show-overflow-tooltip="true"></el-table-column>
                      <el-table-column label="类型" width="60"></el-table-column>
                      <el-table-column prop="businessTypeName" label="业务类型" width="100" :show-overflow-tooltip="true"></el-table-column>
                      <el-table-column label="状态" width="100"></el-table-column>
                      <el-table-column prop="retryCount" label="重试次数" width="90"></el-table-column>
                      <el-table-column prop="createTime" label="创建时间" width="160"></el-table-column>
                      <el-table-column prop="updateTime" label="更新时间" width="160"></el-table-column>
                      <!--
                      <el-table-column label="SQL" width="80"></el-table-column> -->
                      <el-table-column label="已删除" width="100" align="center" v-if="switchRadio == 2"></el-table-column>
                      <el-table-column prop="desc" label="描述" min-width="120" :show-overflow-tooltip="true"></el-table-column>
                      <el-table-column fixed="right" label="操作" min-width="90"></el-table-column>
                    </el-table>
                  </template>
                </span>

                <span v-if="allDataList.length>0" v-for="data in allDataList">
                    <el-divider content-position="left">结果(全局链路ID={{ data.traceId }})</el-divider>

                    <div style="font-weight: 500; font-size: 14px;">
                      <template>
                        <el-table :data="data.dataList" border style="width: 100%" :row-style="{ height: 10+'px'}" :cell-style="{padding:0+'px'}"> <!-- height="250" -->
                          <el-table-column fixed label="序号" type="index" width="50"></el-table-column>
                          <el-table-column label="三方单号" max-width="220" :show-overflow-tooltip="true">
                            <template slot-scope="scope" v-if="scope.row.thirdNo != null && scope.row.thirdNo !== ''">
                              <span>
                                <i @click="copy(scope.row.thirdNo)" class="el-icon-document-copy"></i>&nbsp;&nbsp;{{ scope.row.thirdNo }}
                              </span>
                            </template>
                          </el-table-column>
                          <el-table-column label="业务单号" max-width="220" :show-overflow-tooltip="true">
                            <template slot-scope="scope" v-if="scope.row.businessNo != null && scope.row.businessNo !== ''">
                              <span>
                                <i @click="copy(scope.row.businessNo)" class="el-icon-document-copy"></i>&nbsp;&nbsp;{{ scope.row.businessNo }}
                              </span>
                            </template>
                          </el-table-column>

                          <el-table-column prop="appName" label="应用名称" width="100" :show-overflow-tooltip="true"></el-table-column>
                          <el-table-column label="类型" width="90" :show-overflow-tooltip="true">
                            <template slot-scope="scope">
                              <span v-if="scope.row.typeName === '推送'">
                                <span style="color: #c51096;">{{ scope.row.typeName }}</span>
                              </span>
                              <span v-else>
                                <span>{{ scope.row.typeName }}</span>
                              </span>
                            </template>
                          </el-table-column>
                          <el-table-column prop="businessTypeName" label="业务类型" width="100" :show-overflow-tooltip="true"></el-table-column>
                          <el-table-column label="状态" width="100" :show-overflow-tooltip="true">
                            <template slot-scope="scope">
                              <span v-if="scope.row.statusName === '处理失败' || scope.row.statusName === '推送失败'">
                                <span v-if="scope.row.pushBody != null && scope.row.pushBody !== '' && scope.row.responseBody != null && scope.row.responseBody != ''">
                                  <span style="color: red;">{{ scope.row.statusName }}[因第三方]</span>
                                </span>
                                <span v-else>
                                  <span style="color: red;">{{ scope.row.statusName }}</span>
                                </span>
                              </span>
                              <span v-else>
                                <span style="color: green;">{{ scope.row.statusName }}</span>
                              </span>
                            </template>
                          </el-table-column>
                          <el-table-column prop="retryCount" label="重试次数" width="90"></el-table-column>
                          <el-table-column prop="createTime" label="创建时间" width="160"></el-table-column>
                          <el-table-column prop="updateTime" label="更新时间" width="160"></el-table-column>
                          <el-table-column label="SQL" width="80">
                            <template slot-scope="scope">
                              <span>
                                <i @click="copy(scope.row.sql)" class="el-icon-document-copy"></i>&nbsp;&nbsp;SQL
                              </span>
                            </template>
                          </el-table-column>
                          <el-table-column label="已删除" width="100" align="center" v-if="data.deleted === 1">
                            <template slot-scope="scope">
                              <span v-if="scope.row.deleted != null && scope.row.deleted === 1">
                                <svg t="1691468608589" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="4016" width="16" height="16"><path d="M414.245926 751.028148l437.57037-453.12c7.300741-7.49037 7.111111-19.531852-0.474074-26.832593-7.49037-7.300741-19.531852-7.111111-26.832593 0.474074L398.506667 712.722963 199.111111 513.327407c-7.395556-7.395556-19.437037-7.395556-26.832593 0l0 0c-7.395556 7.395556-7.395556 19.437037 0 26.832593l212.574815 212.574815c6.731852 6.731852 17.161481 7.300741 24.557037 1.896296C411.211852 753.682963 412.823704 752.545185 414.245926 751.028148z" fill="#d4237a" p-id="4017"></path></svg>
                              </span>
                            </template>
                          </el-table-column>
                          <el-table-column prop="desc" label="描述" min-width="120" :show-overflow-tooltip="true"></el-table-column>

                          <el-table-column fixed="right" label="操作" min-width="90">
                            <template slot-scope="scope">
                              <el-button @click="handleDetailClick(scope.row)" type="text">详情</el-button>
                              <el-dropdown @command="handleCommand($event, scope.row)">
                                <span class="el-dropdown-link" style="margin-left: 5px; color: #409EFF;">更多操作</span>
                                <el-dropdown-menu slot="dropdown">
                                  <span v-if="scope.row.deleted == null || scope.row.deleted === 0">
                                    <el-dropdown-item command="a" icon="el-icon-delete">删除</el-dropdown-item>
                                  </span>
                                  <span v-if="scope.row.statusName === '处理失败' || scope.row.statusName === '推送失败'">
                                    <el-dropdown-item command="b" icon="el-icon-success">更改状态为成功</el-dropdown-item>
                                  </span>
                                  <span v-else>
                                    <el-dropdown-item command="c" icon="el-icon-error">更改状态为失败</el-dropdown-item>
                                    <el-dropdown-item command="f" icon="el-icon-refresh">更改状态为失败并重试</el-dropdown-item>
                                  </span>

                                  <span v-if="scope.row.statusName === '处理失败' || scope.row.statusName === '推送失败'">
                                    <span v-if="(scope.row.statusName === '处理失败' || scope.row.statusName === '推送失败') && scope.row.platformName == 'WMS ->'">
                                        <el-dropdown-item command="d" icon="el-icon-edit">修改推送内容</el-dropdown-item>
                                    </span>
                                    <span v-if="scope.row.statusName === '推送失败' && scope.row.platformName === '对接平台 ->'">
                                        <el-dropdown-item command="e" icon="el-icon-edit">修改推送内容</el-dropdown-item>
                                    </span>
                                  </span>
                                </el-dropdown-menu>
                              </el-dropdown>
                              <span v-if="scope.row.statusName === '处理失败' || scope.row.statusName === '推送失败'">
                                  <el-button @click="handleRetryClick(scope.row)" type="text" style="margin-left: 5px; color: #409EFF;">重试</el-button>
                              </span>
                            </template>
                          </el-table-column>
                        </el-table>
                      </template>

                      <el-dialog :title="'[ ' + Record_Body_Title + ' ] 业务数据和推送内容'" :visible.sync="Push_Body_dialogVisible" :show-close="false" width="50%">
                          <div>
                              业务数据 &nbsp;&nbsp;&nbsp; <el-button @click="formatBusinessData('业务数据')" type="text" style="padding: 0px 0px;">查看格式化结果</el-button>
                          </div>
                          <div style="display: block; margin: 5px 0;">
                              <el-input type="textarea" placeholder="请输入业务数据" v-model="api_param" :autosize="{minRows:4,maxRows:10}"></el-input>
                          </div>
                          <div style="margin-top: 25px;">
                              推送内容 &nbsp;&nbsp;&nbsp; <el-button @click="formatBusinessData('推送内容')" type="text" style="padding: 0px 0px;">查看格式化结果</el-button>
                          </div>
                          <div style="display: block; margin: 5px 0;">
                              <el-input type="textarea" placeholder="请输入推送内容" v-model="push_body" :autosize="{minRows:4,maxRows:10}"></el-input>
                          </div>

                          <div style="margin-top: 20px;">
                              <el-button type="primary" @click="update_api_param()">更新业务数据</el-button>
                              <el-button type="primary" @click="update_push_body()">更新推送内容</el-button>
                              <el-button type="primary" @click="update_api_param_push_body()">更新业务数据和推送内容</el-button>
                          </div>
                      </el-dialog>

                      <el-dialog :title="'[ ' + FORMAT_TITLE + ' ] 格式化结果'" :visible.sync="FORMAT_TITLE_dialogVisible" :show-close="false" width="70%">
                          <el-alert title="说明" type="warning" style="width: 26%;" :closable="false">
                              <template slot='title'>
                                <div>不可以将格式化结果内容更新到数据库</div>
                              </template>
                          </el-alert>
                          <div style="margin-top: 5px; border: 1px solid #eae3e3; padding: 10px; background: aliceblue; overflow: auto;">
                              <pre>{{ format_result }}</pre>
                          </div>

                      </el-dialog>

                      <!-- 接收记录详情 -->
                      <el-dialog :title="'[ ' + RECEIVE_Record_Body_Title + ' ] 内容体'" :visible.sync="RECEIVE_Record_Body_dialogVisible" :show-close="false" width="50%">
                          <div style="display: block; margin: 5px 0;">
                              <label style="display: inline-block; text-align: right;">[ 记录编码 ]</label><label>&nbsp;&nbsp;&nbsp;{{receiveRecord.apiRecordCode }}</label>&nbsp;&nbsp;<i @click="copy(receiveRecord.apiRecordCode)" class="el-icon-document-copy"></i>
                          </div>
                          <div style="display: block; margin: 5px 0;">
                              <label style="display: inline-block; text-align: right;">[ 链路追踪 ]</label><label>&nbsp;&nbsp;&nbsp;{{receiveRecord.traceId }}</label>
                              <span v-if="receiveRecord.traceId != null && receiveRecord.traceId != ''">&nbsp;&nbsp;<i @click="copy(receiveRecord.traceId)" class="el-icon-document-copy"></i>
                              </span>
                          </div>
                          <div style="display: block; margin: 5px 0;">
                              <label style="display: inline-block; text-align: right;">[ 创建时间 ]</label><label>&nbsp;&nbsp;&nbsp;{{receiveRecord.createTime }}</label>
                          </div>
                          <div style="display: block; margin: 5px 0;">
                              <label style="display: inline-block; text-align: right;">[ 更新时间 ]</label><label>&nbsp;&nbsp;&nbsp;{{receiveRecord.updateTime }}</label>
                          </div>
                          <div style="display: block; margin: 5px 0;">
                              <label style="display: inline-block; text-align: right;">[ 接收类型 ]</label><label>&nbsp;&nbsp;&nbsp;{{receiveRecord.receiveTypeName }}</label>
                          </div>
                          <div style="display: block; margin: 5px 0;">
                            <label style="display: inline-block; text-align: right;">[ 执行语句 ]</label>
                            <span>
                              &nbsp;&nbsp;SQL&nbsp;&nbsp;<i @click="copy(receiveRecord.sql)" class="el-icon-document-copy"></i>
                            </span>
                          </div>
                          <div style="display: block; margin: 5px 0;">
                              <label style="display: inline-block; text-align: right; color: #e6a23c;">[ 接收内容 ]</label><label>&nbsp;&nbsp;&nbsp;{{receiveRecord.receiveBody }}</label>
                              <span v-if="receiveRecord.receiveBody != null && receiveRecord.receiveBody != ''">&nbsp;&nbsp;<i @click="copy(receiveRecord.receiveBody)" class="el-icon-document-copy"></i>
                              </span>
                          </div>
                          <span v-if="receiveRecord.actionBody != null && receiveRecord.actionBody != ''">
                              <div style="display: block; margin: 5px 0;">
                                <label style="display: inline-block; text-align: right; color: #e6a23c;">[ 处理内容 ]</label><label>&nbsp;&nbsp;&nbsp;{{receiveRecord.actionBody }}</label>
                              </div>
                          </span>
                          <span v-if="receiveRecord.finishBody != null && receiveRecord.finishBody != ''">
                              <div style="display: block; margin: 5px 0;">
                                <label style="display: inline-block; text-align: right; color: #e6a23c;">[ 完成内容 ]</label><label>&nbsp;&nbsp;&nbsp;{{receiveRecord.finishBody }}</label>
                              </div>
                          </span>
                          <span v-if="receiveRecord.receiptBody != null && receiveRecord.receiptBody != ''">
                              <div style="display: block; margin: 5px 0;">
                                <label style="display: inline-block; text-align: right; color: #e6a23c;">[ 回执内容 ]</label><label>&nbsp;&nbsp;&nbsp;{{receiveRecord.receiptBody }}</label>
                              </div>
                          </span>
                          <span v-if="receiveRecord.errorBody != null && receiveRecord.errorBody != ''">
                              <div style="display: block; margin: 5px 0;">
                                <label style="display: inline-block; text-align: right;">[ 错误原因 ]</label><label>&nbsp;&nbsp;&nbsp;{{receiveRecord.errorBody }}</label>
                              </div>
                          </span>
                          <span v-if="receiveRecord.extraBody != null && receiveRecord.extraBody != ''">
                              <div style="display: block; margin: 5px 0;">
                                <label style="display: inline-block; text-align: right; color: #e6a23c;">[ 扩展内容 ]</label><label>&nbsp;&nbsp;&nbsp;{{receiveRecord.extraBody }}</label>
                              </div>
                          </span>
                      </el-dialog>

                      <!-- 推送记录详情 -->
                      <el-dialog :title="'[ ' + PUSH_Record_Body_Title + ' ] 内容体'" :visible.sync="PUSH_Record_Body_dialogVisible" :show-close="false" width="50%">
                            <div style="display: block; margin: 5px 0;">
                                <label style="display: inline-block; text-align: right;">[ 记录编码 ]</label><label>&nbsp;&nbsp;&nbsp;{{pushRecord.apiRecordCode }}</label>&nbsp;&nbsp;<i @click="copy(pushRecord.apiRecordCode)" class="el-icon-document-copy"></i>
                            </div>
                            <div style="display: block; margin: 5px 0;">
                                <label style="display: inline-block; text-align: right;">[ 链路追踪 ]</label><label>&nbsp;&nbsp;&nbsp;{{pushRecord.traceId }}</label>&nbsp;&nbsp;<i @click="copy(pushRecord.traceId)" class="el-icon-document-copy"></i>
                            </div>
                            <div style="display: block; margin: 5px 0;">
                                <label style="display: inline-block; text-align: right;">[ 创建时间 ]</label><label>&nbsp;&nbsp;&nbsp;{{pushRecord.createTime }}</label>
                            </div>
                            <div style="display: block; margin: 5px 0;">
                                <label style="display: inline-block; text-align: right;">[ 更新时间 ]</label><label>&nbsp;&nbsp;&nbsp;{{pushRecord.updateTime }}</label>
                            </div>
                            <div style="display: block; margin: 5px 0;">
                                <label style="display: inline-block; text-align: right;">[ 推送类型 ]</label><label>&nbsp;&nbsp;&nbsp;{{pushRecord.pushTypeName }}</label>
                            </div>
                            <div style="display: block; margin: 5px 0;">
                              <label style="display: inline-block; text-align: right;">[ 执行语句 ]</label>
                              <span>
                                &nbsp;&nbsp;SQL&nbsp;&nbsp;<i @click="copy(pushRecord.sql)" class="el-icon-document-copy"></i>
                              </span>
                            </div>
                            <div style="display: block; margin: 5px 0;">
                                <label style="display: inline-block; text-align: right; color: #e6a23c;">[ 推送内容 ]</label><label>&nbsp;&nbsp;&nbsp;{{pushRecord.pushBody }}</label>
                                <span v-if="pushRecord.pushBody != null && pushRecord.pushBody != ''">&nbsp;&nbsp;<i @click="copy(pushRecord.pushBody)" class="el-icon-document-copy"></i>
                                </span>
                            </div>
                            <span v-if="pushRecord.actionBody != null && pushRecord.actionBody != ''">
                                <div style="display: block; margin: 5px 0;">
                                  <label style="display: inline-block; text-align: right; color: #e6a23c;">[ 处理内容 ]</label><label>&nbsp;&nbsp;&nbsp;{{pushRecord.actionBody }}</label>
                                </div>
                            </span>
                            <span v-if="pushRecord.finishBody != null && pushRecord.finishBody != ''">
                                <div style="display: block; margin: 5px 0;">
                                  <label style="display: inline-block; text-align: right; color: #e6a23c;">[ 完成内容 ]</label><label>&nbsp;&nbsp;&nbsp;{{pushRecord.finishBody }}</label>
                                </div>
                            </span>
                            <span v-if="pushRecord.receiptBody != null && pushRecord.receiptBody != ''">
                                <div style="display: block; margin: 5px 0;">
                                  <label style="display: inline-block; text-align: right; color: #e6a23c;">[ 回执内容 ]</label><label>&nbsp;&nbsp;&nbsp;{{pushRecord.receiptBody }}</label>
                                </div>
                            </span>
                            <span v-if="pushRecord.responseBody != null && pushRecord.responseBody != ''">
                                <div style="display: block; margin: 5px 0;">
                                  <label style="display: inline-block; text-align: right; color: #e6a23c;">[ 响应内容 ]</label><label>&nbsp;&nbsp;&nbsp;{{pushRecord.responseBody }}</label>
                                </div>
                            </span>
                            <span v-if="pushRecord.errorBody != null && pushRecord.errorBody != ''">
                                <div style="display: block; margin: 5px 0;">
                                  <label style="display: inline-block; text-align: right; color: #e6a23c;">[ 异常内容 ]</label><label>&nbsp;&nbsp;&nbsp;{{pushRecord.errorBody }}</label>
                                </div>
                            </span>
                            <span v-if="pushRecord.previousErrorBody != null && pushRecord.previousErrorBody != ''">
                                <div style="display: block; margin: 5px 0;">
                                    <label style="display: inline-block; text-align: right; color: #e6a23c;">[ 历史异常 ]</label><label>&nbsp;&nbsp;&nbsp;{{pushRecord.previousErrorBody }}</label>
                                    <span v-if="pushRecord.previousErrorBody != null && pushRecord.previousErrorBody != ''">&nbsp;&nbsp;<i @click="copy(pushRecord.previousErrorBody)" class="el-icon-document-copy"></i>
                                    </span>
                                </div>
                            </span>
                        </el-dialog>

                    </div>
                </span>

                <div style="margin-top: 15px;">
                  <el-alert title="说明" type="warning" style="width: 26%;">
                    <template slot='title'>
                      <div>说明</div>
                      <div>1. A -> [B] 表示该条记录是B系统的接收记录</div>
                      <div>2. [A] -> B 表示该条记录是A系统的推送记录</div>
                      <div>3. 伟添和部分蜀海在此处查询无效,需要移步到他处查询</div>
                    </template>
                  </el-alert>
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
  name: "SelectTrace",
  data() {

    return {
      env: Config.env,
      host: Config.host,

      traceId: '',
      businessNo: '',
      thirdNo: '',
      loading: false,
      allDataList: [],

      RECEIVE_Record_Body_Title: '',
      RECEIVE_Record_Body_dialogVisible: false,
      PUSH_Record_Body_Title: '',
      PUSH_Record_Body_dialogVisible: false,
      isShowQuery: true,
      receiveRecord: {},
      pushRecord: {},
      // 点击的最近一次按钮   1和2
      curClickBtn: 0,

      switchRadio: '1',


      Record_Body_Title: '',
      Record_Body_dialogVisible: false,
      Push_Body_dialogVisible: false,
      push_body: '',
      api_param: '',
      update_record_code: '',

      FORMAT_TITLE: null,
      FORMAT_TITLE_dialogVisible: false,
      format_result: '',

      updateBusinessDataUrl: '',

      selectAppCode: '',
      selectAppCode2: '',
      AppOptions: [],

    }
  },

  created: function () {

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

    // 其他页面跳转而来
    let traceId = this.$route.query.traceId;
    if (traceId) {
      this.traceId = traceId
      this.onSubmit()
      //this.isShowQuery = false
    }

  },
  methods: {
    handleCommand(command, row) {
      if (command === 'a') {
        this.deleteDetailClick(row)
      } else if (command === 'b') {
        this.updateSuccess(row)
      } else if (command === 'c') {
        this.updateFail(row)
      } else if (command === 'd') {
        this.handlePushBodyClick(row, 'WMS', 'tools')
      } else if (command === 'e') {
        this.handlePushBodyClick(row, '对接平台', 'ab')
      } else if (command === 'f') {
        this.updateFailAndRetry(row)
      }
    },

    // 提交
    onSubmit() {
      if (!this.traceId) {
        this.$message({
          message: '全局链路ID为空',
          type: 'warning'
        });
        return;
      }
      this.curClickBtn = 1
      this.loading = true
      this.allDataList = []
      axios({
        url: this.host + '/toolkit/trace/select',
        method: 'POST',
        data: {
          traceId: this.traceId,
          switchRadio: this.switchRadio,
          selectAppCode: this.selectAppCode
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

        this.allDataList = response.data;
        this.loading = false

        if (this.allDataList.length === 0) {
          this.$message({
            message: '未查询到数据',
            type: 'warning'
          });
        }
      }, error => {
        console.log(error)
        this.loading = false
        this.$message({
          message: '查询失败',
          type: 'warning'
        });
      })

    },

    // 提交
    onSubmit2() {
      if (!this.businessNo && !this.thirdNo) {
        this.$message({
          message: '请输入查询条件',
          type: 'warning'
        });
        return;
      }
      this.curClickBtn = 2
      this.loading = true
      this.allDataList = []
      axios({
        url: this.host + '/toolkit/trace/select2',
        method: 'POST',
        data: {
          businessNo: this.businessNo,
          switchRadio: this.switchRadio,
          selectAppCode: this.selectAppCode2
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

        this.allDataList = response.data;

        this.loading = false

        if (this.allDataList.length === 0) {
          this.$message({
            message: '未查询到数据',
            type: 'warning'
          });
        }
      }, error => {
        console.log(error)
        this.loading = false
        this.$message({
          message: '查询失败',
          type: 'warning'
        });
      })

    },

    handleDetailClick(row) {
      let platformName = row.platformName;
      if (platformName === 'WMS ->') {

        if (row.businessNo) {
          this.PUSH_Record_Body_Title = row.businessNo
        } else {
          this.PUSH_Record_Body_Title = row.thirdNo
        }

        axios({
          url: this.host + '/toolkit/tools/getPushRecordDetail',
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
          this.PUSH_Record_Body_dialogVisible = true
        }, error => {
          console.log(error)
          this.$message({
            message: '查询推送记录失败',
            type: 'warning'
          });
        })
      } else if (platformName === '-> WMS') {

        if (row.businessNo) {
          this.RECEIVE_Record_Body_Title = row.businessNo
        } else {
          this.RECEIVE_Record_Body_Title = row.thirdNo
        }

        axios({
          url: this.host + '/toolkit/tools/getReceiveRecordDetail',
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
          this.receiveRecord = response.data
          this.RECEIVE_Record_Body_dialogVisible = true
        }, error => {
          console.log(error)
          this.$message({
            message: '查询接收记录失败',
            type: 'warning'
          });
        })

      } else if (platformName === '-> 对接平台') {

        if (row.businessNo) {
          this.RECEIVE_Record_Body_Title = row.businessNo
        } else {
          this.RECEIVE_Record_Body_Title = row.thirdNo
        }

        axios({
          url: this.host + '/toolkit/ab/getReceiveRecordDetail',
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

          this.receiveRecord = response.data
          this.RECEIVE_Record_Body_dialogVisible = true
        }, error => {
          console.log(error)
          this.$message({
            message: '查询接收记录失败',
            type: 'warning'
          });
        })

      } else if (platformName === '对接平台 ->') {

        if (row.businessNo) {
          this.PUSH_Record_Body_Title = row.businessNo
        } else {
          this.PUSH_Record_Body_Title = row.thirdNo
        }

        axios({
          url: this.host + '/toolkit/ab/getPushRecordDetail',
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
          this.PUSH_Record_Body_dialogVisible = true
        }, error => {
          console.log(error)
          this.$message({
            message: '查询推送记录失败',
            type: 'warning'
          });
        })

      }
    },
    updateFail(row) {

      let platformName = row.platformName;
      this.$confirm('确定将状态改成失败?', '[ ' + row.recordCode + ' ]', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
        showClose: false
      }).then(() => {
        axios({
          url: this.host + '/toolkit/trace/updateFail',
          method: 'GET',
          params: {
            platformName: row.platformName,
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

          if (response.data === 1) {
            this.$message({
              message: '修改成功',
              type: 'success'
            });
            if (this.curClickBtn === 1) {
              this.onSubmit();
            }
            if (this.curClickBtn === 2) {
              this.onSubmit2();
            }
          } else {
            this.$message({
              message: '修改失败',
              type: 'warning'
            });
          }
        }, error => {
          console.log(error)
          this.$message({
            message: '修改失败',
            type: 'warning'
          });
        })
      }).catch(() => {
      });

    },
    updateFailAndRetry(row) {

      let platformName = row.platformName;
      this.$confirm('确定将状态改成失败并重试?', '[ ' + row.recordCode + ' ]', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
        showClose: false
      }).then(() => {
        axios({
          url: this.host + '/toolkit/trace/updateFail',
          method: 'GET',
          params: {
            platformName: row.platformName,
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

          if (response.data === 1) {
            this.handleRetryClick2(row)
          } else {
            this.$message({
              message: '操作失败',
              type: 'warning'
            });
          }
        }, error => {
          console.log(error)
          this.$message({
            message: '操作失败',
            type: 'warning'
          });
        })
      }).catch(() => {
      });

    },
    updateSuccess(row) {

      let platformName = row.platformName;
      this.$confirm('确定将状态改成成功?', '[ ' + row.recordCode + ' ]', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
        showClose: false
      }).then(() => {
        axios({
          url: this.host + '/toolkit/trace/updateSuccess',
          method: 'GET',
          params: {
            platformName: row.platformName,
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

          if (response.data === 1) {
            this.$message({
              message: '修改成功',
              type: 'success'
            });

            if (this.curClickBtn === 1) {
              this.onSubmit();
            }
            if (this.curClickBtn === 2) {
              this.onSubmit2();
            }

          } else {
            this.$message({
              message: '修改失败',
              type: 'warning'
            });
          }
        }, error => {
          console.log(error)
          this.$message({
            message: '修改失败',
            type: 'warning'
          });
        })
      }).catch(() => {
      });
    },
    deleteDetailClick(row) {

      let platformName = row.platformName;
      this.$confirm('确定删除?', '[ ' + row.recordCode + ' ]', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
        showClose: false
      }).then(() => {
        axios({
          url: this.host + '/toolkit/trace/delete',
          method: 'GET',
          params: {
            platformName: row.platformName,
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

          if (response.data === 1) {
            this.$message({
              message: '删除成功',
              type: 'success'
            });

            if (this.curClickBtn === 1) {
              this.onSubmit();
            }
            if (this.curClickBtn === 2) {
              this.onSubmit2();
            }
          } else {
            this.$message({
              message: '删除失败',
              type: 'warning'
            });
          }
        }, error => {
          console.log(error)
          this.$message({
            message: '删除失败',
            type: 'warning'
          });
        })
      }).catch(() => {
      });

    },

    handleRetryClick(row) {
      let url = '';
      let platformName = row.platformName;
      if (platformName === 'WMS ->') {
        url = this.host + '/toolkit/tools/retryPushRecord';
      } else if (platformName === '-> WMS') {
        url = this.host + '/toolkit/tools/retryReceiveRecord';
      } else if (platformName === '-> 对接平台') {
        url = this.host + '/toolkit/ab/retryReceiveRecord';
      } else if (platformName === '对接平台 ->') {
        url = this.host + '/toolkit/ab/retryPushRecord';
      }

      axios({
        url: url,
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

        if (response.data) {
          this.$message({
            message: response.data,
            type: 'warning'
          });
        } else {
          this.$message({
            message: '重试完成',
            type: 'success'
          });
          /*
          if (this.curClickBtn == 1) {
              this.onSubmit();
          }
          if (this.curClickBtn == 2) {
              this.onSubmit2();
          }*/
        }

      }, error => {
        console.log(error)
        this.$message({
          message: '重试失败',
          type: 'warning'
        });
      })
    },

    handleRetryClick2(row) {
      let url = '';
      let platformName = row.platformName;
      if (platformName === 'WMS ->') {
        url = this.host + '/toolkit/tools/retryPushRecord';
      } else if (platformName === '-> WMS') {
        url = this.host + '/toolkit/tools/retryReceiveRecord';
      } else if (platformName === '-> 对接平台') {
        url = this.host + '/toolkit/ab/retryReceiveRecord';
      } else if (platformName === '对接平台 ->') {
        url = this.host + '/toolkit/ab/retryPushRecord';
      }

      axios({
        url: url,
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

        if (response.data) {
          this.$message({
            message: response.data,
            type: 'warning'
          });
        } else {
          this.$message({
            message: '操作成功',
            type: 'success'
          });
          if (this.curClickBtn === 1) {
            this.onSubmit();
          }
          if (this.curClickBtn === 2) {
            this.onSubmit2();
          }
        }

      }, error => {
        console.log(error)
        this.$message({
          message: '重试失败',
          type: 'warning'
        });
      })
    },

    handlePushBodyClick(row, platformName, url) {

      this.updateBusinessDataUrl = url

      if (row.businessNo) {
        this.Record_Body_Title = row.businessNo
      } else {
        this.Record_Body_Title = row.thirdNo
      }

      this.push_body = ''
      this.api_param = ''

      axios({
        url: this.host + '/toolkit/' + this.updateBusinessDataUrl + '/getPushRecordDetail',
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

        this.push_body = response.data.pushBody
        this.api_param = response.data.apiParam
        this.update_record_code = response.data.apiRecordCode
        this.Push_Body_dialogVisible = true
      }, error => {
        console.log(error)
        this.$message({
          message: '查询推送记录失败',
          type: 'warning'
        });
      })
    },

    update_api_param() {

      axios({
        url: this.host + '/toolkit/' + this.updateBusinessDataUrl + '/updateApiParam',
        method: 'POST',
        data: {
          recordCode: this.update_record_code,
          apiParam: this.api_param
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

        this.Push_Body_dialogVisible = false
        if (response.data === 'success') {
          this.$message({
            message: '更新业务数据成功',
            type: 'success'
          });
        } else {
          this.$message({
            message: '更新业务数据失败',
            type: 'warning'
          });
        }
      }, error => {
        console.log(error)
        this.$message({
          message: '更新业务数据失败',
          type: 'warning'
        });
      })
    },

    update_push_body() {

      axios({
        url: this.host + '/toolkit/' + this.updateBusinessDataUrl + '/updatePushBody',
        method: 'POST',
        data: {
          recordCode: this.update_record_code,
          pushBody: this.push_body
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

        this.Push_Body_dialogVisible = false
        if (response.data === 'success') {
          this.$message({
            message: '更新成功',
            type: 'success'
          });
        } else {
          this.$message({
            message: '更新失败',
            type: 'warning'
          });
        }
      }, error => {
        console.log(error)
        this.$message({
          message: '更新失败',
          type: 'warning'
        });
      })
    },

    update_api_param_push_body() {

      axios({
        url: this.host + '/toolkit/' + this.updateBusinessDataUrl + '/updateApiParamPushBody',
        method: 'POST',
        data: {
          recordCode: this.update_record_code,
          pushBody: this.push_body,
          apiParam: this.api_param
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

        this.Push_Body_dialogVisible = false
        if (response.data === 'success') {
          this.$message({
            message: '更新业务数据和推送内容成功',
            type: 'success'
          });
        } else {
          this.$message({
            message: '更新业务数据和推送内容失败',
            type: 'warning'
          });
        }
      }, error => {
        console.log(error)
        this.$message({
          message: '更新业务数据和推送内容失败',
          type: 'warning'
        });
      })
    },


    // 选择应用
    selectApp(appCode) {
      // 应用的名称
      this.selectAppCode = appCode
    },
    // 清除应用
    clearSelectAppCode() {
      this.selectAppCode = ''
    },
    // 选择应用
    selectApp2(appCode) {
      // 应用的名称
      this.selectAppCode2 = appCode
    },
    // 清除应用
    clearSelectAppCode2() {
      this.selectAppCode2 = ''
    },
    formatBusinessData(title) {
      this.format_result = ''
      this.FORMAT_TITLE = title
      this.FORMAT_TITLE_dialogVisible = true

      if (title === '业务数据' && this.api_param) {
        this.format1(this.api_param)
      }
      if (title === '推送内容' && this.push_body) {
        this.format1(this.push_body)
      }
    },

    t(data) {
      // 长整数转成字符串类型, 防止精度丢失
      data = data.replace(/((\W*)s*):s*([0-9]{15,})s*(,?)/g, '$1: $2$3$2 $4')
      return data;
    },

    format1(data) {

      if (data.includes(':')) {
        try {
          //
          data = this.t(data)
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

      if (data) {
        // 显示格式化之后的结果
        this.format_result = data
      }

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