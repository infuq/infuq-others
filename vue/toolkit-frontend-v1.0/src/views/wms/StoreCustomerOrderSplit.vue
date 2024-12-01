<template>
  <div>
    <section class="content clearfix" style="width: 97%;">
      <div class="el-backtop" style="right: 40px; top: 130px;">
        <el-link type="primary" :href="'/'" :underline="false" target="_blank"><i class="el-icon-s-home"></i></el-link>
      </div>
      <el-divider content-position="right">{{ env }}环境</el-divider>


      <el-form :inline="true" class="demo-form-inline">

        <div>
          <el-input v-model="businessNo" placeholder="DH-230804-000002 或 399576908800966656" clearable
                    @clear="clearBusinessNo" style="width: 600px;">
            <template slot="prepend">订货单号或订货单ID</template>
          </el-input>
          <div style="display: inline-block; margin-top: 3px; margin-bottom: 3px; margin-left: 5px;">
            <el-button type="primary" @click="onSubmit(1)">查询</el-button>
          </div>
        </div>

        <!-- 结果 -->
        <div style="margin-top: 15px;">

          <!-- 操作结果 -->
          <div style="margin-top: 10px;">

            <!-- 订货明细 -->
            <span v-for="sco in scodList">
                <span v-if="has_data">
                    <el-divider content-position="left">订货明细数量({{ sco.customerOrderNo }})</el-divider>
                </span>
                <span v-else>
                    <el-divider content-position="left">订货明细数量</el-divider>
                </span>
                <div style="margin-left: 40px; font-weight: 500; font-size: 14px;">

                    <div v-if="sco.customerOrderAncestorNo != null">
                        <div style="width: 400px; display: block; margin: 5px 0;">
                            <label
                                style="display: inline-block; width: 110px; text-align: right;">祖先单号:</label><label>&nbsp;&nbsp;&nbsp;{{
                            sco.customerOrderAncestorNo
                          }}</label>
                        </div>
                        <div style="width: 400px; display: block; margin: 5px 0;">
                            <label
                                style="display: inline-block; width: 110px; text-align: right;">父单号:</label><label>&nbsp;&nbsp;&nbsp;{{
                            sco.customerOrderParentNo
                          }}</label>
                        </div>
                        <div style="display: block; margin: 5px 0;" v-if="sco.childNo != null">
                            <label
                                style="display: inline-block; width: 110px; text-align: right;">子单号:</label><label>&nbsp;&nbsp;&nbsp;{{
                            sco.childNo
                          }}</label>
                        </div>
                    </div>
                    <div style="display: block; margin: 5px 0;"
                         v-if="sco.childNo != null && sco.customerOrderAncestorNo == null">
                        <label style="display: inline-block; width: 110px; text-align: right;">子孙单号:</label><label>&nbsp;&nbsp;&nbsp;{{
                        sco.childNo
                      }}</label>
                    </div>
                    <div style="width: 400px; display: block; margin: 5px 0;" v-if="sco.changeWarehouse == 0">
                        <label style="display: inline-block; width: 110px; text-align: right;">仓库:</label><label>&nbsp;&nbsp;&nbsp;{{
                        sco.warehouseName
                      }}</label>
                    </div>
                    <div style="width: 400px; display: block; margin: 5px 0;" v-if="sco.changeWarehouse == 1">
                        <span style="color: red;"><label
                            style="display: inline-block; width: 110px; text-align: right;">换仓:</label><label>&nbsp;&nbsp;&nbsp;{{
                            sco.warehouseName
                          }}</label></span>
                    </div>
                    <div style="width: 400px; display: block; margin: 5px 0;"
                         v-if="sco.customerOrderFinishType != null">
                        <span style="color: green;"><label
                            style="display: inline-block; width: 110px; text-align: right;">完结类型:</label><label>&nbsp;&nbsp;&nbsp;{{
                            sco.customerOrderFinishType
                          }}</label></span>
                    </div>

                    <template>
                        <el-table :data="sco.storeCustomerOrderDetailsList" border style="width: 95%"
                                  :row-style="{ height: 10+'px'}" :cell-style="{padding:0+'px'}"> <!-- height="250" -->
                            <el-table-column type="selection" width="55"></el-table-column>
                            <el-table-column fixed label="序号" type="index" width="50"></el-table-column>
                            <el-table-column prop="goodsNo" label="商品编码" max-width="100"
                                             :show-overflow-tooltip="true"></el-table-column>
                            <el-table-column prop="goodsName" label="商品名称" max-width="180"
                                             :show-overflow-tooltip="true"></el-table-column>
                            <el-table-column prop="orderQuantity" label="订货数量" width="100"></el-table-column>

                            <el-table-column label="出库" align="center">
                                <el-table-column prop="processedQuantity" width="110">
                                    <template slot-scope="scope" slot="header">
                                        <span style="color: green;">已出库数</span>
                                    </template>
                                </el-table-column>
                                <el-table-column prop="processingQuantity" width="110">
                                    <template slot-scope="scope" slot="header">
                                        <span style="color: green;">出库中数</span>
                                    </template>
                                </el-table-column>
                            </el-table-column>
                            <el-table-column label="发货" align="center">
                                <el-table-column prop="deliveredQuantity" width="110">
                                    <template slot-scope="scope" slot="header">
                                        <span style="color: #0ca5e6;">已发货数</span>
                                    </template>
                                </el-table-column>
                                <el-table-column prop="deliveringQuantity" width="110">
                                    <template slot-scope="scope" slot="header">
                                        <span style="color: #0ca5e6;">发货中数</span>
                                    </template>
                                </el-table-column>
                            </el-table-column>

                            <el-table-column label="退货" align="center">
                                <el-table-column prop="returnedQuantity" width="110">
                                    <template slot-scope="scope" slot="header">
                                        <span style="color: #dc0e49;">已退货数</span>
                                    </template>
                                </el-table-column>
                                <el-table-column prop="returningQuantity" width="110">
                                    <template slot-scope="scope" slot="header">
                                        <span style="color: #dc0e49;">退货中数</span>
                                    </template>
                                </el-table-column>
                            </el-table-column>

                            <el-table-column label="套餐商品" width="100" align="center">
                                <template slot-scope="scope">
                                    <span v-if="scope.row.isSetMeal == 1">
                                        <svg t="1691468608589" class="icon" viewBox="0 0 1024 1024" version="1.1"
                                             xmlns="http://www.w3.org/2000/svg" p-id="4016" width="16" height="16"><path
                                            d="M414.245926 751.028148l437.57037-453.12c7.300741-7.49037 7.111111-19.531852-0.474074-26.832593-7.49037-7.300741-19.531852-7.111111-26.832593 0.474074L398.506667 712.722963 199.111111 513.327407c-7.395556-7.395556-19.437037-7.395556-26.832593 0l0 0c-7.395556 7.395556-7.395556 19.437037 0 26.832593l212.574815 212.574815c6.731852 6.731852 17.161481 7.300741 24.557037 1.896296C411.211852 753.682963 412.823704 752.545185 414.245926 751.028148z"
                                            fill="#d4237a" p-id="4017"></path></svg>
                                    </span>
                                </template>
                            </el-table-column>
                            <el-table-column prop="subQuantity" label="套餐比例" width="100"
                                             align="center"></el-table-column>
                            <el-table-column prop="customerOrderDetailsId" label="订货明细ID"></el-table-column>
                        </el-table>
                    </template>
                </div>
              </span>

          </div>
        </div>
      </el-form>

    </section>
  </div>

