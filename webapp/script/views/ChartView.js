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
  _generateChart(x, y, anchor, barcolor);
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

_generateChart = function (x, y, anchor, barcolor){
var chart = c3.generate({
    bindto: anchor,
    size: {
     height: _calculateTransformationY(chartheight),
     //height: chartheight,
     width: _calculateTransformationX(chartwidth)
    },
    padding: {
      bottom: _calculateTransformationY(20)
    },
    data: {

      columns: [
        y  
      ],
      axes: {
        VALUE: 'y2',
        RANK: 'y2'
      },

        type: 'bar',
         colors: {
        RANK: barcolor,
        VALUE: barcolor
      },
      },
 
    bar: {
        width: {
            ratio: 0.7 // this makes bar width 50% of length between ticks
        } 
        // or
        //width: 7 // this makes bar width 100px
    },
    axis: {
      rotated: rotate,
      x: {
        type: 'category',
        categories: x.slice(1, x.length), 
        //categories: x, 
        tick: {
                rotate: -45,
                multiline: false
            },
      },
      y: {
        show: false
      },
       y2: {
        show: true
      }
    }, legend: {
        show: false
    }
});

};

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