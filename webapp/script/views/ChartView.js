DiscourseAnalysis.ChartView = (function() {

var that = {},
rotate,
chartheight,
chartwidth,

init = function (){
  rotate = true;
  chartheight = 200;
  //chartwidth = 47;
},

generateChartView = function (anchor, barcolor, data){
  x = _makeChartData(data, 0);
  y = _makeChartData(data, 1);
  _generateSimpleChart(x, y, anchor, barcolor);
},

_makeChartData = function(data_raw, pos){
  //chartheight = data_raw.length*1.5;
var frequency_list = [];
for (var i = 0; i < data_raw.length-1; i++){
  var entry = data_raw[i][pos];
  frequency_list.push(entry);
} 
return frequency_list;
},

_generateSimpleChart = function(x, y, anchor, barcolor){
  var chart = c3.generate({
    bindto: anchor,
    size: {
     height: _calculateTransformationY(chartheight),
     width: _calculateTransformationX(chartwidth)
    },
    data: {
      columns: [
        y
      ],
    },
    axes: {
      VALUE: 'y2',
      RANK: 'y2'
    },
    colors: {
      RANK: barcolor,
      VALUE: barcolor
    },
    axis: {
      rotated: rotate,
      x: {
        type: 'category',
        categories: x.slice(1, x.length),
        tick: {
          rotate: -45,
          multiline: false,
        },
      },
      y: {
        show: false
      },
      y2: {
        show: false
      }
    },
    legend: {
      show: false
    }
  });
},

_calculateTransformationX = function (width){

    return ($(window).width()*(width/100));
},

_calculateTransformationY = function (height){

    return ($(window).height()*(height/100));
};


that.init = init;
that.generateChartView = generateChartView;

return that;

}());