</template>


<script src="http://d3js.org/d3.v3.min.js" charset="utf-8"></script>
<script>

import Config from '@/assets/js/route.js'
import axios from 'axios';

export default {
  name: "StoreCustomerOrderSplit",
  data() {

    return {
      env: Config.env,
      host: Config.host,

      has_data: false,

      businessNo: '',

      scodList: [],

      nodes: {},
      links: [],
    }
  },

  methods: {

    clearSvg() {
      d3.select('body').selectAll('svg').remove();
    },

    // https://blog.csdn.net/qq_39408204/article/details/103799835
    draw(links) {
      this.links = links

      const nodes = {};
      this.links.forEach(function (link) {
        link.source = nodes[link.source] || (nodes[link.source] = {
          name: link.source,
          finishType: link.finishType,
          changeWarehouse: link.changeWarehouse
        });
        link.target = nodes[link.target] || (nodes[link.target] = {
          name: link.target,
          finishType: link.finishType,
          changeWarehouse: link.changeWarehouse
        });
      });
      this.nodes = nodes

      const width = 1560, height = 800;

      const force = d3.layout.force()
          .nodes(d3.values(nodes))
          .links(links)
          .size([width, height])
          .linkDistance(250)
          .charge(-4000)
          .on("tick", tick)
          .start();

      const svg = d3.select("body").append("svg")
          .attr("width", "100%")
          .attr("height", height);

      const marker =
          svg.append("marker")
              .attr("id", "resolved")
              .attr("markerUnits", "userSpaceOnUse")
              .attr("viewBox", "0 -5 10 10")
              .attr("refX", 59)
              .attr("refY", 0)
              .attr("markerWidth", 8)
              .attr("markerHeight", 8)
              .attr("orient", "auto")
              .attr("stroke-width", 2)
              .append("path")
              .attr("d", "M0,-5L10,0L0,5")
              .attr('fill', '#595D68');

      const edges_line = svg.selectAll(".edgepath")
          .data(force.links())
          .enter()
          .append("path")
          .attr({
            'd': function (d) {
              return 'M ' + d.source.x + ' ' + d.source.y + ' L ' + d.target.x + ' ' + d.target.y
            },
            'class': 'edgepath',
            'id': function (d, i) {
              return 'edgepath' + i;
            }
          })
          .style("stroke", '#595D68')
          .style("pointer-events", "none")
          .style("stroke-width", 1)
          .attr("marker-end", function (d) {
            if (d.rela === '自身') {
              return ''
            } else {
              return 'url(#resolved)'
            }
          });

      const edges_text = svg.append("g").selectAll(".edgelabel")
          .data(force.links())
          .enter()
          .append("text")
          .style("pointer-events", "none")
          .attr({
            'class': 'edgelabel',
            'id': function (d, i) {
              return 'edgepath' + i;
            },
            'dx': 60,
            'dy': -5
          });

      edges_text.append('textPath')
          .attr('xlink:href', function (d, i) {
            return '#edgepath' + i
          })
          .style("pointer-events", "none")
          .text(function (d) {
            return d.rela;
          });


      const circle = svg.append("g").selectAll("circle")
          .data(force.nodes())
          .enter().append("circle")
          .style("fill", function (node) {
            let color;
            const link = links[node.index];
            if (link) {
              if (link.type === "1") {
                return color = "#d6dce2";
              } else if (link.type === "3") {
                return color = "#d7e2d6";
              } else {
                return color = "#e2d6db";
              }
            }
          })
          .style('stroke', function (node) {
            let color;
            const link = links[node.index];
            if (link) {
              if (link.type === "1") {
                return color = "#C03939";
              } else if (link.type === "3") {
                return color = "#5095FF";
              } else if (link.source.name.length <= 4) {
                return color = "#CD994C";
              } else {
                return color = '#1943AC'
              }
            }
          })
          .attr("r", 40)
          .call(force.drag);


      const text = svg.append("g").selectAll("text")
          .data(force.nodes())
          .enter()
          .append("text")
          .attr("dy", ".35em")
          .attr("text-anchor", "middle")
          .style('fill', function (node) {
            let color;
            const link = links[node.index];
            return color = '#000000';
          })
          .attr('x', function (d) {
            let l = 1;
            if (d.finishType) {
              l = l + 1;
            }
            if (d.changeWarehouse === 1) {
              l = l + 1;
            }

            // 只有一行
            if (l === 1) {
              d3.select(this).append('tspan')
                  .attr('x', 0)
                  .attr('y', 2)
                  .text(function () {
                    var display;

                    var success = d.name.search(/^DH-\d{6}-\d{6}$/g)
                    if (success === 0) {
                      display = d.name + "(祖先)";
                    } else {
                      display = d.name;
                    }

                    return display
                  });
              // 两行
            } else if (l === 2) {
              d3.select(this).text(function () {
                return '';
              });

              d3.select(this).append('tspan')
                  .attr('x', 0)
                  .attr('y', -7)
                  .text(function () {
                    var display;

                    var success = d.name.search(/^DH-\d{6}-\d{6}$/g)
                    if (success === 0) {
                      display = d.name + "(祖先)";
                    } else {
                      display = d.name;
                    }

                    return display
                  });
              if (d.finishType) {
                d3.select(this).append('tspan')
                    .attr('x', 0)
                    .attr('y', 15)
                    .style('fill', function (node) {
                      var color;
                      var link = links[node.index];
                      return color = '#008000';
                    })
                    .text(function () {
                      return d.finishType;
                    });
              }
              if (d.changeWarehouse === 1) {
                d3.select(this).append('tspan')
                    .attr('x', 0)
                    .attr('y', 15)
                    .style('fill', function (node) {
                      var color;
                      var link = links[node.index];
                      return color = '#ff0000';
                    })
                    .text(function () {
                      return '换仓';
                    });
              }

              // 三行
            } else if (l == 3) {
              d3.select(this).text(function () {
                return '';
              });

              d3.select(this).append('tspan')
                  .attr('x', 0)
                  .attr('y', -7)
                  .text(function () {
                    var display;

                    var success = d.name.search(/^DH-\d{6}-\d{6}$/g)
                    if (success == 0) {
                      display = d.name + "(祖先)";
                    } else {
                      display = d.name;
                    }

                    return display
                  });

              d3.select(this).append('tspan')
                  .attr('x', 0)
                  .attr('y', 15)
                  .style('fill', function (node) {
                    var color;
                    var link = links[node.index];
                    return color = '#008000';
                  })
                  .text(function () {
                    return d.finishType;
                  });
              d3.select(this).append('tspan')
                  .attr('x', 0)
                  .attr('y', 32)
                  .style('fill', function (node) {
                    var color;
                    var link = links[node.index];
                    return color = '#ff0000';
                  })
                  .text(function () {
                    return '换仓';
                  });

            }


          });

      function tick() {
        circle.attr("transform", transform1);
        text.attr("transform", transform2);

        edges_line.attr('d', function (d) {
          const path = 'M ' + d.source.x + ' ' + d.source.y + ' L ' + d.target.x + ' ' + d.target.y;
          return path;
        });

        edges_text.attr('transform', function (d, i) {
          if (d.target.x < d.source.x) {
            let bbox = this.getBBox();
            let rx = bbox.x + bbox.width / 2;
            let ry = bbox.y + bbox.height / 2;
            return 'rotate(180 ' + rx + ' ' + ry + ')';
          } else {
            return 'rotate(0)';
          }
        });
      }

      function linkArc(d) {
        return 'M ' + d.source.x + ' ' + d.source.y + ' L ' + d.target.x + ' ' + d.target.y
      }

      function transform1(d) {
        return "translate(" + d.x + "," + d.y + ")";
      }

      function transform2(d) {
        return "translate(" + (d.x) + "," + d.y + ")";
      }
    },


    // 查询
    onSubmit(type) {

      let _businessNo = this.businessNo

      if (type === 1) {
        if (!this.businessNo) {
          this.$message({
            message: '订货单号为空',
            type: 'warning'
          });
          return;
        }
      }

      this.has_data = false
      this.scodList = []
      this.clearSvg()

      axios({
        url: this.host + '/scod/store_customer_order_split_detail_quantity',
        method: 'GET',
        params: {
          businessNo: _businessNo
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

            if (response.data.storeCustomerOrderDetailList) {
              // 订货单明细
              this.scodList = response.data.storeCustomerOrderDetailList
              this.has_data = true

              var links = []
              var typeArr = ["1", "2", "3"]
              for (let i = 0; i < response.data.storeCustomerOrderDetailList.length; i++) {
                let target = response.data.storeCustomerOrderDetailList[i]['customerOrderNo']
                let source = response.data.storeCustomerOrderDetailList[i]['customerOrderParentNo']
                let customerOrderFinishType = response.data.storeCustomerOrderDetailList[i]['customerOrderFinishType']
                let changeWarehouse = response.data.storeCustomerOrderDetailList[i]['changeWarehouse']
                if (source) {
                  links.push({
                    'source': source,
                    'target': target,
                    'type': typeArr[i % 3],
                    'rela': "",
                    'finishType': customerOrderFinishType,
                    'changeWarehouse': changeWarehouse
                  })
                } else {
                  links.push({
                    'source': target,
                    'target': target,
                    'type': typeArr[i % 3],
                    'rela': "自身",
                    'finishType': customerOrderFinishType,
                    'changeWarehouse': changeWarehouse
                  })
                }
              }

              this.draw(links)

            } else {
              this.$message({
                message: '未查询到数据',
                type: 'warning'
              });
              this.scodList = []
            }
          }, error => {
            this.$message({
              message: '查询失败',
              type: 'warning'
            });
            this.scodList = []
          })
    },

    clearBusinessNo() {
      this.businessNo = ''
      this.has_data = false
      this.scodList = []
      this.clearSvg()
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