<template>
  <div class="stockkline" ref='stockkline'>
    <div>
      <div :id='ID' ref='divchart' style="width:100%;height:100%">
        <div class='kline' id="kline" ref='kline'  v-show="KLine.IsShow"></div>
      </div>
    </div>
    <div class="indexbar" v-show='KLine.IsShow' ref='klineindexbar'>
      <span v-for='(item,index) in KLine.IndexBar.Menu' :key='index' :class='{active:KLine.IndexBar.Selected.indexOf(index)>=0}'
            @click="OnClickIndexBar(item,index)">{{item}}</span>
    </div>
  </div>
</template>

<script>

import HQChart from 'hqchart'
import 'hqchart/src/jscommon/umychart.resource/css/tools.css'

const KLineOption = {
  Type: '历史K线图',
  Windows: [
    { Index: "MA" },
    { Index: "VOL" },
    { Index: "MACD" }
  ],
  KLine: {
    DragMode: 1, //拖拽模式 0 禁止拖拽 1 数据拖拽 2 区间选择
    Right: 1, //复权 0 不复权 1 前复权 2 后复权
    Period: 0, //周期 0 日线 1 周线 2 月线 3 年线
    MaxReqeustDataCount: 1000, //日线数据最近1000天
    MaxRequestMinuteDayCount: 15,    //分钟数据最近15天
    PageSize: 50, //一屏显示多少数据
    IsShowTooltip: true //是否显示K线提示信息
  },
  Border: {
    Left: 1, //左边间距
      Right: 60, //右边间距
      Top: 25
  }
}

export default {
  name:'StockKLine',

  data () {
    let data = {
      Symbol: '600000.sh',
      ID: HQChart.Chart.JSChart.CreateGuid(),
      KLine: {
        JSChart: null,
        Option: KLineOption,
        IsShow: false,
        IndexBar: {
          Menu:['RSI','MACD','KDJ','BOLL','DMI','CCI','OBV','SKDJ','BIAS'],
          // Menu:['BBI', 'MA', 'HMA', 'LMA', 'VMA', 'BOLL', 'SKDJ', 'KDJ', 'MACD', 'RSI', 'OBV', 'BIAS'],
          Selected:[1]
        }
      }
    }
    return data;
  },

  mounted () {
    this.OnSize();
    this.CreateKLineChart();
    this.ChangeChartPeriod();
  },
  methods: {
    OnSize () {
      let stockKLine = this.$refs.stockkline;
      let klineIndexBar = this.$refs.klineindexbar;
      let divChart = this.$refs.divchart;

      let height = stockKLine.offsetHeight;
      let width = stockKLine.offsetWidth;
      let indexBarHeight = klineIndexBar.offsetHeight;

      let chartHeight = height - indexBarHeight;
      let chartWidth = width;

      divChart.style.width = chartWidth+'px';
      divChart.style.height = chartHeight+'px';

      let divKline=this.$refs.kline;

      divKline.style.width = chartWidth+'px';
      divKline.style.height = chartHeight+'px';

      if (this.KLine.JSChart) this.KLine.JSChart.OnSize();
    },

    CreateKLineChart () {
      this.KLine.Option.Symbol = this.Symbol;
      HQChart.Chart.jsChartStyle(null);
      let chart = HQChart.Chart.JSChart.Init(this.$refs.kline);
      chart.SetOption(this.KLine.Option);
      this.KLine.JSChart = chart;
      this.KLine.JSChart.ChangeScriptIndex(0,
        {
          Name: "MA",
          Script: 'MA5:MA(CLOSE,M1);\n\
                  MA10:MA(CLOSE,M2);\n\
                  MA20:MA(CLOSE,M3);\n\
                  MA30:MA(CLOSE,M4);',
          Args: [
              { Name: 'M1', Value: 5},
              { Name: 'M2', Value: 10 },
              { Name: 'M3', Value: 20},
              { Name: 'M4', Value: 30}
          ],
          "Modify": false,
          "Change": false
        }
      );
      this.KLine.JSChart.ChangeScriptIndex(1,
        {
          Name: "VOL",
          Script: 'VOL:VOL,VOLSTICK;\n\
                  MA5:MA(VOL,M1);\n\
                  MA10:MA(VOL,M2);',
          Args: [
              { Name: 'M1', Value: 5},
              { Name: 'M2', Value: 10}
          ],
          "Modify": false,
          "Change": false
        }
      );
    },

    ChangeChartPeriod () {
      this.KLine.IsShow = true;
      var _this = this;
      setTimeout(() =>_this.OnSize() ,50)
    },

    ChangeSymbol (symbol) {
      if (this.Symbol==symbol) return;
      this.Symbol = symbol;
      this.KLine.JSChart.ChangeSymbol(this.Symbol);
    },

    OnClickIndexBar (name,index) {
      if(name == "BOLL") name="BOLL副图";//副图指标中的【BOLL】即对应K线图中的【BOLL副图】
      this.KLine.JSChart.ChangeIndex(2, name);
      this.KLine.IndexBar.Selected = [index];
    }
  }
}

</script>

<style lang="scss">
$border: 1px solid #e1ecf2;

.stockkline
{
    width:100%;
    height:100%;
}

.klineLightTheme{
    .periodbar{
        background:#eff5ff;
        border-color:#dde4f4;
        color:#1e52a6;
        .active{
            background: #fff;
            border-top: 2px solid #1e52a6;
            border-left:1px solid #dde4f4;
            border-right: 1px solid #dde4f4;
            border-bottom: 1px solid #fff;
        }
    }
    .lineGroup{
        .el-checkbox{
            color:#1f2d3d;
        }
    }
    .indexbar{
        background:#e1ecf2;
    }
    .menuTwo{
        background-color: #eff5ff;
    }
    .periodIndexbar .preiod .itemList{
        background: #eff5ff;
        border: 1px solid #dde4f4;
        .item{
            color: #666;
            &.active{
                color: #fff;
                background-color: #1e52a6;
            }
        }
    }
}

.klineDarkTheme{
    .periodbar{
        background:#313b4c;
        border-color:#232f43;
        color:#fff;
        .active{
            background: #000;
            border-top: 2px solid #3f9eff;
            border-left:1px solid #313b4c;
            border-right: 1px solid #313b4c;
            border-bottom: 1px solid #000;
        }
    }
    .lineGroup{
        .el-checkbox{
            color:#fff;
        }
    }
    .indexbar{
        background:#232f43;
    }
    .menuTwo{
        background-color: #000;
    }
    .periodIndexbar .preiod .itemList{
        background: #232f43;
        border: 1px solid #232f43;
        .item{
            color: #fff;
            &.active{
                background-color: #3f9eff
            }
        }
    }
}

.kline
{
    left:0px;
    top:0px;
    position: relative;
    width:100%;
    height:100%;
}

.indexbar
{
    width: 100%;
    height: 30px;
    display: flex;
    flex-direction: row;
}

.indexbar span
{
    height: 30px;
    line-height: 30px;
    text-align: center;
    cursor: pointer;
    flex-grow: 1;
}

.indexbar span.active
{
    color: #fff;
    background-color: #125fd9;
}

</style>
