DiscourseAnalysis.WordcloudView = (function() {

var that = {},
width,
height,
s,
anchoring,
color,


init = function (w, h){
//width = 49;
width = w;
height = h;
color = d3.scale.category20c();
},

generateCloud = function (data, anchor){
  anchoring = anchor;
  data = _makeWordcloudData(data);
  _makeWordcloud(data);
},

_makeWordcloudData = function (data_raw){
    s = d3.scale.pow().exponent(2).domain([0, data_raw[1][1]*1.1]).range([13,_calculateTransformationY(height)/4]);
    s.clamp(true);
    s.nice();

    
var frequency_list = [];
for (var i = 0; i < data_raw.length; i++){
	var entry = {"text":data_raw[i][0], "size":s(data_raw[i][1])};
	frequency_list.push(entry);
} 
return frequency_list;
},


//http://www.niemanlab.org/2011/10/word-clouds-considered-harmful/
			
_makeWordcloud = function (data){
    cloud = d3.layout.cloud()
            .size([_calculateTransformationX(width)*1.2, _calculateTransformationY(height)*1.2])
            .words(data)
            .rotate(0)
            .fontSize(function(ds) { return ds.size; })
            .on("end", draw);


    cloud.start();


function draw (words) {
        d3.select(anchoring).append("svg")
                .attr("width", "" + _calculateTransformationX(width) + "px")
                .attr("height", ""  + _calculateTransformationY(height) + "px")
                .attr("class", "wordcloud")
                .append("g")
                // without the transform, words words would get cutoff to the left and top, they would
                // appear outside of the SVG area
                .attr("transform", "translate(" + _calculateTransformationX(width)/2 + "," + _calculateTransformationY(height)/2 + ")")
                .selectAll("text")
                .data(words)
                .enter().append("text")
                .style("font-size", function(ds) { return ds.size + "px"; })
                .style("fill", function(ds, i) { return color(i); })
                .style("font-weight", "bold")
                .attr("text-anchor", "middle")
                .attr("transform", function(ds) {
                    //return "translate(" + [ds.x, ds.y] + ")rotate(" + ds.rotate + ")";
                    return "translate(" + [ds.x, ds.y] + ")rotate(" + ((Math.random() * 8) - 4 )+ ")";
                })
                .text(function(ds) { return ds.text; });
    }
},
	
_calculateTransformationX = function (width){

    return ($(window).width()*(width/100));
},

 _calculateTransformationY = function (height){

    return ($(window).height()*(height/100));
};

that.init = init;
that.generateCloud = generateCloud;

return that;
}());