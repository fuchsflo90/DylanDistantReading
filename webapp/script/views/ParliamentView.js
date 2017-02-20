DiscourseAnalysis.ParliamentView = (function() {

var that = {},
anchor,
seats,

/*var dataset = [
  { label: 'SPÖ', count: 53 }, 
  { label: 'ÖVP', count: 51 },
  { label: 'FPÖ', count: 38 },
  { label: 'GRÜNE', count: 24 },
  { label: 'NEOS', count: 9 },
  { label: 'STRONACH', count: 6 },
  { label: 'OHNNE KLUB', count: 3 }
];

// Alternative
var colorpattern = d3.scale.ordinal()
  .range(['#F77', '#777', '#00d', '#0d0', '#FbF', '#FFb', '#ccc']); */


init = function (){
anchor = '#parlament';
seats = [
            ['SPÖ', 53],
            ['ÖVP', 51],
            ['FPÖ', 38],
            ['GRÜNE', 24],
            ['NEOS', 9],
            ['STRONACH', 6],
            ['OHNE KLUB', 3]
        ];
},


//http://grokbase.com/t/gg/c3js/149aesdmj5/pie-chart-values-instead-of-percentages
generateParliament = function () {
var chart = c3.generate({
	bindto: anchor,
    data: {
        columns: seats,

        type: 'donut',
        onclick: function (d, i) { console.log("onclick", d, i); }
        //onmouseover: function (d, i) { console.log("onmouseover", d, i); },
        //onmouseout: function (d, i) { console.log("onmouseout", d, i); }
    },
    donut: {
    
        //title: "September 2015",
    
        label: {
           format: function(value) {
                return value;
            },
            show: true
          },

    },
      legend: {
        position: 'right'
    },
    color: {
        pattern: ['#FF4444', '#444444', '#4444FF', '#44FF44', '#FF44FF', '#FFFF44', '#888888'], // the three color levels for the percentage values.
        /*threshold: {
            unit: 'Sitze', // percentage is default
            max: 184, // 100 is default
            values: [53, 51, 38, 24, 9, 6, 3]
        } */
    },
    size: {
        height: 360
    },
    tooltip: {
    	 format:{
      		value:function(x){
      			return x + ' Sitze';
       }
    }
	}
});
};

that.init = init;
that.generateParliament  = generateParliament;

return that;
}());