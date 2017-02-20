DiscourseAnalysis.TestCloud = (function() {

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
    s = d3.scale.pow().exponent(2).domain([0, data_raw[1][1]]).range([18,_calculateTransformationY(height)/3]);
    s.clamp(true);
    s.nice();
var frequency_list = [];
for (var i = 0; i < data_raw.length; i++){
  var entry = {"text":data_raw[i][0], "size":s(data_raw[i][1])};
  frequency_list.push(entry);
} 
return frequency_list;
},


_makeWordcloud = function(data){

var fill = d3.scale.category20();

var layout = d3.layout.cloud()
    .size([_calculateTransformationX(width) , _calculateTransformationY(height)])
    /*.words([
      "Hello", "world", "normally", "you", "want", "more", "words",
      "than", "this"].map(function(d) {
      return {text: d, size: 10 + Math.random() * 90, test: "haha"};
    }))*/
    .words(data)
    .padding(0)
    .rotate(0)
    .font("Impact")
    .fontSize(function(d) { return d.size; })
    .on("end", draw);

layout.start();

function draw(words) {
  d3.select(anchoring).append("svg")
      .attr("width", layout.size()[0])
      .attr("height", layout.size()[1])
    .append("g")
      .attr("transform", "translate(" + layout.size()[0] / 2 + "," + layout.size()[1] / 2 + ")")
    .selectAll("text")
      .data(words)
    .enter().append("text")
      .style("font-size", function(d) { return d.size + "px"; })
      //.style("font-family", "Impact")
      .style("font-weight", "bold")
      .style("fill", function(d, i) { return fill(i); })
      .attr("text-anchor", "middle")
      .attr("transform", function(d) {
        return "translate(" + [d.x, d.y] + ")rotate(" + ((Math.random() * 8) - 4 )+  ")";
      })
      .text(function(d) { return d.text; });
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