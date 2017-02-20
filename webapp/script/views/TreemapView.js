DiscourseAnalysis.TreemapView = (function() {

var that = {},
mapheight,
mapwidth,
anchoring,


init = function (){
    mapheight = 70;
    mapwidth = 100;
},

generateTreemap = function (data, anchor){
    anchoring = anchor;
    data = data.slice(1,80);
    _makeTreemap(_makeTreemapData(data));
},

_makeTreemapData = function (data_raw){
s = d3.scale.pow().exponent(2); 
var frequency_list = [];
for (var i = 0; i < data_raw.length; i++){
    var entry = {"name":data_raw[i][0], "size":s(data_raw[i][1])};
    frequency_list.push(entry);
} 
return frequency_list;
},

_makeTreemap = function (data_root){

   // instantiate d3plus
  var visualization = d3plus.viz()
    .container(anchoring)
    .height(_calculateTransformationY(mapheight))
    .data(data_root)
    .type("tree_map")
    .id("name")
    .size("size")
    .tooltip({"share": false})
    //.labels({"align": "left", "valign": "top"})
    .draw();

    d3plus.textwrap().container('.d3plus_label').resize(true).size(6,30);

}, 

_calculateTransformationX = function (width){

    return ($(window).width()*(width/100));
},

_calculateTransformationY = function (height){

    return ($(window).height()*(height/100));
};

that.init = init;
that.generateTreemap = generateTreemap;

return that;
}());