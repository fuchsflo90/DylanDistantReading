DiscourseAnalysis.ElectionsView = (function() {

var that = {},
data,
x,
y1,
y2,
chartdata,
anchor,


init = function (data){
    anchor = '#wahlergebnisse';
    chartdata = data;
    x = _makeChartData(data, 0);
    y1 = _makeChartData(data, 1);
    y2 = _makeChartData(data, 2);
},

_makeChartData = function(data_raw, pos){
var frequency_list = [];
for (var i = 0; i < data_raw.length; i++){
  var entry = data_raw[i][pos];
  frequency_list.push(entry);
} 
return frequency_list;
},

generateElectionsChart = function (){
var wahlenchart = c3.generate({
    bindto: anchor,
    data: {
        axes: {
            'y1':'FPÖ',
            'y2':'Grüne',
        },
        columns: [
            y1,
            y2
        ],
        colors: {
            Grüne: '#2ca02c' 
        }
    },   
    axis : {
            x: {
            label: 'Nationalratswahlen',
            type: 'category',
            categories: x.slice(1, x.length), 
        },
        y:{
            max: 50,
            label: 'Stimmenanteil [%]'
        }
    },
     tooltip: {
         format:{
            value:function(y){
                return y + ' %';
       }
    }
}
    
});
};

that.init = init;
that.generateElectionsChart = generateElectionsChart;

return that;
}());